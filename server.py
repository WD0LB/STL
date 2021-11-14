from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)

def write_to_file_stl(data):
	with open('database_stl.txt', mode='a') as database:
		email = data['email']
		subject = data['subject']
		message = data['message']
		file = database.write(f'\n{email}, {subject}, {message}')
def write_to_csv_stl(data):
	with open('database_stl.csv', mode='a', newline='') as database:
		email = data['email']
		subject = data['subject']
		message = data['message']
		csv_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email,subject,message])
@app.route('/stl', methods=['POST','GET'])
def stl():
	if request.method == 'POST':
		try:
			data = request.form.to_dict()
			write_to_file_stl(data)
			write_to_csv_stl(data)
		except :
			return 'something went wrong'
		return 'stl connection success'
	else:
		return 'stl connection failled'