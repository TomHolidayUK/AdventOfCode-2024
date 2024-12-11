# Find if a value is of a certain type
value = "hello"
isinstance(value, int)

# convert int char to int 
char = 5
int_representation = int(char)

# sort array of ints
int_array = [2,5,8,3,7]
sorted_array = sorted(int_array)

# how to use list comrehension 
# new_list = [expression for item in iterable if condition]
# the if part is optional
# the if part can be used to selectively add to the list like above or to 
# selectively apply the expression like below
line = []
row = [int(char) if char != '.' else '.' for char in line]

# slicing 
# general form is sequence[start:stop:step]
# we can use negative indexing to refer to values near the end of a list or string
# -1 = the last element and so on
lst[:]	# Copy the entire list
lst[2:]	# From index 2 to the end
lst[:3]	# From the start to index 3 (excl.)
lst[::2]	# Take every second element (step=2)
lst[::-1]	# Reverse the list
lst[:-1]	# All elements except the last one
lst[-3:]	# Last 3 elements
lst[1:-1]	# Remove first and last elements