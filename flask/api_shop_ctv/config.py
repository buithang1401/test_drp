from app import app
from flaskext.mysql import MySQL

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'xxxx'
app.config['MYSQL_DATABASE_PASSWORD'] = 'xxxx'
app.config['MYSQL_DATABASE_DB'] = 'xxxx'
app.config['MYSQL_DATABASE_HOST'] = 'xxxx'
mysql.init_app(app)