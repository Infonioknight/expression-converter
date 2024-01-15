def infix_to_postfix(data, nearly=False):
    def precedence_check(nearly, stack_item, check_item):
        if nearly:
            return stack_item > check_item
        else:
            return stack_item >= check_item

    stack = []
    precedence = {
        '^': 3,
        '*': 2,
        '/': 2,
        '+': 1,
        '-': 1
    }

    solution = ''
    cleaned = data.replace(' ', '')

    for character in cleaned:
        # Capital characters
        if (ord(character) >= 65 and ord(character) <= 90) or (ord(character) >= 97 and ord(character) <= 122):
            solution += character

        elif character in '([{':
            stack.append(character)

        elif character in ')}]':
            if character == ')':
                while stack[-1] != '(':
                    solution += stack.pop()
                stack.pop()
            if character == '}':
                while stack[-1] != '{':
                    solution += stack.pop()
                stack.pop()
            if character == ']':
                while stack[-1] != '[':
                    solution += stack.pop()
                stack.pop()
        else:
            while (stack) and (stack[-1] not in '({[') and precedence_check(nearly, precedence[stack[-1]], precedence[character]):
                item = stack.pop()
                solution += item
            stack.append(character)
    while stack:
        item = stack.pop()
        solution += item
    return solution         

def postfix_to_infix(data):
    stack = []
    cleaned = data.replace(' ', '')

    for character in cleaned:
        if (ord(character) >= 65 and ord(character) <= 90) or (ord(character) >= 97 and ord(character) <= 122):
            stack.append(character)
        
        elif character in '+-^*/':
            if len(stack) < 2:
                return 'Invalid input'
            second = stack.pop()
            first = stack.pop()
            stack.append(f"({first} {character} {second})")
        
        else:
            return 'Invalid Input'
    if len(stack) != 1:
        return "Invalid Input"
    return stack.pop()[1:-1]

def infix_to_prefix(data):
    mapping_table = str.maketrans({
        '{': '}',
        '}': '{',
        '(': ')',
        ')': '(',
        '[': ']',
        ']': '['
    })
    cleaned = data.replace(' ', '')[::-1].translate(mapping_table)
    return infix_to_postfix(cleaned, True)[::-1] 

def prefix_to_infix(data):
    mapping_table = str.maketrans({
        '{': '}',
        '}': '{',
        '(': ')',
        ')': '(',
        '[': ']',
        ']': '['
    })
    stack = []
    cleaned = data.replace(' ', '')[::-1]
    for character in cleaned:
        if (ord(character) >= 65 and ord(character) <= 90) or (ord(character) >= 97 and ord(character) <= 122):
            stack.append(character)
        elif character in '-+/*^':
            if len(stack) < 2:
                return 'Invalid Input'
            first = stack.pop()
            second = stack.pop()
            stack.append(f'({first} {character} {second})')
    if len(stack) != 1:
        return 'Invalid Input'
    else:
        return stack.pop()

def prefix_to_postfix(data):
    cleaned = data.replace(' ', '')[::-1]
    stack = []
    for character in cleaned:
        if (ord(character) >= 65 and ord(character) <= 90) or (ord(character) >= 97 and ord(character) <= 122):
            stack.append(character)
        elif character in '+-/*^':
            if len(stack) < 2:
                return 'Invalid Input'
            else:
                first = stack.pop()
                second = stack.pop()
                stack.append(f"{first}{second}{character}")
    if len(stack) != 1:
        return "Invalid Input"
    else:
        return stack.pop()

def postfix_to_prefix(data):
    cleaned = data.replace(' ', '')
    stack = []
    for character in cleaned:
        if (ord(character) >= 65 and ord(character) <= 90) or (ord(character) >= 97 and ord(character) <= 122):
            stack.append(character)
        elif character in '+-/*^':
            if len(stack) < 2:
                return 'Invalid Input'
            else:
                second = stack.pop()
                first = stack.pop()
                stack.append(f"{character}{first}{second}")
    if len(stack) != 1:
        return "Invalid Input"
    else:
        return stack.pop()