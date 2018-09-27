import numpy as np
import matplotlib
matplotlib.use("Agg");
import matplotlib.pyplot as plt
import random
                                                                                                                                                                          
def author():                                                                                                                                                                     
        return 'aherrero6'                                                                                                                                                                        
                                                                                                                                                                          
def gtid():                                                                                                                                                                       
        return 903454513                                                                                                                                                                          
                                                                                                                                                                          
def get_spin_result(win_prob):                                                                                                                                                                            
        result = False                                                                                                                                                                            
        if np.random.random() <= win_prob:                                                                                                                                                                        
                result = True                                                                                                                                                                     
        return result                                                                                                                                                                     
                                                                                                                                                                          
def unrealisticSimulator(seed, winAmount):
        winnings = np.array([0]);
        win_prob = 0.5 # set appropriately to the probability of a win                                                                                                                                                                            
        np.random.seed(seed) # do this only once                                                                                                                                                                                         
                                                                                                                                                                          
        # add your code here to implement the experiments
        episodeWinnings = 0;
        while (episodeWinnings < winAmount):
                won = False;
                betAmount = 1;
                while (won is False):
                        won = get_spin_result(win_prob);
                        if (won):
                                episodeWinnings = episodeWinnings + betAmount;
                                winnings = np.append(winnings,np.array([episodeWinnings]));
                        else:
                                episodeWinnings = episodeWinnings - betAmount;
                                betAmount = betAmount*2;
                                winnings = np.append(winnings,np.array([episodeWinnings]));
        return winnings;

def realisticSimulator(seed, winAmount, maxLoss):
        winnings = np.array([0]);
        win_prob = 0.5 # set appropriately to the probability of a win                                                                                                                                                                            
        np.random.seed(seed) # do this only once                                                                                                                                                                                         
                                                                                                                                                                          
        # add your code here to implement the experiments
        episodeWinnings = 0;
        while (episodeWinnings < winAmount):
                won = False;
                betAmount = 1;
                while (won is False):
                        won = get_spin_result(win_prob);
                        if (won):
                                episodeWinnings = episodeWinnings + betAmount;
                                winnings = np.append(winnings,np.array([episodeWinnings]));
                        else:
                                episodeWinnings = episodeWinnings - betAmount;
                                betAmount = betAmount*2;
                                winnings = np.append(winnings,np.array([episodeWinnings]));
                        # Additional condition for realistic simulator
                        if((episodeWinnings-betAmount)<(-maxLoss)): return winnings;
        return winnings;

def experiment1Figure1():
        ##  Graph drawing 
        plt.figure();
        plt.suptitle('Figure 1: 10 runs with unrealistic simulator', fontsize=12)
        plt.xlim([0, 300])
        plt.ylim([-256, 100])
        for x in range(0,10):
                result = unrealisticSimulator(int(round(random.random(),3)*100), 80);
                plt.plot(result, label=str("simulation#" + str(x)));
        plt.legend(loc='upper right');
        plt.savefig('Figure1.png');
        plt.clf();
        print("Figure 1 done.");

def experiment1Figure2():
##      Data collection    
        data = None;
        for i in range(0,1000):
                newRow = list(unrealisticSimulator(int(round(np.random.random(),3)*100), 80));
                if (len(newRow) > 300):
                        newRow = newRow[0:300];
                else:
                        lastValue = newRow[len(newRow)-1];
                        for j in range(0,(300-len(newRow))):
                                newRow.append(lastValue);
                if(i==0):
                        data = np.array(newRow);
                else:
                        data = np.vstack([newRow, data]);
##      Graph drawing     
        meanArray = np.mean(data, axis=0);
        stdUpArray = meanArray + np.std(data, ddof=1);
        stdDownArray = meanArray - np.std(data, ddof=1);
        plt.figure();
        plt.suptitle('Figure 2: Mean and std of 1000 runs\nwith unrealistic simulator', fontsize=12)
        plt.xlim([0, 300])
        plt.ylim([-256, 100])
        plt.plot(meanArray, label="Mean of spins");
        plt.plot(stdUpArray, label="Std up");
        plt.plot(stdDownArray, label="Std down");
        plt.legend(loc='upper right');
        plt.savefig('Figure2.png');
        plt.clf();
        print("Figure 2 done.");
        return data;

def experiment1Figure3(data):
##      Graph drawing     
        medianArray = np.median(data, axis=0)
        stdUpArray = medianArray + np.std(data, ddof=1);
        stdDownArray = medianArray - np.std(data, ddof=1);
        plt.figure();
        plt.suptitle('Figure 3: Median and std of 1000 runs\nwith unrealistic simulator', fontsize=12)
        plt.xlim([0, 300])
        plt.ylim([-256, 100])
        plt.plot(medianArray, label="Median of spins");
        plt.plot(stdUpArray, label="Std up");
        plt.plot(stdDownArray, label="Std down");
        plt.legend(loc='upper right');
        plt.savefig('Figure3.png');
        plt.clf();
        print("Figure 3 done.");

def experiment2Figure4():
##      Data collection    
        data = None;
        for i in range(0,1000):
                newRow = list(realisticSimulator(int(round(np.random.random(),3)*100), 80, 256));
                if (len(newRow) > 300):
                        newRow = newRow[0:300];
                else:
                        lastValue = newRow[len(newRow)-1];
                        for j in range(0,(300-len(newRow))):
                                newRow.append(lastValue);
                if(i==0):
                        data = np.array(newRow);
                else:
                        data = np.vstack([newRow, data]);
