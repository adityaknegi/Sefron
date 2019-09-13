# update weight
from efficacy_fractional_contribution import fractional_contribution
from weight_intialized import gaussian_function
from Overall_strength_error import error
import numpy as np
def efficacy_update(reciptive_input,td,output_time,parm,threshold):
    utd=fractional_contribution(reciptive_input,td,parm)
    wik=((parm.learning_rate)*(utd))*error(reciptive_input,td,output_time,parm,threshold) 
    return wik


# update_weight
def update_weight(reciptive_input,y,output_time,w,parm,threshold):
    dwik=efficacy_update(reciptive_input,y,output_time,parm,threshold)
    t=np.linspace(0,parm.Time_interval,301)
    w=w + dwik*gaussian_function(reciptive_input,t,parm)
    return w