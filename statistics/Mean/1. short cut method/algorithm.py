
from rich.console import Console
from rich.table import Table
"""
  Arithmetic Mean (Short Cut Method)
  ---------------
  The arithmetic mean is the sum of the data divided by the number of data points.
  It is the most commonly used measure of central tendency.
  It is also called the average.
  The arithmetic mean is the only measure of central tendency where the sum of the deviations of each value from the mean is always zero. 

  Arithmetic Mean Short Cut Method Formula
  ----------------------------
  Arithmetic Mean = Sum of all values / Total number of values
  
    Where,
      ∑fd = Sum of all frequencies and deviations
      ∑f = Sum of all frequencies
  
  Arithmetic equation
  ----------------------------
  Arithmetic Mean = a + (∑fd / ∑f)

  Example
  ----------------------------
  Class Range : frequency distribution
  ---------------
  0 - 10 : 7
  10 - 20 : 8
  20 - 30 : 20
  30 - 40 : 10
  40 - 50 : 5

"""

# Importing the statistics module

"""
  Class Range : frequency distribution
  ---------------
  0 - 10 : 7
  10 - 20 : 8
  20 - 30 : 20
  30 - 40 : 10
  40 - 50 : 5
"""
# classRange = ['0-10', '10-20', '20-30', '30-40', '40-50']
# frequency = [7, 8, 20, 10, 5]


# classRange input from user
classRange = input('Enter the class range (separated by space: Like 0-10 10-20 ....): ').split(' ')

# frequency input from user
frequency = list(map(int, input('Enter the frequency (separated by space: Like 1 2 3 ...): ').split(' ')))

# method for calculating arithmetic mean
def arithmeticMeanShortCutMethod(classRange, frequency):
  # calculate the assumed mean
  classRangeFirstValue = classRange[0].split('-')[0]
  classRangeLastValue = classRange[-1].split('-')[1]
  assumedMean = (int(classRangeFirstValue) + int(classRangeLastValue)) / 2

  # calculate the mid value
  midValue = []
  for i in classRange:
    [start, end] = i.split('-')
    mid = (int(start) + int(end)) / 2
    midValue.append(mid)
  
  # calculate the deviation
  deviation = []
  for x in midValue:
    d = x - assumedMean
    deviation.append(d)

  # calculate the frequency and deviation
  fd = []
  for i in range(len(frequency)):
    multiply = frequency[i] * deviation[i]
    fd.append(multiply)
  
  # calculate the sum of frequency and deviation
  sumOfFrequency = sum(frequency)
  sumOfDeviation = sum(fd)

  # calculate the arithmetic mean
  arithmeticMean = assumedMean + (sumOfDeviation / sumOfFrequency)

  # print the table
  # print the table title
  table = Table(
    title="Arithmetic Mean (Short Cut Method)", 
    show_header=True, 
    header_style="bold magenta", 
    title_style="bold green"
  )

  # print the table columns
  columns = ["Class Range", "Frequency(f)", "Mid Value(x)", "Deviation(d)", "Frequency * Deviation(fd)"]
  for column in columns:
    table.add_column(column)

  # print the table rows
  for i in range(len(classRange)):
    table.add_row(
      classRange[i], 
      str(frequency[i]), 
      str(midValue[i]), 
      str(deviation[i]), 
      str(fd[i]), 
      style='bright_green'
    )

  # print the table footer row and put value in footer row
  table.add_row('Total', str(sumOfFrequency), '', '', str(sumOfDeviation))

  # print the table
  console = Console()
  console.print(table)

  # return the result
  return arithmeticMean

# calling the arithmeticMeanShortCutMethod() method
arithmeticMean = arithmeticMeanShortCutMethod(classRange, frequency)

# print the result
print('Arithmetic Mean (Short Cut Method) : ', arithmeticMean)
