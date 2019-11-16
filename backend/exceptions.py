class DatabaseException(Exception):

    title = "Database Error"
    detail = "An unexpected database error has occurred."


class ObjectNotFound(DatabaseException):

    title = "Object not found"
    detail = "Requested object does not exist."


class RouteNotFoundError(Exception):

    title = "Route not found"
    detail = "There is no route between the points given by the coordinates."
