# Get user input for the list (as a string)
input_list = input("Enter a list of integers separated by spaces: ")

# Convert the input string to a list of integers
my_list = [int(n) for n in input_list.split()]

# Initialize a variable to store the sum of all integers in the list
total_sum = 0

# Use a for loop to add each item in the list
for number in my_list:
    total_sum += number  # This is equivalent to total_sum = total_sum + number

# Print the final sum
print(total_sum)
