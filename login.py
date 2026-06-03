from flask import Flask,redirect,request,url_for,session,Response

app = Flask(__name__)
app.secret_key = "your_secret_key"

@app.route("/", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "admin" and password == "password":
            print("Login successful")
            session["username"] = username
            return redirect(url_for("welcome"))
        else:
            return Response("Invalid credentials", status=401)
        
    return '''
        <h2>Login</h2>
        <form method="post" action="/">
                <label for="username">Username:</label>
                <input type="text" id="username" name="username"><br><br>
                <label for="password">Password:</label>
                <input type="password" id="password" name="password"><br><br>
                <input type="submit" value="Login">
        </form>
    '''

@app.route("/welcome")
def welcome():
    if "username" in session:
        return f'''
        <h2>Welcome, {session['username']}!</h2>
        <a href="{url_for('logout')}">Logout</a>
        '''

    else:
        return redirect(url_for("login"))
    
@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("login"))    

if __name__ == "__main__":
    app.run(debug=True)