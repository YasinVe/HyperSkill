print("Enter the loan principal:")
loan_principal = int(input())
print("What do you want to calculate?",
"type 'm' for number of monthly payments,",
"type 'p' for the monthly payment", sep = '\n')
payment = input()
if payment == 'm':
    print("Enter the monthly payment:")
    monthly_payment = int(input())
    number_of_month = int(loan_principal / monthly_payment)
    if loan_principal % monthly_payment:
        print(f"It will take {number_of_month + 1} months to repay the loan")
    else:
        if number_of_month == 1:
            print("It will take 1 month to repay the loan")
        else:
            print(f"It will take {number_of_month} months to repay the loan") 
else:
    print("Enter the number of months:")
    number_of_months = int(input())
    if loan_principal % number_of_months:
        monthly_payment = int(loan_principal / (number_of_months)) + 1
        print(f"Your monthly payment = { monthly_payment } and last payment = {loan_principal - (number_of_months - 1) * monthly_payment }")
    else:
        print(f"Your monthly payment = {int(loan_principal / number_of_months)}")
