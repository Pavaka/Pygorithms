def check_input_data(coin_denominations, money_amount):
    """
    Funtion that checks the correctness of the given arguments.
    The function arguments are considered correct if,
    the coin_denominations argument is a list or a tuple
    that cointains only positive integers.
    money_amount is a positive integer.
    """
    if not isinstance(money_amount, int):
        raise MoneyAmountNotAnIntegerError

    if money_amount <= 0:
        raise NonPositiveMoneyAmountError

    if not isinstance(coin_denominations, (tuple, list)):
        raise CoinDenominationsNotAListOrTupleError
    if len(coin_denominations) == 0:
        raise EmptyCoinsListError
    for denomination in coin_denominations:
        if not isinstance(denomination, int):
            raise CoinDenominationNotAnIntegerError
        elif denomination < 1:
            raise CoinDenominationNonPositiveError


class MoneyAmountNotAnIntegerError(Exception):
    pass


class NonPositiveMoneyAmountError(Exception):
    pass


class CoinDenominationsNotAListOrTupleError(Exception):
    pass


class CoinDenominationNotAnIntegerError(Exception):
    pass


class CoinDenominationNonPositiveError(Exception):
    pass


class EmptyCoinsListError(Exception):
    pass
