#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        ans = fct(*args)
    except Exception as i:
        sys.stderr.write("Exception: {}\n".format(i))
        ans = None
    return (ans)
