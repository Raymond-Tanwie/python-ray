animals = ['dog', 'cat', 'crocodile', 'monkey', 'snake']
times = 0

while times < len(animals):
    animal = animals[times]
    if animal == 'crocodile' or animal == 'snake':
        print(animal + " is very dangerous.")
    else:
        print('do not worry, ' + animal + ' is not dangerous')
    times += 1
        
       #  = assigning a value
       #   == is to check if what you assigned is actually working. 