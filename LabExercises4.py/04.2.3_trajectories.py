g = 9.81    #m/s^2
delta_t = 0.01  

def main() :
    Vo = float(input("Enter initial velocity(m/s): "))

    #initialization variables 
    V = Vo      #current velocity 
    S = 0       #currrent position 
    T = 0       #time

    #simulation loop 
    while S >= 0 :      #continue until the ball falls back to the ground 
        S = S + V * delta_t     #update position 
        V = V - g * delta_t     #update velocity
        T += delta_t            #increment time

        if round(T, 2) == int(T) :      #Print position once per simulated second
            exact_pos = (-0.5)*g*T**2 + Vo * T  #exact formula
            print(f"Time: {T:.2f} s, simulated position: {S:.2f} m, Exact position: {exact_pos:.2f} m")

main()