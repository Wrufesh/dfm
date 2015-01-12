from django.contrib import admin
from django import forms
from dms.models import Folder, File, FileTag
#from dms.forms import AddDepartment

class AddDepartment(forms.ModelForm):
	department=forms.CharField(max_length=100)
	department_description=forms.CharField(max_length=200)
	#class Meta:
		#model = Folder
		#exclude = ['parent_folder']

class ChoiceInLine(admin.TabularInline):
	model=Folder
	extra=3

class ViewChange(admin.ModelAdmin):

	list_display=('folder_name','parent_folder','folder_description')
	inlines=[ChoiceInLine]
	list_filter=['parent_folder']
	#form = AddDepartment

admin.site.register(Folder, ViewChange)
admin.site.register(File)
admin.site.register(FileTag)
#admin.site.register(File)
#admin.site.register(FileTag)

# Register your models here.
