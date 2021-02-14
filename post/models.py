from django.db import models
from django.shortcuts import render,redirect,HttpResponseRedirect,reverse
from django.contrib.auth.models import User
from django.conf import settings 



# post
class post(models.Model):
    status=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    author_name=models.CharField(max_length=19)
    

    def __str__(self):
        if len(self.status)>50:
            return self.status[:50]+"..."
        return self.status

    def get_absolute_url(self):
        return reverse("edit", kwargs={"pk": self.pk})
    


# comment
class comment(models.Model):
    comment=models.TextField()
    commenter_name=models.CharField(max_length=19)
    comment_date=models.DateTimeField(auto_now_add=True)
    comment_id=models.IntegerField(default=-1)
   

    

    def __str__(self):
        if len(self.comment)>50:
            return self.comment[:50]+"..."
        return self.comment

# this is a demo database of comment
class ans(models.Model):
    ans=models.TextField()
    ans_name=models.CharField(max_length=19)
    ans_date=models.DateTimeField(auto_now_add=True)
    post=models.ForeignKey(post,related_name="posts",on_delete=models.CASCADE)

    def __str__(self):
        if len(self.ans)>50:
            return self.ans[:50]+"..."
        return self.ans


# profile picture
class profilepic(models.Model):
    user = models.OneToOneField(User, null=True,on_delete=models.CASCADE)
    profile_pic=models.ImageField(null=True,blank=True,upload_to='profile_pic/')
    



class profile_pic_model(models.Model):
    user=models.CharField(max_length=100)
    pic=models.ImageField(null=True,blank=True,upload_to='profilepicture/')