class CustomException(Exception):
    def __init__(self, message, file_name='logs.txt'):
        super().__init__(message)
        self.file_name = file_name

    def log_error(self):
        with open(self.file_name, 'a') as log_file:
            log_file.write(f"Error: {self.__class__.__name__} - {self}\n")


try:
    raise CustomException("This is a custom exception message")
except CustomException as ce:
    ce.log_error()
