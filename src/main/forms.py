from django import forms

class Class_form (forms.Form):
    university = forms.CharField(label='university', max_length=50)
    course_code = forms.CharField(label='course code', max_length=20)
    course_name = forms.CharField(label='course name', max_length=50)
