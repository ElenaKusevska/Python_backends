import random
from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def index():
    state1 = random.getstate()
    draw = random.randint(1,6)
    state2 = random.getstate()
    return {
               "state_before_draw": state1,
               "draw": draw,
               "state_after_draw": state2
           }

if __name__ == '__main__':
    app.run(debug=True)
