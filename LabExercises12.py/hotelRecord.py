def display_name_phoneNum(CustomersFile, SuspectsFile):
    try:
        with open(CustomersFile, 'r') as cFile, open(SuspectsFile, 'r') as sFile:
            customers = cFile.readlines()  # Read all customer records into a list
            for sName in sFile:  # Iterate through each suspect
                sName = sName.strip()
                contacts = []  # List to store contacts for the current suspect
                print(f"** Contacts of the guest: {sName}: **")

                for line in customers:
                    floatingline = line.strip()
                    fields = floatingline.split(',')
                    if len(fields) != 4:
                        print("Invalid Input in customers.txt")
                        continue

                    name, number, inday, outday = fields
                    try:
                        inday = int(inday)  # Convert suspect's check-in/check-out to integers
                        outday = int(outday)
                    except ValueError:
                        print("Invalid date format in record")
                        continue

                    if sName == name:
                        sInday, sOutday = inday, outday  # Save suspect's stay period

                        # Check contacts with other customers
                        for other_line in customers:
                            other_line = other_line.strip()
                            other_fields = other_line.split(',')

                            if len(other_fields) != 4:
                                continue

                            otherName, otherNum, otherInday, otherOutday = other_fields
                            try:
                                otherInday = int(otherInday)
                                otherOutday = int(otherOutday)
                            except ValueError:
                                continue

                            # Check if there is an overlap in stay periods
                            if ((sInday <= otherOutday and sOutday >= otherInday) and otherName != name):
                                contacts.append((otherName, otherNum))

                # Sort contacts alphabetically by name
                contacts.sort(key=lambda x: x[0])

                if contacts:
                    for otherName, otherNum in contacts:
                        print(f"\tContact with {otherName}, phone {otherNum}")
                else:
                    print(f"\tThe guest {sName} had no contacts.")

    except FileNotFoundError as e:
        print(f"The file is not found: {e.filename}")


def main():
    files1 = 'customers.txt'
    files2 = 'suspects.txt'
    display_name_phoneNum(files1, files2)


main()
