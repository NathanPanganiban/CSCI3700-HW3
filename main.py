
from flask import Flask, jsonify, render_template_string
import psycopg2

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        dbname="baskets",
        user="nathanp",
        password="test",
        host="localhost"
    )
    return conn


@app.route('/api/update_basket_a', methods=['GET'])
def update_basket_a():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO basket_a (a, fruit_a) VALUES (5, 'Cherry');")
        conn.commit()
        cur.close()
        conn.close()
        return "Success!"
    except Exception as e:
        return f"Error: {e}"


@app.route('/api/unique', methods=['GET'])
def unique_fruits():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT DISTINCT fruit_a FROM basket_a;")
        unique_a = [row[0] for row in cur.fetchall()]
        cur.execute("SELECT DISTINCT fruit_b FROM basket_b;")
        unique_b = [row[0] for row in cur.fetchall()]
        cur.close()
        conn.close()

        html = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Unique Fruits</title>
        </head>
        <body>
            <h1>Unique Fruits</h1>
            <table border="1">
                <tr>
                    <th>Unique Fruits in Basket A</th>
                    <th>Unique Fruits in Basket B</th>
                </tr>
                <tr>
                    <td><ul>{% for fruit in unique_a %}<li>{{ fruit }}</li>{% endfor %}</ul>< td>
                    <td><ul>{% for fruit in unique_b %}<li>{{ fruit }}</li>{% endfor %}</ul></td>
                </tr>
            </table>
        </body>
        </html>
        """
        return render_template_string(html, unique_a=unique_a, unique_b=unique_b)
    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
	app.run(debug=True)
