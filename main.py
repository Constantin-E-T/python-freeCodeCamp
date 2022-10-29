# Functions

def hello(name, age):
    print(f'Hello {name}, you are {age} years old')

    return name


hello('Emilian', '35')
# hello()

def change(value):
    value = 255

val = 10

change(val)

print(val)

def talk(phrase):
    def say(word):
        print(word)

    words = phrase.split(' ')

    for word in words:
        say(word)

talk('I am going to stay right here!')

