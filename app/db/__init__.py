import os
from distutils import config

from flask import Blueprint, cli
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

database = Blueprint('database', __name__,)

@database.cli.command('create')
def init_db():
    db.create_all()

@database.before_app_first_request
def create_db_file():
    root = config.Config.BASE_DIR
    dbDirectory = os.path.join(root,'..',config.Config.DB_DIR)
    if not os.path.exists(dbDirectory):
        os.mkdir(dbDirectory)
    db.create_all()

@database.before_app_first_request
def upload_folder():
    root = config.Config.BASE_DIR
    # set the name of the apps log folder to logs
    uploadfolder = os.path.join(root,'..',config.Config.UPLOAD_FOLDER)
    # make a directory if it doesn't exist
    if not os.path.exists(uploadfolder):
        os.mkdir(uploadfolder)
    db.create_all()