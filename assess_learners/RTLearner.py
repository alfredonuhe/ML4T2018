import numpy as np  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
class RTLearner(object):  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
    def __init__(self, leaf_size = 1, verbose = False):
        self.leaf_size = leaf_size
        self.verbose = verbose
        self.tree = None
  		   	  			    		  		  		    	 		 		   		 		  
    def author(self):  		   	  			    		  		  		    	 		 		   		 		  
        return 'aherrero6' # replace tb34 with your Georgia Tech username  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
    def addEvidence(self,dataX,dataY):  		   	  			    		  		  		    	 		 		   		 		  
        """  		   	  			    		  		  		    	 		 		   		 		  
        @summary: Add training data to learner  		   	  			    		  		  		    	 		 		   		 		  
        @param dataX: X values of data to add  		   	  			    		  		  		    	 		 		   		 		  
        @param dataY: the Y training values
        """

        if dataX.shape[0] <= self.leaf_size: return np.array([-1, np.mean(dataY), -1, -1])

        if np.allclose(dataY, dataY[0]): return np.array([-1, dataY[0], -1, -1])
        else:
            i = int(np.random.choice(dataX.shape[1], 1))
            splitVal = np.median(dataX[:,i])
            
            dataY.shape = (len(dataY),1)
            data = np.hstack((dataX, dataY))
            leftDataX = data[data[:,i] <= splitVal][:,:-1]
            leftDataY = data[data[:,i] <= splitVal][:,-1]
            rightDataX = data[data[:,i] > splitVal][:,:-1]
            rightDataY = data[data[:,i] > splitVal][:,-1]

            if int(leftDataY.shape[0]) == 0 or int(rightDataY.shape[0]) == 0:
                return np.array([-1, np.mean(dataY), -1, -1])
            
            leftTree = self.addEvidence(leftDataX, leftDataY)
            rightTree = self.addEvidence(rightDataX, rightDataY)

            if leftTree.ndim == 1:
                root = np.array([i, splitVal, 1, 1+1])
            else:
                root = np.array([i, splitVal, 1, leftTree.shape[0]+1])

            result = np.vstack((root, leftTree, rightTree))

            if self.verbose == True:
                print "\nRoot ------------------"
                print root
                print "\nLeft ------------------"
                print leftTree
                print leftTree.shape
                print leftTree.ndim
                print "\nRight ------------------"
                print rightTree
                print "\nResult ------------------"
                print result

            self.tree = result
            return result
        
    def query(self,points):  		   	  			    		  		  		    	 		 		   		 		  
        """  		   	  			    		  		  		    	 		 		   		 		  
        @summary: Estimate a set of test points given the model we built.  		   	  			    		  		  		    	 		 		   		 		  
        @param points: should be a numpy array with each row corresponding to a specific query.  		   	  			    		  		  		    	 		 		   		 		  
        @returns the estimated values according to the saved model.  		   	  			    		  		  		    	 		 		   		 		  
        """
        
        result = np.array([])
        
        if self.verbose == True:
            print self.tree
        
        for i in range(0,points.shape[0]):
            currentNode = 0
            while self.tree[currentNode,0] != -1:
                if points[i, int(self.tree[currentNode, 0])] <= self.tree[currentNode, 1]:
                    currentNode = currentNode + int(self.tree[currentNode,2])
                else:
                    currentNode = currentNode + int(self.tree[currentNode,3])
                    
            result = np.append(result, [self.tree[currentNode,1]])

        return result	   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
if __name__=="__main__":  		   	  			    		  		  		    	 		 		   		 		  
    print "This class is RTLearner"  		   	  			    		  		  		    	 		 		   		 		  
