# -*- coding: utf-8 -*-
"""
Created on Wed May 29 18:30:07 2024

@author: stefano.pauletta
"""
import pandas as pd


affectation=['Commerce',
             'Res_multi',
             'Res_ind',
             'Administration',
             'Education',
             'Sport',
             'Hospital',
             'Industry']
index_year=2021
index=pd.date_range(start='1/1/'+ str(index_year), 
                    end='31/12/' + str(index_year) +' 23:00',freq="1h")
Load_Curve_DB={}
for aff in affectation:
    target=aff + '.feather'
    # target=aff + '.csv'
    try:
        # bld_curve = pd.read_csv(target, sep=";")
        bld_curve = pd.read_feather(target)
        # bld_curve.to_feather(aff + '.feather')
        bld_curve.index=index
        Load_Curve_DB[aff]=bld_curve
    except:
        print(target + ' Not Found')    

