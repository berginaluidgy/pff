import pprint
import time
import random
import dropbox
from django.db.models import Count
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from dropbox import DropboxOAuth2FlowNoRedirect
from django.core.exceptions import ObjectDoesNotExist
import requests
from django.shortcuts import render,redirect,get_object_or_404
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from rest_framework import status
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.exceptions import AuthenticationFailed
from .serializers import UserSerializer
from .serializers import CareerSerializer, MissionSerializer, UploadVideoSerializer, SocialAccessSerializer

from .models import User
from django.http import JsonResponse
import jwt
from datetime import datetime
import json
from.models import userAccount,videoView,videos,Career,uploadVideo,socialaccess,Message,Mission,MVideo
# from.testy import liste_video
import requests
from rest_framework import status
from datetime import datetime, timedelta


# Create your views here.
class RegisterView(APIView):
    @csrf_exempt
    def post(self, request):
        print('hi2')
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(serializer)
        serializer.save()
        userAccountsaver=userAccount.objects.create(name=serializer.data['name'],identifiant=serializer.data['id'],email=serializer.data['email'],
        telephone=request.data['telephone']  )
        userAccountsaver.save()
        print(serializer.data,request.data,serializer.data['id'])
        return Response(serializer.data)


class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')
        
        serializer = UserSerializer(user)
        return Response(serializer.data)

        # payload = {
        #     'id': user.id,
        #     'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
        #     'iat': datetime.datetime.utcnow()
        # }

        # token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')

        # response = Response()

        # response.set_cookie(key='jwt', value=token, httponly=True)
        
        # response.data = {
        #     'jwt': token
        # }
        return response


class UserView(APIView):

    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated!1')

        try:
            payload = jwt.decode(token, 'secret', algorithm=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!2')

        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)


class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response
    

def apiShLink (request,user,vd):
    dataUser=userAccount.objects.get(pk=user)
    urlredirect='https://youtu.be/'+vd
    # request.build_absolute_uri()
    print(dataUser.name,request.get_host())
    return redirect(urlredirect)
    
     

@api_view(['get'])
def apiVideos(request,id):
    #  datauser=request.data['identifiant']
     ModelMVideo=MVideo.objects.all()
     
     dataall=[]
     for channel in ModelMVideo:
        url = "https://youtube-v31.p.rapidapi.com/search"

        querystring = {"channelId":channel.ChannelId,"part":"snippet,id","order":"date","maxResults":"50"}

        headers = {
        "X-RapidAPI-Key": "b28d2ceb18mshf318642e9225b01p19150cjsndc248bf6ef6e",
        "X-RapidAPI-Host": "youtube-v31.p.rapidapi.com"
        }
# 12133e9a12msh1984ed0d1fcc838p142f51jsnb872243c6adc
        response = requests.get(url, headers=headers, params=querystring)
        trytomade=response.json()

        body=trytomade['items']
        data=[]
        
        for videodata in body:
                try:
                    print('rirtest')
                    video_id=videodata['id']['videoId']
                    
                    videoViews = videoView.objects.filter(idvideos=id, videosname=video_id)
                    if videoViews.exists():

                        print('exist')
                        pass
                             

                    else:
                        print('non exist') 
                        try:
                            racine=videodata['id'] 
                            videodataunique={
                                                'prix_view':str(random.randint(1,3)),
                                                'prix_share':str(random.randint(4,10)),
                                            'video_id':video_id,
                                            'youtube_video_link':'https://youtu.be/'+video_id,
                                            'linkshare':request.get_host()+'/getshrlink/1/'+video_id,
                                            'title':videodata['snippet']['title'],
                                            'description':videodata['snippet']['description'],
                                            'thumbnails':videodata['snippet']['thumbnails']['medium']['url'],
                                            'regarder':'regarder plus de 3 minutes pour voir le gain augmenter,partager ,like commenter sinon vous ne serez pas payer.'
                                    }         
                                        
                                                
                            data.append(videodataunique)                
                          
                        except:
                                 print('')   
                    # if not videoViews.videosname==video_id:
                    #         print(videoViews,video_id,'okeui')
                    # else:
                    #         print('rirtest3')
                               
                except:
                    print('') 
        dataall.append(data)    
            

     
                                                                                    
   
     return Response(dataall)




