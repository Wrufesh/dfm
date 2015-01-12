from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from dms.models import Folder, File, FileTag
from django.utils import timezone
from dms.forms import AddFolder, AddFile, SearchForm

def index(request):
	return HttpResponse('This is an Index Page')

#This function gives list of parent folders of folder_id inchuding itself
def getFathers(folder_id):
	if folder_id == None:
		rev_fathers=None
	else:
		fathers=[]
		rev_fathers=[]
		father=Folder.objects.get(id=folder_id)
		fathers.append(father)
		while father.parent_folder_id != None:
			father=Folder.objects.get(id=father.parent_folder_id)
			fathers.append(father)
		rev_fathers=reversed(fathers)
	return rev_fathers

def getChildrenFolders(folder_id):
	folders=Folder.objects.filter(parent_folder_id=folder_id)
	return folders	

def getChildrenFiles(folder_id):
	files=File.objects.filter(folder_id=folder_id)
	return files


def explore(request, folder_id):
	rev_fathers=getFathers(folder_id)
	folders=getChildrenFolders(folder_id)
	files=getChildrenFiles(folder_id)
	search_form=SearchForm()
	context={'children':folders , 'fathers':rev_fathers , 'files':files, 'folder_id':folder_id, 'search_form':search_form }
	return render(request,'dms/explore.html',context)


def addFolder(request, folder_id):
	form=AddFolder()
	context={'form':form, 'folder_id':folder_id}
	return render(request,'dms/add_folder.html',context)
	#return HttpResponse('This is the folder addition page')

def saveFolder(request,folder_id):
	if request.method == 'POST':
		form=AddFolder(request.POST)
		#data=form.cleaned_data
		if form.is_valid():
			name_folder=form.cleaned_data['folder_name']
			description_folder=form.cleaned_data['folder_description']
			if folder_id==None:
				folder_parent=None
				r_link='/dms/explore/'
			else:
				folder_parent=Folder.objects.get(id=folder_id)
				r_link='/dms/explore/'+str(folder_id)+'/'
			new_folder=Folder(folder_name=name_folder, parent_folder=folder_parent, folder_description=description_folder)
			new_folder.save()
			return HttpResponseRedirect(r_link)
	else:
		form=AddFolder()
	context={'form':form, 'folder_id':folder_id}
	return render(request,'dms/add_folder.html',context)


def addFile(request,folder_id):
	form=AddFile()
	context={'form':form, 'folder_id':folder_id}
	return render(request,'dms/add_file.html',context)

def saveFile(request, folder_id):
	#if folder_id=None:
		
	if request.method== 'POST':
		form=AddFile(request.POST, request.FILES)
		if form.is_valid():
			new_file=form.save(commit=False)
			if folder_id==None:
				new_file.folder=None
				rlink='/dms/explore/'
			else:
				new_file.folder=Folder.objects.get(id=folder_id)
				rlink='/dms/explore/'+str(folder_id)+'/'
			new_file.uploader=request.user
			new_file.save()
			#Clean data here
			return HttpResponseRedirect(rlink)
	else:
		form=AddFile()
	context={'form':form, 'folder_id':folder_id}
	return render(request,'dms/add_file.html',context)
			
			

def searchResult(request, folder_id):
	if request.method=='POST':
		search_form=SearchForm(request.POST)
		if search_form.is_valid():
			keyword=search_form.cleaned_data['keyword']
			sr_folders=Folder.objects.filter(folder_name__contains=keyword)
			sr_files = [f for f in File.objects.filter() if keyword in f.filename()]
			context={'sr_folders':sr_folders, 'sr_files':sr_files, 'keyword':keyword}
			return render(request, 'dms/search_result.html', context)			
			#return HttpResponse(sr_folder)
	else:
		search_form=SearchForm()
	rev_fathers=getFathers(folder_id)
	folders=getChildrenFolders(folder_id)
	files=getChildrenFiles(folder_id)

	context={'children':folders , 'fathers':rev_fathers , 'files':files, 'folder_id':folder_id, 'search_form':search_form }
	return render(request,'dms/explore.html',context)
			
	
def syncMedia(request, folder_id):

	return HttpResponse('Syncing')
# Create your views here.
