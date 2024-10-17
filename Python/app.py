from flask import Flask, make_response

app = Flask(__name__)

@app.after_request
def set_security_headers(response):
    # Content Security Policy
    response.headers['Content-Security-Policy'] = "default-src 'self'; script-src 'self'; object-src 'none';"
    
    # X-Frame-Options
    response.headers['X-Frame-Options'] = 'DENY'
    
    # X-Content-Type-Options
    response.headers['X-Content-Type-Options'] = 'nosniff'
    
    # Strict-Transport-Security
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    
    # Referrer-Policy
    response.headers['Referrer-Policy'] = 'no-referrer'
    
    return response

@app.route('/')
def index():
    return 'Hello, Secure World!'

if __name__ == '__main__':
    app.run(ssl_context=('cert.pem', 'key.pem'))  # Run with SSL
