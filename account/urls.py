from django.urls import path
from .views import *

app_name = 'account'
urlpatterns = [
    path('', account, name='account'),
    '''# path('', my_fbv, name='courses-list'),
    

    path('create/', CourseCreateView.as_view(), name='courses-create'),
    path('<int:id>/', CourseView.as_view(), name='courses-detail'),
    path('<int:id>/update/', CourseUpdateView.as_view(), name='courses-update'),
    path('<int:id>/delete/', CourseDeleteView.as_view(), name='courses-delete'),'''
]