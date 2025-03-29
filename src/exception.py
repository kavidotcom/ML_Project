import sys
import logging

def error_messages(error, error_details):
    _, _, exc_tb = error_details.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in script name {0} line number {1} error message {2}".format(
        file_name, exc_tb.tb_lineno, str(error)
    )


class CustomException(Exception):
    def __init__(self, error_message, error_details):
        super().__init__(error_message)
        self.error_message = error_messages(error_message, error_details)

    def __str__(self):
        return self.error_message
    

if __name__ == "__main__" :

    try :
        a = 1/0
    except Exception as e:
        logging.info("Divide by zero error")
        raise CustomException(e, sys)
    