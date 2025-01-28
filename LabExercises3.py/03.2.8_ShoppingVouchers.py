def calculate_vouchers_value(spending) :
    if spending < 10 :
        return 0 
    elif 10 <= spending <=60 :
        return spending * 0.08 
    elif 60 < spending <= 150 :
        return spending * 0.10 
    elif 150 < spending <= 210 :
        return spending * 0.12 
    elif spending > 210 :
        return spending * 0.14 

def main() :
    spending = float(input("How much money did the customer spend?: "))
    
    print(f"The customer receives a voucher of ${calculate_vouchers_value(spending)} on his ${spending} spending.")

main() 