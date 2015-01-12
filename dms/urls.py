from django.conf.urls import patterns, url
from dms import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^search/((None/)|(?P<folder_id>\d+)/)$' ,views.searchResult, name='search_result'),
    url(r'^explore/(|(?P<folder_id>\d+)/)$',views.explore, name='explore'),
    url(r'^addfolder/((None/)|(?P<folder_id>\d+)/)$',views.addFolder, name='add_folder'),
    url(r'^addfolder/((None/)|(?P<folder_id>\d+)/)save/$',views.saveFolder, name='save_folder'),
    url(r'^addfile/((None/)|(?P<folder_id>\d+)/)$',views.addFile, name='add_file'),
    url(r'^addfile/((None/)|(?P<folder_id>\d+)/)save/$',views.saveFile, name='save_file'),
    url(r'^sync/((None/)|(?P<folder_id>\d+)/)$',views.syncMedia, name='sync'),
    # ex: /polls/5/
    #url(r'^(?P<poll_id>\d+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    #url(r'^(?P<poll_id>\d+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    #url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
)


