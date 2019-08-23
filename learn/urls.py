from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.route_home, name="learn-home"),
    path('about/', views.route_about, name="learn-about"),
    path('contact/', views.route_contact, name="learn-contact"),
    path('<str:coursename>/',views.route_course,name="learn-course"),
    path('<str:coursename>/<str:topicname>/',views.route_topic,name="learn-topic"),
    path('<str:coursename>/<str:topicname>/<str:subtopicname>',views.route_subtopic,name="learn-subtopic"),
    path('add_<str:toadd>_to_<str:keyname>',views.route_add_new,name="learn-add"),
    path('remove_<str:toremovefrom>_<str:fromby>',views.route_remove,name="learn-remove"),
    path('edit_<str:subname>',views.route_edit_subtopic,name="learn-edit"),

    

    

]
