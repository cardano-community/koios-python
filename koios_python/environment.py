#!/usr/bin/env python
"""
Provides all enviroment variables and constants used in the library
"""
from time import sleep
import json
import requests


# Timing
BASE_TIMEOUT= 10
LIMIT_TIMEOUT= 60
BASE_TIMEOUT= 10
SLEEP_TIME= 10
OFFSET= 0
RETRYING_TIME= 1
LIMIT_RETRYING_TIMES= 10


# Function to initialize timeout
def init_timeout():
    global timeout
    timeout = BASE_TIMEOUT

# Function to Get alive timeout
def get_timeout():
    return timeout

# Function to update a new timeout dynamically
def set_timeout(new_timeout):
    global timeout
    timeout = new_timeout


# Exceptions Functions
def Exception_Handler(func):

    # Inner function handles exceptions
    def inner_function(*args, **kwargs):
        retrying_time = RETRYING_TIME
        init_timeout()
        timeout = get_timeout()
        print('timeout '+str(timeout))
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
            
            # Timeout error
            except requests.exceptions.ReadTimeout as timeout_error:
                print(f"Exception: {timeout_error}")
                if timeout < LIMIT_TIMEOUT:
                    timeout= timeout + 10
                    # Updating the new Timeout for the function
                    set_timeout(timeout)

                else:
                    print(f"Reach Limit Timeout= {LIMIT_TIMEOUT} seconds")
                    break
                print(f"Retrying with longer timeout: Total Timeout= {timeout}s")

            # Bad JSON error
            except json.decoder.JSONDecodeError as decode_error:
                print(f"Exception Decode: Payload too heavy....bad JSON returned. {decode_error}")
                sleep(SLEEP_TIME)
                try:
                    retrying_time += 1
                except UnboundLocalError as error:
                    print(f"Something went wrong XD: {error}")
                    
                print(f"Retrying one more time...({retrying_time} times)")
                if retrying_time >= LIMIT_RETRYING_TIMES:
                    print("Reached limit of attempts")
                    break
                      
            # UnboundLocalError
            except UnboundLocalError as error:
                print(f"Exception 1: {error}")
            
 
            # All other exceptions
            except Exception as e:
                print(f"Exception 2: {e}")
                
    return inner_function