from flask import Flask, request
import csv
app = Flask(__name__)

def write_to_file_stl(data):
	with open('database_stl.txt', mode='a') as database:
		device = data['device']
		date = data['date']
		comment = data['comment']
		file = database.write(f'\n{device}, {date}, {comment}')
def write_to_csv_stl(data):
	with open('database_stl.csv', mode='a', newline='') as database:
		device = data['device']
		date = data['date']
		comment = data['comment']
		csv_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([device,date,comment])

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