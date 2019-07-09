from django import forms

class Property_form (forms.Form):
    street = forms.CharField(label='street', max_length=50)
    post_code = forms.CharField(label='post_code', max_length=20)
    suburb = forms.CharField(label='suburb', max_length=50)
    # images = 
