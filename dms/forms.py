
from dms.models import Folder, File
from django import forms


class AddFolder(forms.Form):
	folder_name=forms.CharField(max_length=100)
	folder_description=forms.CharField(max_length=200)

class AddFile(forms.ModelForm):

	class Meta:
		model =File
		exclude= ['uploader','folder']

class SearchForm(forms.Form):
	keyword=forms.CharField(max_length=100, label='', widget=forms.TextInput(attrs={'placeholder': 'Enter File or Folder name'}))
