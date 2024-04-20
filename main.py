from flask import Flask
from website import create_app
import sqlite3
import my_db


app = create_app()

if __name__ == '__main__':
    app.run(debug=True)