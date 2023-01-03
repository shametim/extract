from flask import Flask, request
import trafilatura

app = Flask(__name__)


@app.route("/extract", methods=['POST'])
def extract():
    document = request.data.decode('utf-8')

    # extract = trafilatura.extract(document, output_format='json')

    app.logger.info("Extraction complete")

    return extract
