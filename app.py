import os

from flask import Flask, render_template  # From module flask import class Flask
from flask_mysqldb import MySQL
app = Flask(__name__)    # Construct an instance of Flask class for our webapp

app.config['MYSQL_HOST'] = os.environ['DBHOST']
app.config['MYSQL_DB'] = os.environ['DBNAME']
app.config['MYSQL_USER'] = os.environ['DBUSER']
app.config['MYSQL_PASSWORD'] = os.environ['DBPASSWORD']

mysql = MySQL(app)

@app.route('/')   # URL '/' to be handled by main() route handler
def main():

   count = 'infinity'

   if mysql:
        cur = mysql.connection.cursor()
        cur.execute("SELECT count FROM counter WHERE name='counter1'")
        data = cursor.fetchone()
    
        if data:
            count = data[0] 

   return render_template('index.html', count=count)

if __name__ == '__main__':  # Script executed directly?
    app.run(host="0.0.0.0", port=8080, debug=True,use_reloader=True)  # Launch built-in web server and run this Flask webapp
