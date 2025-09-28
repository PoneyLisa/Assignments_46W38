def get_a_list_of_numbers():
    
    list_of_numbers = []
    
    print("Enter numbers separated by spaces. Type 'end' for empty list.") # instruction for the user
    
    user_input = input("Enter the numbers (or 'end' to finish): ").strip() # strip is to remove all the white spaces
       
    if user_input.lower() == 'end':  # Check if user wants to end the input process. The lower() is to make all the uppercase in string to lower case
        return list_of_numbers
    
    number_strings = user_input.split()   #to break input into individual number strings     
        
    for num_str in number_strings:
            try:
                number = float(num_str)

                if number.is_integer():
                    number=int(number)

                list_of_numbers.append(number)
                print(f"Added: {number}")
            
            except ValueError:
                raise ValueError(f"Invalid input: '{num_str}' is not a valid number or 'end'")
        
    return list_of_numbers
        
          
def find_min(list_of_numbers):
    if list_of_numbers:
    # Initialize min with the first number
        minimal = list_of_numbers[0]
           
        # Compare each number with current min
        for number in list_of_numbers:
            if number < minimal:
                minimal = number
        
        return minimal
        
    else:
    # Handle empty list case
        return None
            

def find_max(list_of_numbers):
    if list_of_numbers:
    # Initialize max with the first number
        maximal = list_of_numbers[0]
    
        # Compare each number with current max
        for number in list_of_numbers:
            if number > maximal:
                maximal = number
            
        return maximal
    
    else:
        # Handle empty list case
        return None

if __name__ == "__main__":
    # Call the function and display results
    list_of_numbers = get_a_list_of_numbers()
    print(f"Numbers: {list_of_numbers}")
    
    #Call the function and display results
    get_min = find_min(list_of_numbers)
    print(f"The minimal numbers is: {get_min}")
        
    #Call the function and display results
    get_max = find_max(list_of_numbers)
    print(f"The maximal numbers is: {get_max}")