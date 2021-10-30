# 1
# built-in functions (встроенные функции)
x = print('Hello')
y = set()

print(type(x))
print(type(y))
print(x)
print(y)

# 2
# built-in methods (встроенные методы)

my_list = [1, 2, 3]
my_list.append(4)
print(my_list)
my_list.clear()
print(my_list)


# 3
def print_greeting():
    """
    Print 'Hello!' text
    :return: None
    """
    print('Hello!')

# call to the function (обращение к фугкции)
print_greeting()

# receive the description of the function (получение описания функции)
help(print_greeting)


# 4
def print_greeting_with_name(name = 'Name'):
    '''
    :param name
    :return: None
    '''
    print('Hello ' + name + '!')
print_greeting_with_name('Jack')
help(print_greeting_with_name)
print_greeting_with_name()
x = print_greeting_with_name('Jane')
print(x)


# 5
def sum_of_two_numbers(a = 0, b = 0):
    '''

    :param a: the first addend (первое слагаемое)
    :param b: the second addend
    :return: Sum of a and b
    '''
    return a + b


x = sum_of_two_numbers(34, 1)
# x = sum_of_two_numbers()
print(x)
help(sum_of_two_numbers)


# 6
def is_hello_in_text(text):
    if 'hello' in text.lower():
        return True
    else:
        return False


print(is_hello_in_text('Say hello everyone'))
print(is_hello_in_text('Say everyone'))
print(is_hello_in_text('Hello everyone'))


# 7
def is_hello_in_text(text):
    return 'hello' in text.lower()


print(is_hello_in_text('Hello everyone'))


# 8
def is_string_in_text(string, text):
    return string in text


print(is_string_in_text('he', 'The apple'))
print(is_string_in_text('hey', 'The apple'))


# 9
def greeting_depends_on_gender(name, gender):
    if gender == 'male':
        return gender
        print('Hello ' + name + '! You look great!')
    elif gender == 'female':
        print('Hello ' + name + '! You are so nice!')
        return gender
    else:
        print('Hello ' + name + '! I\'ve never seen the creature like you!')
        return gender


returned_value_1 = greeting_depends_on_gender('Jack', 'male')
returned_value_2 = greeting_depends_on_gender('Jane', 'female')
returned_value_3 = greeting_depends_on_gender('Ja', 'smale')

print(returned_value_1)
print(returned_value_2)
print(returned_value_3)

# 10
def cat_voice():
    print('Meow')

cat_voice()
cat_voice()


def dog_voice():
    print('Woof')

dog_voice()
dog_voice()


# 11
def get_voice(text):
    return text


print(get_voice('Hello friends'))


# 12
# 1 способ. Without List Comprehension
list_odd_numbers = []


def odd_numbers(a, b):
    number = 0
    for i in range(a, b + 1):
        if i % 2 == 0:
            list_odd_numbers.append(i)
    number += 1
    return list_odd_numbers


print(odd_numbers(1, 10))


# 2 способ. With List Comprehension
def odd_numbers(a, b):

    list_odd_numbers = [i for i in range(a, b + 1) if i % 2 == 0]
    return list_odd_numbers


print(odd_numbers(1, 10))




