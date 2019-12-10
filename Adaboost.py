from auxilaryFunctions import *
from creating_classifiers import read_dataset
#import multiprocessing as mulp
#import functools
            
#min_error = float('inf')


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

 
#  Boosting method that uses a number of weak classifiers in ensemble to make a strong classifier.
#  This implementation uses decision stumps, which is a one level Decision Tree. 
#     Parameters:
#     -----------
#     n_clf: int
#         The number of weak classifiers that will be used. 

class Adaboost():
    #number of weak classifiers
    def __init__(self, n_clf=100):
        self.n_clf = n_clf
        
    def fit(self, X, y):
        m_samples, n_features = np.shape(X)
        # Initialize 'M' weights to 1/M
        w = np.ones([m_samples,1])
        w /= m_samples
        #list of classifiers
        self.clfs = []
        min_error = float('inf')
        # Iterate through classifiers
        for ev in range(self.n_clf):
            #Create Decision Stump
            self.clf = DecisionStump()

            # Minimum error given for using a certain feature value threshold
            # for predicting sample label
           
            # Iterate throught every unique feature value and see what value
            # makes the best threshold for predicting y
            #for feature_i in range (n_features):
            for feature_i in range (4):
                if(feature_i%1000 == 0):
                    print (f'classifier: {ev} feature: {feature_i}')
                feature_values = np.expand_dims(X[:, feature_i], axis=1)
                unique_values = np.unique(feature_values)
                # Try every unique feature value as threshold
                for threshold in unique_values:
                    p = 1
                    # Set all predictions to '1' initially
                    prediction = np.ones(np.shape(y))

                    # Label the samples whose values are below threshold as '-1'
                    #To detect false examples
                    prediction[X[:, feature_i] < threshold] = -1

                    # Error = sum of weights of misclassified samples
                    miss_W = np.zeros([m_samples])
                    for i in range(m_samples):
                        if(y[i] != prediction[i]):
                            miss_W[i] = w[i]
                    error = sum(miss_W)
                    
                    # If the error is over 50% we flip the polarity so that samples that
                    # were classified as 0 are classified as 1, and vice versa
                    # E.g error = 0.8 => (1 - error) = 0.2
                    if error > 0.5:
                        error = 1 - error
                        p = -1

                    
                    # If this threshold resulted in the smallest error we save the
                    # configuration
                    #global min_errors
                    if error < min_error:
                        clf.polarity = p
                        clf.threshold = threshold
                        clf.feature_index = feature_i
                        min_error = error

            # Calculate the alpha which is used to update the sample weights,
            # Alpha is also an approximation of this classifier's proficiency
            epsilon = 1e-10
            clf.alpha = 0.5 * math.log((1.0 - min_error) / (min_error + epsilon))

            # Set all predictions to '1' initially
            predictions = np.ones(np.shape(y))

            # The indexes where the sample values are below threshold
            negative_idx = (clf.polarity * X[:, clf.feature_index] < clf.polarity * clf.threshold)

            # Label those as '-1'
            predictions[negative_idx] = -1

            # Calculate new weights 
            # Missclassified samples gets larger weights and correctly classified samples smaller
            yByPred = (y * predictions)
            alpha_Y_Pred = clf.alpha * yByPred
            w *= np.exp(-alpha_Y_Pred)
            # Normalize to one
            w /= np.sum(w)

            # Save classifier
            self.clfs.append(clf)
            #Removing the choosen feature, so as not to be choosen again
            #X = np.delete(X,clf.feature_index,axis=1)
            


    def predict(self, X):
        m_samples = np.shape(X)[0]
        y_pred = np.zeros([m_samples, 1])

        # For each classifier => label the samples
        for clf in self.clfs:
            # Set all predictions to '1' initially
            predictions = np.ones(np.shape(y_pred))
            # The indexes where the sample values are below threshold
            negative_idx = (clf.polarity * X[:, clf.feature_index] < clf.polarity * clf.threshold)
            # Label those as '-1'
            predictions[negative_idx] = -1

            # Add predictions weighted by the classifiers alpha
            # (alpha indicative of classifier's proficiency)
            y_pred += clf.alpha * predictions

        # Return sign of prediction sum
        y_pred = np.sign(y_pred).flatten()

        return y_pred

    def storeClassifiers (self):
        Classifiers_Path = "Classifiers/CLFS.txt"
        file_output = open(Classifiers_Path,"w+")

        for clf in self.clfs:
            file_output.write(str(clf.feature_index) +" "+str(clf.threshold) +" "+str(clf.alpha) +" "+str(clf.polarity) +"\n")

        file_output.close()
        return

            





if __name__ == '__main__':
    #First we get the data
    print ("Training the 160K features to obtain the best 4370 one of them.")
    print ("Reading the Data")
    X, Y = read_dataset()
    print ("Make sure of their shapes :")
    print (f'Shape of X is {X.shape} --> it should be (23089, 162336)')
    print (f'Shape of Y is {Y.shape} --> it should be (23089, 1)')
    assert (X.shape == (23089, 162336)),"X's shape is not correct"
    assert (Y.shape == (23089, 1)),"X's shape is not correct"

    #80% is training data and 20% is testing
    Ntrain  = int(1*len(X))

    Xtrain,Ytrain = X[:Ntrain ,:], Y[:Ntrain,:]
    Xtest,Ytest = X[Ntrain:,:], Y[Ntrain:,:]
    
    #This number is taken from the paper itself (4370)
    print ("Starting the training stage....")
    clf = Adaboost(n_clf=4370)
    clf.fit(Xtrain, Ytrain)
    print ("Finished training, lets store the trained classifiers..")
    clf.storeClassifiers()
    #This prediction is linearizing them, it doesn't obey the principle of cascading
    # Thus it consumes a lot of time, also, it's used on already sampled data 
    # print("Done Storing, lets check on the accuracy tested on 5%' on the sampled data")
    # y_pred = clf.predict(Xtest)
    # accuracy = accuracy_score(Ytest, y_pred)
    # print ("Accuracy:", accuracy)
