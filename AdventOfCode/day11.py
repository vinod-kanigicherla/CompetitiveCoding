import sys

temp = [line.strip() for line in sys.stdin]

class Monkey:
    def __init__(self, id, operation=[None, None], test=0, items=[], inspects=0, true_condition=-1, false_condition= -1):
        self.id = id
        self.items = items
        self.operation = operation # operation[0] = symbol and operation[1] = value
        self.test = test
        self.inspects = inspects
        self.true_condition = true_condition #if true: throw to true_condition
        self.false_condition = false_condition #else: to false_condition

    def __repr__(self):
        return f"{(self.id, self.items, self.operation, self.test, self.true_condition, self.false_condition)}"

    def apply_operation(self, item):

        if self.operation[1] == "old":
            if self.operation[0] == "+":
                item += item
            elif self.operation[0] == "-":
                item -= item
            elif self.operation[0] == "*":
                item *= item
            elif self.operation[0] == "/":
                item /= item

            return item

        if self.operation[0] == "+":
            item += int(self.operation[1])
        elif self.operation[0] == "-":
            item -= int(self.operation[1])
        elif self.operation[0] == "*":
            item = item * int(self.operation[1])
        elif self.operation[0] == "/":
            item /= int(self.operation[1])

        return item


    def test_item(self, item):
        return item % self.test == 0

    def throw(self):
        assert len(self.items) > 0, "self.items shouldn't be empty"
        self.inspects += 1
        item = self.items.pop(0)
        item = int(self.apply_operation(item)/3)
        if self.test_item(item):
            monkeys[self.true_condition].items.append(item)
        else:
            monkeys[self.false_condition].items.append(item)

        self.operation[1]


monkeys = []

for l in temp:
    line = l.split(" ")
    if line[0] == "Monkey":
        monkey = Monkey(int(line[1][0]))
        monkeys.append(monkey)

    if line[0] == "Starting": #items
        monkey_items = list(map(int, [item.replace(",", "") for item in line[2:] if "," in item]))
        monkey_items.append(int(line[-1]))
        monkeys[-1].items = monkey_items

    if line[0] == "Test:": #test
        monkeys[-1].test = int(line[-1])

    if line[0] == "Operation:": #operation
        monkeys[-1].operation = [line[-2], line[-1]]

    if line[0] == "If": #condition
        if line[1] == "true:":
            monkeys[-1].true_condition = int(line[-1])
        if line[1] == "false:":
            monkeys[-1].false_condition = int(line[-1])


print(monkeys)

for i in range(20):
    for monkey in monkeys:
        while monkey.items:
            monkey.throw()
        print([monkey.items for monkey in monkeys])
    print([monkey.items for monkey in monkeys])

print(sorted([monkey.inspects for monkey in monkeys])[-1] * sorted([monkey.inspects for monkey in monkeys])[-2])