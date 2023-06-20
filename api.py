#!/usr/bin/env python3
from flask import Flask, request
import pickle
from urllib.parse import unquote

# From 8 hours of research to figure out why pickle was receiving truncated string/bytes data
# Fun fact - 8 hours was over a fathers day getaway with the wife at the Tides Inn - never heard of it look it up

#outputstr2 = bytes(unquote(outputstr1), 'utf-8')

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home():
    return("So you'd like to learn more about deserialization huh?")

@app.route('/admin', methods=['GET','POST'])
def admin():
    outputstr=""
    if request.method == 'POST':
        try:
            outputstr = pickle.loads(bytes(unquote(request.json['cmd']), 'utf-8'))
        except KeyError:
        # cmds being used - is array of commands, so concat them all
            for inCmd in request.json['cmds']:
                outputstr = outputstr+'\n'+str(pickle.loads(bytes(unquote(inCmd), 'utf-8')))
    else:
        outputstr = pickle.loads(bytes(str(request.args.get('cmd')), 'utf-8'))

    return outputstr

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=80)
