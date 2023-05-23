
from pyomo.environ import  AbstractModel

from Model_Results import Load_results1, Load_results2
#    Percentage_Of_Use, Energy_Flow, Energy_Participation, LDR, Load_results1_Integer, Load_results2_Integer,\
#    Load_results1_Dispatch, Load_results2_Dispatch 
from Model_Creation import Model_Creation
from Model_Resolution import Model_Resolution
#from Economical_Analysis import Levelized_Cost_Of_Energy

model = AbstractModel() # define type of optimization problem
#1:
Model_Creation(model) # Creation of the Sets, parameters and variables.
#2:
instance = Model_Resolution(model) # Resolution of the instance

Time_Series = Load_results1(instance) # Extract the results of energy from the instance and save it in a excel file 
Results = Load_results2(instance)







