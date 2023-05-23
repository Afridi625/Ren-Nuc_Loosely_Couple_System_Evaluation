from pyomo.opt import SolverFactory
from pyomo.environ import Objective, maximize, Constraint
from pyomo.util.infeasible import log_infeasible_constraints
import logging

def Model_Resolution(model):   
    '''
    This function creates the model and call Pyomo to solve the instance of the proyect 
    :param model: Pyomo model as defined in the Model_creation library  
    :return: The solution inside an object call instance.
    '''
    
    from Model_Constraints import  Net_Present_Cost, PV_generation_cons,\
        wind_generation_cons,demand_supply_balance_cons,SMR_cap_limit_cons,\
        SMR_generation_cons, PV_cap_limit_cons,wind_cap_limit_cons, SMR_mincap_limit_cons,\
        PV_mincap_limit_cons,wind_mincap_limit_cons, SMR_Variable_andFuel_Chares2, Solar_Variable_andFuelChares,\
        Wind_Variable_andFuelChares, Rev_nonelectric_production,Nonelec_Variable_Charges, nonelc_Type_1_production_cons,\
        nonelc_cap_limit_cons,nonelc_mincap_limit_cons, nonelc_Type_1_consumption_cons, Total_curtailment_cost,\
        coupling_limit_cons, Rev_saleto_market, Import_Cost,coupling_limit_cons2,SMR_rampup_cons
        
        #,min_generation_cons# ,,curtailment_cons,,SMR_rampdown_cons,SMR_min_generation_cons
        
    #Model objective function construction
    model.ObjectiveFuntion = Objective(rule=Net_Present_Cost, sense=maximize)    
    # 
    model.SMR_generation_constraint  = Constraint(model.t_periods, rule = SMR_generation_cons)
    #
    model.PV_generation_constraint = Constraint(model.t_periods, rule = PV_generation_cons)
    # 
    model.wind_generation_constraint  = Constraint(model.t_periods, rule = wind_generation_cons)
    # 
    model.nonelc_Type_1_consumption_cons  = Constraint(model.t_periods, rule = nonelc_Type_1_consumption_cons)    

    #
    model.Totalcurtailment_cost_cons = Constraint(rule = Total_curtailment_cost)
    
    model.Nonelec_VariableCharges = Constraint(rule = Nonelec_Variable_Charges)
    #
    model.nonelc_Type_1_production_constraint = Constraint(model.t_periods, rule=nonelc_Type_1_production_cons)
    #
    model.SMR_Rampup_constraint = Constraint(model.t_periods, rule=SMR_rampup_cons)
    #
    #model.SMR_Rampdown_constraint = Constraint(model.t_periods, rule=SMR_rampdown_cons)
    #
    model.demand_supply_balance_cons = Constraint(model.t_periods, rule=demand_supply_balance_cons)   
    #
    model.coupling_limit_constraint = Constraint(model.t_periods, rule=coupling_limit_cons)
    #
    model.coupling_limit_constraint = Constraint(model.t_periods, rule=coupling_limit_cons2)
    #
    model.SMR_cap_limit_constraint = Constraint(rule=SMR_cap_limit_cons)
    #
    model.PV_cap_limit_constraint = Constraint(rule=PV_cap_limit_cons)   
    #
    model.wind_cap_limit_constraint = Constraint(rule=wind_cap_limit_cons)     
    #
    model.nonelc_cap_limit_constraint = Constraint(model.t_periods, rule=nonelc_cap_limit_cons)
    #
    model.SMR_mincap_limit_constraint = Constraint(rule=SMR_mincap_limit_cons)
    #
    model.PV_mincap_limit_constraint = Constraint(rule=PV_mincap_limit_cons)   
    #
    model.wind_mincap_limit_constraint = Constraint(rule=wind_mincap_limit_cons)     
    #
    model.nonelc_mincap_limit_constraint = Constraint(rule=nonelc_mincap_limit_cons)
    #
    # Constraint use to calculate variable values being used in objective function
    model.SMR_VariableandFuelChares = Constraint(rule = SMR_Variable_andFuel_Chares2)
    model.Solar_VariableandFuelChares = Constraint(rule = Solar_Variable_andFuelChares)
    model.Wind_VariableandFuelChares = Constraint(rule = Wind_Variable_andFuelChares)
    model.RevNonelcPrduction = Constraint(rule = Rev_nonelectric_production)  
    #model.Revelclocmarket = Constraint(rule = Rev_loc_market)
    model.Rev_saletomarket = Constraint(rule = Rev_saleto_market)
    model.Elcimpcost = Constraint(rule = Import_Cost)
    #model.SMR_min_gen_constraint = Constraint(model.t_periods, rule=SMR_min_generation_cons)
    #
   # model.curtailment_constraint = Constraint(model.t_periods, rule=curtailment_cons)
    
    instance = model.create_instance() # load parameters       
    instance.pprint()
    for con in instance.component_map(Constraint).itervalues():
        con.pprint()
    opt = SolverFactory('glpk') # Solver use during the optimization    
    results = opt.solve(instance, tee=True) # Solving a model instance 
    log_infeasible_constraints(instance,log_expression=True, log_variables=True)
    logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.INFO)
    instance.solutions.load_from(results)  # Loading solution into instance'
    #instance.display()
    return instance
