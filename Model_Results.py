# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.lines as mlines
import matplotlib.ticker as mtick
import matplotlib.pylab as pylab
from pyomo.environ import  Param, RangeSet



def Load_results1(instance):
 
    Names = ['elc_mark_committed_share_t', 'PV_generation','wind_generation',
             'SMR_generation','elc_saleto_market_t','non_elc_Type_1_production',
             'curtailment','non_elc_Type_1_consumption','elcmarket_import']
    Number_Periods = int(instance.t_resolution.extract_values()[None])
    print("Number_Periods:", Number_Periods)
    Time_Series = pd.DataFrame(columns= Names, index=range(1,Number_Periods+1))            
             
    elc_mark_committed_share_t = instance.elc_mark_committed_share_t.extract_values()
    PV_generation = instance.PV_generation.extract_values()
    wind_generation = instance.wind_generation.extract_values()
    SMR_generation = instance.SMR_generation.extract_values()
    elc_saleto_market_t = instance.elc_saleto_market_t.extract_values()
    non_elc_Type_1_production = instance.non_elc_Type_1_production.extract_values() 
    curtailment = instance.curtailment.extract_values()     
    non_elc_Type_1_consumption = instance.non_elc_Type_1_consumption.extract_values()       
    elcmarket_import = instance.elcmarket_import.extract_values()   
    
    for i in range(1,Number_Periods+1):
        Time_Series['elc_mark_committed_share_t'][i] = elc_mark_committed_share_t[i]
        Time_Series['PV_generation'][i] = PV_generation[i]
        Time_Series['wind_generation'][i] = wind_generation[i]
        Time_Series['SMR_generation'][i] = SMR_generation[i]
        Time_Series['elc_saleto_market_t'][i] = elc_saleto_market_t[i]
        Time_Series['non_elc_Type_1_production'][i] = non_elc_Type_1_production[i]
        Time_Series['curtailment'][i] = curtailment[i]        
        Time_Series['non_elc_Type_1_consumption'][i] = non_elc_Type_1_consumption[i]
        Time_Series['elcmarket_import'][i] = elcmarket_import[i]        
  

       # if the step is in minutes
    #columns = pd.DatetimeIndex(1, instance.t_resolution(), instance.t_step_length())# Creation of an index with a start date and a frequency
    Time_Series.index = RangeSet(1, instance.t_resolution)
       
    Time_Series.to_excel('Results/Time_Series.xls') # Creating an excel file with the values of the variables that are in function of the periods

    # Time_Series_2 = pd.DataFrame()        
    # Time_Series_2['Committed Demand'] =  Time_Series['elc_mark_committed_share_t']
    # Time_Series_2['PV Generation'] = Time_Series['PV_generation']
    # Time_Series_2['Wind Generation'] = Time_Series['wind_generation']
    # Time_Series_2['SMR Generation'] = Time_Series['SMR_generation']
    # Time_Series_2['non_elc_Type_1_production'] = Time_Series['non_elc_Type_1_production']
    # Time_Series_2.index  = RangeSet(1, instance.t_resolution)
    
    return Time_Series


def Load_results2(instance):
    '''
    This function extracts the unidimensional variables into a  data frame 
    and creates a excel file with this data
    
    :param instance: The instance of the project resolution created by PYOMO. 
    
    :return: Data frame called Size_variables with the variables values. 
    '''
    # Load the variables that doesnot depend of the periods in python dyctionarys
    
    NPC = instance.ObjectiveFuntion.expr()
    SMR_cap = instance.SMR_cap.value
    Wind_cap = instance.Wind_cap.value
    PV_cap = instance.PV_cap.value
    Nonelc_cap= instance.Nonelc_cap.value

    data3 = [NPC,SMR_cap, Wind_cap, PV_cap,Nonelc_cap] # Loading the values to a numpy array  
    Size_variables = pd.DataFrame(data3,index=['Cost','SMR Capacity','Wind Capacity', 'PV Capacity','Nonelc_cap'])
    Size_variables.to_excel('Results/Size1.xls') # Creating an excel file with the values of the variables that does not depend of the periods
    
    return Size_variables
   
