class MyVeryOwnError(Exception):
    def __init__(self, error_message='my very own error message'):
        self.error_message = error_message
