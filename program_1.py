driver_teeth = int(input("Enter number of teeth on DRIVER gear: "))
driven_teeth = int(input("Enter number of teeth on DRIVEN gear: "))

input_speed = float(input("Enter input speed (RPM): "))
input_torque = float(input("Enter input torque: "))

gear_ratio = driven_teeth / driver_teeth

output_speed = input_speed / gear_ratio
output_torque = input_torque * gear_ratio

print("Gear Ratio:", gear_ratio)
print("Output Speed in RPM:", output_speed)
print("Output Torque:", output_torque)
