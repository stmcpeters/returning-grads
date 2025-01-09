# installed and imported Flask to use
from flask import Flask, request, jsonify

# creates an instance of the Flask class
app = Flask(__name__)

# store data in a list
feedback_data = []

# route decorator to tell Flask what URL should trigger the function
@app.route('/', methods=['POST'])
# function to post the feedback data to the web service
def generate_feedback():
  # get the JSON data from the request
  data = request.get_json()
  # check if data is empty or not provided/invalid
  if not data:
    # return a response with a 400 status code
    return 'No data provided or data is invalid', 400
  # saves data to list
  feedback_data.append(data)
  # print the data to the console
  print(data)
  # return a response with a 200 status code
  return 'Feedback received successfully', 200

# function and route to see data in the browser
@app.route('/', methods=['GET'])
def display_feedback():
  # return the feedback data in JSON format
  return jsonify(feedback_data), 200

# debug mode means that the server will reload itself on code changes
# port is the port number the server will listen on
# host is the IP address of the server
if __name__ == '__main__':
    app.run(debug=True, port=8008, host='0.0.0.0')