#!/usr/bin/env python
"""
Provides all enviroment variables and constants used in the library
"""
import requests
import json

# Timing
LIMIT_TIMEOUT= 60
BASE_TIMEOUT= 10
SLEEP_TIME= 10
OFFSET= 0
RETRYING_TIME= 1
LIMIT_RETRYING_TIMES= 10

# Exceptions Functions
def Exception_Handler(func):
    
    # Inner function handles exceptions
    def inner_function(*args, **kwargs):
        
        timeout = BASE_TIMEOUT
        
        while True:
            try:
                return func(*args, **kwargs)

            # Bad URL/Invalid URL
            except requests.exceptions.InvalidURL as url_error:
                print(f"Exception: {url_error} ! PLEASE CHECK YOUR URL ENDPOINT OR NETWORK ARE CORRECT BEFORE LOOKING INTO OTHER ERRORS !")
                break
            
            # Bad server connection error
            except requests.exceptions.ConnectionError as error:
                print(f"Exception: {error} ! PLEASE CHECK YOUR URL ENDPOINT OR NETWORK ARE CORRECT BEFORE LOOKING INTO OTHER ERRORS !")
                break

             # Bad JSON error
            except json.decoder.JSONDecodeError as json_error:
                print(f"JSON Exception: {json_error}. PLEASE CHECK URL/ENDPOINT & NETWORK FOR YOUR KOIOS SERVER IS FORMATTED CORRECT/EXISTS/ONLINE!")
                break
            # Timeout error
            
            except requests.exceptions.ReadTimeout as timeout_error:
                if timeout < LIMIT_TIMEOUT:
                    timeout= timeout + 10
                else:
                    print(f"Reach Limit Timeout= {LIMIT_TIMEOUT} seconds")
                    break
                print(f"Retriyng with longer timeout: Total Timeout= {timeout}s")
            
            # UnboundLocalError
            except UnboundLocalError as error:
                print(f"Exception: {error}")
                break
                
            # All other exceptions
            except Exception as e:
                print(f"Exception: {e}")
                break
            
    return inner_function
                

            

# def handle_timeout_exceptions(timeout, timeout_error):
#     """
#     Handle the timeout exceptions
#     """
#     print(f"Exception: {timeout_error}")
#     if timeout < LIMIT_TIMEOUT:
#         timeout= timeout + 10
#     else:
#         print(f"Reach Limit Timeout= {LIMIT_TIMEOUT} seconds")
#         return
#     print(f"Retriyng with longer timeout: Total Timeout= {timeout}s")