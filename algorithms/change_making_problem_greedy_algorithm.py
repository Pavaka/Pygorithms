def change_making_problem_greedy_algorithm(coin_denominations, money_amount):
    """

    """
    check_input_data(coin_denominations, money_amount)

    coin_denominations = sorted(coin_denominations, reverse=True)

    for index, denomination in enumerate(iter(coin_denominations)):
        money_left_for_change = money_amount
        current_coin_index = index
        feasible_solution = []
        print(money_amount, index, feasible_solution)
        while True:
            print(money_left_for_change)

            try:
                current_coin_value = coin_denominations[current_coin_index]
            except:
                raise EnvironmentError

            print(current_coin_value, current_coin_index, money_left_for_change)
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
    pass
