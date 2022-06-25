from django.urls import path
from . import views 

urlpatterns = [
    path("", views.home, name='home'),
    path("makeshortlink/", views.make_shortlink, name='make_shortlink'),
    path("<slug:slug>/", views.goto_shortlink, name='goto_shortlink'),
    path("detail/<slug:slug>/", views.detail, name='detail'),
    path("link/<int:id>/confirmdelete/", views.confirm_delete, name='confirm-delete'),
] 