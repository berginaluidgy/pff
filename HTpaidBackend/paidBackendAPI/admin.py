from django.contrib import admin 
from .models import User,videos,userAccount,videoView,Career,Mission,uploadVideo,socialaccess,Message,MVideo

# Register your models here.
admin.site.register(User)
admin.site.register(videos)
admin.site.register(userAccount)
admin.site.register(videoView)
admin.site.register(Career)
admin.site.register(Mission)
admin.site.register(uploadVideo)
admin.site.register(socialaccess)
admin.site.register(Message)
admin.site.register(MVideo)

