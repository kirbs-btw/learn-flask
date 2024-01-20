from flask import Blueprint, render_template

# defining urls in the file 
# recomendet to name as file 
# later importing this variable
views = Blueprint('views', __name__)

# runs when we go to home
@views.route('/')
def home():
    # the retrun gives the output of the site - i think
    return render_template("home.html")
    
@views.route('/name/<string:name>/')
def namedrop(name):
    # the retrun gives the output of the site - i think
    return name

    
@views.route('/num/<int:num>/')
def numdrop(num):
    # the retrun gives the output of the site - i think
    return str(int(num)+10)
