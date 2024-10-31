from flask import Flask, render_template
import util

# Create an application instance
app = Flask(__name__)

# Configuration variables 
username = 'raywu1990'
password = 'test'
host = '127.0.0.1'
port = '5432'
database = 'dvdrental'

# Route to update basket_a by inserting a new row
@app.route('/api/update_basket_a')
def update_basket_a():
    try:
        # Connect to the database
        cursor, connection = util.connect_to_db(username, password, host, port, database)
        
        
        util.run_and_commit_sql(cursor, connection, "INSERT INTO basket_a VALUES (5, 'Cherry');")
        
        
        util.disconnect_from_db(connection, cursor)
        
        
        return render_template('index.html', log_html="Success!")
    
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return render_template('index.html', log_html=error_message)


@app.route('/api/unique')
def unique_fruits():
    try:
        # Connect to the database
        cursor, connection = util.connect_to_db(username, password, host, port, database)
        
        # Execute SQL command to find unique fruits
        sql_query = """
            SELECT
                a.fruit_a AS Basket_A_Fruit,
                b.fruit_b AS Basket_B_Fruit
            FROM
                basket_a a
            FULL JOIN
                basket_b b
            ON
                a.fruit_a = b.fruit_b
            WHERE
                a.fruit_a IS NULL OR b.fruit_b IS NULL;
        """
        records = util.run_and_fetch_sql(cursor, sql_query)
        
        if records == -1:
            raise Exception("Something is wrong with the SQL command")
        else:
            col_names = [desc[0] for desc in cursor.description]
            
            log = records[:10]
        
        
        util.disconnect_from_db(connection, cursor)
        
        
        return render_template('index.html', sql_table=log, table_title=col_names)
    
    except Exception as e:
        
        error_message = f"An error occurred: {str(e)}"
        return render_template('index.html', log_html=error_message)

if __name__ == '__main__':
    # Set debug mode
    app.debug = True
    # Your local machine IP
    ip = '127.0.0.1'
    # Run the Flask app
    app.run(host=ip)