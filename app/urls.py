
from django.urls import path,include
from .views import postlist,registerUser,loginUser,logoutUser, profileUser, getprofiles,likepost, profileupdate

urlpatterns = [
 path('',postlist,name="home"),
 path('register/',registerUser,name="register"),
 path('login/',loginUser,name="login"),
 path('logout/',logoutUser, name="logout"),
 path('find/<str:firstname>/',getprofiles, name="get_profile" ),
 path('profile/',profileUser,name='profile'),
 path('profile/<str:pk>/',profileupdate,name='profileupdate'),
 path('like/<str:pk>',likepost,name="likepost"),
  
]
