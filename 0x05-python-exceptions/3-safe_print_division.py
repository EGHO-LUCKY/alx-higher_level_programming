#!/usr/bin/python3
def safe_print_division(a, b):
    response = None
    try:
        response = a / b
    except Exception:
        pass
    finally:
        print("Inside result: {}".format(response))
    return response
