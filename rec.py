def calc_distance(tank_gas, num_barrels):
  print(f"Tank gas: {tank_gas}, num_barrels:{num_barrels}")
  # Calculate the total amount of gas available, including the barrels
  total_gas = tank_gas + (num_barrels * 100)
  print(f"Total gas: {total_gas}")
  # If there is enough gas to travel 100 km, return the distance traveled
  if total_gas >= 10:
    return 100 + calc_distance(total_gas - 10, num_barrels)
  else:
    # If there is not enough gas to travel 100 km, return the distance traveled
    return total_gas / 10

def calc_distance2(tank_gas, barrels_gas):
    print(f"Tank gas: {tank_gas}, barrels_gas:{barrels_gas}")
    if tank_gas:
        print(f"Travelling for 100km...")
        return 100 + calc_distance2(tank_gas-10, barrels_gas)
    if barrels_gas:
        print("Taking from a barrel")
        return calc_distance2(tank_gas+20, barrels_gas-20)
    return 0

# Initialize variables for the amount of gas in the tank and the number of barrels
tank_gas = 20
num_barrels = 3

# Calculate the distance the car can travel
#distance = calc_distance(tank_gas, num_barrels)

barrels_gas = num_barrels * 100
distance = calc_distance2(tank_gas, barrels_gas)

# Print the result
print("The car can travel a distance of", distance, "km on this amount of gas.")
