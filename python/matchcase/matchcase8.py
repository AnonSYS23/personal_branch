print('Welcome to Latin American Pesos Converter')

user = str(input('Name of the user :'))

def convert_to_colombian_pesos(dollars):
    return dollars * 3564.75  # current exchange rate as of 3/22/23

def convert_to_mexican_pesos(dollars):
    return dollars * 20.75  # current exchange rate as of 3/22/23

def convert_to_argentine_pesos(dollars):
    return dollars * 105.34  # current exchange rate as of 3/22/23

dollars = float(input("Enter a dollar amount to convert: "))

print("Select a currency to convert to:")
print("1. Colombian pesos")
print("2. Mexican pesos")
print("3. Argentine pesos")

choice = int(input("Enter your choice (1, 2, or 3): "))

if choice == 1:
    result = convert_to_colombian_pesos(dollars)
    print(f"${dollars:.2f} is equivalent to {result:.2f} Colombian pesos")
elif choice == 2:
    result = convert_to_mexican_pesos(dollars)
    print(f"${dollars:.2f} is equivalent to {result:.2f} Mexican pesos")
elif choice == 3:
    result = convert_to_argentine_pesos(dollars)
    print(f"${dollars:.2f} is equivalent to {result:.2f} Argentine pesos")
else:
    print("Invalid choice. Please select 1, 2, or 3.")
