"""
Course: CISC108
Assignment: Project 4:
Author: Dina Dawood

# Goblins Magical Loan System
Welcome to the Magic Bank, the #1 bank for wizards looking to get loans.
If you're starting a magical small business and need some Galleons,
this is the place to go!

The Magic Bank is looking to go digital and has contracted you to
create a simple command line interface for its customers. This
interface will log users in, allow them to request a loan amount and
length, and then tell them how much the interest rate would be.
"""

from cisc108 import assertEqual

#1 Define input_name() function
def input_username():
    '''
    Consumes username from user
    Parameters:
        none
    Return:
        username: (str)
    '''
    username = input("What is your username? ")
    return username

#2 Define get_pin() function
def get_pin(username):
    '''
    Consumes and produces an integer for user to use as pin
    Parameters:
        username: (str) - user given username
    Returns:
        user pin: (int)
    '''
    if username == "ada":
        return 1234
    elif username == "babbage":
        return 4321
    elif username == "acbart":
        return 9999
    elif username == "ddawood":
        return 0000
    else:
        return -1

#### NEED UNIT TESTS ####    

assertEqual(get_pin("ada"), 1234)
assertEqual(get_pin("babbage"), 4321)
assertEqual(get_pin("acbart"), 9999)
assertEqual(get_pin("ddawood"), 0000)
assertEqual(get_pin("cat"), -1)

#3 Define login() function
def login(username):
    '''
    Consumes a username and produces a boolean whether can log in
    Parameters:
        username: (str) - user given username
    Returns:
        can login?: (boolean)
    '''
    login_pin = input("Enter pin: ")
    og_pin = get_pin(username)
    if og_pin == login_pin:
        if login_pin == -1:
            return False
        else:
            return True
    else:
        return False

#4 Define input_request() function
def input_request():
    '''
    Consumes nothing and returns a str representing request for loan
    Parameters:
        none
    Returns:
        loan: (str)
    '''
    print("What loan size and duration do you want? (Size in thousands of galleons, duration in years)")
    loan_request = input("Amount and size: ")
    return loan_request

#5 Define get_length() function
def get_length(loan_request):
    '''
    Consumes loan amount and produces an integer representing the length of time for loan.
    Pararmeters:
        loan_request: (str) - user given loan amount
    Returns:
        length: (int)
    '''
    length = int(loan_request[-8:-6].strip())
    return length

#### NEED UNIT TESTS ####    

assertEqual(get_length("$20k for 50 years"), 50)
assertEqual(get_length("$20k for 15 years"), 15)
assertEqual(get_length("$20k for 30 years"), 30)


#6 Define get_amount() function
def get_amount(loan_request):
    '''
    Consumes loan amount and produces an integer representing the loan amount requested
    Pararmeters:
        loan_request: (str) - user given loan amount
    Returns:
        amount: (int)
    '''
    amount = int(loan_request[1:loan_request.find("k")])
    return amount

#### NEED UNIT TESTS ####    

assertEqual(get_amount("$20k for 50 years"), 20)
assertEqual(get_amount("$75k for 50 years"), 75)
assertEqual(get_amount("$48k for 50 years"), 48)


#7 Define calculate_interest() function
def calculate_interest(amount, length):
    '''
    Consumes two integers for amount and length of time requested to produce interest
    Pararmeters:
        amount: (int) - amount requested
        length: (int) - length requested
    Returns:
        interest: (float)
    '''
    interest = (amount/20 + length/2)
    return interest

#### NEED UNIT TESTS ####

assertEqual(calculate_interest(20, 50), 26)
assertEqual(calculate_interest(75, 15), 11.25)
assertEqual(calculate_interest(48, 30), 17.4)

#8 Define handle_request() function
def handle_request():
    '''
    Consumes and produces nothing; composes other functions
    Pararmeters:
        none
    Returns:
        none
    '''
    loan_request = input_request()
    length = get_length(loan_request)
    amount = get_amount(loan_request)
    interest = calculate_interest(amount, length)
    print("Your loan would have an interest rate of " + str(interest))

# Define main() function    
def main():
    username = input_username()
    if login(username):
        print("Incorrect PIN!")
    else:
        print ("Welcome " + username)
        handle_request()


if __name__ == "__main__":
    main()