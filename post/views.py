from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views import generic
from django.views.generic import ListView,DetailView,TemplateView
from django.contrib.auth.forms import UserChangeForm
from .models import post
from .models import comment
from django.contrib import messages
from .models import profilepic
from django.urls import reverse_lazy
from .forms import edit_profile_form
from django.contrib.auth.models import User
from .models import profile_pic_model
from django.core.files.storage import FileSystemStorage




class profile(ListView):
    template_name="profile.html"
    model=post
    ordering=['-id']

    def get_queryset(self):
        query_set=super().get_queryset()
        return query_set.select_related

    def get_context_data(self, *args, **kwargs):
        context = super(profile, self).get_context_data(*args, **kwargs)
        context['profile_pic_list'] = profilepic.objects.all()
        return context

def status_form(request):
        if request.method=="POST":
        
                statuss=request.POST['status_name']
                name=request.POST['name']
                if statuss=='':
                        return HttpResponse('404 not found.You must be write something!')
                else:
                        status_database=post(status=statuss,author_name=name)
                        status_database.save()
                        return redirect('profile')
               

def comment_form(request):
    if request.method=="POST":
        commentss=request.POST['comment_name']
        commenter=request.POST['commenter_name']
        comment_id=request.POST['id']
        comment_database=comment(comment=commentss,commenter_name=commenter,comment_id=comment_id)
        comment_database.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



def profile_pic(request):
        return render (request,"profile_pic.html")



class edit_profile (generic.UpdateView):
        form_class=edit_profile_form
        template_name='edit_profile.html'
        success_url=reverse_lazy('edit_profile')


        def get_object(self):
                return self.request.user

def profile_pic_change(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
       
        return render(request, 'profile_pic.html', {
            'uploaded_file_url': uploaded_file_url
        })
   
        



       




        


    

