import math
import sys
import time
import DTLearner as dlr
import RTLearner as rlr
import BagLearner as blr
import InsaneLearner as ilr
import numpy as np
import matplotlib
matplotlib.use("Agg");
import matplotlib.pyplot as plt

def plotDTLearner(trainX, trainY, testX, testY, verbose):
    plotData = np.array([[0,0,0]])
    for i in range(1,trainX.shape[0]):
        learner = dlr.DTLearner(leaf_size = i)
        learner.addEvidence(trainX, trainY) # train it  		   	  			    		  		  		    	 		 		   		 		  
                                                                                                                                                                              
        # evaluate in sample  		   	  			    		  		  		    	 		 		   		 		  
        predY1 = learner.query(trainX) # get the predictions
        trainY.shape = (len(trainY))
        rmse1 = math.sqrt(((trainY - predY1) ** 2).sum()/trainY.shape[0])
        trainY.shape = (len(trainY))
        c1 = np.corrcoef(predY1, y=trainY)

        # evaluate out of sample  		   	  			    		  		  		    	 		 		   		 		  
        predY2 = learner.query(testX) # get the predictions  		   	  			    		  		  		    	 		 		   		 		  
        rmse2 = math.sqrt(((testY - predY2) ** 2).sum()/testY.shape[0])
        c2 = np.corrcoef(predY2, y=testY)

        plotData = np.vstack((plotData, np.array([[i,rmse1,rmse2]])))
        
        if (verbose):
            print learner.author()
            print  		   	  			    		  		  		    	 		 		   		 		  
            print "In sample results"  		   	  			    		  		  		    	 		 		   		 		  
            print "RMSE: ", rmse1  		   	  			    		  		  		    	 		 		   		 		  
            print "corr: ", c1[0,1]	   	  			    		  		  		    	 		 		   		 		  
            print  		   	  			    		  		  		    	 		 		   		 		  
            print "Out of sample results"  		   	  			    		  		  		    	 		 		   		 		  
            print "RMSE: ", rmse2	   	  			    		  		  		    	 		 		   		 		  
            print "corr: ", c[0,1]

    plotData = np.delete(plotData, (0), axis=0)
    
    # Code for plot generation
    plt.figure()
    plt.suptitle('RMSE with leaf size increase', fontsize=12)
    locs, labels = plt.xticks()
    plt.setp(labels, rotation=30)
    plt.ylabel('Rmse')
    plt.xlabel('Leaf size')
    plt.plot(plotData[:,1], label="Training set")
    plt.plot(plotData[:,2], label="Test Set")
    plt.legend(loc='lower right')
    plt.savefig('Figure1.png')
    plt.clf()

def plotBagLearner(trainX, trainY, testX, testY, verbose):
    plotData = np.array([[0,0,0]])
    for i in range(1,trainX.shape[0]):
        learner = blr.BagLearner(learner = dlr.DTLearner, kwargs = {"leaf_size":i}, bags = 20, boost = False, verbose = False)
        learner.addEvidence(trainX, trainY) # train it  		   	  			    		  		  		    	 		 		   		 		  
                                                                                                                                                                              
        # evaluate in sample  		   	  			    		  		  		    	 		 		   		 		  
        predY1 = learner.query(trainX) # get the predictions
        trainY.shape = (len(trainY))
        rmse1 = math.sqrt(((trainY - predY1) ** 2).sum()/trainY.shape[0])
        trainY.shape = (len(trainY))
        c1 = np.corrcoef(predY1, y=trainY)

        # evaluate out of sample  		   	  			    		  		  		    	 		 		   		 		  
        predY2 = learner.query(testX) # get the predictions  		   	  			    		  		  		    	 		 		   		 		  
        rmse2 = math.sqrt(((testY - predY2) ** 2).sum()/testY.shape[0])
        c2 = np.corrcoef(predY2, y=testY)

        plotData = np.vstack((plotData, np.array([[i,rmse1,rmse2]])))
        
        if (verbose):
            print learner.author()
            print  		   	  			    		  		  		    	 		 		   		 		  
            print "In sample results"  		   	  			    		  		  		    	 		 		   		 		  
            print "RMSE: ", rmse1  		   	  			    		  		  		    	 		 		   		 		  
            print "corr: ", c1[0,1]	   	  			    		  		  		    	 		 		   		 		  
            print  		   	  			    		  		  		    	 		 		   		 		  
            print "Out of sample results"  		   	  			    		  		  		    	 		 		   		 		  
            print "RMSE: ", rmse2	   	  			    		  		  		    	 		 		   		 		  
            print "corr: ", c[0,1]

    plotData = np.delete(plotData, (0), axis=0)
    
    # Code for plot generation
    plt.figure()
    plt.suptitle('RMSE with leaf size increase', fontsize=12)
    locs, labels = plt.xticks()
    plt.setp(labels, rotation=30)
    plt.ylabel('Rmse')
    plt.xlabel('Leaf size')
    plt.plot(plotData[:100,1], label="Training set")
    plt.plot(plotData[:100,2], label="Test Set")
    plt.legend(loc='lower right')
    plt.savefig('Figure2.png')
    plt.clf()

