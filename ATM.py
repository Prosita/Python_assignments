import re

class Bank:
    def __init__(self) -> None:
        self.__Accounts = {"ACC1234":{"Name":"Prosita","Password":"1234","PhoneNo":"9876543210","Balance":30000}}
        self.__NoOfAccounts = 1
    
    def isValid(self,AccountNo):
        if AccountNo not in self.__Accounts:
            print("Account do not exist.")
            return False
        #print(AccountNo)
        Password = input("Enter Your Password : ")

        if self.__Accounts[AccountNo]["Password"] == Password:
            print("\t\t!!!...Valid Credentials...!!!\n")
            return True
        else:
            print("\t\t!!!...Invalid Credentials...!!!")
            return False
    
    def createAccount(self):
        name = input("\nEnter User Name (Without Spaces): ")
        phoneNum = input("Enter Phone Number : ")
        validNum = re.fullmatch('[6-9][0-9]{9}',phoneNum)
        #print(re.fullmatch('[6-9][0-9]{9}',phoneNum))
        while validNum == None:
            phoneNum = input("Enter a valid Phone Number : ")
            validNum = re.fullmatch('[6-9][0-9]{9}',phoneNum)

        amount = int(input("Enter Deposite Amount : "))
        while amount < 500:
            amount = int(input("Deposite Amount should be atleast Rs. 500 : "))

        self.__NoOfAccounts +=1
        __AccountNo = 'ACC'+str(100 + self.__NoOfAccounts)
        print("Your Account Number is: ",__AccountNo)

        __password1 = input("Enter Password : ")
        __password2 = input("Re-Enter Password : ")
        while __password1 != __password2:
            print("Passwords Does not Match...!!!")
            __password1 = input("Enter Password : ")
            __password2 = input("Re-Enter Password : ")

        # self.__Accounts[__AccountNo]["Name"] = name
        # self.__Accounts[__AccountNo]["Password"] = __password1
        # self.__Accounts[__AccountNo]["PhoneNo"] = phoneNum
        # self.__Accounts[__AccountNo]["Balance"] = amount
        self.__Accounts[__AccountNo] = {"Name" : name, "Password" : __password1, "PhoneNo" : phoneNum, "Balance" : amount}
        self.__Accounts[__AccountNo]["History"] = "Amount Deposited: "+str(amount)+" Remaining balance: "+str(amount)+"\n"
        print("Your Account Details are: ")
        for i in self.__Accounts[__AccountNo]:
            print(i," : ",self.__Accounts[__AccountNo][i])

    def withdrawMoney(self,AccNum):
        if self.__Accounts[AccNum]["Balance"] < 500:
            print("Your Account Balance is not sufficient")
            exit()
        money = int(input("Enter Withdraw Amount : "))
        if money > self.__Accounts[AccNum]["Balance"] - 500 :
            print("Withdrawal Money Exceeded...!!!")
        else:
            self.__Accounts[AccNum]["Balance"] -= money
            print("Money Withdrwal Successfull....!!!")
            print("Remaining Balance : ",self.__Accounts[AccNum]["Balance"])

print("\t\t\tWelome to KPMG ATM")
B = Bank()
AccountNo = input("Enter Your Account Number : ").upper()
if not B.isValid(AccountNo):
    exit()

while(True):
    print("\t\tPlease Enter Your Action")
    print("1. New Account Creation\n2. Money Withdrawal\n3. Balance Enquiry\n4. Password Change\n5. Transaction History\n6. Exit")
    action = int(input("Enter Your Choice : "))
    if action == 1: B.createAccount()
    elif action == 2: B.withdrawMoney(AccountNo)
    elif action == 3: B.balanceEnquiry(AccountNo)
    elif action == 4: B.passwordChange(AccountNo)
    elif action == 5: B.transactionHistory(AccountNo)
    elif action == 6: exit()
    else : print("!!!...Invalid Choice...!!!")
    choice = input("Do you want to continue y/n :")
    if choice == "n" or choice == "N": exit()
