# center and standard deviation
import numpy as np

def reciptive_field(input_value,parm):
    """
    sd: stands for standard_dev
    c: center
    q:  number of reciptive field (1..q) # h is insatnce of q
    fs=firing_strenght
    """
    h=np.arange(1,parm.q+1,1) # first reciptive field
    c =(2*h-3)/2/(parm.q-2)
    sd = 1/parm.beta/(parm.q-2)
    
    
    fs = np.exp(-((input_value-c)**2)/(2*(sd**2)))
    firing_time =parm.Time_interval*(1-fs)
    
    # noise of 0.01 add to match paper results # not mention yet
    firing_time=firing_time+0.01
    
    return  np.around(firing_time,decimals=6)




