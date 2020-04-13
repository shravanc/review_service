import os
from flask import Blueprint, current_app

from app.controllers.reviews_controller import index as reviews_index
from app.controllers.reviews_controller import home  as reviews_home
from app.controllers.reviews_controller import train as reviews_train
from app.controllers.reviews_controller import predict as reviews_predict


template_dir = os.path.abspath('app/views/reviews')

reviews_blueprints = Blueprint('recommends', 'api', template_folder=template_dir)
reviews_blueprints.add_url_rule('/sentimnets',      view_func=reviews_index,    methods=['GET'])
reviews_blueprints.add_url_rule('/home',            view_func=reviews_home,     methods=['GET'])
reviews_blueprints.add_url_rule('/train',           view_func=reviews_train,    methods=['POST'])
reviews_blueprints.add_url_rule('/predict',         view_func=reviews_predict,  methods=['POST'])

