from utils import prefix_to_infix, infix_to_prefix, postfix_to_infix, infix_to_postfix, prefix_to_postfix, postfix_to_prefix
from flask import Flask, redirect, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

def match_inputs(initial, final, expression):
    if initial == 'infix':
        if final == 'infix':
            return expression
        elif final == 'prefix':
            return infix_to_prefix(expression)
        else:
            return infix_to_postfix(expression)
    
    elif initial == 'postfix':
        if final == 'postfix':
            return expression
        elif final == 'prefix':
            return postfix_to_prefix(expression)
        else:
            return postfix_to_infix(expression)
    
    else:
        if final == 'prefix':
            return expression
        elif final == 'postfix':
            return prefix_to_postfix(expression)
        else:
            return prefix_to_infix(expression)

@app.route('/solver', methods=['POST'])
def converter():
    if request.method == 'POST':
        data = request.get_json()
        initial = data['initial']
        final = data['final']
        expression = data['expression']

        return match_inputs(initial, final, expression)

        # return {"okay": "This works!"}

if __name__ == '__main__':
    app.run()