##      Graph drawing     
        meanArray = np.mean(data, axis=0);
        stdUpArray = meanArray + np.std(data, ddof=1);
        stdDownArray = meanArray - np.std(data, ddof=1);
        plt.figure();
        plt.suptitle('Figure 4: Mean and std of 1000 runs\nwith realistic simulator', fontsize=12)
        plt.xlim([0, 300])
        plt.ylim([-256, 100])
        plt.plot(meanArray, label="Mean of spins");
        plt.plot(stdUpArray, label="Std up");
        plt.plot(stdDownArray, label="Std down");
        plt.legend(loc='upper right');
        plt.savefig('Figure4.png');
        plt.clf();
        print("Figure 4 done.");
        return data;

def experiment2Figure5(data):
##      Graph drawing     
        medianArray = np.median(data, axis=0)
        stdUpArray = medianArray + np.std(data, ddof=1);
        stdDownArray = medianArray - np.std(data, ddof=1);
        plt.figure();
        plt.suptitle('Figure 5: Median and std of 1000 runs\nwith realistic simulator', fontsize=12)
        plt.xlim([0, 300])
        plt.ylim([-256, 100])
        plt.plot(medianArray, label="Median of spins");
        plt.plot(stdUpArray, label="Std up");
        plt.plot(stdDownArray, label="Std down");
        plt.legend(loc='upper right');
        plt.savefig('Figure5.png');
        plt.clf();
        print("Figure 5 done.");

def question1(seed, winAmount, episodes):
        win_prob = 0.5 # set appropriately to the probability of a win                                                                                                                                                                            
        np.random.seed(seed) # do this only once
        totalWinnings = 0
                                                                                                                                                                          
        # add your code here to implement the experiments
        for i in range(0,episodes):
                episodeWinnings = 0;
                counter = 0
                while (episodeWinnings<winAmount and counter<1000):
                        won = False;
                        betAmount = 1;
                        while (won is False):
                                won = get_spin_result(win_prob);
                                if (won):
                                        episodeWinnings = episodeWinnings + betAmount;
                                else:
                                        episodeWinnings = episodeWinnings - betAmount;
                                        betAmount = betAmount*2;
                        counter = counter + 1
                if(episodeWinnings == 80): totalWinnings = totalWinnings + 1
        return totalWinnings/episodes;

def question2(seed, numbets, episodes):
        win_prob = 0.5 # set appropriately to the probability of a win                                                                                                                                                                            
        np.random.seed(seed) # do this only once
        totalWinnings = 0
                                                                                                                                                                          
        # add your code here to implement the experiments
        for i in range(0,episodes):
                episodeWinnings = 0;
                counter = 0
                while(counter<numbets):
                        won = False;
                        betAmount = 1;
                        while (won is False and counter<numbets):
                                won = get_spin_result(win_prob);
                                counter = counter + 1
                                if (won):
                                        aux = episodeWinnings
                                        episodeWinnings = episodeWinnings + betAmount;
                                else:
                                        aux = episodeWinnings
                                        episodeWinnings = episodeWinnings - betAmount;
                                        betAmount = betAmount*2;
                totalWinnings = totalWinnings + episodeWinnings
        return totalWinnings/episodes;

def question4(seed, numbets, episodes, maxLoss):
        win_prob = 0.5 # set appropriately to the probability of a win                                                                                                                                                                            
        np.random.seed(seed) # do this only once
        totalWinnings = 0
                                                                                                                                                                          
        # add your code here to implement the experiments
        for i in range(0,episodes):
                episodeWinnings = 0;
                counter = 0
                while(counter<numbets):
                        won = False;
                        betAmount = 1;
                        while (won is False and counter<numbets):
                                won = get_spin_result(win_prob);
                                counter = counter + 1
                                if (won):
                                        aux = episodeWinnings
                                        episodeWinnings = episodeWinnings + betAmount;
                                else:
                                        aux = episodeWinnings
                                        episodeWinnings = episodeWinnings - betAmount;
                                        betAmount = betAmount*2;
                                if(episodeWinnings - betAmount < maxLoss):
                                    counter = numbets
                                    break
                if(episodeWinnings>=80):totalWinnings = totalWinnings + 1
        return float(totalWinnings)/float(episodes)
    
def question5(seed, numbets, episodes, maxLoss):
        win_prob = 0.5 # set appropriately to the probability of a win                                                                                                                                                                            
        np.random.seed(seed) # do this only once
        totalWinnings = 0
                                                                                                                                                                          
        # add your code here to implement the experiments
        for i in range(0,episodes):
                episodeWinnings = 0;
                counter = 0
                while(counter<numbets):
                        won = False;
                        betAmount = 1;
                        while (won is False and counter<numbets):
                                won = get_spin_result(win_prob);
                                counter = counter + 1
                                if (won):
                                        aux = episodeWinnings
                                        episodeWinnings = episodeWinnings + betAmount;
                                else:
                                        aux = episodeWinnings
                                        episodeWinnings = episodeWinnings - betAmount;
                                        betAmount = betAmount*2;
                                if(episodeWinnings - betAmount < maxLoss):
                                    counter = numbets
                                    break
                totalWinnings = totalWinnings + episodeWinnings
        return totalWinnings/episodes;
    
if __name__ == "__main__":
##      Run the first five lines to generate data Figures.
        experiment1Figure1();
        data = experiment1Figure2();
        experiment1Figure3(data);
        data = experiment2Figure4();
        experiment2Figure5(data);
        
##      Run the below lines for answers to questions 1, 2, 4 and 5
        print("result Q1: " + str(question1(gtid(), 80, 5000)))
        print("result Q2: " + str(question2(gtid(), 1000, 5000)))
        print("result Q4: " + str(question4(gtid(), 1000, 20000, -256)))
        print("result Q5: " + str(question5(gtid(), 1000, 20000, -256)))
        
