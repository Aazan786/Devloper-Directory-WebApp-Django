from django.urls import path
from .views import*

app_name = "users"

urlpatterns = [
    path('login', loginUser, name = 'login'),
    path('logout', logoutUser, name = 'logout'),
    path('register', registerUser, name = 'register'),

    path('', profiles, name = 'profiles'),
    path('profile/<str:pk>', userProfile, name = 'userprofile'),
    path('account', userAccount, name = 'account'),

    path('edit-profile', editProfile, name = 'editprofile'),
    path('add-skill', addSkill, name = 'addskill'),
    path('update-skill/<str:pk>', updateSkill, name = 'updateskill'),
    path('delete-skill/<str:pk>', deleteSkill, name = 'deleteskill'),

    path('inbox', inbox, name="inbox"),
    path('message/<str:pk>/', viewMessage, name="message"),
    path('create-message/<str:pk>/', createMessage, name="create-message"),
    
]