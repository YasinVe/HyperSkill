import math
print("""
What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal:
""")

"""
P = loan_principal
A = annuity_payment
n = number_of_periods
i = loan_interest
"""
choose = input()
def number_of_monthly_payments():
    P = float(input("Enter the loan principal:\n")) 
    A = float(input("Enter the annuity payment:\n"))
    i = float(input("Enter the loan interest:\n"))/1200
    n = math.ceil(math.log(A/(A - i * P), 1 + i))
    year, month = divmod(n, 12)
    if year:
        if year == 1:
            year_text = str(year)+" year" if not month else str(year) + " year and"
        elif year > 1:
            year_text = str(year)+" years" if not month else str(year) + " years and"
    if not year:
        year_text = ''
    if month:
        if month == 1:
            month_text = str(month) + " month " 
        else:
            month_text = str(month) + " months "
    if not month:
        month_text = ''
    print(f"It will take {year_text} {month_text} to repay this loan!")

def loan_principal():
    A = float(input("Enter the monthly payment:/n"))
    n = float(input("Enter the number of periods:/n"))
    i = float(input("Enter the loan interest:/n"))/1200
    P = A / (i * pow((1+i), n)/(pow((1 + i), n) - 1))
    print(f"Your loan principal = {math.ceil(P)}!")

def annuity_monthly_payment_amount():
    P = float(input("Enter the loan principal:\n"))
    n = float(input("Enter the number of periods:\n"))
    i = float(input("Enter the loan interest:\n"))/1200
    A = P * (i * pow((1+i), n)/(pow((1 + i), n) - 1))
    print(f"Your monthly payment = {math.ceil(A)}!")

if choose == 'n':
    number_of_monthly_payments()
elif choose == 'p':
    loan_principal()
elif choose == 'a':
    annuity_monthly_payment_amount()
