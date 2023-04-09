from django.urls import path
from . import views

urlpatterns=[
    path('',views.PhonesListView.as_view(),name='list'),
    path('phones/create/',views.PhonesCreateView.as_view(),name='create'),
    path('phones/edit/<int:pk>',views.PhonesUpdateView.as_view(),name='update'),
    path('phones/delete/<int:pk>',views.PhonesDeleteView.as_view(),name='delete'),
    path('task/create/',views.TaskCreateView.as_view(),name='task_create'),
    path('task/edit/<int:pk>',views.TaskUpdateView.as_view(),name='task_update'),
    path('task/delete/<int:pk>',views.TaskDeleteView.as_view(),name='task_delete'),
]