from django import forms

#
# class UserForm(forms.Form):
#     name = forms.CharField()
#     age = forms.IntegerField()

# class UserForm(forms.Form):
#     name = forms.CharField(label="Имя")
#     age = forms.IntegerField(label="Возраст")

# class UserForm(forms.Form):
#     name = forms.CharField(label="Имя")
#     comment = forms.CharField(label="Комментарий", widget=forms.Textarea)

# class UserForm(forms.Form):
#     name = forms.CharField(initial="undefined")
#     age = forms.IntegerField(initial=18)

from django import forms


# class UserForm(forms.Form):
#     name = forms.CharField()
#     age = forms.IntegerField(required=False)
#     email = forms.EmailField(required=False)

# class UserForm(forms.Form):
#     name = forms.CharField(min_length=3)
#     age = forms.IntegerField(min_value=1, max_value=100)

class UserForm(forms.Form):
    name = forms.CharField(min_length=3)
    age = forms.IntegerField(min_value=1, max_value=100)
    required_css_class = "field"
    error_css_class = "error"