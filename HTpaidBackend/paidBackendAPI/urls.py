from django.urls import path
from .views import RegisterView, LoginView, UserView, LogoutView,apiVideos,apiShLink,timerSpy,boolSpy,accountinf,jobstate,makeCareer,sendvideo,videofile,listvideos,sendsocial,metier,message,Account,Missions,oneaction,isview
from .views import DashboardStats


# from rest_framework.routers import DefaultRouter
# from .views import UserViewSet, MessageViewSet

# router = DefaultRouter()
# router.register(r'users', UserViewSet)
# router.register(r'messages', MessageViewSet)


urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('user', UserView.as_view()),
    path('logout', LogoutView.as_view()),
    path('Xapi<int:id>', apiVideos),
    path('timer/<str:vidname>/<str:idname>', timerSpy),
    path('getshrlink/<int:user>/<str:vd>', apiShLink),
    path('setbool/<int:booleans>',boolSpy),
     path('account',accountinf),
      path('info/true',jobstate),
      path('setCareer',makeCareer),
      path('publish',sendvideo),
      path('filevideo',videofile),
      path('listvideo',listvideos),
      path('social',sendsocial),
       path('Metier/<int:id>',metier),
       path('Message/<int:UserIdParam>',message),
       path('Account',Account),
       path('Mission/<int:id>',Missions),
       path('ActionsDo',oneaction),
       path('api/dashboard-stats/', DashboardStats.as_view(), name='dashboard-stats'),
       path('Check',isview)
]
