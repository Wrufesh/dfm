from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import os
import pdb

def getFathers(folder_id, filename):
	if folder_id == None:
		rev_fathers=['ROOT', filename]
	else:
		fathers=[]
		rev_fathers=[]
		fathers.append(filename)
		father=Folder.objects.get(id=folder_id)
		fathers.append(father.folder_name)
		while father.parent_folder_id != None:
			father=Folder.objects.get(id=father.parent_folder_id)
			fathers.append(father.folder_name)
		fathers.append('ROOT')
		rev_fathers=reversed(fathers)
	return rev_fathers

def get_upload_path(instance, filename):
    if instance.folder==None:
    	f_id=None
    else:
    	f_id=instance.folder.id
    f_list=getFathers(f_id, filename)
    #pdb.set_trace()
    #f_list.append(filename)
    return os.path.join(*f_list)

class Folder(models.Model):

	folder_name=models.CharField(max_length=100)
	parent_folder=models.ForeignKey('self', null=True, blank=True)
	folder_description=models.TextField(max_length=200)
	
	def __unicode__(self):
		return self.folder_name

class FileTag(models.Model):
	
	tag_name=models.CharField(max_length=100)
	description=models.TextField(max_length=200)
	
	def __unicode__(self):
		return self.tag_name

class File(models.Model):

	folder=models.ForeignKey(Folder, null=True, blank=True)
	uploaded_file=models.FileField(upload_to=get_upload_path)
	pub_date = models.DateTimeField('date published',default=timezone.now())
	tag=models.ManyToManyField(FileTag)
	notes=models.TextField(max_length=200)
	uploader=models.ForeignKey(User)

	def __unicode__(self):
		return str(self.uploaded_file)
		#return os.path.basename(self.uploaded_file.name)

	def filename(self):
		return os.path.basename(self.uploaded_file.name)

