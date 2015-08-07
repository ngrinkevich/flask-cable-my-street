from flask_wtf import Form
from wtforms import validators, TextField, SelectField
from wtforms.fields.html5 import EmailField
from .models import CustomerInterest

class RegisterCustomerInterestForm(Form):

    customerType = SelectField(u'Customer Type', choices=[('residential', 'Residental'), ('business', 'Business'), ('residentialBusiness', 'Residential Business')], validators=[validators.required()])
    title = SelectField(u'Title', choices=[('Mr', 'Mr'), ('Mrs', 'Mrs'), ('Miss', 'Miss'), ('Ms', 'Ms'), ('Dr', 'Dr')], validators=[validators.required()])
    firstName = TextField(u'First Name', validators=[validators.required()])
    lastName = TextField(u'Last Name', validators=[validators.required()])
    email = TextField(u'Email', validators=[validators.required(),validators.Email()])
    #premiseId = TextField(u'Premise Id', validators=[validators.required()])
    buildingNumber = TextField(u'Building Number', validators=[validators.required()])
    street = TextField(u'Street', validators=[validators.required()])
    postcode = TextField(u'Postcode', validators=[validators.required()])
        
    # businessName = TextField(u'Password', validators=[validators.optional()])
    # mobile = TextField(u'Password', validators=[validators.optional()])
    # landline = TextField(u'Password', validators=[validators.optional()])
    # provider = TextField(u'Password', validators=[validators.optional()])
    # contractenddate = TextField(u'Password', validators=[validators.optional()])
    # mobileProvider = TextField(u'Password', validators=[validators.optional()])
    # mobileContractEndDate = TextField(u'Password', validators=[validators.optional()])

    # interestedInTV = TextField(u'Password', validators=[validators.optional()])
    # interestedInBB = TextField(u'Password', validators=[validators.optional()])
    # interestedInPhone = TextField(u'Password', validators=[validators.optional()])
    # interestedInMobile = TextField(u'Password', validators=[validators.optional()])
    # interestedInBusiness = TextField(u'Password', validators=[validators.optional()])
    
    # updateByEmail = TextField(u'Password', validators=[validators.optional()])
    # updateByPhone = TextField(u'Password', validators=[validators.optional()])
    # updateByPost = TextField(u'Password', validators=[validators.optional()])
    # updateBySMS = TextField(u'Password', validators=[validators.optional()])


    def validate(self):
        check_validate = super(RegisterCustomerInterestForm, self).validate()

        # if our validators do not pass
        if not check_validate:
            return False

        # check if User's interest is already registered with this email
        customerInterest = CustomerInterest.query.filter_by(email=self.email.data).first()
        if customerInterest:
            self.email.errors.append('This email has been already registered')
            return False

      

        return True