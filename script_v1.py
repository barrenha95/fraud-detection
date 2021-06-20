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
import pandas as pd #Fora data manipulation



DF = pd.read_csv("DATABASE.csv")
DF.head()