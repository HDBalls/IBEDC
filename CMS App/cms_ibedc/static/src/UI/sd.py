def hello_decorator(val):
    def inner1(val):
         
        if val == 1:
            return True
        
        if val == 2:
            return False
         
    return inner1
 
 
# adding decorator to the function
@hello_decorator
def sum_two_numbers(val):
    print("Inside the function")

sum_two_numbers(1)
