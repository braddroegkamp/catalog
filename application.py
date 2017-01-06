from flask import Flask
import login_detail
import json_detail
import main_routing

app = Flask(__name__)

# include bluprints for all components of app
app.register_blueprint(login_detail.app_login_detail)
app.register_blueprint(json_detail.app_json_detail)
app.register_blueprint(main_routing.app_main)


if __name__ == '__main__':
	app.secret_key = 'abcde12345'
	app.debug = True
	app.run(host='0.0.0.0', port=8000)
