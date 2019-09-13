import numpy as np
from efficacy_fractional_contribution import fractional_contribution

def gaussian_function(reciptive_input,t,parm):
	t=t.reshape(-1,1)
	reciptive_input=np.tile(reciptive_input,len(t)).reshape(-1,13)

	return np.exp(-np.power((t-reciptive_input),2)/2/(np.power(parm.sigma,2)))


def time_weight_intialized(reciptive_input,y,parm):
    
    """  
    for texting potential at equation 22 and 23 true
    parameters['wik']=np.multiply(parameters['wik'],gaussian_function(reciptive_input,reciptive_input))

    np.sum(parameters['wik']*spike_response_function(y,reciptive_input))

    """
    t=np.linspace(0,parm.Time_interval,301)
    return fractional_contribution(reciptive_input,y,parm)*gaussian_function(reciptive_input,t,parm)