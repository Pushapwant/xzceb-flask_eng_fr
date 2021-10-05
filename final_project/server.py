# server.py modified by Pushapwant
from machinetranslation import translatory
#import translatory
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def translateToFrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    translated_Text = translatory.englishToFrench(textToTranslate)
    return translated_Text

@app.route("/frenchToEnglish")
def translateToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    translated_Text = translatory.frenchToEnglish(textToTranslate)
    return translated_Text

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
# end
