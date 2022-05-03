from django import forms
from .models import Friend


"""class HelloForm(forms.Form):
    name = forms.CharField(label='name')
    mail = forms.CharField(label='mail')
    age = forms.IntegerField(label='age')

    name = forms.CharField(label='name', \
        widget=forms.TextInput(attrs={'class':'form-control'}))
    mail = forms.CharField(label='mail', \
        widget=forms.TextInput(attrs={'class':'form-control'}))
    age = forms.IntegerField(label='age', \
        widget=forms.NumberInput(attrs={'class':'form-control'}))
"""

"""class HelloForm(forms.Form):
    check = forms.BooleanField(label='Checkbox', required=False)
"""

"""class HelloForm(forms.Form):
    check = forms.NullBooleanField(label='Check')
"""

"""class HelloForm(forms.Form):
    data = [
        ('one', 'item 1'),
        ('two', 'item 2'),
        ('three', 'item 3'),
    ]
    choice = forms.ChoiceField(label='Choice', \
    choices=data)
"""

"""class HelloForm(forms.Form):
    data=[
        ('one', 'radio 1'),
        ('two', 'radio 2'),
        ('three', 'radio 3')
    ]
    choice = forms.ChoiceField(label='radio', \
            choices=data, widget=forms.RadioSelect())
"""

"""class HelloForm(forms.Form):
    data = [
        ('one', 'item 1'),
        ('two', 'item 2'),
        ('three', 'item 3'),
        ('four', 'item 4'),
        ('five', 'item 5'),
    ]
    choice = forms.ChoiceField(label='radio', \
            choices=data, widget=forms.Select(attrs={'size': 5}))
"""

"""class HelloForm(forms.Form):
    data = [
        ('one', 'item 1'),
        ('two', 'item 2'),
        ('three', 'item 3'),
        ('four', 'item 4'),
        ('five', 'item 5'),
    ]
    choice = forms.MultipleChoiceField(label='radio', \
            choices=data, widget=forms.SelectMultiple(attrs={'size': 6}))
"""

"""class HelloForm(forms.Form):
    id = forms.IntegerField(label='ID')
"""

class HelloForm(forms.Form):
    name = forms.CharField(label='Name', \
        widget=forms.TextInput(attrs={'class':'form-control'}))
    mail = forms.EmailField(label='Email', \
        widget=forms.EmailInput(attrs={'class':'form-control'}))
    gender = forms.BooleanField(label='Gender', required=False, \
        widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    age = forms.IntegerField(label='Age', \
        widget=forms.NumberInput(attrs={'class':'form-control'}))
    birthday = forms.DateField(label='Birth', \
        widget=forms.DateInput(attrs={'class':'form-control'}))

class FriendForm(forms.ModelForm):
    class Meta:
        model = Friend
        fields = ['name','mail','gender','age','birthday']

def create(request):
    if(request.method == 'POST'):
        obj = Friend()
        field = FriendForm(request.POST, instance=obj)
        friend.save()
        return redirect(to='/hello')
    params = {
        'title':'Hello',
        'form':FriendForm(),
    }
    return render(request, 'hello/create.html', params)