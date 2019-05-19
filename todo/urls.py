from django.conf.urls import url
from todo import views

urlpatterns = [
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', views.signin, name='login'),
    url(r'^$', views.main, name='main'),
    url(r'^list/$', views.todo_list, name='todo_list'),
    url(r'^create/$', views.todo_create, name='todo_create'),
    url(r'^edit/(?P<pk>\d+)/$', views.todo_edit, name='todo_edit'),
    url(r'^view/(?P<pk>\d+)/$', views.todo_view, name='todo_view'),
    url(r'^delete/(?P<pk>\d+)/$', views.todo_delete, name='todo_delete'),
    url(r'^complete/(?P<pk>\d+)/$', views.todo_complete, name='todo_complete'),
    url(r'^undo/complete/(?P<pk>\d+)/$', views.undo_complete, name='undo_complete'),
]
