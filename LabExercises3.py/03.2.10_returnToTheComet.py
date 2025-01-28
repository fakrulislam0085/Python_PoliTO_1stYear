import math
#Global Variables
G = 6.67e-11   #Gravitational constant in N m^2 / kg^2
M = 2.2e14     #Mass of Halley's Comet in kg
D = 9.4        #Comet's Diameter in km
R = (D/2) * 1e3    #Convert Km into m

def escape_velocity() :
    return math.sqrt((2 * G * M) / R)

def returning_to_surface(Ve, LV) :
    if LV < Ve :
        print("You will return to the surface of Halley's Comet.")
    else :
        print("You will escape from the Halley's Comet.")
        recquiredMass = ((LV**2) * R) / 2*G
        massDifference = recquiredMass - M 
        print(f"The comet needs to have an additional {massDifference:.2e} kg of mass to keep you on it's surface.")

def main() :
    Ve = escape_velocity()     #m/s
    escape_velocity_earth = 11 * 1000  #m/hr
    try :
        launchVelocity = float(input("Enter the launch velocity(in km/hr): "))
        LV = (launchVelocity * 1e3) / 3600  #km/h to m/s
        print(f"\nEscape velocity of Halley's Comet: {Ve:.3f} m/s")
        print(f"Your launch velocity: {LV:.3f} m/s")
        returning_to_surface(Ve, LV) 

    except ValueError :
        print(f"Error: Please give a valid input!")
        return
    

main()