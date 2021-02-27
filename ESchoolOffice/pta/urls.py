from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('des_create', views.create, name='des_create'),
    path('des_index', views.PTADesignationIndexView.as_view(), name='des_index'),
    path('des/<int:pk>/', views.PTADesignationDetailView.as_view(), name='des_detail'),
]