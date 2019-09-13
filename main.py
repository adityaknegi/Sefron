import numpy as np
from parameter_intialized import parm
from Spike_time import spike_time
from Norm_STDP import V_STDP
from weight_intialized import time_weight_intialized
from train import train
parameters ={}
parameters['x1'], parameters['x2'] = None,None
# for tracking output fire time


# input is normalized 0 tp 1
# class1 x1, x2 0 to 0.4 x2 class x2 , x2 0.6 to 1
np.random.seed(1995)
for x in ('x1','x2'):
    # x1 then x2 
    parameters[x] =np.concatenate([np.random.rand(50) *0.4,np.random.rand(50) *0.4 +0.6])
# desired ouput time
parameters['class']=np.concatenate([np.ones(50)*2,np.ones(50)*4])
parameters["ouput_fire_time"]=4 # -1 for no fire parameters["ouput_fire_time"]
yy=(np.concatenate((parameters['x1'].reshape(-1,1),parameters['x2'].reshape(-1,1),parameters['class'].reshape(-1,1)),axis=1))
X = yy[:,:2]
y=yy[:,-1]
parm=parm()

parameters['input'],parameters['y']=spike_time(X,y,parm)
reciptive_input = parameters['input'][0]
output=parameters['y'][0]

threshold=V_STDP(reciptive_input,output,parm)
print(threshold)
parameters['w']=np.zeros((301,13))
parameters['w']=time_weight_intialized(reciptive_input,output,parm)
epoch=10
train(epoch,parameters['input'],parameters['class'],parameters['w'],parm,threshold)