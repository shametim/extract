from flask import Flask, request
import trafilatura

app = Flask(__name__)


@app.route("/extract", methods=['POST'])
def extract():
    doc = trafilatura.extract(
        request.data.decode('utf-8'), output_format='json')

    return doc
