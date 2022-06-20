import random
import datetime

class BasicAccount:

    ''' BasicAccount class represents the Basic Account class of the assignment'''
   
    # The account number count, which will be incremented upon the addition of each instance
    
    acNum = 0

    def __init__(self,theacName,theOpeningBalance):
        BasicAccount.acNum += 1
        self.acNum = BasicAccount.acNum
        self.acName = str(theacName)
        self.balance = float(theOpeningBalance)
        self.cardNumber = []
        self.cardExp = []
            



    '''The string method for the Basic Account class, which will print a message when printing
    an instance of a premium account containing appropriate details of the account'''

    def __str__(self):
        return "The current balance of {self.acName}'s account is £{self.balance}".format(self=self)
    


    
    '''The deposit method for the two account classes, which only alters the balance 
        if a positive amount is inserted as expected'''

    def deposit(self,depositedAmount):

        try:
            if depositedAmount > 0:
                self.balance += depositedAmount
            else:
                print("Unable to deposit, only a positive number can be deposited")
        
        except Exception as exp:
            print("You can only deposit a positive number into your account")
       



    '''The withdraw method for the Basic Account class, the withdrawal method will alternate
        between the two, due to the premium accounts being able to have overdrafts'''

    def withdraw(self,withdrawAmount):

        try: 
            if withdrawAmount <= self.balance and withdrawAmount > 0:
                self.balance = self.balance - withdrawAmount
                print(str(self.acName) + " has withdrawn: £" + str(withdrawAmount))
                print("New balance is: £" + str(self.balance))
            else:
                print("Can not withdraw: £" + str(withdrawAmount))
                print("Account Balance: £" + str(self.balance))
            
        except Exception as exp:
            print("You can only withdraw a positive number from your account")
    



    '''The getAvailableBalance method for the Basic Account class, which returns the total available 
        balance as a float'''

    def getAvailableBalance(self):
        return float("{self.balance}".format(self=self))




    '''The getBalance method, which returns the balance of the account as a float,
       which becomes a negative value if the account is overdrawn '''

    def getBalance(self):
        return float("{self.balance}".format(self=self))




    '''The printBalance method, which prints a string containing the balance of the account
        in a suitable manner'''

    def printBalance(self):
        print ("The balance for " + str(self.acName) + "'s account is currently:"  + str(self.balance))
    



    '''The getName method, which returns the account name as a string (the account owner's name)'''

    def getName(self):
        return str("{self.acName}".format(self=self))

    


    '''The getAcNum method, which returns the account number as a string'''

    def getAcNum(self):
        return str("{self.acNum}".format(self=self))




    '''The issueNewCard method, that sets a new card number and expiry date''' 

    def issueNewCard(self):
        
        newCardNum = random.randint(1000000000000000,9999999999999999)
       
       # The below if statement was created in case this is not the first card issued,
       # in which there would be a small chance of a duplicate card number.

        if newCardNum == self.cardNumber:
            newCardNum = random.randint(1000000000000000,9999999999999999)
            self.cardNumber = newCardNum
        else:
            self.cardNumber = newCardNum
        

        expDate = datetime.datetime.now() + datetime.timedelta(weeks=(3*52))
        
        month = expDate.strftime("%m")
        year = expDate.strftime("%y")
        newExpiryDate = (int(month),int(year))
        
        self.cardExp = newExpiryDate


       

    ''' The closeAccount method for the Basic Account class, which always returns true
        as basic accounts are unable to go overdrawn'''

    def closeAccount(self):
        self.withdraw(self.balance)
        print("Any remaining funds have now been withdrawn, this account is now closed.")
        return True




class PremiumAccount(BasicAccount):

    '''Premium Accounts have access to all the features of a basic account, 
     with additional features in terms of overdraft facilities'''
   
    # I set the overdraft variable to false, under the premise that this becomes true
    # when a new overdraft limit is set for the account, which assumes that the setoverdraftLimit
    # is what activates the account owner's overdraft facilities.

    def __init__(self,theacName,theOpeningBalance,theOverdraftLimit):
        super().__init__(theacName,theOpeningBalance,)
        self.overdraftLimit = float(theOverdraftLimit)
        self.overdraft = False




    '''The string method for the Premium Account class, which will print a message when printing
    an instance of a premium account containing appropriate details of the account'''

    def __str__(self):
        return "The current balance of {self.acName}'s account is £{self.balance}, with an overdraft of £{self.overdraftLimit}".format(self=self)




    '''The method to set the overdraft limit, which will set the attribute self.overdraft limit
        to true and change the overdraft limit to the inputted amount'''

    def setoverdraftLimit(self,newLimit):
        if newLimit >= 0:
            self.overdraft = True
            self.overdraftLimit = float(newLimit)
        else:
            print("Invalid overdraft limit")




    '''The withdraw method for Premium accounts that will override the previous withdraw method
        due to the presence of the overdraft feature, which will allow account balances to be a
            negative number.'''

    def withdraw(self,withdrawAmount):

        try:

            if withdrawAmount <= self.balance and withdrawAmount > 0:
                self.balance = self.balance - withdrawAmount
                print(str(self.acName) + " has withdrawn: £" + str(withdrawAmount))
                print("New balance is: £" + str(self.balance))   
       
       
            elif withdrawAmount > self.balance: 
                totalFunds = (self.balance + self.overdraftLimit)
            
                if withdrawAmount <= totalFunds:
                    self.balance = (totalFunds - withdrawAmount) - self.overdraftLimit
                    print(str(self.acName) + " has withdrawn: £" + str(withdrawAmount))
                    print("New balance (including overdraft) is: £" + str(totalFunds-withdrawAmount))
                else:
                    print("Can not withdraw: £" + str(withdrawAmount))
                    print("Account Balance: £" + str(self.balance) + " with an overdraft of: £" + str(self.overdraftLimit))

        except Exception as exp:
            print("You can only withdraw a positive number from your account")




    ''' The getAvailableBalance method for the premium account class, which differs from the basic
        account version in that it will return the balance with the overdraft limit included.'''

    def getAvailableBalance(self):
        if self.overdraftLimit > 0:
            return self.balance + self.overdraftLimit
        else:
            return self.balance
    



    ''' The printBalance method for the premium account class, which also prints if the account
        has overdraft facilities activated and the overdraft limit'''

    def printBalance(self):
        print ("The balance for " + str(self.acName) + "'s account is currently: £"  + str(self.balance) + " Overdraft available: " + str(self.overdraft) + " Overdraft remaining: £" + str(self.overdraftLimit-(-self.balance)))




    '''The close account method for the Premium Account class,
        which as required will not execute if the user is overdrawn '''

    def closeAccount(self):
        if self.balance < 0:
            print("Can not close account due to customer being overdrawn by £" + str(0 - self.balance))
            return False
        else:
            self.withdraw(self.balance)
            print("Any remaining funds have now been withdrawn, this account is now closed.")
            return True




