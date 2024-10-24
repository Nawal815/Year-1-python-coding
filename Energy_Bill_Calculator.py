#Energy bill calculator program

#---------------------------
#subprograms
#---------------------------
def energy_cost(previous_meter_reading, current_meter_reading, calorific_value):
    units_used = current_meter_reading - previous_meter_reading
    kwh = units_used * 1.022 * (calorific_value / 3.6)
    cost = 0.0284 * kwh
    return int(cost)
#---------------------------
#Main program
#---------------------------
previous_meter_reading = int(input("Enter the previous meter reading:"))
current_meter_reading = int(input("Enter the current meter reading rounded down:"))
calorific_value = 39.3
cost = energy_cost(previous_meter_reading, current_meter_reading, calorific_value)
print("Cost is £", cost)