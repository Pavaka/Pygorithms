problem_types = ("min", "max")
signs = ("le", "eq", "ge")


def check_input_data(function_coefficients, matrix_A, vector_B,
                     problem_type, signs_vector, non_negative_constraints):

    listalike_args = function_coefficients, matrix_A,\
        vector_B, signs_vector, non_negative_constraints
    type_errors = FuncCoefTypeError, MatrixATypeError,\
        VectorBTypeError, SignsVectorTypeError, NonNegativeConstraintTypeError

    for index, item in enumerate(iter(listalike_args)):
        try:
            _is_list(item)
        except NotAListError:
            raise type_errors[index]

    if problem_type not in problem_types:
        raise ProblemTypeValueError

    try:
        _all_values_numbers(function_coefficients)
    except ValueNaNError:
        raise FuncCoefValueError

    for row in matrix_A:
        if not isinstance(row, list):
            raise MatrixAValueError
        for i in row:
            if not isinstance(i, (int, float)):
                raise MatrixAValueError

    try:
        _all_values_numbers(vector_B)
    except ValueNaNError:
        raise VectorBValueError

    for value in signs_vector:
        if value not in signs:
            raise SignsVectorValueError

    for constraint in non_negative_constraints:
        if not isinstance(constraint, bool):
            raise NonNegativeConstraintValueError

    variables_count = set()
    variables_count.add(len(function_coefficients))
    for row in matrix_A:
        variables_count.add(len(row))
    variables_count.add(len(non_negative_constraints))
    _check_incompitable_size(variables_count)

    constraints_count = set()
    constraints_count.add(len(matrix_A))
    constraints_count.add(len(vector_B))
    constraints_count.add(len(signs_vector))
    _check_incompitable_size(constraints_count)


def _check_incompitable_size(item):
    if len(item) > 1:
        raise IncompitableVectorSizesError


def _is_list(item):
    if item == []:
        raise NotAListError
    if not isinstance(item, list):
        raise NotAListError


def _all_values_numbers(item):

    for value in item:
        if not isinstance(value, (int, float)):
            raise ValueNaNError


class ValueNaNError(Exception):
    pass


class NotAListError(Exception):
    pass


class IncompitableVectorSizesError(Exception):
    pass


class FuncCoefTypeError(Exception):
    pass


class MatrixATypeError(Exception):
    pass


class VectorBTypeError(Exception):
    pass


class SignsVectorTypeError(Exception):
    pass


class NonNegativeConstraintTypeError(Exception):
    pass


class ProblemTypeValueError(Exception):
    pass


class FuncCoefValueError(Exception):
    pass


class MatrixAValueError(Exception):
    pass


class VectorBValueError(Exception):
    pass


class SignsVectorValueError(Exception):
    pass


class NonNegativeConstraintValueError(Exception):
    pass
