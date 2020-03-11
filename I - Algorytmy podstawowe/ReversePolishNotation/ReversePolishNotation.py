from Stack import Stack


def read(name):
    file = open(name, 'r')
    input_data = file.read().splitlines()
    file.close()
    return input_data


def clear_stack(stack, temp):
    for i in range(stack.Size()):
        if stack.Top() == '(':
            stack.Pop()
            break
        else:
            if stack.Top() != '(':
                temp += stack.Top()
            stack.Pop()
    return temp


def infix_to_rpn(input_data):
    stack = Stack()
    temp = ""
    output = []
    dictionary = {
        '^': 3,
        '*': 2,
        '/': 2,
        '+': 1,
        '-': 1,
        '(': 0
    }
    for item in input_data:
        for char in item:
            if char in dictionary and char != '(':
                if stack.isEmpty():
                    stack.Push(char)
                elif dictionary.get(char) <= dictionary.get(stack.Top()):
                    temp += stack.Top()
                    stack.Pop()
                    stack.Push(char)
                elif dictionary.get(char) > dictionary.get(stack.Top()):
                    stack.Push(char)
            elif char == '(':
                stack.Push(char)
            elif char == ')':
                temp = clear_stack(stack, temp)
            elif char == '=':
                temp = clear_stack(stack, temp)
                output.append(temp)
                temp = ""
            else:
                temp += char
    return output


def rpn_to_infix(input_data):
    output = []
    temp = []
    symbols = ['^', '*', '/', '+', '-', '(', '=']
    for item in input_data:
        for char in item:
            if char not in symbols:
                temp.insert(0, char)
            else:
                r = temp.pop(0)
                l = temp.pop(0)

                if char in ["+", "-"]:
                    if r[0] == "(" and r[-1] == ")":
                        r = r[1:-1]

                    if l[0] == "(" and l[-1] == ")":
                        l = l[1:-1]

                temp.insert(0, "(" + l + char + r + ")")
        output.append(temp[0][1:-1])
    return output


print(infix_to_rpn(read("inputdata_inf.txt")))
print(rpn_to_infix(read("inputdata_rpn.txt")))
