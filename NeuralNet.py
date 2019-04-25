import LossFunctions
import numpy as np

class NeuralNet:
    def __init__( self ):
        self.nnLayers = list()
        self.nLayers = 0

        # Hyperparameters
        self.learningRate = 0.5

        self.Cost = np.array([[]])
        
    def Append( self, nnLayer ):
        self.nnLayers.append( nnLayer )
        
        if self.nLayers > 0:      
            self.nnLayers[-1].SetNNodesPrev( self.nnLayers[-2].GetNNodes() )
            self.nnLayers[-1].Initialize()
    
        self.nLayers += 1

    def ForwardProp( self ):
        A = None
        for i in range( self.nLayers ):
            A = self.nnLayers[i].ForwardProp( A )

    def BackwardProp( self ):
        dA = None
        for i in range( self.nLayers-1, -1, -1 ):
            dA = self.nnLayers[i].BackwardProp( dA )  

    def UpdateParams( self, alpha ):
        for i in range( self.nLayers ):
            #print( i )
            A = self.nnLayers[i].UpdateParams( alpha )
        
    def ComputeCost( self ):
        loss = self.nnLayers[-1].L # 
        C = -1/np.shape( loss )[1] * np.sum( loss )
        self.Cost = np.append( self.Cost, np.array([[C]]) )

    def Train( self, nEpochs ):
        for i in range( 0, nEpochs+1 ):
            self.ForwardProp()
            self.BackwardProp()
            self.UpdateParams( self.learningRate )
            self.ComputeCost()

            if i % 100 == 0:
                print( '=> Epoch %i: Cost=%.6f, w1=%s' % (i,self.Cost[-1],np.array2string(self.nnLayers[1].W.T)) )       
                #print( 'BackwardProp: dW=%s, db=%s' % (np.array2string(self.nnLayers[1].dW.T),np.array2string(self.nnLayers[1].db.T)) )        
   
    def Eval( self, X, Y ):
        self.nnLayers[0].SetData( X )
        self.nnLayers[-1].SetData( Y )
        self.ForwardProp()
        Yest = ( self.nnLayers[-1].A_prev >= 0.5 )
        rateCorrect = np.mean( Yest == Y )
        return rateCorrect

    def Reset( self ):
        pass
