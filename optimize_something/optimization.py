import pandas as pd  		   	  			    		  		  		    	 		 		   		 		  
import matplotlib
matplotlib.use("Agg");
import matplotlib.pyplot as plt		   	  			    		  		  		    	 		 		   		 		  
import numpy as np  		   	  			    		  		  		    	 		 		   		 		  
import datetime as dt
import scipy.optimize as spo
from util import get_data, plot_data

def assess_portfolio(sd = dt.datetime(2008,1,1), ed = dt.datetime(2009,1,1), \
    syms = ['GOOG','AAPL','GLD','XOM'], \
    allocs=[0.1,0.2,0.3,0.4], \
    sv=1000000, rfr=0.0, sf=252.0, \
    gen_plot=False):

    # Read in adjusted closing prices for given symbols, date range
    dates = pd.date_range(sd, ed)
    prices_all = get_data(syms, dates)  # automatically adds SPY
    prices = prices_all[syms]  # only portfolio symbols
    prices_SPY = prices_all['SPY']  # only SPY, for comparison later

    # Get daily portfolio value and daily return
    dpv = ((prices/prices.ix[0,:])*allocs).sum(axis=1)
    spy_dpv = prices_SPY/prices_SPY[0]
    dr = (dpv[1:]/dpv.values[:-1])-1

    # Get portfolio statistics (note: std_daily_ret = volatility)
    cr, adr, sddr, sr = [(dpv[len(dpv)-1]/dpv[0])-1,
                         np.mean(dr),
                         np.std(dr, ddof=1),
                         (np.mean(dr-rfr))/(np.std(dr, ddof=1))*np.sqrt(252)] # add code here to compute stats

    # Add code here to properly compute end value
    ev = dpv[len(dpv)-1]
    return cr, adr, sddr, sr, ev, dpv, spy_dpv

def calc_negative_sr(allocs, prices):

    # Get daily portfolio value and daily return
    dpv = ((prices/prices.ix[0,:])*allocs).sum(axis=1)
    dr = (dpv[1:]/dpv.values[:-1])-1
    rfr = 0.00
    
    # Get portfolio statistics (note: std_daily_ret = volatility)
    sr = np.mean(dr-rfr)/(np.std(dr, ddof=1))*np.sqrt(252) # add code here to compute stats

    return sr*(-1)

def constraint1(x):
    result = 0
    for i in range(0,len(x)):
        result = result + float(x[i])
    return result - 1
  		   	  			    		  		  		    	 		 		   		 		  
