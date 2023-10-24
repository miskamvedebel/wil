class Food(object):
    def __init__(self, n, v, w) -> None:
        self.name = n
        self.value = v
        self.calories = w
    
    def getValue(self):
        return self.value

    def getCost(self):
        return self.calories
    
    def density(self):
        return self.getValue() / self.getCost()

    def __str__(self) -> str:
        return self.name + ': <' + str(self.value) + ', ' + str(self.calories) + '>'

def build_menu(names, values, calories):
    """names, values, calories lists of same length
    name is list of strings
    values and calories are lists of numbers
    returns list of Foods
    """

    menu = []
    for i in range(len(values)):
        menu.append(Food(names[i], values[i], calories[i]))

    return menu

def greedy(items, max_cost, key_function):
    items_copy = sorted(items, key=key_function, reverse=True)
    result = []
    total_value, total_cost = 0.0, 0.0

    for i in range(len(items_copy)):
        if (total_cost + items_copy[i].getCost()) <= max_cost:
            result.append(items_copy[i])
            total_cost += items_copy[i].getCost()
            total_value += items_copy[i].getValue()

    return (result, total_value)

def test_greedy(items, constraint, key_function):
    taken, val = greedy(items, constraint, key_function)
    print('Total value of items taken =', val)
    for item in taken:
        print('   ', item)

def test_greedys(foods, max_units):
    print('Use greedy by value to allocate', max_units, 'calories')
    test_greedy(foods, max_units, Food.getValue)
    print('\nUse greedy by cost to allocate', max_units, 'calories')
    test_greedy(foods, max_units, lambda x: 1/Food.getCost(x))
    print('\nUse greedy by density to allocate', max_units, 'calories')
    test_greedy(foods, max_units, Food.density)
    

if __name__ == '__main__':

    names = ['wine', 'beer', 'pizza', 'burger', 'fries', 'cola', 'apple', 'donut', 'cake']
    values = [89, 90, 95, 100, 90, 79, 50, 10, 10]
    calories = [123, 154, 258, 354, 365, 150, 95, 195, 250]

    assert len(names) == len(values) == len(calories)
    foods = build_menu(names, values, calories)

    test_greedys(foods=foods, max_units=750)