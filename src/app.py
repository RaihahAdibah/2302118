from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# Database configuration
db_config = {
    'host': 'mysqldb',
    'user': 'user',
    'password': 'pass',
    'database': 'testdb'
}

# Initialize database table
def init_db():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS submissions (
            id INT AUTO_INCREMENT PRIMARY KEY,
            search_term VARCHAR(255),
            submit_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        search_term = request.form.get('search')
        # Save to database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO submissions (search_term) VALUES (%s)', (search_term,))
        conn.commit()
        conn.close()
        return redirect('/')
    
    # Get all submissions
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM submissions ORDER BY submit_time DESC')
    submissions = cursor.fetchall()
    conn.close()
    
    return render_template('index.html', submissions=submissions)

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)