# This is the function that will be tested by the autograder  		   	  			    		  		  		    	 		 		   		 		  
# The student must update this code to properly implement the functionality  		   	  			    		  		  		    	 		 		   		 		  
def optimize_portfolio(sd=dt.datetime(2008,1,1), ed=dt.datetime(2009,1,1), \
    syms=['GOOG','AAPL','GLD','XOM'], gen_plot=False):  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
    # Read in adjusted closing prices for given symbols, date range  		   	  			    		  		  		    	 		 		   		 		  
    dates = pd.date_range(sd, ed)  		   	  			    		  		  		    	 		 		   		 		  
    prices_all = get_data(syms, dates)  # automatically adds SPY  		   	  			    		  		  		    	 		 		   		 		  
    prices = prices_all[syms]  # only portfolio symbols  		   	  			    		  		  		    	 		 		   		 		  
    prices_SPY = prices_all['SPY']  # only SPY, for comparison later
  		   	  			    		  		  		    	 		 		   		 		  
    # find the allocations for the optimal portfolio  		   	  			    		  		  		    	 		 		   		 		  
    # note that the values here ARE NOT meant to be correct for a test case
    allocs = [1/float(len(prices.values[0,:]))] * len(prices.values[0,:])
    bounds = [[0,1]]*len(prices.values[0,:])
    cons = ({'type': 'eq', 'fun': constraint1})
    
    result = spo.minimize(calc_negative_sr, allocs, args=(prices,), method="SLSQP", bounds=bounds, constraints=cons, options={"disp":True})

    if (result.success):
        # Get daily portfolio value and other stats
        allocs = result.x
        cr, adr, sddr, sr, _, port_val, prices_SPY = assess_portfolio(sd, ed, syms, result.x) 		   	  			    		  		  		    	 		 		   		 		  	   	  			    		  		  		    	 		 		   		 	    
                                                                                                                                                                              
        # Compare daily portfolio value with SPY using a normalized plot  		   	  			    		  		  		    	 		 		   		 		  
        if gen_plot:  		   	  			    		  		  		    	 		 		   		 		  
            # add code to plot here  		   	  			    		  		  		    	 		 		   		 		  
            df_temp = pd.concat([port_val, prices_SPY], keys=['Portfolio', 'SPY'], axis=1)
            plt.figure();
            plt.suptitle('Daily portfolio value and SPY', fontsize=12)
            locs, labels = plt.xticks()
            plt.setp(labels, rotation=30)
            plt.ylabel('Normalized prize')
            plt.xlabel('Dates')
            plt.plot(df_temp["Portfolio"], label="Portfolio")
            plt.plot(df_temp["SPY"], label="SPY")
            plt.legend(loc='upper left')
            plt.savefig('plot.pdf')
            pass  		   	  			    		  		  		    	 		 		   		 		                                                                                                                                                                        
        return allocs, cr, adr, sddr, sr
    else:
        print result.message
        return
  		   	  			    		  		  		    	 		 		   		 		  
def test_code():  		   	  			    		  		  		    	 		 		   		 		  
    # This function WILL NOT be called by the auto grader  		   	  			    		  		  		    	 		 		   		 		  
    # Do not assume that any variables defined here are available to your function/code  		   	  			    		  		  		    	 		 		   		 		  
    # It is only here to help you set up and test your code  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
    # Define input parameters  		   	  			    		  		  		    	 		 		   		 		  
    # Note that ALL of these values will be set to different values by  		   	  			    		  		  		    	 		 		   		 		  
    # the autograder!  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
    start_date = dt.datetime(2008,06,01)  		   	  			    		  		  		    	 		 		   		 		  
    end_date = dt.datetime(2009,06,01)  		   	  			    		  		  		    	 		 		   		 		  
    symbols = ['IBM', 'X', 'GLD', 'JPM']  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
    # Assess the portfolio  		   	  			    		  		  		    	 		 		   		 		  
    #allocations, cr, adr, sddr, sr = optimize_portfolio(sd = start_date, ed = end_date,\
    #    syms = symbols, \
    #    gen_plot = False)
    allocations, cr, adr, sddr, sr = optimize_portfolio(sd = start_date, ed = end_date,\
        syms = symbols, \
        gen_plot = True) 
  		   	  			    		  		  		    	 		 		   		 		  
    # Print statistics  		   	  			    		  		  		    	 		 		   		 		  
    print "Start Date:", start_date  		   	  			    		  		  		    	 		 		   		 		  
    print "End Date:", end_date  		   	  			    		  		  		    	 		 		   		 		  
    print "Symbols:", symbols  		   	  			    		  		  		    	 		 		   		 		  
    print "Allocations:", allocations  		   	  			    		  		  		    	 		 		   		 		  
    print "Sharpe Ratio:", sr  		   	  			    		  		  		    	 		 		   		 		  
    print "Volatility (stdev of daily returns):", sddr  		   	  			    		  		  		    	 		 		   		 		  
    print "Average Daily Return:", adr  		   	  			    		  		  		    	 		 		   		 		  
    print "Cumulative Return:", cr  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
if __name__ == "__main__":  		   	  			    		  		  		    	 		 		   		 		  
    # This code WILL NOT be called by the auto grader  		   	  			    		  		  		    	 		 		   		 		  
    # Do not assume that it will be called  		   	  			    		  		  		    	 		 		   		 		  
    test_code()  		   	  			    		  		  		    	 		 		   		 		  
