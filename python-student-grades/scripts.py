# import csv module to read grades.csv
import csv 
# import built-in statistics module to do calculations
import statistics

# initialize empty lists to hold subject scores
math_scores = []
science_scores = []
english_scores = []

# Calculate the average grade for each subject across all students.
  # function called subject_average that will take a file as a parameter and use the data to calculate the average scores for each subject
def subject_average(filename):
# opens file in read mode
  with open(filename, 'r') as subjects:
    # reader object will read/iterate over the file
    data = csv.reader(subjects)
    # skips the first line of the file - header row
    heading = next(data)

    for row in data:
      # append the scores to the respective lists
      # try/except block for error handling; if a value cannot be converted to an integer, it will be set to 0
      try:
        math_scores.append(int(row[1]))
      except ValueError:
        math_scores.append(0)
      try:
        science_scores.append(int(row[2]))
      except ValueError:
        science_scores.append(0)
      try:
        english_scores.append(int(row[3]))
      except ValueError:
        english_scores.append(0)

    # calculate the average scores for each subject
    print('Average math grade is: {}'.format(statistics.mean(math_scores))) # returns 84
    print(f"Average science grade is: {statistics.mean(science_scores)}") # returns 0 bc of invalid data
    print(f"Average english grade is: {statistics.mean(english_scores)}") # returns 91.2 

# call the function with the file name
subject_average('grades.csv')

# Find the student(s) with the highest overall grade (average of all three subjects).


# Determine which subject has the highest average grade overall.

# Create a simple report that summarizes these findings.
# Use Python's string formatting capabilities to present the results in a readable format.

