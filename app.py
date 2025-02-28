from flask import Flask, request, render_template, app, jsonify, url_for
import numpy as np
import pandas as pd
import pickle

app = Flask(__name__)

model = pickle.load(open('regmodel.pkl'))

@app.route('/')
def home():
    return render_template('home.html')