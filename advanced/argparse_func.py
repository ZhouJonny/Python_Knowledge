from argparse import ArgumentParser

parser = ArgumentParser(description='A simple program to greet the user.')

parser.add_argument('name', type=str, help='The name of user to greet')
parser.add_argument('age', type=int, help='The age of user to greet')

parser.add_argument('-c', '--capitalize', action='store_true', help='Capitalize the greeting')
parser.add_argument('-g', '--greet', type=str, default='Hello', help='Customize the greeting message')
parser.add_argument('--excited', action='store_true', help='Add an exclamation mark to the greeting')


args = parser.parse_args()

name = args.name
age = args.age
capitalize = args.capitalize
greet = args.greet
excited = args.excited

greeting = f"{greet}, {name}. You are {age} years old."
if capitalize:
    greeting = greeting.upper()
if excited:
    greeting += '!'

print(greeting)
"""
C:\Users\Jonny\AppData\Local\Programs\Python\Python310\python.exe C:\Users\Jonny\PycharmProjects\Python_Knowledge\advanced\argparse_func.py zyj 26 -c -g nihao --excited
NIHAO, ZYJ. YOU ARE 26 YEARS OLD.!
"""
