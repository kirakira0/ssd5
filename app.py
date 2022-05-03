from flask import Flask, request, make_response, redirect

app = Flask(__name__)

# DANGER WARNING: Even though Flask lets us manufacture and return 
# our own strings we should never do this. We are illustrating
# horrible code on purpose to show what vulnerabilities look like.
# Don't ever do this in practice.

@app.route("/", methods=['GET'])
def home():
    return """
        <p>This is just a fake form for now, submit anything</p>
        <form method="post" action="/login">
        <p>Email: <input type="text" name="email"></p>
        <p>Password: <input type="password" name="password"></p>
        <p><input type="submit" value="Login"></p></form>"""

@app.route("/login", methods=["POST"])
def login():
    # For now, we're just getting started, so assume login is
    # always okay and just deliver a fake authentication token.
    # We'll do real auth later after the XSS and CSRF demos.  
    request.form.get("email")
    request.form.get("password")
    response = make_response(redirect("/dashboard"))
    response.set_cookie("auth_token", "Fake-token-for-now")
    return response, 303
    
@app.route("/dashboard", methods=['GET'])
def dashboard():
    return """
        <h1>What would you like to do today?</h1>
        <p><a href="/details?account=100">Savings account details</a></p>
        <p><a href="/details?account=998">Checking account details</a></p>
        <p><a href="/transfer">Transfer</a></p>"""

@app.route("/details", methods=['GET', 'POST'])
def details():
    account_number = request.args['account']
    # DANGER DANGER BAD BAD BAD XSS VULNERABILITY
    return f"""
        <h1>Details for Account {account_number}</h1>
        <p>Details coming soon
        <p><a href="/dashboard">Back to Dashboard</a></p>"""

@app.route("/transfer", methods=["GET"])
def transfer():
    return """
        <h1>Make a Transfer</h1>
        <p>Transfer implementation coming soon</p>
        <p><a href="/dashboard">Back to Dashboard</a></p>"""