from  efficacy_fractional_contribution import fractional_contribution
from Spike import spike_response_function

import numpy as np 



def V_STDP(reciptive_input,t,parm):
    """
    ideal posynaptic potential at time of firing 
    t: ouput firing time (ta or td) example parameters['ouput_fire_time'] or parameters['class'][i](one value)
    
    """
    f_c=fractional_contribution(reciptive_input,t,parm)

    value=np.matmul(spike_response_function(reciptive_input,t,parm),f_c)    
    return value