#Write a Python program that reads a text file named numbers.txt that contains 20 integers.

try:
    # More descriptive variable names
    input_file = open("integers_file_processor/numbers.txt", "r")
    print(input_file)  # Shows file info
    
    # Read lines
    all_lines = input_file.readlines()
    input_file.close()
    
    # Convert to list of integers
    all_numbers = []
    for line in all_lines:
        all_numbers.append(int(line.strip()))
    
    # Separate into even and odd lists
    even_numbers = []
    odd_numbers = []
    for number in all_numbers:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            odd_numbers.append(number)
    
    # Write even numbers to file
    even_output_file = open("even.txt", "w")
    for even_num in even_numbers:
        even_output_file.write(str(even_num) + "\n")
    even_output_file.close()
    
    # Write odd numbers to file
    odd_output_file = open("odd.txt", "w")
    for odd_num in odd_numbers:
        odd_output_file.write(str(odd_num) + "\n")
    odd_output_file.close()
    
    print("even.txt and odd.txt created!")
    print(f"Even numbers: {len(even_numbers)}, Odd numbers: {len(odd_numbers)}")

except FileNotFoundError:
    print("numbers.txt not found! Create it first.")
except ValueError:
    print("Invalid numbers in file.")