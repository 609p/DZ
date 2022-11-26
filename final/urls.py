


from django.contrib import admin
from django.urls import path
from tur import views
from django.views.generic import ListView, DeleteView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('/', views.index, name = 'home'),
    path('', views.index, name = 'home'),
    path('profile', views.profile, name = 'profile'),
    path('posts',views.posts),
    path('newpost',views.newposts),
    path('post/<int:id>',views.post),
    path('editpost/<int:id>',views.editpost),
    path('saveeditpost/<int:id>',views.saveeditpost),
    path('deletepost/<int:id>',views.deletepost),
    path('export',views.export),
    path('registration',views.registration),
    path('login',views.login_user),
    path('logout',views.logout_user),

]
