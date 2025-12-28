# Input temperature in Celsius
temp_c = float(input("Enter temperature in Celsius: "))

# Convert to Fahrenheit
temp_f = temp_c * (9/5) + 32

# Print Fahrenheit temperature
print("Temperature in Fahrenheit:", temp_f)

# Print advice based on Celsius temperature
if temp_c < 0:
    print("Very cold! Wear thick jacket")
elif 0 <= temp_c <= 15:
    print("Cold. Wear jacket")
elif 16 <= temp_c <= 25:
    print("Nice weather")
else:
    print("Hot! Stay hydrated")

             
