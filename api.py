from flask import Flask, jsonify, request, send_from_directory
import svme

app = Flask(__name__, static_url_path='')

@app.route('/ui/<path:path>')
def send_ui(path):
    return send_from_directory('ui', path)

@app.route('/calc', methods=['GET'])
def calc():
    p_sc = request.args.get("p_sc")
    spike_sc = request.args.get("spike_sc")
    spike_cc = request.args.get("spike_cc")
    spike_amt = float(request.args.get("spike_amt"))
    return svme.spike_effect_across_world(p_sc, spike_sc, spice_cc, spike_amt)


if __name__ == '__main__':
    app.run(debug=True)
