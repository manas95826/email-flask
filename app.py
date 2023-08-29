from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load the pipeline
pipeline_filename = 'email_spam_pipeline.pkl'
with open(pipeline_filename, 'rb') as pipeline_file:
    clf = pickle.load(pipeline_file)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        text = request.form.get('text')
        if text:
            prediction = clf.predict([text])
            if prediction[0] == 1:
                result = "This is a spam email."
            else:
                result = "This is not a spam email."
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
