# imports the os module
import os
# installed and imported requests module to use
import requests

def process_file(file_path):
    # Process the file content and return a dictionary
    feedback_dir = file_path
    files = os.listdir(feedback_dir)

    # iterate over each file, read, and turn the content into a dictionary
    # split the content by lines and assign each line to a key in the dictionary

    #for file in files:
      
    # pass

# testing to see if the function accesses the directory
# process_file('/Users/tpl1122_15/Desktop/returning-grads/HTTP-request-python/data/feedback')


# def upload_to_web_service(data):
#     # Send POST request to the web service
#     pass

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