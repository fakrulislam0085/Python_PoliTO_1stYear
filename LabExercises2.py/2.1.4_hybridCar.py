# Input variables
costOfNewCar = int(input("Cost of a new car: "))
estimateKm = int(input("The estimate of km traveled /year: "))
estimatedFuelCost = float(input("Estimated fuel cost (per liter): "))
efficiencyKmPerLitre = float(input("Efficiency in km per litre: "))
resaleValueAfterFiveyrs = int(input("The estimate of the resale value after 5 years: "))

# Calculate total fuel consumption over 5 years
totalFuelConsumption = (estimateKm * 5) / efficiencyKmPerLitre

# Calculate total fuel cost for 5 years
totalFuelCost = totalFuelConsumption * estimatedFuelCost

# Calculate total cost of ownership for 5 years
totalCostOfOwnership = costOfNewCar + totalFuelCost - resaleValueAfterFiveyrs

# Output the total cost of ownership
print("\n----- Results -----")
print(f"Total Fuel Consumption over 5 years: {totalFuelConsumption:.2f} liters")
print(f"Total Fuel Cost over 5 years: €{totalFuelCost:.2f}")
print(f"Total Cost of Ownership (5 years): €{totalCostOfOwnership:.2f}")

# Run the program twice for hybrid and gasoline models to compare
