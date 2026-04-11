import sys
import logging

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info() # used to get the details of the exception and we are interested only in traceback
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = f"Error occured in script : [{file_name}] at line number : [{line_number}] error message : [{str(error)}]"
    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message) # because we are inheriting from the base class Exception, we need to call the constructor of the base class to initialize the error message
        self.error_message = error_message_detail(error_message,error_detail)

    def __str__(self):
        return self.error_message
