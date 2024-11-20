from flask import Flask, render_template, redirect, request, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'abi'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'restaurent'
mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

# Route to view all customers
@app.route('/customers')
def customerss():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM customers")
    customers_info = cur.fetchall()
    cur.close()
    return render_template('restaurent.html', customers=customers_info)

# Route to search for a specific customers by ID
@app.route('/search_customers', methods=['POST', 'GET'])
def search_customers():
    search_results = []
    search_term = ''
    if request.method == "POST":
        search_term = request.form['cust_id']
        cur = mysql.connection.cursor()
        query = "SELECT * FROM customers WHERE cust_id LIKE %s"
        cur.execute(query, ('%' + search_term + '%',))
        search_results = cur.fetchmany(size=1)
        cur.close()
        return render_template('restaurent.html', customers=search_results)

# Route to insert a new customers
@app.route('/insert_customers', methods=['POST'])
def insert_customers():
    if request.method == "POST":
        cust_id = request.form['cust_id']
        cust_name = request.form['cust_name']
        food = request.form['food']
        quantity = request.form['quantity']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO customers (cust_id, cust_name, food, quantity) VALUES (%s, %s, %s, %s)", (cust_id, cust_name, food, quantity))
        mysql.connection.commit()
        return redirect(url_for('customers'))

# Route to delete a customers by ID
@app.route('/delete_customers/<string:cust_id>', methods=['GET'])
def delete_customers(cust_id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM customers WHERE cust_id = %s", (cust_id,))
    mysql.connection.commit()
    return redirect(url_for('customers'))

# Route to update an existing customers
@app.route('/update_customers', methods=['POST', 'GET'])
def update_customers():
    if request.method == 'POST':
        cust_id = request.form['cust_id']
        cust_name = request.form['cust_name']
        food = request.form['food']
        quantity = request.form['quantity']
        
        cur = mysql.connection.cursor()
        cur.execute("UPDATE customers SET cust_name = %s, food = %s, quantity = %s WHERE cust_id = %s", (cust_name, food, quantity, cust_id))
        mysql.connection.commit()
        return redirect(url_for('customers'))

if __name__ == "_main_":
    app.run(debug=True)
