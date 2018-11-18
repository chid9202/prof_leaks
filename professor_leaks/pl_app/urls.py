from django.urls import path, include # new

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('school_list/<str:search_school>', views.school_list, name='school_list'),
    path('school_detail/<str:search_school>', views.school_detail, name='school_detail'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('professors/', views.prof_list, name='prof_list' ),
    path('professor_detail/<str:prof_name>', views.prof_detail, name='prof_detail')
]
