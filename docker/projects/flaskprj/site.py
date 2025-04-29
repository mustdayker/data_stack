#site.py

from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def index():
    
    # Подобная форма установки соединения в реальной практике
    # СТРОГО ЗАПРЕЩЕНА
    # Данный пример сделан для удобства в учебных целях
    
    conn = psycopg2.connect(dbname='mydata', user='postgres',
                            password='1234', host='dbps')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM women LIMIT 10')
    records = cursor.fetchall()
    
    cursor.close()
    conn.close()
    

    # html_code = '<h1>Hello from Docker!</h1>' + f'{"<p>".join(map(str, records))}'

    html_code = """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Добро пожаловать!</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                line-height: 1.6;
                margin: 0;
                padding: 0;
                background-color: #f4f4f4;
                color: #333;
            }
            .container {
                max-width: 800px;
                margin: 50px auto;
                padding: 20px;
                background: #fff;
                border-radius: 8px;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
                text-align: center;
            }
            h1 {
                color: #2c3e50;
            }
            p {
                margin-bottom: 20px;
            }
            .btn {
                display: inline-block;
                padding: 10px 20px;
                background: #3498db;
                color: #fff;
                text-decoration: none;
                border-radius: 5px;
                transition: background 0.3s;
                cursor: pointer;
                border: none;
                font-size: 16px;
            }
            .btn:hover {
                background: #2980b9;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Добро пожаловать!</h1>
            <p>Приветствуем вас на нашей странице. Мы рады вас видеть!</p>
            <p>Это простая приветственная страница, которую вы можете настроить по своему вкусу.</p>
            <button onclick="showMessage()" class="btn">Узнать больше</button>
        </div>
    
        <script>
            function showMessage() {
                alert("Ты пидор!");
            }
        </script>
    </body>
    </html>
    """

    return html_code

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4000)