from flask import Flask, jsonify, render_template, session
from website import create_app

import sqlite3
import my_db

from controllers.error import error_handler


app = create_app()

if not app.debug:
    import logging
    from logging.handlers import RotatingFileHandler
    
    file_handler = RotatingFileHandler('./error/flask_log.log', maxBytes=2000, backupCount=10)
    file_handler.setLevel(logging.WARNING)
    
    app.logger.addHandler(file_handler)

# 에러 핸들러

error_handler(app)

if __name__ == '__main__':
    app.run(debug=True)