@api_view(['post'])
def timerSpy(request,vidname,idname):
    
    getrequest=request.data

    return Response(getrequest)

@api_view(['get'])
def boolSpy(request,booleans):
  

    return Response(booleans)

@api_view(['post'])
def accountinf(request):
    getrequest=request.data
    
    print(getrequest)
    dataUser=userAccount.objects.get(identifiant=getrequest['identifiant'])
    print(dataUser.name)
    tab={
        'name':dataUser.name,
        'money':dataUser.money,
        'telephone':dataUser.telephone,
        'howmanydoyoushare':dataUser.howmanydoyoushare,
        'howmanydoyouparrainage':dataUser.howmanydoyouparrainage,
        'username':dataUser.username,
    }
    
    return Response(tab)

@api_view(['get'])
def jobstate(request):

    tabUserJob=[
        ['Partenaire','Que si vous avez un ou des reseaux sociaux comme Youtube,Facebook,Tiktok Monetise','Ilimite'],
        ['Manager','Vous vous occupes seulement du bonne continuite du reseau social confie','Contrat'],
    ['Video Maker','Votre seul role sera de creer des videos ,du script et des vignettes pour des videos qui seront publies sur des reseaux sociaux','Contrat'],
    ['Viewer','En tant que Viewer vous aurez comme mission de visualiser des videos ou des posts sur des reseaux sociales ,de les partages et de les commentes'],
    ]
    
    return Response(tabUserJob)

@api_view(['post'])
def makeCareer(request):
    careerinfo=request.data
    CareerTab=Career.objects.create(idUser=careerinfo['id'],type=careerinfo['type'],careerB=datetime.now(),contrat='none', contratEnCours=False,contratRenouvelable=False,typeOfWork='none',preveousMoney=0,money=0)
    response=careerinfo['type']
    print(response)
    return Response(response)


@api_view(['POST'])
def videofile(request):
    file=request.data['file']
    Response(file)


@api_view(['POST'])
def sendvideo(request):
    receiveinfo=request.data
    print(request.data['video'],'ok')
    rec=str(request.data['video'])
    recv=rec.replace("'\'","\\")
    reci=receiveinfo['image']
    rect=receiveinfo['title']
    recidUser=receiveinfo['idUser']


    file_obj = request.FILES.get('video')
    file_obj_img=request.FILES.get('image')
    if not file_obj and not file_obj_img:
      return Response({'error': 'Aucun fichier n\'a été uploadé'}, status=status.HTTP_400_BAD_REQUEST)

        # Sauvegarde du fichier
    path = default_storage.save(f'uploads/{file_obj.name}', ContentFile(file_obj.read()))
    pathimg = default_storage.save(f'uploads/{file_obj_img.name}', ContentFile(file_obj.read()))
    print(path,'rire2')
    print(pathimg,'rire2')
    def upload_video_to_dropbox(file_path, dropbox_path,file_path_img,dropbox_path_img):
       

        APP_KEY = 'm6yit15q69uy2vf'
        APP_SECRET = 'ted12iwqcprmdud'
        REFRESH_TOKEN = 'tcxWZ-dUkcIAAAAAAAAAAQt_EwvI-rtXfbnCk_pwTHaTirzw2TuD_1fRegZGE02y'
        
        def refresh_access_token():
            
            
            try:
                dbx2 = dropbox.Dropbox(
                app_key=APP_KEY,
                app_secret=APP_SECRET,
                oauth2_refresh_token=REFRESH_TOKEN
            )
        
        # La bibliothèque gère automatiquement le rafraîchissement du token
        # Vous pouvez vérifier que ça fonctionne en appelant une méthode de l'API
                dbx2.users_get_current_account()

                print(dbx2)
                print("Nouveau access token obtenu avec succès")
                return dbx2
            except Exception as e:
                print(f"Erreur lors du rafraîchissement du token : {e}")
                return None
                
        
        
        
        # dbx = dropbox.Dropbox(access_token)
        dbx=refresh_access_token()
        print(file_path)
        print(recv)
        try:
            with open(file_path, "rb") as f:
                dbx.files_upload(f.read(), dropbox_path)
                print(f"File uploaded to {dropbox_path}")
            with open(file_path_img, "rb") as f:
                dbx.files_upload(f.read(), dropbox_path_img)
                print(f"File uploaded to {dropbox_path_img}")    
        except Exception as e:
            print(f"Erreur lors du téléchargement du fichier sur Dropbox : {e}")
            return False, str(e)


    
    file_path =path
    file_path_img=pathimg 
    print(recv)
    dropbox_path = "/ydriver/"+"".join((file_obj.name).split())+'/'+file_obj.name
    dropbox_path_img = "/ydriver/"+"".join((file_obj.name).split())+'/'+file_obj_img.name

    upload_video_to_dropbox(file_path, dropbox_path,file_path_img,dropbox_path_img)
    stockeddatabase=uploadVideo.objects.create(idUser=recidUser,TilteName=rect,parentAdresseName="".join((file_obj.name).split()),BaseName=file_obj.name,
                                               Miniaturename=file_obj_img.name,MparentAdresseName="".join((file_obj.name).split()),MBaseName=file_obj_img.name)
    
    return Response('ok')

