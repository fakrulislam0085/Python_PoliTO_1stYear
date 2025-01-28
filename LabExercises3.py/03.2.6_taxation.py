def calculate_tax(income, status) :
    if status.lower() == "single" :
        if income <= 8000 :
            tax = 0.10 * income 
        elif income <= 32000 :
            tax = 800 + 0.15*(income - 800)
        elif income > 32000: 
            tax = 4400 + 0.25*(income - 4400)
    elif status.lower() == 'married' :
        if income <= 16000 :
            tax = 0.10 * income 
        elif income <= 64000: 
            tax = 1600 + 0.15*(income - 1600) 
        elif income > 64000:
            tax = 8800 + 0.25*(income - 8800) 
        
    return tax 

def main() :
    income = float(input("Enter the income: "))
    status = input("Marital Status(Single/Married): ")

    result = calculate_tax(income, status)

    print(f"Tax for this person: ${result}")

main()