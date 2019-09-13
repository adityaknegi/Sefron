import numpy as np
def spike_response_function(t_i_k,t,parm):
    if isinstance(t,(np.ndarray,list)):
        s=t.reshape(-1,1)-np.tile(t_i_k,len(t)).reshape(-1,13)
    else:
        s=t-t_i_k
        
    x=s/parm.toh
    s_r_f = x*np.exp(1-x)
    s_r_f[np.where(s_r_f<=0)]=0
    return s_r_f