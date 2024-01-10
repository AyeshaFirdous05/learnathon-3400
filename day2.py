print("Hello, Iam Ayesha.\nWelcome to the world of python.")


# Function to calculate total cost with tax
def calculate_total_cost(item_cost, tax_rate):
    # Calculate tax amount
    tax_amount = item_cost * (tax_rate / 100)
    
    # Calculate total cost
    total_cost = item_cost + tax_amount
    
    return total_cost

# Get item cost and tax rate as input
item_cost = float(input("Enter the cost of the item: $"))
tax_rate = float(input("Enter the tax rate in percentage: "))

# Calculate and print the total cost
total_cost = calculate_total_cost(item_cost, tax_rate)
print(f"The total cost, including tax, is: ${total_cost:.2f}")


# Function to calculate the area of a rectangle
def calculate_rectangle_area(length, width):
    area = length * width
    return area

# Get length and width as input
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Calculate and print the area
area = calculate_rectangle_area(length, width)
print(f"The area of the rectangle is: {area} square units.")


# Get input values for variables
variable1 = input("Enter the value for variable1: ")
variable2 = input("Enter the value for variable2: ")

# Print the original values
print(f"Original values: variable1 = {variable1}, variable2 = {variable2}")

# Swap the values
variable1, variable2 = variable2, variable1

# Print the swapped values
print(f"After swapping: variable1 = {variable1}, variable2 = {variable2}")