"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from SnapShare import app
import flickr_helper
from flickr_helper import FlickrHelper
import custom_logs as cl
import os
log = cl.CLog(module=__name__, file="SnapShare.log")

log.logger.info("Main started")

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route("/upload/", methods=['POST'])
def upload():
    flickr_rest = FlickrHelper("rest")
    pid_xml = flickr_rest.upload()

    return render_template(
        'confirmation.html',
        title='Confirmation Page'
        pid = photo_id;
        )

@app.route("/test/", methods=['POST'])
def test():
    return render_template(
      
        )