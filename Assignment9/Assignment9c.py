"""
This file contains code that makes infinite calls to nameless function by getting code reference
"""
from inspect import currentframe
from types import FunctionType


def myself(*args, **kw):
    """
    This return Reference to code that called this function
    """
    caller_frame = currentframe(1)
    code = caller_frame.f_code
    return FunctionType(code, caller_frame.f_globals)(*args, **kw)

if __name__ == "__main__":
    print (lambda n: n * myself(n+1))(5)
