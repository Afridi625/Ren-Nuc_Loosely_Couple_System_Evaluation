import pandas as pd

xlsx = pd.ExcelFile('Inputs/Inputs.xlsx')
df1= pd.read_excel(xlsx, 'Inp_Parameters_Sets', header=None)  #header None means that start indexation from first row
df2= pd.read_excel(xlsx, 'Inp_Parameters_Single',header=None)
#
def Committed_demand(model, t): #t is period variable
    return float(df1[0][t]) #here t is the row and 0 is the column
#
def elc_mark_committed_supply_price(model, t): #t is period variable
    return float(df1[1][t]) #here t is the row and 1 is the column

#
def Rev_loc_market(model): #t is period variable
    return float(df1[7][t_resolution]) #here t is the row and 1 is the column
#
def elc_mark_spot_price(model, t): #t is period variable
    return float(df1[2][t]) #here t is the row and 2 is the column
#
def e_wind_genprofile_t(model, t): #t is period variable
    return float(df1[3][t]) #here t is the row and 3 is the column
#
def inialize_pv_genprofile_t(model, t): #t is period variable
    return float(df1[4][t]) #here t is the row and 4 is the column

#
def Non_electric_Type_1_value(model, t): #t is period variable
    return float(df1[5][t]) #here t is the row and 4 is the column

#
def elc_curtailment_cost(model, t): #t is period variable
    return float(df1[8][t]) #here t is the row and 8 is the column

#
def t_resolution(model): 
    return int(df2.iat[1,1]) #2nd column, 2nd row
#
def t_sim_period(model): 
    return int(df2.iat[2,1]) #2nd column, 3rd row
#
def t_step_length(model): 
    return int(df2.iat[3,1]) #2nd c.olumn, 4th row
#
def SMR_capex_fixed_cost(model): 
    return float(df2.iat[5,1]) #2nd column, 6th row
#
def wind_capex_fixed_cost(model): 
    return float(df2.iat[6,1]) #2nd column, 7th row
#
def solar_capex_fixed_cost(model): 
    return float(df2.iat[7,1]) #2nd column, 8th row
#
def nonelc_capex_fixed_cost_1(model): 
    return float(df2.iat[8,1]) #2nd column, 9th row
#
def SMR_fuel_var_cost(model): 
    return float(df2.iat[10,1]) #2nd column, 11th row
#
def wind_var_cost(model): 
    return float(df2.iat[11,1]) #2nd column, 12th row
#
def solar_var_cost(model): 
    return float(df2.iat[12,1]) #2nd column, 13th row
#
def nonelc_var_cost_1(model): 
    return float(df2.iat[13,1]) #2nd column, 14th row

#
def smr_min_gen_lvl(model): 
    return float(df2.iat[15,1]) #2nd column, 4th row
#
def r_up_limit(model): 
    return float(df2.iat[16,1]) #2nd column, 4th row
#
def r_down_limit(model): 
    return float(df2.iat[17,1]) #2nd column, 4th row
#
def smr_max_mw(model): 
    return int(df2.iat[19,1]) #2nd column, 4th row
#
def wind_max_mw(model): 
    return int(df2.iat[20,1]) #2nd column, 4th row
#
def solar_max_mw(model): 
    return int(df2.iat[21,1]) #2nd column, 4th row
#
def nonelc_max_mw(model): 
    return int(df2.iat[22,1]) #2nd column, 4th row
#
def smr_min_mw(model): 
    return int(df2.iat[23,1]) #2nd column, 4th row
#
def wind_min_mw(model): 
    return int(df2.iat[24,1]) #2nd column, 4th row
#
def solar_min_mw(model): 
    return int(df2.iat[25,1]) #2nd column, 4th row
#
def nonelc_min_mw(model): 
    return int(df2.iat[26,1]) #2nd column, 4th row
#
def couple_max_limit(model): 
    return int(df2.iat[28,1]) #2nd column, 4th row
#
def non_elc_efficiency_1(model): 
    return float(df2.iat[29,1]) #2nd column, 4th row




















