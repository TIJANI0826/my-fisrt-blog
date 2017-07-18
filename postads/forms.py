from django import forms
from .models import PostAd
CATEGORIES =(
	('LAB','labor'),
	('CAR','cars'),
	('TRU','trucks'),
	('WRI','writing'),
	)
LOCATIONS =(
	('BRO','Bronx'),
	('BRK','Brooklyn'),
	('QNS','Queens'),
	('MAN','Manhattan'),
	)
class PostAdForm(forms.ModelForm):
	error_css_class ='error'
	category = forms.ChoiceField(required=True,
		widget=forms.Select, choices=CATEGORIES)
	location = forms.ChoiceField(required=True,
		widget=forms.Select, choices=LOCATIONS)
	class Meta:
		model = PostAd
		fields = '__all__'
		widgets = {
			'name':forms.TextInput(attrs={'placeholder':'What\'s your name?'}),
			'email':forms.TextInput(attrs={'placeholder':'john@example.com'}),
			'gist':forms.TextInput(attrs={'placeholder':'In a few words,I\'m lookig for'}),
			'expire':forms.TextInput(attrs={'placeholder':'MM/DD/YYYY'})
		}