def plotDTLearnerVsRTLearner(trainX, trainY, testX, testY, verbose):
    plotData = np.array([[0,0,0,0,0]])
    timeData = np.array([[0,0,0,0,0]])
    varData = np.array([[0,0,0]])
    for i in range(1,trainX.shape[0]):

        # code for DTLearner
        DTlearner = dlr.DTLearner(leaf_size = i)
        DtLearnTime = time.time()
        DTlearner.addEvidence(trainX, trainY) # train it
        DtLearnTime = time.time() - DtLearnTime
                                                                                                                                                                              
        # evaluate in sample
        DtQueryTime = time.time()
        predY1Dt = DTlearner.query(trainX) # get the predictions
        DtQueryTime = time.time() - DtQueryTime
        trainY.shape = (len(trainY))
        rmse1Dt = math.sqrt(((trainY - predY1Dt) ** 2).sum()/trainY.shape[0])
        trainY.shape = (len(trainY))

        # evaluate out of sample
        predY2Dt = DTlearner.query(testX) # get the predictions  		   	  			    		  		  		    	 		 		   		 		  
        rmse2Dt = math.sqrt(((testY - predY2Dt) ** 2).sum()/testY.shape[0])

        # code for RTLearner
        RTlearner = rlr.RTLearner(leaf_size = i)
        RtLearnTime = time.time()
        RTlearner.addEvidence(trainX, trainY) # train it
        RtLearnTime = time.time() - RtLearnTime
                                                                                                                                                                              
        # evaluate in sample
        RtQueryTime = time.time()
        predY1Rt = RTlearner.query(trainX) # get the predictions
        RtQueryTime = time.time() - RtQueryTime
        trainY.shape = (len(trainY))
        rmse1Rt = math.sqrt(((trainY - predY1Rt) ** 2).sum()/trainY.shape[0])
        trainY.shape = (len(trainY))

        # evaluate out of sample
        predY2Rt = RTlearner.query(testX) # get the predictions  		   	  			    		  		  		    	 		 		   		 		  
        rmse2Rt = math.sqrt(((testY - predY2Rt) ** 2).sum()/testY.shape[0])

        plotData = np.vstack((plotData, np.array([[i,rmse1Dt,rmse2Dt,rmse1Rt,rmse2Rt]])))
        timeData = np.vstack((timeData, np.array([[i,DtLearnTime,DtQueryTime,RtLearnTime,RtQueryTime]])))

    for i in range(2,plotData.shape[0]):
        var1 = (plotData[i,2]/plotData[i-1,2])-1
        var2 = (plotData[i,4]/plotData[i-1,4])-1
        varData = np.vstack((varData, np.array([[i,var1,var2]])))

    plotData = np.delete(plotData, (0), axis=0)
    timeData = np.delete(timeData, (0), axis=0)
    varData = np.delete(varData, (0), axis=0)

    # Code for training set rmse plot generation
    plt.figure()
    plt.suptitle('RMSE with leaf size increase', fontsize=12)
    locs, labels = plt.xticks()
    plt.setp(labels, rotation=30)
    plt.ylabel('Rmse')
    plt.xlabel('Leaf size')
    plt.plot(plotData[:100,1], label="DTLearner training set")
    plt.plot(plotData[:100,3], label="RTLearner training set")
    plt.legend(loc='lower right')
    plt.savefig('Figure3.png')
    plt.clf()

    # Code for test set rmse plot generation
    plt.figure()
    plt.suptitle('RMSE with leaf size increase', fontsize=12)
    locs, labels = plt.xticks()
    plt.setp(labels, rotation=30)
    plt.ylabel('Rmse')
    plt.xlabel('Leaf size')
    plt.plot(plotData[:100,2], label="DTLearner test Set")
    plt.plot(plotData[:100,4], label="RTLearner test Set")
    plt.legend(loc='lower right')
    plt.savefig('Figure4.png')
    plt.clf()

    # Code for learning time plot generation
    plt.figure()
    plt.suptitle('DTLearner and RTLearner learn time performace difference', fontsize=12)
    locs, labels = plt.xticks()
    plt.setp(labels, rotation=30)
    plt.ylabel('Time')
    plt.xlabel('Leaf size')
    plt.plot(timeData[:50,1] - timeData[:50,3], label="Time difference (s)")
    plt.legend(loc='upper right')
    plt.savefig('Figure5.png')
    plt.clf()

    # Code for learning time plot generation
    plt.figure()
    plt.suptitle('DTLearner and RTLearner query time performace difference', fontsize=12)
    locs, labels = plt.xticks()
    plt.setp(labels, rotation=30)
    plt.ylabel('Time')
    plt.xlabel('Leaf size')
    plt.plot(timeData[:50,2] - timeData[:50,4], label="Time difference (s)")
    plt.legend(loc='upper right')
    plt.savefig('Figure6.png')
    plt.clf()

    # Code for rsme variation plot generation
    plt.figure()
    plt.suptitle('Variation of rmse in test set with leaf size increase', fontsize=12)
    locs, labels = plt.xticks()
    plt.setp(labels, rotation=30)
    plt.ylabel('Variation')
    plt.xlabel('Leaf size')
    plt.plot(varData[:,1], label="DTLearner rmse variation %")
    plt.plot(varData[:,2], label="RTLearner rmse variation %")
    plt.legend(loc='upper right')
    plt.savefig('Figure7.png')
    plt.clf()

