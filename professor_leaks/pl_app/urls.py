from django.urls import path, include # new

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('school_list/<str:search_school>', views.school_list, name='school_list'),
    path('school_detail/<str:search_school>', views.school_detail, name='school_detail'),
    path('accounts/', include('django.contrib.auth.urls')), # new

]
