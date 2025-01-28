def conversion_unit(sUnit, tUnit) :
    #conversion factors for each compatible unit pair 
    conversion_factors = {
            ('ml', 'fl') : 0.033814,
            ('l', 'fl') : 33.814,
            ('l', 'gal') : 0.264172,
            ('g', 'oz') : 0.035274,
            ('kg', 'lb') : 2.20462,
            ('mm', 'in') : 0.0393701,
            ('cm', 'in') : 0.393701,
            ('m', 'ft') : 3.28084,
            ('km', 'mi') : 0.621371
        }
    print("Welcome to the Unit Conversion Program")
    print("Supported Starting Units are: ",', '.join(sUnit))
    print("Supported Target Units are: ",', '.join(tUnit))

    #get user input for starting unit and targeting unit 
    start_unit = input("Enter the starting unit of measurement: ").strip().lower()
    if start_unit not in sUnit :
        print(f"Error: {start_unit} is not a valid starting unit.")
        return 
    target_unit = input("Enter the targeting Unit of measurement: ").strip().lower() 
    if target_unit not in tUnit :
        print(f"Error: {target_unit} is not a valid targeting unit.")
        return 
    
    #check compatibility :
    if (start_unit, target_unit) not in conversion_factors: 
        print(f"Error: Conversion from {start_unit} to {target_unit} is not supported.")
        return 

    #get the value to be converted
    try :
        value = float(input(f"Enter the value to be converted from {start_unit}: "))
    except ValueError :
        print(f"Error: Please enter a valid numeric value.")
        return 

    #perform the conversion 
    converted_factor = conversion_factors[(start_unit, target_unit)]
    converted_value = value * converted_factor 

    print(f"\nInput: {value} {start_unit}")
    print(f"Output: {converted_value:.4f} {target_unit}")

def main() :
    starting_unit = ['ml', 'l', 'g', 'kg','mm','cm','m','km']
    target_unit = ['fl','oz','gal','oz', 'lb','in','ft','mi']

    conversion_unit(starting_unit, target_unit)

main()