def shuffleData(data, rounds):
    result = data
    randomNumbers = np.random.choice(result.shape[0]-1, result.shape[0], replace=True)
    print randomNumbers
    for i in range(0,rounds):
        if (result.ndim > 1):
            for i in range(0,result.shape[0]):
                randomNumber = randomNumbers[i]
                auxData = result[i,:]
                result[i,:] = result[randomNumber,:]
                result[randomNumber,:] = auxData
        else:
            for i in range(0,result.shape[0]):
                randomNumber = randomNumbers[i]
                auxData = result[i]
                result[i] = result[randomNumber]
                result[randomNumber] = auxData
    return result
  		   	  			    		  		  		    	 		 		   		 		  
if __name__=="__main__":  		   	  			    		  		  		    	 		 		   		 		  
    if len(sys.argv) != 2:  		   	  			    		  		  		    	 		 		   		 		  
        print "Usage: python testlearner.py <filename>"  		   	  			    		  		  		    	 		 		   		 		  
        sys.exit(1)
    inf = open(sys.argv[1])
    # treat Instambul.csv date problem
    if "Istanbul.csv" in sys.argv[1]:
                data = np.array([map(str,s.strip().split(',')) for s in inf.readlines()])
                data = data[1:,1:].astype(np.float)
    else:
        data = np.array([map(float,s.strip().split(',')) for s in inf.readlines()])
  		  		  		    	 		 		   		 		  
    # compute how much of the data is training and testing  		   	  			    		  		  		    	 		 		   		 		  
    train_rows = int(0.6* data.shape[0])  		   	  			    		  		  		    	 		 		   		 		  
    test_rows = data.shape[0] - train_rows
  		   	  			    		  		  		    	 		 		   		 		  
    # separate out training and testing data
    trainX = data[:train_rows,0:-1]  		   	  			    		  		  		    	 		 		   		 		  
    trainY = data[:train_rows,-1]  		   	  			    		  		  		    	 		 		   		 		  
    testX = data[train_rows:,0:-1]  		   	  			    		  		  		    	 		 		   		 		  
    testY = data[train_rows:,-1] 		   	  			    		  		  		    	 		 		   		 		  

    plotDTLearner(trainX, trainY, testX, testY, False)

    plotBagLearner(trainX, trainY, testX, testY, False)

    plotDTLearnerVsRTLearner(trainX, trainY, testX, testY, False)
