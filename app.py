from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    # The MCP Grand Finale script parses this exact string below to auto-update the site!
    message = "Welcome to the DevOps Grand Finale Demo!"
    
    # Dynamically grab the pipeline build number
    app_version = os.environ.get("APP_VERSION", "1.0.0")
    
    return render_template('index.html', message=message, version=app_version, status="success")

if __name__ == '__main__':
    # Use the certs auto-generated during the Docker build
    app.run(host='0.0.0.0', port=5000, ssl_context=('cert.pem', 'key.pem'))
