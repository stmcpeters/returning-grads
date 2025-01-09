# imports the os module
import os
# installed and imported requests module to use
import requests
# import JSON module
import json

def process_file(file_path):
    # Process the file content and return a dictionary
    feedback_dir = file_path
    files = os.listdir(feedback_dir)

    # iterate over each file in the directory
    for file in files:
        # creates a full file path by joining the directory path and the file name
        full_file_path = os.path.join(feedback_dir, file)
        # opens each file in read mode
        with open(full_file_path, 'r') as file:
            # create dictionary to store file content
            content = {}
            # assigns each line of file to a key in the dictionary
            content['title'] = file.readline().strip()
            content['name'] = file.readline().strip()
            content['date'] = file.readline().strip()
            content['feedback'] = file.readline().strip()

            # convert content dictionary to JSON format
            data = json.dumps(content)
            # returns the JSON data
            return data
    pass

# testing to see if the function accesses the directory
process_file('/Users/tpl1122_15/Desktop/returning-grads/HTTP-request-python/data/feedback')


def upload_to_web_service(data):
    # Send POST request to the web service
    pass

# # Main execution
# feedback_dir = '/data/feedback'
# files = os.listdir(feedback_dir)

# for file in files:
#     file_path = os.path.join(feedback_dir, file)
#     feedback_dict = process_file(file_path)
  
#     if feedback_dict:
#         upload_to_web_service(feedback_dict)
#         print(f"Uploaded feedback from {file}")
#     else:
#         print(f"Failed to process {file}")

# print("Processing complete.")