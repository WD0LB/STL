from flask import Flask, request
app = Flask(__name__)

@app.route('/stl', methods=['POST','GET'])
def stl():
	if request.method == 'POST':
		try:
			data = request.form.to_dict()
			print(data)
		except :
			return 'something went wrong'
		return 'stl connection success'
	else:
		return 'stl connection failled'