class BusinessException(Exception):
    def __init__(self, message: str, status_code: int):
        self.message = message
        self.status_code = status_code


class NotFoundException(BusinessException):
    def __init__(self, message="Resource not found"):
        super().__init__(message, 404)


class AlreadyExistsException(BusinessException):
    def __init__(self, message="Resource already exists"):
        super().__init__(message, 409)


class UnauthorizedException(BusinessException):
    def __init__(self, message="Unauthorized"):
        super().__init__(message, 401)


class ForbiddenException(BusinessException):
    def __init__(self, message="Forbidden"):
        super().__init__(message, 403)


class BadRequestException(BusinessException):
    def __init__(self, message="Bad request"):
        super().__init__(message, 400)
