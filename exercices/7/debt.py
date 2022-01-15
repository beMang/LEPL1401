def give_money(borrowed_money: dict, from_person, to_person, amount):
    if from_person == to_person or type(from_person) != str or type(to_person) != str or (type(amount) != int and type(amount) != float) or type(borrowed_money) != dict:
        raise ValueError()
    else:
        try:
            borrowed_money[from_person][to_person] = borrowed_money.get(
                from_person).get(to_person, 0) - amount
        except Exception:
            borrowed_money[from_person] = {to_person: -amount}
        try:
            borrowed_money[to_person][from_person] = borrowed_money.get(
                to_person).get(from_person, 0) + amount
        except Exception:
            borrowed_money[to_person] = {from_person: amount}


def total_money_borrowed(borrowed_money):
    if type(borrowed_money) != dict:
        raise ValueError()
    else:
        sum = 0
        for k, v in borrowed_money.items():
            for person, value in v.items():
                if value > 0:
                    sum += value
        return sum


borrowed_money = {}
give_money(borrowed_money, "Mark", "Steve", 2000000)
give_money(borrowed_money, "Mark", "Bill", 2000000)
give_money(borrowed_money, "Serguei", "Bill", 5000000)
give_money(borrowed_money, "Bill", "Larry", 6000000)
give_money(borrowed_money, "Larry", "Linus", 5.5)
give_money(borrowed_money, "Steve", "Mark", 2000000)
