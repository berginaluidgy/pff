from django.db import models
from datetime import date
from django.utils import timezone
import datetime
# Create your models here.
from django.contrib.auth.models import AbstractUser,BaseUserManager


# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=255,unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    username=models.CharField(  max_length=256,unique=True, null=True)

    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = ['username']
        
    


class videos(models.Model):
    identifiant=models.IntegerField(unique=True)
    videosId=models.CharField(max_length=255)
    timer=models.DateField()
    description=models.CharField(max_length=255)
    isplaying=models.BooleanField()
    issharing=models.BooleanField()
    istrue=models.BooleanField()
    videoslink=models.CharField(max_length=255,default='')


class videoView(models.Model):
    videosname=models.CharField(max_length=256)
    idvideos=models.CharField(max_length=256)
    timerboolean=models.BooleanField()


class userAccount(models.Model):
    name = models.CharField(max_length=255,unique=True)
    email = models.EmailField(unique=True)
    telephone=models.IntegerField()
    username=models.CharField(max_length=256,unique=True, null=True)
    identifiant=models.IntegerField()
    money=models.IntegerField(default=0)
    howmanydoyoushare=models.IntegerField(default=0)
    howmanydoyouviews=models.IntegerField(default=0)
    howmanydoyouparrainage=models.IntegerField(default=0)

class Career(models.Model):
    idUser=models.IntegerField()
    type=models.CharField(max_length=256)
    careerB=models.DateField(default=date.today)
    contrat=models.CharField(max_length=256)
    contratDate=models.DateField(default=date.today)
    contratEnCours=models.BooleanField(default=False)
    contratRenouvelable=models.BooleanField(default=False)
    typeOfWork=models.CharField(max_length=256)
    money=models.IntegerField()
    preveousMoney=models.IntegerField()
    

class Mission(models.Model):
    idUser=models.IntegerField()
    idmission=models.IntegerField()
    MissionName=models.CharField(max_length=256)
    missionType=models.CharField(max_length=256)
    MissionDate=models.DateField(default=timezone.now())
    EndMissionDate=models.DateField(default=timezone.now() + datetime.timedelta(days=30))
    ifMissionSuccesfully=models.BooleanField()
    predicateReceiveMoney=models.IntegerField()
    Point=models.IntegerField(default=0)
    missionbut=models.IntegerField(default=0)


    
class uploadVideo(models.Model):
    idUser=models.CharField(max_length=256)
    TilteName=models.CharField(max_length=256)
    parentAdresseName=models.CharField(max_length=256)
    BaseName=models.CharField(max_length=256)
    Miniaturename=models.CharField(max_length=256)
    MparentAdresseName=models.CharField(max_length=256)
    MBaseName=models.CharField(max_length=256)


class socialaccess(models.Model):
    idUser=models.CharField(max_length=256)
    ismonetised=models.BooleanField()
    nameyoutube=models.CharField(max_length=256)
    nbrSub=models.IntegerField()
    email=models.EmailField()
    password=models.CharField(max_length=256)
    


class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f'Message from {self.sender} to {self.receiver}'  

class MVideo (models.Model):
    addBy=models.CharField(max_length=256)
    type=models.CharField(max_length=256)
    urlChannel=models.CharField(max_length=256)
    ChannelId=models.CharField(max_length=256)




    
# print(Message.objects.all()[0].timestamp)