from flask import Flask, render_template, request, jsonify
"""
Flask: to call the library of flask to create  website app. 
render_template: to use html file
request: to reach to sendind data
jsonify: to convert data to json to send it as a request

"""
app = Flask(__name__) # to create the object

def is_prime(n):
    if n <= 1:
        return "neither prime nor composite"
    for i in range(2,n//2):
        if (n % i) == 0:
            return "not a prime number"
    return "a prime number"

@app.route('/') # to create path to the App
def index():    # Render the index.html template
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check():
    number = int(request.json['number']) # Get the number from the JSON request
    result = is_prime(number)
    return jsonify(result=result) # Return the result as a JSON response
 # Run the app in debug mode
if __name__ == '__main__':
    app.run(debug=True)
