import NeuralNet
import NNLayers
import numpy as np
import sklearn
import sklearn.datasets
import sklearn.linear_model
import matplotlib.pyplot as plt

np.random.seed(3) # set a seed so that the results are consistent

DNN = list()

nEpochs = 10000
alpha = 0.1

####################################
def load_planar_dataset():
    np.random.seed(1)
    m = nsamples # number of examples
    N = int(m/2) # number of points per class
    D = 2 # dimensionality
    X = np.zeros((m,D)) # data matrix where each row is a single example
    Y = np.zeros((m,1), dtype='uint8') # labels vector (0 for red, 1 for blue)
    a = 4 # maximum ray of the flower

    for j in range(2):
        ix = range(N*j,N*(j+1))
        t = np.linspace(j*3.12,(j+1)*3.12,N) + np.random.randn(N)*0.2 # theta
        r = a*np.sin(4*t) + np.random.randn(N)*0.2 # radius
        X[ix] = np.c_[r*np.sin(t), r*np.cos(t)]
        Y[ix] = j
        
    X = X.T
    Y = Y.T

    return X, Y
####################################

def load_sign_class_dataset( n ):
    
    X = np.random.randn( 1, n ) * 0.1
    Y = ( X >= 0 )
    return X, Y

#nsamples = 1000
#X, Y = load_planar_dataset()
X, Y = load_sign_class_dataset( 1000 )

NN = NeuralNet.NeuralNet()
NN.Append( NNLayers.InputLayer( X ) )
NN.Append( NNLayers.FeedFwdLayer( nnodes=2, actfcn='Tanh' ) )
NN.Append( NNLayers.FeedFwdLayer( nnodes=1, actfcn='Sigmoid' ) )
NN.Append( NNLayers.OutputLayer( Y, 'CrossEntropy' ) )

NN.Iterate( nEpochs )

plt.plot( NN.Cost )
plt.show()