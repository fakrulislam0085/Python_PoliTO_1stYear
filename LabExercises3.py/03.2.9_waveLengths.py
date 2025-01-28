def electromagnetin_spectrum(wl) :
    if wl > 1e-1 :
        spectrum = "Radio Wave"
        frequency = "< 3 * 10^9 Hz"
    elif 1e-3 <= wl <= 1e-1 :
        spectrum = "Microwave"
        frequency = "From 3 * 10^9 to 3 * 10^11 Hz"
    elif 7e-7 <= wl < 1e-3 :
        spectrum = "Infared"
        frequency = "From 3 * 10^11 to 4 * 10^14 Hz"
    elif 4e-7 <= wl < 7e-7 :
        spectrum = "Visible light"
        frequency = "From 4 * 10^14 to 7.5 * 10^14 Hz"
    elif 1e-8 <= wl < 4e-7 :
        spectrum = "Ultraviolet"
        frequency = "From 7.5 * 10^14 to 3 * 10^16 Hz"
    elif 1e-11 <= wl < 1e-8 :
        spectrum = "X-rays"
        frequency = "From 3 * 10^16 to 3 * 10^19 Hz"
    elif wl < 1e-11 :
        spectrum = "Gamma rays"
        frequency = "> 3 * 10^19 Hz"
    
    return spectrum , frequency 

def main() :
    try :
        print("Welcome to the Electromagnetic Spectrum Analyzer!")
        WaveLength = float(input("Enter the wave length value in meters(e.g., 1.23e-7): "))
        type, frequency = electromagnetin_spectrum(WaveLength)
        print(f"\nWave Length: {WaveLength} m")
        print(f"\nThe corresponding part of the electromagnetic spectrum is:\nType: {type}\nFrequency: {frequency}")

    except ValueError :
        print(f"Error: Please enter a valid real number in scientific notation.")
        return

main()