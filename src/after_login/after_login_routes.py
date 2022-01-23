from flask import Blueprint, render_template
views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def home():
    return render_template("before_login/homepage.html")

@views.route('/homepage', methods=['GET', 'POST'])
def homepage():
    return render_template("after_login/home.html")


@views.route('/zdroje', methods=['GET', 'POST'])
def zdroje():
    return render_template("lectures/zdroje.html")

@views.route('/new_base', methods=['GET', 'POST'])
def new_base():
    return render_template("after_login/home.html")


