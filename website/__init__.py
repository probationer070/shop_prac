from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('sqlite:///mydb.db', echo=True)

Session = sessionmaker(bind=engine)
Base = declarative_base()
# DB_NAME = "mydb.db"

def create_app():
    
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'semicircle_secret_key'
    # app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    # db.init_app(app)
    
    # 블루프린트 인스턴스 가져오기
    from controllers.views import views
    from controllers.auth import auth

    # 플라스크 앱에 등록하기
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    from models.models import User, Items
    Base.metadata.create_all(engine)

    return app
