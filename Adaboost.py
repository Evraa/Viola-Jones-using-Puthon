from auxilaryFunctions import *
#Class for stumps
class DecisionStump():
    def __init__(self):
        # Determines if sample shall be classified as -1 or 1 given threshold
        self.polarity = 1
        # The index of the feature used to make classification
        self.feature_index = None
        # The threshold value that the feature should be measured against
        self.threshold = None
        # Value indicative of the classifier's accuracy
        self.alpha = None

#Class for Adaboost
class Adaboost:
    #M: is the #of base learners
    def __init__(self,M):
        self.M = M
    def fit(self,X,Y):
        #Variables for decision stumps and their corresponding alphas
        self.models = []
        self.alphas = []
        #n: #od examples 
        N, _ = X.shape
        #W: array of weights fo each example, initialized with uniform equal values for all of them
        W = np.ones(N) / N 
        #We create punch of M stumps
        for m in range(self.M):
            tree = DecisionTreeClassifier(max_depth=1)
            tree.fit(X,Y,sample_weight=W)
            P = tree.predict(X)
        #Calculate the error
        err = W.dot(P != Y)
        alpha = 0.5*(np.log(1-err) - np.log(err))
        #Store theri alphas
        W = W*np.exp(-alpha*Y*P)
        W = W/W.sum()
        #And then store these stumps
        self.models.append(tree)
        self.alphas.append(alpha)

    def predict(self,X):
        #we need to return accuracy here
        N, _= X.shape
        FX = np.zeros(N)
        for alpha, tree in zip(self.alphas ,self.models):
            FX += alpha*tree.predict(X)
                #First return the accuracy
        return np.sign(FX), FX

    def score(self,X,Y):
        P,FX = self.predict(X)
        L = np.exp(-Y*FX).mean()
        return np.mean(P == Y) , L


if __name__ == '__main__':
    #First we get the data
    dataSet = datasets.load_digits()
    X = dataSet.data
    Y = dataSet.target
    digit1 = 1
    digit2 = 8
    idx = np.append(np.where(Y == digit1)[0], np.where(Y == digit2)[0])
    Y = dataSet.target[idx]
    # Change labels to {-1, 1}
    Y[Y == digit1] = -1
    Y[Y == digit2] = 1
    X = dataSet.data[idx]

    #80% is training data and 20% is testing
    Ntrain  = int(0.8*len(X))
    Xtrain,Ytrain = X[:Ntrain], Y[:Ntrain]
    Xtest,Ytest = X[Ntrain:], Y[Ntrain:]
    
    #T = # od iterations
    
    T = 200
    train_errors = np.empty(T)
    test_losses = np.empty(T)
    test_errors = np.empty(T)
    for num_trees in range(T):
        if num_trees == 0:
            train_errors [num_trees] = None
            test_errors [num_trees] = None
            test_losses [num_trees] = None
            continue
        if num_trees % 20 == 0:
            print (num_trees)
        model = Adaboost(num_trees)
        model.fit(Xtrain, Ytrain)
        acc , loss = model.score(Xtest,Ytest)
        acc_train, _ = model.score(Xtrain ,Ytrain)

        train_errors [num_trees] = 1 - acc_train
        test_errors [num_trees] = 1 - acc
        test_losses [num_trees] = loss
        
        if num_trees == T-1:
            print("Finalt train error" , 1 - acc_train)
            print("Finalt test error" , 1 - acc)

    plt.plot(test_errors , label="test errors")
    plt.plot(test_losses , label="test loss")
    plt.legend()
    plt.show()

    plt.plot(train_errors , label="train errors")
    plt.plot(test_errors , label="test errors")
    plt.legend()
    plt.show()

    
        