import sys

def error_message_details(error, error_detail:sys): # error_detail will be present inside sys

    # the below code tells, in which file, on which line number, the exception has occured !
    _, _, exc_tb = error_detail.exc_info()

    # in which filename we're probably getting the error...
    file_name = exc_tb.tb_frame.f_code.co_filename

    # display error message
    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )

    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message