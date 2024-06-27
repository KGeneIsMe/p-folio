import csv

from flask import Flask, render_template, request, redirect

app = Flask(__name__)


def submit_form_to_file(data_dict):
    file_path = r'./database.txt'
    with open(file_path, 'a') as txt_file:
        for key, value in data_dict.items():
            txt_file.write(f"{key}: {value}\n")
        txt_file.write(f'\n')


def submit_form_to_csv(data_dict):
    # file_path = r'./database.csv'
    with open('database.csv', 'a', newline='') as csv_file:
        email = data_dict['email']
        subject = data_dict['subject']
        message = data_dict['message']
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route("/")
def root():
    return render_template('index.html')


@app.route("/<string:page_name>")
def get_page(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            submit_form_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'Did not save to database!'
    else:
        return 'Form not submitted!'
