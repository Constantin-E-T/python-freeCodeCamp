# Dictionaries

dog = {
    'name': 'Roger',
    'age': 8,
    'color': 'Green'
}

dog['name'] = 'Syd'

print(dog['name'])
print(dog.get('name'))
print(dog.get('color', 'Blue'))

# print(dog.pop(dog.popitem()))
# print(dog.pop('name'))

print('color' in dog)

dog['Favorite food'] = 'Meat'

print(len(dog))

del dog['color']
print(list(dog.keys()))
print(list(dog.values()))
print(list(dog.items()))