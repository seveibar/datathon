from flask import Flask, jsonify, request

app = Flask(__name__, static_url_path='')

@app.route('/')

@app.route('/recalculate', methods=['GET','POST'])
def recalculate():
    #x_table = #TODO get x_table
    #new_value = request.form['<?>'] (what format? Country Code? Year? Value?




if __name__ == '__main__':
    app.run(debug=True)
