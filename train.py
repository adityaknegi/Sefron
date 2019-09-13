from preprocess import preprocess
from feedforword import feedforword
from update import update_weight
from predict import predict
def train(epochs,X,y,W,parm,threshold):
    X_train, X_test, y_train, y_test = preprocess(X,y)

    for epoch in range(epochs):
        for Xi,yi in zip(X_train,y_train):
            time=feedforword(Xi,parm,W,threshold)
            if  time<=3 and yi==4:
                W=update_weight(Xi,yi,time,W,parm,threshold)
            elif time>=3.0 and yi==2:
                W=update_weight(Xi,yi,time,W,parm,threshold)
            #print(" fire at {} desired {} ".format(time,yi))
        print('epoch {} Train accuracy {} Test accuracy {}'.format(epoch,predict(X_train,y_train,parm,W,threshold),predict(X_test,y_test,parm,W,threshold)))


            