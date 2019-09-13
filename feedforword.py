import numpy as np
import matplotlib.pyplot as plt 
from Spike import spike_response_function

def feedforword(reciptive_input,parm,W,threshold,Print=False,stop_at_Threshold=True):
    """
    t_g : globle clock 
    
    potential : Potential at Output Neuron
    
    flag : To find when potential is equal to  threshould
    
    potential_accumulation : For  Potential plot at each global time with step size 0.01
    linspace vas arrange : linspace faster and 

    """
    t=np.linspace(0,parm.Time_interval+1,401)
    index =np.arange(0,len(reciptive_input),1)
    value =W[np.int64((reciptive_input)*100),index]
    potential=np.dot(spike_response_function(reciptive_input,t,parm),value)
    fire_time=np.argmax(potential>threshold)/100
    
        
   # print(np.max(potential_accumulation))
   
    if Print == True:
        #print(np.max(potential_accumulation))
      
        plt.plot(t,potential)
        plt.ylabel("potential")
        plt.xlabel("firing time")

        #print("potential {}".format(y_potential))
        if fire_time>0:
            plt.plot(fire_time,potential[int(fire_time*100)], marker='*', markersize=8, color="red")  
        plt.savefig("potential__accumulation")
        
    if fire_time==0:
        fire_time=4
    else:
        fire_time=fire_time+0.01
    

    return fire_time
