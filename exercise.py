animals = ['dog', 'cat', 'crocodile', 'monkey', 'snake']
animals2 = ['crocodile', 'monkey', 'snake']

def check(animalName):
   if animalName == 'crocodile' or animalName == 'snake': 
       return True 
   else:
       return False
    


def listAnimals(animalsArray):
    times = 0
    while times < len(animalsArray):
        animal = animalsArray[times]
        isDangerous = check(animal)
        print(isDangerous)
        if isDangerous:
            print(animal + " is very dangerous.")
        else:
            print('do not worry, ' + animal + ' is dangerous')
            
        times += 1
        
listAnimals(animals)
print('---------------') 
listAnimals(animals2)