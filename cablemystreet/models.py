from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class CustomerInterest(db.Model):

    id = db.Column(db.Integer(), primary_key=True)
    customerType = db.Column(db.String())
    title = db.Column(db.String())
    firstName = db.Column(db.String())
    lastName = db.Column(db.String())
    email = db.Column(db.String(120), unique=True)
    premiseId = db.Column(db.String())
    buildingNumber = db.Column(db.String())
    street = db.Column(db.String())
    postcode = db.Column(db.String())
        
    businessName = db.Column(db.String(), nullable=True)
    mobile = db.Column(db.String(), nullable=True)
    landline = db.Column(db.String(), nullable=True)
    provider = db.Column(db.String(), nullable=True)
    contractenddate = db.Column(db.String(), nullable=True)
    mobileProvider = db.Column(db.String(), nullable=True)
    mobileContractEndDate = db.Column(db.String(), nullable=True)

    interestedInTV = db.Column(db.Boolean(), nullable=True)
    interestedInBB = db.Column(db.Boolean(), nullable=True)
    interestedInPhone = db.Column(db.Boolean(), nullable=True)
    interestedInMobile = db.Column(db.Boolean(), nullable=True)
    interestedInBusiness = db.Column(db.Boolean(), nullable=True)
    
    updateByEmail = db.Column(db.Boolean(), nullable=True)
    updateByPhone = db.Column(db.Boolean(), nullable=True)
    updateByPost = db.Column(db.Boolean(), nullable=True)
    updateBySMS = db.Column(db.Boolean(), nullable=True)

