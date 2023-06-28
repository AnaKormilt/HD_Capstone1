# The below program will allow user to access either an investment caculator or home loan repayment calculator.
import math
# Sleep function from Time module will be used to give user time to read the error message, if the entered format of input is not suitable.
import time

# to simplify the mane code several functions were defined to take user imput and to calculate according to given formulas
def get_user_input_for_investment_calculator():
    while True:    
        try: 
            deposit_amount = int(input("Eneter the amount of money, you are going to deposit (without currency sign): "))
            interest_rate = float(input("Enter the desired interest rate in %: "))
            num_of_years = int(input("Enter the number of years you plan on investing: "))
            break
        except:
            print("Please make sure that you enter deposit amount, interest rate and the number of years in numerical format.")
            time.sleep(2)
    return (deposit_amount, interest_rate, num_of_years)

def calculate_total_amount(deposit_amount, interest_rate, num_of_years):
    while True:
        interest_rate_percent = interest_rate / 100
        interest = input("""
Choose the desired type of interest: 
simple   - continually calculated on the initial amount invested and is only calculated once per year
compound - calculated on the current total

Enter either \'simple\' or \'compound\' from the  menu above to proceed: """)   
        if interest.lower() == "simple":
            total_amount = deposit_amount * (1 + interest_rate_percent * num_of_years)
            break
        elif interest.lower() == "compound":
            total_amount = deposit_amount * math.pow((1 + interest_rate_percent), num_of_years)
            break
        else:
            print("You have entered neither \'simple\' nor \'compound\' or the spelling was incorrect, please try again.")
            time.sleep(2)
    return total_amount

def get_user_input_for_bond_calculator():
    while True:    
        try: 
            house_value = int(input("Enter the present value of the house (without currency sign): "))
            interest_rate = float(input("Enter interest rate in %: "))
            months_to_repay = int(input("Enter the number of months you plan to take to repay the bond: "))
            break
        except:
            print("Please make sure that you enter house value, the interest rate, and the number of months to repay the bond in numerical format.")
            time.sleep(2)
    return (house_value, interest_rate, months_to_repay)   

def calculate_repayment(interest_rate, house_value, months_to_repay):
    monthly_interest_rate = (interest_rate / 100) / 12
    return (monthly_interest_rate * house_value) / (1 - (1 + monthly_interest_rate)**(-months_to_repay))

# Program starts here
print("Welcome to our finance calculator!")

while True:
    user_choice = input("""
Choose the calculation you need:
investment - to calculate the amount of interest you'll earn on your investment
bond       - to calculate the amout you'll have to pay on a home loan

Enter either \'investment\' or \'bond\' from the  menu above to proceed: """)
    if user_choice.lower() == "investment":
        deposit_amount, interest_rate, num_of_years = get_user_input_for_investment_calculator() 
        total_amount = calculate_total_amount(deposit_amount, interest_rate, num_of_years)
        print(f"Your total amount will be: {round(total_amount, 3)}")
        break

    elif user_choice.lower() == "bond":
        house_value, interest_rate, months_to_repay = get_user_input_for_bond_calculator()
        repayment = calculate_repayment(house_value, interest_rate, months_to_repay)
        print(f"The amount of money you will have to repay each month: {round(repayment, 3)}")
        break

    else:
        print("\nYou have entered neither \'investment\' nor \'bond\' or the spelling was incorrect, please try again.")
        time.sleep(2)
