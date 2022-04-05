from flask import Flask, render_template

userApp=Flask(__name__)

@userApp.route("/")
def login():
    return render_template("login.html")

@userApp.route("/register")
def register():
    return render_template("register.html")

if __name__=="__main__":
    userApp.run()