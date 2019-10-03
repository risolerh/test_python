import pymysql
from _configuration.app import app
from _configuration.db_conn import mysql
from flask import jsonify
from flask import flash, request
#from werkzeug import generate_password_hash, check_password_hash

@app.route('/')
def users():
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM EMPLEADOS")
		rows = cursor.fetchall()
		resp = jsonify(rows)
		resp.status_code = 200
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()
	return resp

@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp


if __name__ == "__main__":
    app.run()