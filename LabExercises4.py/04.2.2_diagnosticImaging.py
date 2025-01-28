import math 

def decay_model() :
#given values 
    half_life = 6   #half_life of Technetium-99 in hours
    lambda_val = math.log(2) / half_life    #decay constant calculation
    time_hours = 24   #total time in hours 

    #display header 
    print("Hour\tRelative Amount (A/A0)")

    for t in range(time_hours+1) :
        relative_amount = math.exp(-lambda_val * t) 
        print(f"{t}\t{relative_amount:.4f}")

decay_model()

