# imports the os module
import os
# installed and imported requests module to use
import requests
# import JSON module
import json

# function to upload data to the web service
def upload_to_web_service(data):
    # Send POST request to the web service
    response = requests.post('http://127.0.0.1:8008/', data=data, headers={'Content-Type': 'application/json'})
    print(response.status_code, response.text)
    pass

# function to process the file content
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
            # pass JSON data to the upload_to_web_service function
            upload_to_web_service(data)
    pass



# Main execution
# call the process_file function with the directory path to the feedback files
process_file('/Users/tpl1122_15/Desktop/returning-grads/HTTP-request-python/data/feedback')
print("Processing complete.")