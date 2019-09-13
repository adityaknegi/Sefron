from feedforword import feedforword
def predict(X_test,y_test,parm,w,threshold):
    accu=0
    for X,y in zip(X_test,y_test):
        output=feedforword(X,parm,w,threshold)
        accu+=1 if (output > 3 and y==4) or (output<=3 and y==2) else 0 
    return accu/len(X_test)*100
