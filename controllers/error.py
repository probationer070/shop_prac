from flask import Flask, jsonify, render_template, session

# import traceback

def error_handler(app):

  @app.errorhandler(404)
  def page_not_found(e):
      import datetime as date
      day = date.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
      app.logger.error('page_not_found;user:{0};where:{1};'.format(session['usr_name'], day))
      return render_template('404.html'), 404

  @app.errorhandler(500)
  def error_handling_500(e):
    return jsonify({'Error': "Some Error.."}, 500)
  
  @app.errorhandler(NameError)
  def handle_error(e):
    return jsonify({'Error': "서버 상에서 오류가 발생했습니다."}, 500)
  
  @app.errorhandler(Exception)
  def handle_error(e):
    return jsonify({'Error': "서버 상에서 오류가 발생했습니다."}, 500)
  
  @app.errorhandler(AttributeError)
  def handle_Attr_error(e):
    return jsonify({'Error': "서버 상에서 오류가 발생했습니다."}, 500)
  
  @app.errorhandler(TypeError)
  def handle_type_error(e):
    return jsonify({'Error': "데이터의 값이 잘못 입력되었습니다."}, 500)

  @app.errorhandler(ValueError)
  def handle_value_error(e):
      return jsonify({'Error': "데이터에 잘못된 값이 입력되었습니다."}, 500)


  
