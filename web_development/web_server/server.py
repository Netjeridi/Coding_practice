from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def my_home():
    # render templates will look in a folder called 'templates' for html files,
    # so we need to store the files there
    return render_template('index.html')


# dynamically accept new html files to create new pages
@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        data = request.form.to_dict()
        return redirect('submitted.html')
    else:
        return "Something went wrong. Data not submitted."
