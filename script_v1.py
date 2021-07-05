# The main objective of this project is to create a Fraud Detection model
# We are using a Synthetic Financial Dataset obtained in: https://www.kaggle.com/ealaxi/paysim1

# DATA DESCRIPTION

## step = It's a measure of time, 1 step = 1 hour
### This could be used to split train and test data
### In this data frame we have 744 steps (30 days)

## type = Type of the financial transaction
### cash-in :When you put your money in the bank account ("deposito")
### cash-out:When you remove your money from the bank account ("saque")
### debit   :When something debits from your bank account
### payment :When you pay something with your bank account
### transfer:When you transfer money to anoter bank account

## amount         = Amount of the transaction in local currency
## nameOrig       = Customer who started the transaction 
## oldbalanceOrg  = Initial balance before the transaction
## newbalanceOrig = New balance after the transaction
## nameDest       = Customer who is recipient of the transaction

## oldbalanceDest = Initial balance recipient before the transaction. 
### Note that there is not information for customers that start with M (Merchants).

## newbalanceDest = New balance recipient after the transaction.
### Note that there is not information for customers that start with M (Merchants).

## isFraud = This is the transactions made by the fraudulent agents inside the simulation.
### Here the agents aims to profit by taking control of customers accounts
### They try to transfer to another account and then cash out of the system.

## isFlaggedFraud = A model created to control massive transfers from one account to another
### Flags attempts to transfer more than 200.000 in a single transaction.

# LIBRARIES
import os             #For operational system comands
import pandas as pd   #For data manipulation
import numpy  as np   #Necessary to manipulate multidimentional array objects
import statistics     #Statistics features and metrics
import seaborn as sns #For plots


# IMPORTING DATA
os.chdir("C:/Users/jvibarrenha/Desktop/FRAUD_DETECTION")
DF = pd.read_csv("DATABASE.csv")
DF.head()


# CATEGORIZING FEATURES BY TIPE
numeric_features     = ['step', 'amount'  , 'oldbalanceOrg', 'newbalanceOrig', 'oldbalanceDest', 'newbalanceDest', 'isFraud', 'isFlaggedFraud']
categorical_features = ['type', 'nameOrig', 'nameDest']

# DISTRIBUTION ANALYSIS
## The first step I like to do is study the data distribuition
## This step can give a lot of insights about problem behaviour and about which methods can be used
## I like to do this analysis with all features
## We can do this analysis by two ways:
### With numeric indicators like: Mean, Median, Variance and Standard Deviation

# NUMERIC INDICATORS
int(np.min(DF['amount'])) #Show the mean value of that distribuition
int(np.max(DF['amount'])) #Show the mean value of that distribuition
int(np.mean(DF['amount'])) #Show the mean value of that distribuition
int(np.median(DF['amount'])) #Show the value that is in the middle of the data
int(np.std(DF['amount'])) #Measure of dispersion of data (0 = no dispersion, >0 = standard amount of deviation from the mean)

# The minimun value is 0
# The maximun value is 92,445,516
# The mean value of this example is 179,861
# The median value of this example is 74,871
# The standard deviation of this example is 603,858

# The conclusion here is:
## The biggest concentration is between 0 and 800,000
## We have at least one big outlier (92 M), this info can generate some insights

# To help with this analysis I will create a function

def Dist_Ind(dataframe, col_name):
    min_val    = int(np.min(   dataframe[str(col_name)]))
    max_val    = int(np.max(   dataframe[str(col_name)]))
    mean_val   = int(np.mean(  dataframe[str(col_name)]))
    median_val = int(np.median(dataframe[str(col_name)]))
    std_val    = int(np.std(   dataframe[str(col_name)]))

    return(print(  "\n feature: "+ str(col_name)
                 + "\n min: "    + str(min_val)          
                 + "\n Max: "    + str(max_val)          
                 + "\n Mean: "   + str(mean_val)          
                 + "\n Median: " + str(median_val)          
                 + "\n Std: "    + str(std_val)))

#Dist_Ind(DF, 'amount') # Only a test of the function

# Checking info from all numeric features
for feature in numeric_features:
    Dist_Ind(DF, feature)


### JHONNY REMEMBER TO CONVERT INTO NUMERIC BEFORE RUN THIS LINE
sns.histplot(DF['amount'])
# EXPLORING DATA
## Check if we can create new features with nameOrig and nameDest
## Check if exists nameOrig = nameDest
## Create a new feature: new balance - oldbalance
## Check if exists concentration of activity in some part of the time

# Hypothesis of frauds
## Number of tranferencies
### All cashs with only one transfer
### A lot of tiny transfers trying to avoid attention

## Way to get the money
### Transfer to another account
### Cash-out the money 
