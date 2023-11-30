numbers = [12, 56, 64, 2, 9, 35]

def minMax(array):
    minValue = array[0]
    maxValue = array[0]
    for value in array:
        if value > maxValue:
            maxValue = value
        if value < minValue:
            minValue = value
    print(f"minimum value is {minValue} and maximum is {maxValue}")

minMax(numbers)

