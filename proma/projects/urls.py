from django.urls import path

from . import views

app_name = 'projects'


urlpatterns = [
    path('projects/', views.ProjectListView.as_view(), name='project-list'),
    path('projects/create/', views.ProjectCreateView.as_view(), name='project-create'),
    path('projects/<int:id>/', views.ProjectDetailView.as_view(), name='project-detail'),
    path('projects/<int:id>/update/', views.ProjectUpdateView.as_view(), name='project-update'),
]
