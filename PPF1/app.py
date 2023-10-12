from flask import Flask, request, jsonify, render_template
from flask_mysqldb import MySQL
from flask_socketio import SocketIO

app= Flask(__name__)

#####
#Configuracion de la BD
#####

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'srv_user'
app.config['MYSQL_PASSWORD'] = '4335'
app.config['MYSQL_DB'] = 'PPD'

mysql= MySQL(app)

socketio= SocketIO(app)







if __name__ == '__main__':
    socketio.run(app, debug=True)