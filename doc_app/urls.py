from django.urls import path
from . import views


urlpatterns = [
  
  
   path('', views.index , name='index'),
   path('case_history', views.case_history , name='case_history'),
   path('dashboard', views.dashboard , name='dashboard'),
   path('main', views.main , name='main'),
   path('va', views.va, name='va'),
   path('vitals', views.vitals , name='vitals'),
   path('post_handler', views.post_handler , name='post_handler'),

#    path('hello', views.case_history , name='case_history'),
#    path('hello', views.case_history , name='case_history'),

   


]