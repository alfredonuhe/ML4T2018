			    		  		  		    	 		 		   		 		    		   	  			    		  		  		    	 		 		   		 		  
import numpy as np  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
class BagLearner(object):  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
    def __init__(self, learner , kwargs, bags = 20, boost = False, verbose = False):
        self.learnerList = []
        self.learner = learner
        self.kwargs = kwargs
        self.bags = bags
        self.boost = boost
        self.verbose = False
        
    def author(self):  		   	  			    		  		  		    	 		 		   		 		  
        return 'aherrero6' # replace tb34 with your Georgia Tech username  		   	  			    		  		  		    	 		 		   		 		  

    def addEvidence(self,dataX,dataY):  		   	  			    		  		  		    	 		 		   		 		  
        """  		   	  			    		  		  		    	 		 		   		 		  
        @summary: Add training data to learner  		   	  			    		  		  		    	 		 		   		 		  
        @param dataX: X values of data to add  		   	  			    		  		  		    	 		 		   		 		  
        @param dataY: the Y training values  		   	  			    		  		  		    	 		 		   		 		  
        """
        dataY.shape = (dataY.shape[0],1)
        data = np.hstack((dataX, dataY))
        dataSize = data.shape[0]
        
        for i in range(0, self.bags):
            self.learnerList.append(self.learner(**self.kwargs))
            bagData = np.array(data[np.random.random_integers(dataSize-1),:])
            for j in range(0,dataSize):
                bagData = np.vstack((bagData, data[np.random.random_integers(dataSize-1),:]))
            
            bagData = np.delete(bagData, (0), axis=0)
            self.learnerList[i].addEvidence(bagData[:,:-1], bagData[:,-1])
        
    def query(self,points):  		   	  			    		  		  		    	 		 		   		 		  
        """  		   	  			    		  		  		    	 		 		   		 		  
        @summary: Estimate a set of test points given the model we built.  		   	  			    		  		  		    	 		 		   		 		  
        @param points: should be a numpy array with each row corresponding to a specific query.  		   	  			    		  		  		    	 		 		   		 		  
        @returns the estimated values according to the saved model.  		   	  			    		  		  		    	 		 		   		 		  
        """
        result = np.array(self.learnerList[0].query(points))
        
        for i in range(1, self.bags):
            result = np.vstack((result, self.learnerList[i].query(points)))

        if(result.ndim > 1): result = np.average(result, axis=0)
        return result
    
if __name__=="__main__":  		   	  			    		  		  		    	 		 		   		 		  
    print "This class is BagLearner"  		   	  			    		  		  		    	 		 		   		 		  
