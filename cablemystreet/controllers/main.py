from flask import Blueprint, render_template, flash, request, redirect, url_for, Response, jsonify

from cablemystreet.extensions import cache
from cablemystreet.forms import RegisterCustomerInterestForm
from cablemystreet.models import db, CustomerInterest
import json
#from time import sleep

main = Blueprint('main', __name__)


@main.route('/')
@cache.cached(timeout=1000)
def home():
    return render_template('index.html')


@main.route("/getCMSResponse")
def getCMSResponse():
    #sleep(0.5)
    data = json.load(open('cablemystreet/fixtures/getCMSResponse.json')) 
    return jsonify(data)


@main.route("/registerCustomer", methods=["GET", "POST"])
def registerCustomer():
    form = RegisterCustomerInterestForm(csrf_enabled=True)
    if form.validate_on_submit():
        
        customerInterest = CustomerInterest()
        form.populate_obj(customerInterest)
        db.session.add(customerInterest)
        db.session.commit()
        
        flash("User Interest Added suscessfully", "success")
    else:
        print "not success"
    return render_template("register-customer.html", form=form)

@main.route("/sendEmail")
def sendEmail():
    return 

@main.route("/authorizeAccess")
def authorizeAccess():
    return 



