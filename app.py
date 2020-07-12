# -*- coding: utf-8 -*-
from flask import Flask # Flaskパッケージをインポート

app = Flask(__name__) # Flaskクラスのインスタンス生成

@app.route('/') # URLを指定。URLにリクエストが来ると関数が実行される
def index():
	return 'Hello, world.'

if __name__ == '__main__':
	app.run()