def extract_CSV_file(readFile) :
    readLine = readFile.readline().strip() # Read a single line

    if not readLine : 
        return None   #end of file
    fields = readLine.split(',') # Split the line into fields

    if len(fields) != 4 :
        raise ValueError(f"Invalid line format: {readLine}")
    
    #create a dictionary for the record 
    record = {
        'ID' : fields[0],
        'Surname' : fields[1],
        'First name' : fields[2],
        'Score' : int(fields[3])
    }

    return record

def main() :
    file_name = 'CSV.txt' 

    try :
        with open(file_name, 'r') as infile :
            # Skip the header line
            infile.readline()
            while True :
                record = extract_CSV_file(infile) 
                if not record :
                    break 
                print(record)

    except FileNotFoundError :
        print(f"The file {file_name} does not exist.")
    except ValueError as e :
        print(f"Invalid input. Error: {e}")
    except Exception as explanation :
        print(f"An unexpected error occurred: {explanation}")


main() 