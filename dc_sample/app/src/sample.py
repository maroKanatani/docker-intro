import sqlalchemy as sa
from flask import Flask

app = Flask(__name__)
 
@app.route('/')
def hello():
    url = 'mysql+pymysql://root:root@localhost:33306/dc_db?charset=utf8'
    engine = sa.create_engine(url, echo=True)
    rows = engine.execute('SELECT * FROM users')

    names = [("<h1>" + row['name'] + "</h1>") for row in rows]
    response = ''.join(names)

    return response
 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)