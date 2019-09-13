from app import app

# enable server setup with (python filename.py) without (flask run)
if __name__ == '__main__':
	app.run()
	# app.run(debug=Ture) #for debugging without .env file