from flask import Flask, request
import trafilatura

app = Flask(__name__)


@app.route("/extract")
def hello_world():
    string = request.args.get('string')

    app.logger.info("Extracting start")

    extract = trafilatura.extract(string, output_format='json')

    app.logger.info("Extraction complete: %s" + string)

    return extract
