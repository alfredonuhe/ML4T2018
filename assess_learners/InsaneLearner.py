import numpy as np
import BagLearner as bl
import LinRegLearner as lrl
class InsaneLearner(object):  		   	  			    		  		  		    	 		 		   		 		  
  	def __init__(self, verbose = False):  		   	  			    		  		  		    	 		 		   		 		  
                self.verbose = verbose
                self.learnerList = []
  	def author(self):  		   	  			    		  		  		    	 		 		   		 		  
                return 'aherrero6' # replace tb34 with your Georgia Tech username  		   	  			    		  		  		    	 		 		   		 		  
  	def addEvidence(self,dataX,dataY):  		   	  			    		  		  		    	 		 		   		 		  
                for i in range(0,20):
                        self.learnerList.append(bl.BagLearner(learner = lrl.LinRegLearner, kwargs = {}, bags = 20, boost = False, verbose = False))
                        self.learnerList[i].addEvidence(dataX,dataY)
  	def query(self,points):
                result = np.array(self.learnerList[0].query(points))
                for i in range(1, len(self.learnerList)):
                    result = np.vstack((result, self.learnerList[i].query(points)))
                return np.average(result, axis=0) 		   	  			    		  		  		    	 		 		   		 		  
