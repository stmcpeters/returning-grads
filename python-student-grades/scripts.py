# import csv module to read grades.csv
import csv 
# import built-in statistics module to do calculations
import statistics
# import math module to use NaN
import math

# Calculate the average grade for each subject across all students.
  # function called subject_average that will take a file as a parameter and use the data to calculate the average scores for each subject
def subject_average(filename):
# opens file in read mode
  with open(filename, 'r') as subjects:
    # reader object will read/iterate over the file
    data = csv.reader(subjects)
    # skips the first line of the file - header row
    heading = next(data)

    # initialize empty lists to hold subject scores
    math_scores = []
    science_scores = []
    english_scores = []

    for row in data:
      # append the scores to the respective lists
      # try/except block for error handling; if a value cannot be converted to an integer, it will be set to NaN to represent missing/invalid data
      try:
        math_scores.append(int(row[1]))
      except ValueError:
        math_scores.append(math.nan)

      try:
        science_scores.append(int(row[2]))
      except ValueError:
        science_scores.append(math.nan)

      try:
        english_scores.append(int(row[3]))
      except ValueError:
        english_scores.append(math.nan)

    # calculate the average scores for each subject
    math_scores = statistics.mean(math_scores) # returns 84
    science_scores = statistics.mean(science_scores) # returns NaN bc of invalid data
    english_scores = statistics.mean(english_scores) # returns 91.2 

# return the average scores for each subject to be used in the report
    return math_scores, science_scores, english_scores

# call the function with the file name
# subject_average('grades.csv')

############################################################################################################

# Find the student(s) with the highest overall grade (average of all three subjects).
def highest_overall_grade(filename):
    with open(filename, 'r') as students:
      # reader object will read/iterate over the file
      data = csv.reader(students)
      # skips the first line of the file - header row
      heading = next(data)

# initialize an empty dictionary to store student names and their average grades
      student_grades = {}

      # iterate over the data to calculate the average grade for each student
      for row in data:
        try:
          # converts each grade to an integer and calulates the average using statistics module
          grades = [int(row[1]), int(row[2]), int(row[3])]
          student_grades[row[0]] = statistics.mean(grades)
          # if any error occurs, the average is set to NaN
        except ValueError:
          student_grades[row[0]] = math.nan

      # find the student with the highest average grade
      # max function will return the key with the highest value
      # get method will return the value of the key (student name) with the highest value
      highest_grade = max(student_grades, key=student_grades.get) 

  #return the student with the highest overall grade to be used in the report
      return highest_grade
    
# call the function with the file name
# highest_overall_grade('grades.csv')

############################################################################################################

# Determine which subject has the highest average grade overall.
def highest_average_subject(filename):
    with open(filename, 'r') as subjects:
      # reader object will read/iterate over the file
      data = csv.reader(subjects)
      # skips the first line of the file - header row
      heading = next(data)

      # initialize empty lists to hold average scores for each subject
      math_averages = []
      science_averages = []
      english_averages = []

      # iterate over data to calculate the average grade for each subject
      for row in data:
        try:
          math_averages.append(int(row[1]))
        except ValueError:
          math_averages.append(math.nan)
        
        try:
          science_averages.append(int(row[2]))
        except ValueError:
          science_averages.append(math.nan)
        
        try:
          english_averages.append(int(row[3]))
        except ValueError: 
          english_averages.append(math.nan)
      
      # calculate the average grade for each subject
      math_avg = statistics.mean(math_averages)
      science_avg = statistics.mean(science_averages)
      english_avg = statistics.mean(english_averages)

      # find the subject with the highest average grade
      # max function will return the key with the highest value
      highest_avg = max(math_avg, science_avg, english_avg)
      if highest_avg == math_avg:
        return "Math"
      elif highest_avg == science_avg:
        return "Science"
      else:
        return "English"
      
# call the function with the file name
# highest_average_subject('grades.csv')

###########################################################################################################     
# Create a simple report that summarizes these findings.
def create_report(math_avg, science_avg, english_avg, highest_grade, highest_subject):
  report = f"""
  Subject Average Grades:
    Math: {math_avg}
    Science: {science_avg}
    English: {english_avg}

  Student with the highest overall grade: {highest_grade}
  Subject with the highest average grade: {highest_subject}
  """
  return report

# main function that will call all the functions and generate the report
def main():
  filename = 'grades.csv'

  # calculate subject averages
  math_avg, science_avg, english_avg = subject_average(filename)
  
  # student with highest overall grade
  highest_overall_student = highest_overall_grade(filename)

  # subject with highest average grade
  highest_subject_average = highest_average_subject(filename)

  # create and print the report
  report = create_report(math_avg, science_avg, english_avg, highest_overall_student, highest_subject_average)
  print(report)

# call the main function
if __name__ == '__main__':
  main()

