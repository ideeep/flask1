from flask import Flask, request, jsonify

app1 = Flask(__name__)

@app1.route('/')
def index():
    return "Hello, world!"

@app1.route('/cal', methods=['GET'])
def cal():
    number = int(request.json['number'])  # Convert to integer and use a default value of 0 if 'number' is not provided
    print(number)
    return jsonify(number)  # Return the 'number' as a JSON object

if __name__ == '__main__':
    app1.run()
