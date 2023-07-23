# Task 1

# Write a decorator that ensures a function is only called by users with a specific role. Each function should have an user_type with a string type in kwargs. Example:
# @is_admin
# def show_customer_receipt(user_type: str):
    # Some very dangerous operation

# show_customer_receipt(user_type='user')
# > ValueError: Permission denied

# show_customer_receipt(user_type='admin')
# > function pass as it should be


# Solution:
@is_admin
def show_customer_receipt(user_type: str):
    # Some very dangerous operation
    print("Customer receipt is shown.")

def is_admin(func):
    def wrapper(*args, **kwargs):
        user_type = kwargs.get('user_type')
        if user_type == 'admin':
            return func(*args, **kwargs)
        else:
            raise ValueError('Permission denied')
    return wrapper

# Testing the function with different user types
try:
    show_customer_receipt(user_type='user')
except ValueError as e:
    print(e)  # Output: Permission denied

show_customer_receipt(user_type='admin')
# Output: Customer receipt is shown.


# Task 2

# Write a decorator that wraps a function in a try-except block and prints an error if any type of error has happened. Example:

# @catch_errors
# def some_function_with_risky_operation(data):
#     print(data['key'])


# some_function_with_risky_operation({'foo': 'bar'})
# > Found 1 error during execution of your function: KeyError no such key as foo

# some_function_with_risky_operation({'key': 'bar'})
# > bar

# Solution:

def catch_errors(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Found 1 error during execution of your function: {type(e).__name__} - {e}")
    return wrapper

@catch_errors
def some_function_with_risky_operation(data):
    print(data['key'])

some_function_with_risky_operation({'foo': 'bar'})
# Output: Found 1 error during execution of your function: KeyError - 'key'

some_function_with_risky_operation({'key': 'bar'})
# Output: bar