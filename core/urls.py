from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('signup/', views.CreateNewUser.as_view(), name='create-user'),
    path('login/', views.MyLoginView.as_view(), name='login'),
    path('logout/', views.MyLogoutView.as_view(), name='logout'),
    path('users_list/', views.UsersListView.as_view(), name='users-list'),
    path('thank_you/', views.thank_you, name='thank-you')
]
