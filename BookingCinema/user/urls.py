from django.urls import path
from .import views
# from .views import 

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    # path('', HomeView.as_view(), name='index'),
]
