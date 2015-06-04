def change_making_problem_greedy_algorithm(coin_denominations, money_amount):
    """
    Function that solves the change making problem using a greedy algorithm
    approach. The function  takes two arguments, a list or tuple of positive
    integers, and a positive integer. It returns a list that contains
    the coins that must be returned.
    Each coint that must be returned is represented by its denomination.
    Example:
    change_making_problem_greedy_algorithm([1, 2, 7], 12)
    will return a list [7, 2, 2, 1]
    This means that you will return 4 coins with the respective
    denominations.
    """
    check_input_data(coin_denominations, money_amount)

    coin_denominations = sorted(coin_denominations, reverse=True)

    for index, denomination in enumerate(iter(coin_denominations)):
        money_left_for_change = money_amount
        current_coin_index = index
        feasible_solution = []
        while True:

            try:
                current_coin_value = coin_denominations[current_coin_index]
            except:
                raise NoFeasibleSolutionError

            if money_left_for_change - current_coin_value > 0:
                money_left_for_change -= current_coin_value
                feasible_solution.append(current_coin_value)
                continue
            elif (money_left_for_change - current_coin_value) == 0:
                feasible_solution.append(current_coin_value)
                return feasible_solution
            else:
                current_coin_index += 1


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

    for denomination in coin_denominations:
        if not isinstance(denomination, int):
            raise CoinDenominationNotAnIntegerError
        elif denomination < 1:
            raise CoinDenominationNonPositiveError


class NoFeasibleSolutionError(Exception):
    pass


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
