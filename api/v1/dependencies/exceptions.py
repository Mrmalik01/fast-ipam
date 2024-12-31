
class FieldErrorException(Exception):
    def __init__(self, field: str, value: str, message: str):
        self.field = field
        self.value = value
        self.message = message
        super().__init__(message)


class PutOperationException(Exception):
    def __init__(self, message):
        super().__init__(message)


class InternalServerErrorException(Exception):
    def __init__(self, message):
        super().__init__(message)


class NotFoundException(FieldErrorException):
    def __init__(self, field: str, value: str, message: str):
        super().__init__(field, value, message)


class BadRequestException(Exception):
    def __init__(self, message):
        super().__init__(message)