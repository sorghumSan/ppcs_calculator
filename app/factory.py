'''
Author: gsl
Date: 2024-01-04 15:06:28
LastEditTime: 2024-01-09 15:59:36
FilePath: /workspace/model_service/app/factory.py
Description: 

Copyright (c) 2024 by gsl, All Rights Reserved. 
'''
from flask import Flask
import config
from ppc_predict import ppc_bp

def create_app():

    app = Flask(__name__)
    
    app.register_blueprint(ppc_bp)
    
    app.config.from_object(config.BaseConfig)

    return app
