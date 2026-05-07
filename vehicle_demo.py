import vehicle


car = vehicle.Car("Toyota", "Camry", 35000, 22000, 4)

truck = vehicle.Truck("Ford", "F-150", 50000, 31000, "4WD")

suv = vehicle.SUV("Honda", "CR-V", 27000, 28000, 5)


print("USED CAR INVENTORY\n")

print("The following car is in inventory:")
print("Make:", car.get_make())
print("Model:", car.get_model())
print("Mileage:", car.get_mileage())
print("Price:", car.get_price())
print("Number of doors:", car.get_doors())

print("\nThe following pickup truck is in inventory:")
print("Make:", truck.get_make())
print("Model:", truck.get_model())
print("Mileage:", truck.get_mileage())
print("Price:", truck.get_price())
print("Drive type:", truck.get_drive_type())

print("\nThe following SUV is in inventory:")
print("Make:", suv.get_make())
print("Model:", suv.get_model())
print("Mileage:", suv.get_mileage())
print("Price:", suv.get_price())
print("Passenger capacity:", suv.get_passenger_capacity())


# Reflection Questions:
# 1. The Automobile class is the superclass.
# 2. The Car, Truck, and SUV classes are subclasses.
# 3. The subclasses inherit make, model, mileage, and price.
# 4. The Car class has the unique attribute doors.
# 5. The Truck class has the unique attribute drive type.
# 6. The SUV class has the unique attribute passenger capacity.
# 7. Inheritance is useful because it prevents repeating code.
# 8. Copying and pasting code could cause mistakes and make updates harder.