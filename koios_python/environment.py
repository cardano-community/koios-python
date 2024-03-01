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


def init_timeout():
    '''
    Function to initialize timeout
    '''
    global timeout
    timeout = BASE_TIMEOUT


def get_timeout():
    '''
    Function to Get alive timeout
    '''
    return timeout


def set_timeout(new_timeout):
    '''
    Function to update a new timeout dynamically
    '''
    global timeout
    timeout = new_timeout


def Exception_Handler(func):
    '''
    Exceptions Functions to use as Decorator
    '''

    def inner_function(*args, **kwargs):
        '''
        Inner function handles exceptions
        '''
        retrying_time = RETRYING_TIME
        init_timeout()
        timeout = get_timeout()
        while True:

            try:
                return func(*args, **kwargs)

            # Bad URL/Invalid URL
            except requests.exceptions.InvalidURL as url_error:
                print(f"Exception: {url_error} ! PLEASE CHECK YOUR URL ENDPOINT OR NETWORK ARE CORRECT BEFORE LOOKING INTO OTHER ERRORS !")
                break

            # Bad server connection error
            except requests.exceptions.ConnectionError as connection_error:
                print(f"Exception: {connection_error} ! PLEASE CHECK YOUR URL ENDPOINT OR NETWORK ARE CORRECT BEFORE LOOKING INTO OTHER ERRORS !")
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
                except UnboundLocalError as unbound_error:
                    print(f"Something went wrong XD: {unbound_error}")

                print(f"Retrying one more time...({retrying_time} times)")
                if retrying_time >= LIMIT_RETRYING_TIMES:
                    print("Reached limit of attempts")
                    break
   
            # UnboundLocalError
            except UnboundLocalError as unbound_error:
                print(f"Exception: {unbound_error}")

            # All other exceptions
            except Exception as general_error:
                print(f"Exception: {general_error}")

    return inner_function
