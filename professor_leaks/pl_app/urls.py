from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('school_list/<str:search_school>', views.school_list, name=school_list),
    # path('schoo_detail/<str:school_name>', views.school_detail, name=school_detail),

]
