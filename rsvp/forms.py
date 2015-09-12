from wtforms import Form, TextField, TextAreaField, validators

class AddressRegistrationForm(Form):
    first_name = TextField("First name", [validators.required(), validators.Length(min=1, max=50)])
    last_name = TextField("Last name", [validators.required(), validators.Length(min=1, max=50)])
    email = TextField("Email", [validators.required(), validators.Email()])
    address = TextAreaField("Mailing address", [validators.required(), validators.length(max=200)])
    
