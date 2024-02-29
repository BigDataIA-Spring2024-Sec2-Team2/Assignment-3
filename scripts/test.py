import time

def my_function(param1, param2):
    # Example function that may raise an error
    # Here we raise an error if param1 is less than 0
    if param1 < 0:
        raise ValueError("Parameter param1 is less than 0")
    else:
        return f"Success with params: {param1}, {param2}"

def retry_function(func, max_attempts=3, delay=1,**kwargs):
    attempts = 0
    while attempts < max_attempts:
        try:
            result = func(**kwargs)
            return result
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Attempting to fix the issue and retrying...")
            # Perform error handling and attempt to fix the issue
            # For demonstration purposes, we'll just wait for a delay
            time.sleep(delay)
            kwargs['param1'] = 10
            attempts +=  1
    raise RuntimeError(f"Failed after {max_attempts} attempts")

# Example usage
try:
    result = retry_function(my_function, max_attempts=5, delay=2, param1=-10, param2="hello")
    print("Function executed successfully:", result)
except RuntimeError as e:
    print(e)
