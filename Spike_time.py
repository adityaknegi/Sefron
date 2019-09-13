
import numpy as np
from reciptive_field import reciptive_field


def spike_time(X,y,parm):
    # 1 for bias
    parameters=np.zeros((X.shape[0],X.shape[1]*(parm.q)+1))
    for row in range(X.shape[0]):
        for col in range(X.shape[1]):
            i_col=col*parm.q+1
            parameters[row,i_col:i_col+parm.q]=reciptive_field(X[row,col],parm)
    return parameters,y