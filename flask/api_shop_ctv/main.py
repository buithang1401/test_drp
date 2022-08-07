import pymysql
from app import app
from config import mysql
from flask import jsonify
from flask import flash, request
        
@app.route('/city')
def city():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM city")
        empRows = cursor.fetchall()
        respone = jsonify(empRows)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()  

@app.route('/city/<string:id>')
def city_details(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM city WHERE id =%s", id)
        empRow = cursor.fetchone()
        respone = jsonify(empRow)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()

#@app.route('/city/<string:id>')
@app.route('/test')
def test_details():
    try:
        id = request.args.get('id', default='*', type=int)
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        sql="SELECT * FROM city WHERE id =%s", id
        print(sql)
        cursor.execute("SELECT * FROM city WHERE id =%s", id)
        empRow = cursor.fetchone()
        respone = jsonify(empRow)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()     


@app.route('/order_brcd')
def order_brcd():
    try:
        id = request.args.get('id', default='*', type=int)
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("select id,region,vnpt_it_ma_gd from vnpt_dealer.order WHERE id =%s", id)
        empRow = cursor.fetchone()
        respone = jsonify(empRow)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()

@app.errorhandler(404)
def showMessage(error=None):
    message = {
        'status': 404,
        'message': 'Record not found: ' + request.url,
    }
    respone = jsonify(message)
    respone.status_code = 404
    return respone


if __name__ == "__main__":
    app.run()