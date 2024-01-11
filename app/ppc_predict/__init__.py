'''
Author: gsl
Date: 2024-01-04 15:21:32
LastEditTime: 2024-01-05 10:27:20
FilePath: /workspace/model_service/app/ppc_predict/__init__.py
Description: 

Copyright (c) 2024 by gsl, All Rights Reserved. 
'''

from flask import  Blueprint
#从Flask导入Blueprint类，实例化这个类就获得了我们的蓝本对象。

ppc_bp = Blueprint("ppcs",__name__,url_prefix='/ppcs')
from . import predict

