from django.urls import path
from .views import (
    CategoryView,
    SkillView,
    HeroView,
    SocialView,
    EducationView,
    WorkView,
    ProjectView,
)

urlpatterns = [
    path('category/',CategoryView.as_view()),
    path('category/<str:pk>/', CategoryView.as_view()),
    path('skills/', SkillView.as_view()),
    path('skills/<str:pk>/', SkillView.as_view()),
    path('project/', ProjectView.as_view()),    
    ]