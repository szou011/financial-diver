from flask import Flask, render_template

from bokeh.client import pull_session
from bokeh.embed import server_document

app_url = "http://localhost:5100/bokeh_app"

app = Flask(__name__)

@app.route('/')
def bkapp_page():

    script = server_document(app_url)
    return render_template('embed.html', script=script, framework='Flask')

if __name__ == '__main__':
    app.run(port=8080)