'''
There is an ATM machine that stores banknotes of 5 denominations: 20, 50, 100, 200, and 500 dollars. 

Initially the ATM is empty. The user can use the machine to deposit or withdraw any amount of money.

When withdrawing, the machine prioritizes using banknotes of larger values.

For example, if you want to withdraw $300 and there are 2 $50 banknotes, 1 $100 banknote, and 1 $200 banknote, then the machine will use the $100 and $200 banknotes.
However, if you try to withdraw $600 and there are 3 $200 banknotes and 1 $500 banknote, 
then the withdraw request will be rejected because the machine will first try to use the $500 banknote and then be unable to use banknotes to complete the remaining $100. 
Note that the machine is not allowed to use the $200 banknotes instead of the $500 banknote.
Implement the ATM class:

ATM() Initializes the ATM object.
void deposit(int[] banknotesCount) Deposits new banknotes in the order $20, $50, $100, $200, and $500.
int[] withdraw(int amount) Returns an array of length 5 of the number of banknotes that will be handed to the user in the order $20, $50, $100, $200, and $500, and update the number of banknotes in the ATM after withdrawing. Returns [-1] if it is not possible (do not withdraw any banknotes in this case).
 
 - we always use the biggest available bill
 - we have to store an array as our 'deposits' in the format [20s, 50s, 100s, 200s, 500s] where each element in the array would denote the amount of bills we have for that particular value
 - we have to return an array in the same format for a withdraw (if the withdraw is possible, else -1)
 - we need a reference for mapping each index to the value
 - as we are collecting bills for a withdrawal, if the withdrawal is not possible, we have to give the bills back to the deposits array


if we have a deposit of [1, 2, 3, 4]
go through every position of deposits and add them

if we get a withdrawal of 2200
get 500s until we ran out (2000)
get 200 until we fill the remaining amount (just 1 bill)
since remaining amount==0 return bills


'''
class ATM():
    def __init__(self):
        self.values={
            0:20, 
            1:50,
            2:100,
            3:200,
            4:500
        }
        self.deposits=[0]*5
    
    def deposit(self, banknotesCount):
        for i in range(len(banknotesCount)):
            self.deposits[i]+=banknotesCount[i]

    #withdraw 2300, deposits:[1, 2, 3, 4]
    def withdraw(self, amount):
        remainingAmount = amount
        withdrawal = [0]*5
        initialDeposits = self.deposits.copy()
        for i in range(len(self.deposits)-1, -1, -1):
            if remainingAmount == 0:
                return withdrawal

            # Determine the number of bills to use
            billsToUse = min(self.deposits[i], remainingAmount // self.values[i])
            if billsToUse > 0:
                withdrawal[i] += billsToUse
                self.deposits[i] -= billsToUse
                remainingAmount -= self.values[i] * billsToUse

        if remainingAmount > 0:
            self.deposits = initialDeposits
            return [-1]
        return withdrawal

atm = ATM()
atm.deposit([0, 1, 2, 3, 4])
print(atm.withdraw(2300))
print(atm.withdraw(2000))
            

    