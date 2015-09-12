from flask import Blueprint, request, flash, render_template, redirect, url_for
from forms import AddressRegistrationForm
from models import User, db, Invitee

views_bp = Blueprint("views_bp", __name__)

@views_bp.route("/", methods=['GET'])
def index():
    return "Hello World"

@views_bp.route("/gather", methods=["POST", "GET"])
def gather_address():
    form = AddressRegistrationForm(request.form)
    message=None
    if request.method == "POST" and form.validate():
        invitee = Invitee(form.first_name.data, form.last_name.data,
                          form.email.data, form.address.data)
        db.session.add(invitee)
        db.session.commit()
        message="That worked!"
        return render_template("gather.html", form=form, message=message)
    return render_template("gather.html", form=form, message=message)
    