def refresh_access_token():

    APP_KEY = 'm6yit15q69uy2vf'
    APP_SECRET = 'ted12iwqcprmdud'
    REFRESH_TOKEN = 'tcxWZ-dUkcIAAAAAAAAAAQt_EwvI-rtXfbnCk_pwTHaTirzw2TuD_1fRegZGE02y'
    
    try:
        dbx2 = dropbox.Dropbox(
            app_key=APP_KEY,
            app_secret=APP_SECRET,
            oauth2_refresh_token=REFRESH_TOKEN
        )
        # Vérifiez si le token est valide en appelant une méthode de l'API
        dbx2.users_get_current_account()
        print("Le token d'accès a été rafraîchi avec succès")
        return dbx2
    except Exception as e:
        print(f"Erreur lors du rafraîchissement du token d'accès : {e}")
        return None



def list_files_in_dropbox_folder(folder_path):
    dbx = refresh_access_token()
    if dbx is None:
        return False, "Échec du rafraîchissement du token d'accès"

    try:
        files = dbx.files_list_folder(folder_path)
        file_names = [entry.name for entry in files.entries]
        return True, file_names
    except Exception as e:
        print(f"Erreur lors de la liste des fichiers sur Dropbox : {e}")
        return False, str(e)

@api_view(['GET'])
def listvideos(request):

    folder_path = "/ydriver/ApprendreReact_Lesformulaires.mp4"
    success, message = list_files_in_dropbox_folder(folder_path)
    if not success:
        return Response({'error': message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return Response({'files': message})


@api_view(['POST'])
def sendsocial(request):
    Userid=request.data['Userid']
    nom=request.data['nom']
    sub=request.data['sub']
    email=request.data['email']
    Pass=request.data['password']
    ismoneti=request.data['check']
    modelsocial=socialaccess.objects.create(idUser=Userid,ismonetised=ismoneti,nameyoutube=nom,email=email,nbrSub=sub,password=Pass)
    print(modelsocial)
    return  Response({'fin':'success'},200)


@api_view(['GET'])
def metier(request,id):
    UserC=Career.objects.get(idUser=id)
    UserObject={
        'id':UserC.idUser,
        'type':UserC.type,
        'CareerB':UserC.careerB,
        'contratdate':UserC.contratDate,
        'Contrat':UserC.contrat,
        'contratEnCours':UserC.contratEnCours,
        'ContratRenouvelable':UserC.contratRenouvelable,
        'typeOfWork':UserC.typeOfWork,
        'previousMoney':UserC.preveousMoney,
        'money':UserC.money,
    }
    print(UserC)
    return Response(UserObject)


@api_view(['GET','POST'])
def message(request,UserIdParam):
    # messages = Message.objects.filter(Sender='')
    

    if request.method=='POST':
        sender= get_object_or_404(User,pk=request.data['send'])
        receive= get_object_or_404(User,pk=request.data['receive'])
        content=request.data['content']
        Userid=UserIdParam
        if Userid==0:
            Userid=request.data['Userid']
        # Useridreceiver=request.data['Userid2']

        # models=Message.objects.create(sender=sender,seceiver=receive,content=content)
        
         
        if not Userid or not content:
            return Response({"error": "User ID and content are required"}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.get(id=Userid)
        last_message = Message.objects.filter(receiver=user.pk).order_by('-timestamp').first()
        
        if last_message:
            time_since_last_message = datetime.now() - last_message.timestamp
            if time_since_last_message < timedelta(hours=2):
                return Response({"error": "You can only send a message every two hours"}, status=status.HTTP_429_TOO_MANY_REQUESTS)

        new_message = Message.objects.create(sender=sender,receiver=receive,content=content)
        return Response({"message": "Message sent successfully", "message_id": new_message.id}, status=status.HTTP_201_CREATED)

    if request.method=='GET':
         if UserIdParam==0:
            return Response({'error':'erreur'})
         else:
            Usersender=User.objects.get(id=UserIdParam)
            sender=Usersender
            models=Message.objects.get(sender=sender)
            return Response({'Send':models.content})



@api_view(['GET','POST'])
def Account(request):
    id=request.data['id']
    CareerM=Career.objects.get(idUser=id)
    UserM=User.objects.get(id=id)
    userAccountM=userAccount.objects.get(identifiant=id)
    MissionM=None
    try:
        Mission.objects.get(idUser=id)
    except:
        pass
    else:
        MissionM=Mission.objects.get(idUser=id)
    Account={
        'User':UserM.name,
        'email':UserM.email,
        'Phone':userAccountM.telephone,
        'CareerMoney':CareerM.money,
        'MissionDate':MissionM.MissionDate,
        'ifMissionSuccesfully':MissionM.ifMissionSuccesfully,
        'Point':MissionM.Point,
    }
    return Response(Account)


 
@api_view(['GET','POST'])  
def Missions(request,id):
    if request.method=='GET':
        response=0
        try:
            mission=Mission.objects.get(idUser=id)
            
        except:
            response=504
        else:
            response=200

        return Response(response)    
    else:
        requestModels=request.data
        mission=Mission.objects.create(idUser=id,idmission=requestModels['idmission'],MissionName=requestModels['MissionName'],missionType=requestModels['missionType'],
        ifMissionSuccesfully=False,predicateReceiveMoney=requestModels['predicateReceiveMone'],Point=0,missionbut=requestModels['missionbut'])
        return Response({'response':'Mission Ajouter'})

        
@api_view(['POST'])  
def oneaction(request):
    id=request.data['id']
    isimp=request.data['isimp']
    modelsmission=Mission.objects.get(idmission=id)
    but=modelsmission.missionbut
    if but>100:
        if isimp==0:
            modelsmission.Point+=6
            print(modelsmission.Point)
            modelsmission.save()
        elif isimp==1:
            time.sleep(3)
            modelsmission.Point+=9
            print(modelsmission.Point)
            modelsmission.save()
        else:
            return Response({'erreur':'Erreur'})    

    elif but<100:
        modelsmission.Point+=1
        modelsmission.save()

    else:
        return Response({'erreur':'Erreur'}) 

    return Response('Action')    
@api_view(['POST'])
def isview(request):
    print(id)
    idUser=request.data['idUser']
    name=request.data['name']
    videoViews=videoView.objects.filter(idvideos=idUser)
    videoView.objects.create(videosname=name,idvideos=idUser,timerboolean=True)
    return Response({'taille':len(videoViews)})


class DashboardStats(APIView):
    def get(self, request):
        total_users = User.objects.count()
        users_with_career = Career.objects.values('idUser').distinct().count()
        users_with_missions = Mission.objects.values('idUser').distinct().count()
        
        # Users registered per day (last 30 days)
        thirty_days_ago = timezone.now() - timedelta(days=30)
        users_per_day = User.objects.filter(date_joined__gte=thirty_days_ago) \
            .extra({'date': "date(date_joined)"}) \
            .values('date') \
            .annotate(count=Count('id'))
        
        # Last login for each user
        last_logins = User.objects.values('id', 'last_login')
        
        total_videos = uploadVideo.objects.count()
        total_social_accounts = socialaccess.objects.count()
        users_with_social = socialaccess.objects.values('idUser').distinct().count()
        
        return Response({
            'total_users': total_users,
            'users_with_career': users_with_career,
            'users_with_missions': users_with_missions,
            'users_per_day': list(users_per_day),
            'last_logins': list(last_logins),
            'total_videos': total_videos,
            'total_social_accounts': total_social_accounts,
            'users_with_social': users_with_social
        })