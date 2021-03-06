# project/main/views.py


#################
#### imports ####
#################

from flask import render_template, Blueprint, request, flash, redirect, url_for

from forms import SignUpForm
from project import db
from project.models import Email, User


################
#### config ####
################

main_blueprint = Blueprint('main', __name__,)


################
#### routes ####
################


@main_blueprint.route('/', methods=['GET', 'POST'])
def index():
    """Landing page for users to enter emails."""
    form = SignUpForm(request.form)
    if form.validate_on_submit():
        test = Email.query.filter_by(email=form.email.data).first()
        if test:
            flash('Sorry that email aleady exists!', 'danger')
        else:
            email = Email(email=form.email.data)
            db.session.add(email)
            db.session.commit()
            db.session.add(User(email=form.email.data, password=form.password.data, admin=False))
            db.session.commit()

            flash('Thank you for your interest!', 'success')
            #Send to RetirementInfo page to gather info
            return redirect(url_for('main.index'))
    return render_template('main/index.html', form=form)
