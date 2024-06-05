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
                 annual_consumption=True,
                 SRE=1000,
                 central_ECS=True,
                 index_year=2021):
        """
        Class constructor. 
        """
        self.affectation = affectation
        self.SRE=SRE
        self.annual_cons=annual_consumption
        self.cECS=central_ECS
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
            dati['Load1']=dati['Load1']*self.SRE*self.annual_cons
            dati['Load2']=dati['Load1']*self.SRE*self.annual_cons
            dati['Load3']=dati['Load1']*self.SRE*self.annual_cons
            return dati
        except:
            print(self.affectation + '.feather not found')
            return pd.DataFrame(index=self.index)
    
if __name__ == "__main__":

        profile = chargeCurve(affectation="Administration",
                                      annual_consumption=10000,
                                      SRE=1000,
                                      central_ECS=True)
        print(profile.DB)