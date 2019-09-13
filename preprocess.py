from sklearn.model_selection import train_test_split

def preprocess(X,y):
    return train_test_split(X, y, test_size=0.5, random_state=102)
