import os

import psycopg2

from flask import Flask, render_template  # From module flask import class Flask
app = Flask(__name__)    # Construct an instance of Flask class for our webapp

host = os.environ['DBHOST']
db = os.environ['DBNAME']
db_user = os.environ['DBUSER']
db_password = os.environ['DBPASSWORD']

db_conn = psycopg2.connect(host=host, dbname=db, user=db_user, password=db_password)

@app.route('/')   # URL '/' to be handled by main() route handler
def main():

   count = 'infinity'

   if db_conn:
        cur = db_conn.cursor()
        cur.execute("SELECT count FROM counter WHERE name='counter1'")
        data = cursor.fetchone()
    
        if data:
            count = data[0] 

   return render_template('index.html', count=count)

if __name__ == '__main__':  # Script executed directly?
    app.run(host="0.0.0.0", port=8080, debug=True,use_reloader=True)  # Launch built-in web server and run this Flask webapp
