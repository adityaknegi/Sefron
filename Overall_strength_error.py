from Norm_STDP import V_STDP

def overall_strength(reciptive_input,to,parm,threshold):
    """
    determine overall strength required by syanptices to make firing poosible 
    """
    
    return threshold/V_STDP(reciptive_input,to,parm)

def error(reciptive_input,y,output_time,parm,threshold):
    """
    ta : actual output
    td : desired output
    
    """
    
    td=y
    ta=output_time
    E =overall_strength(reciptive_input,td,parm,threshold)- overall_strength(reciptive_input,ta,parm,threshold)
    
    return E
