# project/user/views.py


#################
#### imports ####
#################

from flask import render_template, Blueprint, url_for, redirect, flash, request
from flask_login import login_user, logout_user, login_required

from project import bcrypt
from project.models import User, Email
from project.user.forms import LoginForm

from project.calculators import RetirementCalc


################
#### config ####
################

user_blueprint = Blueprint('user', __name__,)


################
#### routes ####
################

@user_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    """Login page for admins."""
    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(
                user.password, request.form['password']):
            login_user(user)
            flash('You are logged in. Welcome!', 'success')
            if user.admin == True:
                return redirect(url_for('user.admin'))
            else:
                #send them to their Retirement Calc page"
                return redirect(url_for('user.RetirementCalc'))
        else:
            flash('Invalid email and/or password.', 'danger')
            return render_template('user/login.html', form=form)
    return render_template('user/login.html', form=form)


@user_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You were logged out. Bye!', 'success')
    return redirect(url_for('main.index'))


@user_blueprint.route('/admin')
@login_required
def admin():
    """Displays submitted emails to the admin."""
    signups = Email.query.all()
    return render_template('user/admin.html', signups=signups)

@user_blueprint.route('/RetirementCalc')
@login_required
def retirementCalc():
    """Displays Retirement Calculation graphs for a specific user"""
    userinfo = Email.query.get(1)
    info = {"currentValue":userinfo.currentValue,
            "companyMatch":userinfo.companyMatch,
            "yearlyContributions":userinfo.yearlyContributions,
            "age_at_retire":userinfo.age_at_retire,
            "dob":userinfo.dob}
    
    fv1 = RetirementCalc(info, 0.05)
    fv2 = RetirementCalc(info, 0.07)
    fv3 = RetirementCalc(info, 0.10)
    return render_template('user/retirementCalc.html')
    