"""
  Arithmetic Mean (Step Deviation Method)
  ---------------------------------------

  Formula:
  --------
  D = (x - a) / i
  
    Where,
      D = Deviation
      x = Mid value
      a = Assumed Mean
      i = Class interval

  Arithmetic Mean = a + (∑fD / ∑f) * i

    Where,
      a = Assumed Mean
      ∑fD = Sum of all frequencies and deviations
      ∑f = Sum of all frequencies
      i = Class interval

  Example
  -------
  Class Range : frequency distribution
  ---------------
  0 - 10 : 7
  10 - 20 : 8
  20 - 30 : 20
  30 - 40 : 10
  40 - 50 : 5

"""

# input from user
# classRange = input('Enter the class range (separated by space: Like 0-10 10-20 ....): ').split('-')
# frequency = list(map(int, input('Enter the frequency (separated by space: Like 1 2 3 ...): ').split(' ')))

classRange = ['0-10', '10-20', '20-30', '30-40', '40-50']
frequency = [7, 8, 20, 10, 5]

# method for calculating arithmetic mean
def arithmeticMeanStepDeviationMethod(classRange, frequency):

  # get class range first value
  classRangeFirstValue = classRange[0].split('-')[0]

  # get class range last value
  classRangeLastValue = classRange[-1].split('-')[1]

  # calculate the assumed mean (a)
  assumedMean = (int(classRangeFirstValue) + int(classRangeLastValue)) / 2

  # calculate the mid value (x)
  midValue = []
  for i in classRange:
    [first, last] = i.split('-')
    mid = (int(first) + int(last)) / 2
    midValue.append(mid)

  # calculate the class interval (i)
  [first, last] = classRange[0].split('-')
  classInterval = int(last) - int(first)

  # calculate the deviation (D)
  deviation = []
  for x in midValue:
    D = (x- assumedMean) / classInterval
    deviation.append(D)

  # calculate the frequency and deviation f*D
  multiplicationOfFrequencyAndDeviation = []
  for i in range(len(frequency)):
    fD = frequency[i] * deviation[i]
    multiplicationOfFrequencyAndDeviation.append(fD)

  # calculate the sum of all frequencies ∑f
  sumOfAllFrequencies = sum(frequency)

  # calculate the sum of all frequencies and deviations ∑fD
  sumOfAllFrequenciesAndDeviations = sum(multiplicationOfFrequencyAndDeviation)

  # calculate the arithmetic mean a + (∑fD / ∑f) * i
  mean = assumedMean + (sumOfAllFrequenciesAndDeviations / sumOfAllFrequencies) * classInterval

  # return the result
  return mean



mean =  arithmeticMeanStepDeviationMethod(classRange, frequency)

print('Arithmetic Mean: ', mean)