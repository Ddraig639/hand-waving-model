# main.py

# Import the arrays from arrays.py
from arrayf import array1, array2

# Display the arrays
print("Array 1:", array1)
print("Array 2:", array2)

# Delete the second array
del array2

# Try to print the second array to confirm it's deleted
try:
    print("Array 2:", array2)
except NameError:
    print("Array 2 has been deleted.")
