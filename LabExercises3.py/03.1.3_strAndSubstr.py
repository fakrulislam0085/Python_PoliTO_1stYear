long_sequence = input("Write the long sequence: ")     #20 characters according to question
short_sequence = input("Write the short sequence: ")    #3 characters according to question


#check whether the short_sequence is present or not
if short_sequence in long_sequence :
    print("YES: The long sequence contains the short sequence")

    #find out the first index of first occurrence
    start_position = long_sequence.find(short_sequence)
    print(f"Starting position of the first occurrence's is: {start_position}")

    #count times
    count = long_sequence.count(short_sequence)
    print(f"Short sequence appers in total is {count} times")

else :
    print("The long sequence does not contain the short sequence")