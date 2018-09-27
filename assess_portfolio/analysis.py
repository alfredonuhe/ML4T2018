import pandas as pd
import decimal as dec
import numpy as np
import datetime as dt
from util import get_data, plot_data
import matplotlib
matplotlib.use("Agg");
import matplotlib.pyplot as plt

# This is the function that will be tested by the autograder
# The student must update this code to properly implement the functionality
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
    dpv = ((prices/prices.ix[0,:])*allocs*sv).sum(axis=1)
    spy_dpv = prices_SPY/prices_SPY[0]*sv
    dr = (dpv[1:]/dpv.values[:-1])-1

    # Get portfolio statistics (note: std_daily_ret = volatility)
    cr, adr, sddr, sr = [(dpv[len(dpv)-1]/dpv[0])-1,
                         np.mean(dr),
                         np.std(dr, ddof=1),
                         (np.mean(dr-rfr))/(np.std(dr, ddof=1))*np.sqrt(252)] # add code here to compute stats

    # Compare daily portfolio value with SPY using a normalized plot
    if gen_plot:
        plotData = pd.DataFrame(data=dpv/dpv[0],
                    index=prices_all.index.values,
                    columns=["Portfolio"])
        # Code for plot generation
        df_temp = pd.concat([plotData, prices_SPY/prices_SPY[0]], axis=1)
        
        plt.figure();
        plt.suptitle('Daily portfolio value and SPY', fontsize=12)
        locs, labels = plt.xticks()
        plt.setp(labels, rotation=30)
        plt.ylabel('Normalized prize')
        plt.xlabel('Dates')
        plt.plot(df_temp["Portfolio"], label="Portfolio")
        plt.plot(df_temp["SPY"], label="SPY")
        plt.legend(loc='upper left')
        plt.savefig('plot.png')
        plt.clf();
        pass

    # Add code here to properly compute end value
    ev = dpv[len(dpv)-1]
    return cr, adr, sddr, sr, ev

def test_code():
    # This code WILL NOT be tested by the auto grader
    # It is only here to help you set up and test your code

    # Define input parameters
    # Note that ALL of these values will be set to different values by
    # the autograder!
    start_date = dt.datetime(2010,1,1)
    end_date = dt.datetime(2010,12,31)
    symbols = ['GOOG', 'AAPL', 'GLD', 'XOM']
    allocations = [0.2, 0.3, 0.4, 0.1]
    start_val = 1000000  
    risk_free_rate = 0.0
    sample_freq = 252

    # Assess the portfolio
    cr, adr, sddr, sr, ev = assess_portfolio(sd = start_date, ed = end_date,\
        syms = symbols, \
        allocs = allocations,\
        sv = start_val, \
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
    test_code()
