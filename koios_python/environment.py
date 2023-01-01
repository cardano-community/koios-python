#!/usr/bin/env python
"""
Provides all enviroment variables and constants used in the library
"""

# Timing
LIMIT_TIMEOUT= 60
BASE_TIMEOUT= 10
SLEEP_TIME= 10
OFFSET= 0
RETRYING_TIME= 1
LIMIT_RETRYING_TIMES= 10

# Exceptions Functions
def handle_timeout_exceptions(timeout, timeout_error):
    """
    Handle the timeout exceptions
    """
    print(f"Exception: {timeout_error}")
    if timeout < LIMIT_TIMEOUT:
        timeout= timeout + 10
    else:
        print(f"Reach Limit Timeout= {LIMIT_TIMEOUT} seconds")
        return
    print(f"Retriyng with longer timeout: Total Timeout= {timeout}s")