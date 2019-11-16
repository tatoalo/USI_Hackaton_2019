class DatabaseException(Exception):

    title = "Database Error"
    detail = "An unexpected database error has occurred."


class ObjectNotFound(DatabaseException):

    title = "Object not found"
    detail = "Requested object does not exist."
