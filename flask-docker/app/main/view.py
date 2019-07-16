from . import main_blueprint
from flask import render_template, send_from_directory, current_app as app


@main_blueprint.route('/')
def index():
    return render_template('index.html')

@main_blueprint.route('/upload/<filename>')
def uploaded_file(filename):
    print('upload file')
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename) 


@main_blueprint.route('/images')
def compare_images():
    image_name= 'images/upload/songoku.png'
    return render_template('image.html', image_name=image_name)