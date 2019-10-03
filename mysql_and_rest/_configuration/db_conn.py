from .app import app
from flaskext.mysql import MySQL
import yaml

with open("D:/CONFIGURACIONES/enviroment.yaml") as file:
    SQL_PROPS = yaml.load(file).get('database')
    print(SQL_PROPS)

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = SQL_PROPS.get('user')
app.config['MYSQL_DATABASE_PASSWORD'] = SQL_PROPS.get('pwd')
app.config['MYSQL_DATABASE_DB'] = SQL_PROPS.get('db')
app.config['MYSQL_DATABASE_HOST'] = SQL_PROPS.get('host')
mysql.init_app(app)