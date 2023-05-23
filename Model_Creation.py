from pyomo.environ import  Param, RangeSet, NonNegativeReals, Var, Binary
#
from Model_Initialization import Committed_demand, e_wind_genprofile_t,\
    inialize_pv_genprofile_t, elc_mark_committed_supply_price, t_resolution,\
    t_sim_period,SMR_capex_fixed_cost,wind_capex_fixed_cost, solar_capex_fixed_cost, \
    SMR_fuel_var_cost,wind_var_cost,solar_var_cost,smr_max_mw, wind_max_mw,\
     solar_max_mw,smr_min_mw, wind_min_mw,solar_min_mw, t_step_length, Rev_loc_market,\
    nonelc_capex_fixed_cost_1, Non_electric_Type_1_value, nonelc_var_cost_1, nonelc_max_mw,\
    nonelc_min_mw,non_elc_efficiency_1,smr_min_gen_lvl,elc_mark_spot_price, r_up_limit,\
    r_down_limit,couple_max_limit, elc_curtailment_cost
'''   
    ,,\
    smr_min_gen_lvl,r_up_limit,r_down_limit,\
    elc_mark_spot_price,\
    couple_max_limit,,  # Import library with initialitation funtions for the parameters
'''
#
def Model_Creation(model):
    '''
#################################################################################
                                Model time steps and resolution
#################################################################################
    '''  
    # Model time and resolution
    model.t_resolution = Param(initialize=t_resolution) # Number of periods 
    model.t_sim_period = Param(initialize=t_sim_period) # Length of each period (hours)
    model.t_step_length = Param(initialize=t_step_length) # Each period length (hours)
    
    
    
    
    
 
    #Annualized Capex and Fixed O&M Cost
    model.SMR_capex_fixed_cost = Param(initialize=SMR_capex_fixed_cost) # SMR 
    model.wind_capex_fixed_cost = Param(initialize=wind_capex_fixed_cost) # Wind
    model.solar_capex_fixed_cost = Param(initialize=solar_capex_fixed_cost) # Solar
    model.nonelc_capex_fixed_cost_1 = Param(initialize=nonelc_capex_fixed_cost_1) # Non-electric
   # model.Rev_loc_market = Param(initialize=99999999999999, mutable=True)#, rule = Rev_loc_market2) # MW    
    #Fuel cost and variable O&M Cost
    model.SMR_fuel_var_cost = Param(initialize=SMR_fuel_var_cost) # SMR 
    model.wind_var_cost = Param(initialize=wind_var_cost) # Wind
    model.solar_var_cost = Param(initialize=solar_var_cost) # Solar
    model.nonelc_var_cost_1 = Param(initialize=nonelc_var_cost_1) # Non-electric    

    #SMR technical data
    model.smr_min_gen_lvl= Param(initialize=smr_min_gen_lvl) # min generation level 
    model.r_up_limit = Param(initialize=r_up_limit) # Ramp up (%/hr)
    model.r_down_limit = Param(initialize=r_down_limit) # Ramp down (%/hr)
    
    #Installed capacity
    model.smr_max_mw = Param(initialize=smr_max_mw) # SMR max capacity (MW)
    model.wind_max_mw = Param(initialize=wind_max_mw) # Wind max capacity (MW)
    model.solar_max_mw = Param(initialize=solar_max_mw) # Wind max capacity (MW)
    model.nonelc_max_mw = Param(initialize=nonelc_max_mw) # Nonelc max capacity (MW)
    
    model.smr_min_mw = Param(initialize=smr_min_mw) # SMR min capacity (MW)
    model.wind_min_mw = Param(initialize=wind_min_mw) # Wind min capacity (MW)
    model.solar_min_mw = Param(initialize=solar_min_mw) # Wind min capacity (MW)
    model.nonelc_min_mw = Param(initialize=nonelc_min_mw) # Nonelc min capacity (MW)    
    
    #
    model.couple_max_limit = Param(initialize=couple_max_limit) # coupling point capacity (MW) 
    model.non_elc_efficiency_1 = Param(initialize=non_elc_efficiency_1) # non-electric production efficiency
    
    #Sets
    model.t_periods = RangeSet(1, model.t_resolution) # Creation of a set from 1 to the end of resolution
         
    # Committed supply = In inputshet, column 0 and each row.                 
    model.elc_mark_committed_share_t = Param(model.t_periods, initialize=Committed_demand) # Committed demand (MW) 

    # Committed supply price = In inputsheet, column 1 and each row.                 
    model.elc_mark_commSupply_price_t = Param(model.t_periods, initialize=elc_mark_committed_supply_price) # (Curreny/MWh)     
    
    # Sport Market price = In inputsheet, column 2 and each row.                 
    model.elc_market_spot_price_t = Param(model.t_periods, initialize=elc_mark_spot_price) # (Curreny/MWh) 
    
    # Curtailment cost                 
    model.curtailment_cost_t = Param(model.t_periods, initialize = elc_curtailment_cost) # (Curreny/MWh) 
    
    # Wind normilized profile = In inputsheet, column 3 and each row.                 
    model.e_wind_genprofile_t = Param(model.t_periods, initialize = e_wind_genprofile_t) # (%) 
    
    # PV normilized profile = In inputsheet, column 4 and each row.                 
    model.e_pv_genprofile_t = Param(model.t_periods, rule=inialize_pv_genprofile_t) # (%) 
    
    # Non-electric production value = In inputsheet, column 5 and each row.                 
    model.Non_electric_Type_1_value = Param(model.t_periods, initialize = Non_electric_Type_1_value) # (Curreny/unit) 
    
    #Following are variables that are to be optimized
    model.curtailment = Var(model.t_periods, within=NonNegativeReals, initialize=0) # MW 

    model.PV_generation = Var(model.t_periods, within=NonNegativeReals, initialize=0) 

    model.wind_generation = Var(model.t_periods, within=NonNegativeReals, initialize=0)
