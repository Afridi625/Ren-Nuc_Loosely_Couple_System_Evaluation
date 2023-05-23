# Objective funtion
from pyomo.environ import  value

def Net_Present_Cost(model): # OBJETIVE Function maximization

    '''        
##########################################################################################################
                                                  Objective Function
##########################################################################################################
    '''
    return (model.Rev_loc_market  - model.SMR_Variable_andFuel_Chares - \
            model.wind_capex_fixed_cost*model.Wind_cap - model.Wind_Variable_andFuelChares -\
            model.solar_capex_fixed_cost*model.PV_cap - model.Nonelec_Variable_Charges\
            - model.Solar_Variable_andFuelChares - model.nonelc_capex_fixed_cost_1*model.Nonelc_cap -\
            model.Import_Cost + model.Rev_nonelectric_production + model.Rev_saleto_market -\
            model.SMR_capex_fixed_cost*model.SMR_cap - model.Total_curtail_cost)
        
'''        
##########################################################################################################
                                                #3). Capacity & Geneartin Relation 
##########################################################################################################
'''
def PV_generation_cons(model,t):
    return model.PV_generation [t]==model.e_pv_genprofile_t[t]*model.PV_cap

def SMR_generation_cons(model,t):
    return model.SMR_generation [t] <= model.SMR_cap

def wind_generation_cons(model, t):
    return model.wind_generation[t]==model.e_wind_genprofile_t[t] *model.Wind_cap

def nonelc_Type_1_production_cons(model,t):
    return model.non_elc_Type_1_production[t]== model.non_elc_Type_1_consumption[t] * model.non_elc_efficiency_1

def nonelc_Type_1_consumption_cons(model,t):
    return model.non_elc_Type_1_consumption[t] <= model.Nonelc_cap

'''        
##########################################################################################################
                                                #1). Market Import and Sale
##########################################################################################################

'''
def Rev_saleto_market (model):
    return model.Rev_saleto_market == sum(model.elc_saleto_market_t[t]*model.elc_market_spot_price_t[t] for t in model.t_periods)

#def Rev_loc_market (model):
#    return model.Rev_loc_market == sum(model.elc_mark_committed_share_t[t]*model.elc_mark_commSupply_price_t[t] for t in model.t_periods)

def Import_Cost (model):
    return model.Import_Cost == sum(model.elcmarket_import[i]*model.elc_market_spot_price_t[i] for i in model.t_periods)

def Rev_nonelectric_production (model):
    return model.Rev_nonelectric_production == sum(model.non_elc_Type_1_production[i]*\
                        model.Non_electric_Type_1_value[i] for i in model.t_periods)
'''        
##########################################################################################################
                                                #2). Variable O&M Cost
##########################################################################################################
'''
def SMR_Variable_andFuel_Chares2 (model):
    return model.SMR_Variable_andFuel_Chares == sum((model.SMR_generation[i]* model.SMR_fuel_var_cost) for i in model.t_periods)

def Wind_Variable_andFuelChares (model):
    return model.Wind_Variable_andFuelChares == sum((model.wind_generation[i]*\
                            model.wind_var_cost) for i in model.t_periods)

def Solar_Variable_andFuelChares (model):
    return model.Solar_Variable_andFuelChares == sum((model.PV_generation[i]*\
                          model.solar_var_cost) for i in model.t_periods)
 
def Nonelec_Variable_Charges (model):
    return model.Nonelec_Variable_Charges == sum(model.non_elc_Type_1_consumption[i]* model.nonelc_var_cost_1 for i in model.t_periods)

'''        
##########################################################################################################
                                                #4). Capacity Lower and Upper Limit
##########################################################################################################
'''
def SMR_cap_limit_cons(model):
    return model.SMR_cap <= model.smr_max_mw

def PV_cap_limit_cons(model):
    return  model.PV_cap <= model.solar_max_mw

def wind_cap_limit_cons(model):
    return  model.Wind_cap <= model.solar_max_mw

def nonelc_cap_limit_cons(model, t):
    return model.Nonelc_cap <= model.nonelc_max_mw

def SMR_mincap_limit_cons(model):
    return model.smr_min_mw <= model.SMR_cap 

def PV_mincap_limit_cons(model):
    return model.solar_min_mw <= model.PV_cap 

def wind_mincap_limit_cons(model):
    return model.wind_min_mw <= model.Wind_cap 

def nonelc_mincap_limit_cons(model):
    return model.nonelc_min_mw <= model.Nonelc_cap 
'''        
##########################################################################################################
                                                #4). SMR Technical Parameters and Limits
##########################################################################################################
'''
def SMR_rampup_cons(model,t):
    if t==1:
        return model.SMR_generation[t] <= (model.SMR_generation[model.t_resolution]+model.SMR_cap*model.r_up_limit)
    else:
        return model.SMR_generation[t] <= model.SMR_generation[t-1]+model.SMR_cap*model.r_up_limit
    
def SMR_min_generation_cons(model,t):
    return model.SMR_generation[t] >= model.SMR_cap*model.smr_min_gen_lvl 

def SMR_rampdown_cons(model,t):
    if t==1:        
             return model.SMR_generation[t] >= (model.SMR_generation[model.t_resolution]-model.SMR_cap*model.r_up_limit)
    else:    
             return model.SMR_generation[t] >= (model.SMR_generation[t-1]-model.SMR_cap*model.r_up_limit)

'''        
##########################################################################################################
                                                #5). System Constraints 
##########################################################################################################
'''
def coupling_limit_cons(model,t):
      return model.couple_max_limit * model.import_yes_no[t] >= model.elcmarket_import[t]
  
def coupling_limit_cons2(model,t):
      return (model.couple_max_limit *(1-model.import_yes_no[t])>= model.elc_saleto_market_t[t])
                                            
def demand_supply_balance_cons(model, t):
    return (model.SMR_generation[t] + model.wind_generation[t] + model.PV_generation[t] +\
           model.elcmarket_import[t]) >= (model.elc_saleto_market_t[t] + model.elc_mark_committed_share_t[t] + \
           model.non_elc_Type_1_consumption[t])

def curtailment_cons(model, t):
    return model.curtailment[t] == (model.SMR_generation[t] + model.wind_generation[t] + model.PV_generation[t] +\
          model.elcmarket_import[t] - model.elc_saleto_market_t[t] - model.elc_mark_committed_share_t[t] - \
          model.non_elc_Type_1_consumption[t]) 

def Total_curtailment_cost (model):
    return model.Total_curtail_cost == sum(model.curtailment[i]*\
                        model.curtailment_cost_t[i] for i in model.t_periods)