# -*- coding: utf-8 -*-
'''
Created on 2015年10月12日

@author: leilei
'''
from flask.app import Flask

app = Flask(__name__)


@app.route('/<s>')


app.run(host="127.0.0.1", port=80, debug=True)