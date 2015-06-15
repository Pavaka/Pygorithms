def check_input_data(costs, vector_a, vector_b):

    if not _is_list(vector_a):
        raise VectorANotListError

    if not _is_list(vector_b):
        raise VectorBNotListError

    if not _is_list(costs):
        raise CostsNotListError

    if 0 in (len(costs), len(vector_a), len(vector_b)):
        raise EmptyListError

    _check_all_values_positive_integers(costs)
    _check_all_values_positive_integers(vector_a)
    _check_all_values_positive_integers(vector_b)


class EmptyListError(Exception):
    pass


class VectorANotListError(Exception):
    pass


class VectorBNotListError(Exception):
    pass


class CostsNotListError(Exception):
    pass


class ListContainsNaN(Exception):
    pass


class NegativeValueError(Exception):
    pass


def _is_list(item):
    if isinstance(item, (list, tuple)):
        return True
    else:
        return False


def _check_all_values_positive_integers(values):
    for value in values:
        if not isinstance(value, int):
            raise ListContainsNaN
        if value <= 0:
            raise NegativeValueError

__all__ = ["check_input_data", "VectorANotListError",
           "VectorBNotListError", "CostsNotListError",
           "ListContainsNaN", "NegativeValueError",
           "EmptyListError"]
