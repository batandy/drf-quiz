from django.urls import path, include
from .views import *
from . import views
from rest_framework import urls

urlpatterns  =[
    path('', only_category),
    path('<int:cat_id>', only_quiz),
    path("<int:cat_id>/<int:quiz_id>/", quiz_detail),
    # path('cat/<int:cat_id>',category_detail),
    
    path('signup/', views.UserCreate.as_view()),
    path('api-auth/', include('rest_framework.urls')),
]