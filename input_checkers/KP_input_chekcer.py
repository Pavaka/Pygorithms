def check_input_data(items, capacity):
    """ This is a function that checks if the given input
    is correct. This means that the capacity must be an positive integer.
    Items must be a list or tuple. All items in items must be
    a list or a tupele of size two, and both elements inside have to
    be integers greater that or equal to zero.
    """

    if not isinstance(capacity, int):
        raise CapacityNotAnIntegerError

    if capacity < 0:
        raise NegativeCapacityError

    if not isinstance(items, (list, tuple)):
        raise ItemsNotAListOrTupleError

    for item in items:
        if not isinstance(item, (list, tuple)):
            raise InvalidItemError

        if len(item) != 2:
            raise InvalidItemError

        if not isinstance(item[0], int) or not isinstance(item[1], int):
            raise InvalidItemError

        if item[0] < 0:
            raise ItemWithNegativeValueError

        if item[1] < 0:
            raise ItemWithNegativeWeightError


class NegativeCapacityError(Exception):
    pass


class ItemWithNegativeValueError(Exception):
    pass


class ItemWithNegativeWeightError(Exception):
    pass


class CapacityNotAnIntegerError(Exception):
    pass


class ItemsNotAListOrTupleError(Exception):
    pass


class InvalidItemError(Exception):
    pass
