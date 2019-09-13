
import numpy as np 

def efficanychange(reciptive_input,t,parm):
    """
    efficacy change delta 
    t:: postsynaptic firing ta :: actual firing time  output td :desired
    ti :: fire time of presynpatic neuron 
    dealy : posynaptic_time - presynaptic_time
    -A : it is zero beacause only one posynaptic are consider after that ingnore

    """
    delay=t-reciptive_input
    efficany_change =np.zeros((delay.shape[0]))
    efficany_change[np.where(delay>=0)]=parm.A*np.exp(-delay[np.where(delay>=0.0)]/parm.efficacy_value)
    
    efficany_change[np.where(delay<0)]=0

    return efficany_change 

def fractional_contribution(reciptive_input,t,parm,check=False):
    """
    Store factional contribution of each presynaptic spike (tik)to fire a postsynaptic
    
    value of A does not matter A/A while  calculation fractional contribution
    
    """
    
    value=efficanychange(reciptive_input,t,parm)
    
    
    # check sum is 1
    if check==True:
        print("Total fractional contribution is {}"  \
              .format(np.sum(value/np.sum(value))))
    return value/np.sum(value)