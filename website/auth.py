from flask import Blueprint

# defining urls in the file 
# recomendet to name as file 
auth = Blueprint('auth', __name__)

@auth.route('/auth')
def authentication():
    return '<h2>im auth</h2>'
