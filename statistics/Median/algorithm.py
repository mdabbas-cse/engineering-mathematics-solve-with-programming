"""
Median is the middle value of a sorted list of numbers.

Formula
-------
Median = l + ((n/2 - cf) /f) * i

  Where,
    l = Lower limit of median class
    n = Total number of values
    cf = Total of all the preceeding frequencies median class
    f = Frequency of median class
    i = Class interval
Example
-------
No. of days for which absend (less than)
5, 10, 15, 20, 25, 30, 35, 40, 45

No. of students
29, 224, 465, 582, 634, 644, 650, 653, 655
"""
# input classes from user
classes = list(map(int, input(
    'Enter the classes (separated by space: Like 5 10 15 20 ....): ').split(' ')))

# input frequency from user
frequency = list(map(int, input(
    'Enter the frequency (separated by space: Like 1 2 3 ...): ').split(' ')))

# input class interval from user
classInterval = int(input('Enter the class interval: '))


# generate interval classes range
def intervalClass(classes, classInterval):
    initInterval = 0
    intervalClass = []
    for i in classes:
        newInterval = initInterval + classInterval
        intervalClass.append(f'{initInterval}-{newInterval}')
        initInterval = newInterval

    return intervalClass


# ordinary frequency
def ordinaryFrequency(frequency):
    for i in range(len(frequency)):
        if i == 0:
            frequency[i] = frequency[i]
        else:
            frequency[i] = frequency[i] - frequency[i-1]

    return frequency


# method for calculating median
def median(classes, frequency, classInterval):
    intervalClasses = intervalClass(classes, classInterval)
    ordinaryFrequencyList = ordinaryFrequency(frequency)
    print(intervalClasses)
    print(ordinaryFrequencyList)


median(classes, frequency, classInterval)
