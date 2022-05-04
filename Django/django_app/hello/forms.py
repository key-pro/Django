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

class FindForm(forms.Form):
    find = forms.CharField(label='Find', required=False, \
        widget=forms.TextInput(attrs={'class':'form-control'}))

"""class CheckForm(forms.Form):
    str = forms.CharField(label='Name', \
        widget=forms.TextInput(attrs={'class':'form-control'}))
"""

"""class CheckForm(forms.Form):
    empty = forms.CharField(label='Empty', empty_value=True, \
        widget=forms.TextInput(attrs={'class':'form-control'}))
    min = forms.CharField(label='Min', min_length=10, \
        widget=forms.TextInput(attrs={'class':'form-control'}))
    max = forms.CharField(label='Max', max_length=10, \
        widget=forms.TextInput(attrs={'class':'form-control'}))
"""

"""class CheckForm(forms.Form):
    required = forms.IntegerField(label='Required', \
        widget=forms.NumberInput(attrs={'class':'form-control'}))
    min = forms.CharField(label='Min', min_length=100, \
        widget=forms.TextInput(attrs={'class':'form-control'}))
    max = forms.CharField(label='Max', max_length=1000, \
        widget=forms.TextInput(attrs={'class':'form-control'}))
"""

class CheckForm(forms.Form):
    date = forms.DateField(label='Date', input_formats=['%d'], \
        widget=forms.DateInput(attrs={'class':'forms-control'}))
    time = forms.TimeField(label='Time', \
        widget=forms.TimeInput(attrs={'class':'form-control'}))
    datetime = forms.DateTimeField(label='DateTime', \
        widget=forms.DateTimeInput(attrs={'class':'form-control'}))