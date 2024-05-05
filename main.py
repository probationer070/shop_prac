from flask import Flask, jsonify, render_template, session
from website import create_app

import sqlite3
import my_db



app = create_app()

if not app.debug:
    import logging
    from logging.handlers import RotatingFileHandler
    
    file_handler = RotatingFileHandler('./error/flask_log.log', maxBytes=2000, backupCount=10)
    file_handler.setLevel(logging.WARNING)
    
    app.logger.addHandler(file_handler)

@app.errorhandler(404)
def page_not_found(e):
    import datetime as date
    day = date.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    app.logger.error('page_not_found;user:{0};where:{1};'.format(session['usr_name'], day))
    return render_template('404.html'), 404

@app.errorhandler(500)
def error_handling_500(error):
    return jsonify({'Error': "Some Error.."}, 500)

if __name__ == '__main__':
    app.run(debug=True)