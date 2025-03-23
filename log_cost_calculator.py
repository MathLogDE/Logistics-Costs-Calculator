#imputs
pack_weight = 0
pack_weight = float(input("Enter the weight of the package: "))
distance_to_delivery = 0
distance_to_delivery = float(input("Enter the distance to delivery: "))

#constants
COST_PER_KM = 500
ADMIN_COST = 1000
MAX_DISTANCE = 500
MIN_DISTANCE = 5
MAX_WEIGHT = 10
package_handlable = False

#test if the package fullfill the requirements:

if pack_weight > MAX_WEIGHT:
    print("The package is too heavy to be delivered")
elif distance_to_delivery > MAX_DISTANCE:
    print("The distance is too far to be delivered")
elif distance_to_delivery < MIN_DISTANCE:
    print("The distance is too short to be delivered")
else:
    package_handlable = True

#calculate the total cost of delivery 
if package_handlable:
    total_cost = (distance_to_delivery * COST_PER_KM) + ADMIN_COST
    print(f"The total cost of delivery is: ${total_cost:.2f}");