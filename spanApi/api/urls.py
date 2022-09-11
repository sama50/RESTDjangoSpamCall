from django.urls import path
from api import views

urlpatterns = [
    path('regi/', views.UserRegistrationView().as_view()),
    path('login/', views.UserLoginView().as_view()),
    path('profile/', views.UserProfileView().as_view()),
    path('addspan/', views.UserAddSpan().as_view()),
    path('checkspan/', views.UserCheckSpan().as_view()),
    path('getallspan/', views.GetAllSpanNumber().as_view()),
    path('filterby/', views.GetSpanName().as_view()),
    
]