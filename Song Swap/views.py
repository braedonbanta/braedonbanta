from flask import Blueprint, render_template

views = Blueprint('views', __name__, template_folder='Templates')


@views.route('/')
def home(a):
    print(a)
    return render_template('popup_window.html', idk=a)
