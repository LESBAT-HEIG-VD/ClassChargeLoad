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
                 annual_consumption=10000,
                 SRE=1000,
                 Lausanne=False,
                 index_year=2021):
        """
        Class constructor. 
        affectation in ['Commerce',
                     'Res_multi',
                     'Res_ind',
                     'Administration',
                     'Education',
                     'Sport',
                     'Hospital',
                     'Industries']
        ref_cons in [158673,
                     249280,
                     158772,
                     114220,
                     488202,
                     204771,
                     204771,
                     119109]
        """
        self.affectation = affectation
        self.dict={'Commerce':158673,
                     'Res_multi':249280,
                     'Res_ind':158772,
                     'Administration':114220,
                     'Education':488202,
                     'Sport':204771,
                     'Hospital':204771,
                     'Industries':119109}
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
        Load 1: Normal building
        Load 2: Refurbished building
        Load 3: Heavily refurbished building

        """
        try:
            dati = pd.read_feather(r'Curves/'+self.affectation + '.feather')
            dati.index=self.index
            
            dati['Load1']=dati['Load1']*self.SRE*self.annual_cons/self.dict[self.affectation]
            dati['Load2']=dati['Load2']*self.SRE
            if self.affectation!="Res_multi_Lau":
                dati['Load3']=dati['Load3']*self.SRE
            return dati
        except:
            print(self.affectation + '.feather not found')
            return pd.DataFrame(index=self.index)
    
if __name__ == "__main__":
        """ use import chargeCurve as cc and then use cc.changeCurve()
        """
        profile = chargeCurve(affectation="Commerce",
                                      annual_consumption=250000,
                                      SRE=1000,
                                      Lausanne=False)
        print(profile.DB)