from django.contrib import admin
from .models import post
from .models import comment
from .models import ans
from .models import profilepic
from .models import profile_pic_model




admin.site.register(post)
admin.site.register(comment)
admin.site.register(ans)
admin.site.register(profilepic)
admin.site.register(profile_pic_model)