#Mvariables
    model.SMR_cap = Var(within=NonNegativeReals, initialize=0) # MW
    model.Wind_cap = Var(within=NonNegativeReals, initialize=0) # MW
    model.PV_cap = Var(within=NonNegativeReals, initialize=0) # MW
    model.Nonelc_cap = Var(within=NonNegativeReals, initialize=0) # MW
    
    #import control
    model.import_yes_no =Var(model.t_periods,within=Binary)
    #sets
    model.non_elc_Type_1_consumption = Var(model.t_periods, within=NonNegativeReals, initialize=0) # MW
    model.non_elc_Type_1_production = Var(model.t_periods, within=NonNegativeReals, initialize=0) # MW
    model.elc_saleto_market_t = Var(model.t_periods, within=NonNegativeReals, initialize=0) # MW
    model.elcmarket_import = Var(model.t_periods, within=NonNegativeReals, initialize=0) # MW    
    model.SMR_generation = Var(model.t_periods, within=NonNegativeReals, initialize=0) # MW   
        
#Objective 
    model.Rev_saleto_market = Var(within=NonNegativeReals, initialize=0) # MW
    
#    def Rev_loc_market2 (model):
#        return model.Rev_loc_market == sum(model.elc_mark_committed_share_t[t] * model.elc_mark_commSupply_price_t[t] for t in model.t_periods)
#    model.Rev_loc_market = Var(within=NonNegativeReals)#, rule = Rev_loc_market2) # MW

    model.Total_curtail_cost = Var(within=NonNegativeReals, initialize=0) # MW
    model.Rev_nonelectric_production = Var(within=NonNegativeReals, initialize=0) # MW
    model.Import_Cost = Var(within=NonNegativeReals, initialize=0) # MW
    model.SMR_Variable_andFuel_Chares = Var(within=NonNegativeReals, initialize=0) # MW
    model.Wind_Variable_andFuelChares = Var(within=NonNegativeReals, initialize=0) # MW
    model.Solar_Variable_andFuelChares = Var(within=NonNegativeReals, initialize=0) # MW
    model.Nonelec_Variable_Charges = Var(within=NonNegativeReals, initialize=0) # MW    
    
    model.Rev_loc_market = Param(initialize = Rev_loc_market)
    
      
