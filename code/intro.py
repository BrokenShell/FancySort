""" Fancy Sort

Method: List.sort() - Modifies the list (Destructive)
Function: sorted(List) - Returns a new sorted list (Non-destructive)
"""

arr_1 = [2, 9, 1, 8, 3, 7, 4, 6, 5]
arr_1.sort()
print(f"Same list with new order: {arr_1=}")
# The equals sign after the variable name will change the way it prints
# It adds the variable name to the printout: `arr_1=[1, 2, 3, 4, 5, 6, 7, 8, 9]`

arr_2 = [2, 9, 1, 8, 3, 7, 4, 6, 5]
arr_3 = sorted(arr_2)
print(f"Original list with old order: {arr_2=}")
print(f"New list with new order: {arr_3=}")
