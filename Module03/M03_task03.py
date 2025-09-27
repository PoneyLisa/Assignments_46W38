
numbers = [] # initialization of an empty list to store numbers

print("Enter numbers one by one. Type 'end' when you're finished.") # instruction for the user

while True:
    user_input = input("Enter a number (or 'end' to finish): ").strip() # strip is to remove all the white spaces
       
    if user_input.lower() == 'end':  # Check if user wants to end the input process. The lower() is to make all the uppercase in string to lower case
        break
    
    try:
        number = float(user_input)  # Try to convert to float first (handles both integers and decimals)
        
        
        if number.is_integer():     # If it's a whole number, convert to int for cleaner display
            number = int(number)
        
        numbers.append(number)
        print(f"Added: {number}")
        
    except ValueError:
        print("Invalid input! Please enter a valid number or 'end' to finish.")

if numbers:
    print(f"You entered {len(numbers)} numbers:")
    print(f"Numbers: {numbers}")
   
else:
    print("No numbers were entered.")