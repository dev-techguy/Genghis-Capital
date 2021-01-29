# define the function to receive the array/list to be checked here
def receiveArray(L):
    n = len(L)  # set a variable and assign the length of the array
    sum_of_actual_array = (n + 1) * (n + 2) / 2  # get the summation of all the elements that should be in the array
    sum_of_passed_array = sum(L)
    return sum_of_actual_array - sum_of_passed_array


# Run the program here
if __name__ == '__main__':
    missing_value = receiveArray([2, 3, 1, 5])  # call the function to be executed
    print(missing_value)
