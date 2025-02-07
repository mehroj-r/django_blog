from django.urls import path
from myblog import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('post/<int:id>', views.postID, name='post'),

]
