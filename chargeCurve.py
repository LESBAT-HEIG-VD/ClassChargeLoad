# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 15:32:17 2022

@author: stefano.pauletta
"""

import pandas as pd
import pyarrow.feather as feather
import numpy as np
import math


class chargeCurve:
    """
    Class to 
    """

    def __init__(self,
                 affectation="Res_multi",
                 annual_consumption=119109,
                 SRE=1000,
                 Lausanne=False,
                 index_year=2021):
        """
        Class constructor. 
        affectation in ['Commerce',
                     'Res_multi',
                     'Res_multi_Lau',
                     'Res_ind',
                     'Administration',
                     'Education',
                     'Sport',
                     'Hospital',
                     'Industries']
        ref_cons in [158673,
                     249280,
                     116000,
                     158772,
                     114220,
                     488202,
                     204771,
                     204771,
                     119109]
        """
        self.affectation = affectation
        self.dict={'Commerce':[158763,74730,65835,1400],
                     'Res_multi':[249280,173253,133593,2500],
                     'Res_multi_Lau':[127859,42684,32097,800],
                     'Res_ind':[158772,118880,104033,1000],
                     'Administration':[114220,65073,46175,1400],
                     'Education':[488202,215402,146769,5000],
                     'Sport':[283115,253040,243536,3500],
                     'Hospital':[204771,108776,89187,2100],
                     'Industries':[119109,73114,59322,1000]}
        self.SRE=SRE
        self.annual_cons=annual_consumption
        self.loc=Lausanne
        if self.loc==True:
            self.affectation = 'Res_multi_Lau'
        self.year=index_year
        self.index=pd.date_range(start='1/1/'+ str(self.year), 
                    end='31/12/' + str(self.year) +' 23:00',freq="1h")
        self.DB=self.load_DB()
        return None

    def load_DB(self):
        """
        Method to access the source file 
        For Lausanne=False:
            affectation: the one it is given
            Load 1: Normal building
            Load 2: Refurbished building
            Load 3: Heavily refurbished building
        For Lausanne=True:
            affectation: only multifamily building
            Load 1: Normal building
            Load 2: Refurbished building
            Load 3: Heavily refurbished building 
                    with decentralized ECS production
        Load curves need to be multiplied by SRE to get the kWh 
        for each year hour
        """
        try:
            dati = pd.read_feather(r'Curves/'+self.affectation + '.feather')
            dati.index=self.index
            
            dati['Load1']=dati['Load1']*self.annual_cons/self.SRE*self.dict[self.affectation][3]/self.dict[self.affectation][0]
            dati['Load2']=dati['Load2']#*self.annual_cons/self.SRE*self.dict[self.affectation][3]/self.dict[self.affectation][1]
            dati['Load3']=dati['Load3']#*self.annual_cons/self.SRE*self.dict[self.affectation][3]/self.dict[self.affectation][2]
            return dati
        except:
            print(self.affectation + '.feather not found')
            return pd.DataFrame(index=self.index)
    
if __name__ == "__main__":
        """ use import chargeCurve as cc and then use cc.changeCurve()
        """
        
        profile_Lausanne = chargeCurve(annual_consumption=116000,
                                      SRE=800,
                                      Lausanne=True)
        profile_Yverdon=chargeCurve(affectation="Industries",
                         annual_consumption=119109,
                         SRE=1000,
                         Lausanne=False,
                         index_year=2021)
        print(profile_Lausanne.DB)
        print(profile_Yverdon.DB)