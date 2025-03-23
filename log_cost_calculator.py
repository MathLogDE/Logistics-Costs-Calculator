pack_weight = 0
pack_weight = float(input("Enter the weight of the package: "))
distance_to_delivery = 0
distance_to_delivery = float(input("Enter the distance to delivery: "))

#constants
cost_per_km = 500
admin_cost = 1000
max_distance = 500
min_distance = 5
max_weight = 10
package_handlable = False

#test if the package fullfill the requirements:

if pack_weight > max_weight:
    print("The package is too heavy to be delivered")
elif distance_to_delivery > max_distance:
    print("The distance is too far to be delivered")
elif distance_to_delivery < min_distance:
    print("The distance is too short to be delivered")
else:
    package_handlable = True

#calculate the total cost of delivery 
if package_handlable:
    total_cost = (distance_to_delivery * cost_per_km) + admin_cost
    print("The total cost of delivery is: $", total_cost)