from flask import Flask, request, render_template_string, redirect
import time
import sys

# ==== Web Server (Flask) ====
app = Flask(__name__)
VALID_USERNAME = "admin"
VALID_PASSWORD = "password123"

HTML_PAGE = '''
<!DOCTYPE html>
<html>
<head><title>Login</title></head>
<body>
    <h2>Test Login Page</h2>
    <form action="/login" method="POST">
        Username: <input name="username" type="text"><br>
        Password: <input name="password" type="password"><br>
        <input type="submit" value="Login">
    </form>
    <p>{{ message }}</p>
</body>
</html>
'''

@app.route("/login", methods=["GET", "POST"])
def login():
    message = ""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username == VALID_USERNAME and password == VALID_PASSWORD:
            message = "Login successful"
        else:
            message = "Invalid credentials"
    return render_template_string(HTML_PAGE, message=message)

@app.route("/")
def index():
    return redirect("/login")

if __name__ == "__main__":
    try:
        print("[*] Web login test server running at http://127.0.0.1:5000/login")
        app.run(port=5000, debug=False, use_reloader=False)
    except KeyboardInterrupt:
        print("\n[*] Shutting down web login server.")
        sys.exit(0)
