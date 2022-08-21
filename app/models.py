from email.policy import default
from django.db import models
import uuid
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=255,blank=True,null=True)
    dob = models.DateField(blank=True,null=True)
    email = models.EmailField(blank=True,null=True)

    profile_img =  models.ImageField(upload_to='images/',default='profiles/user-default.png')
   
    @property
    def imageURL(self):
        try:
            url = self.profile_img.url
        except:
            url=''
        return url
    
class Follow(models.Model):
    followed_by = models.ForeignKey(Profile, on_delete=models.CASCADE,  related_name='followedby')
    followed_to = models.ForeignKey(Profile, on_delete=models.CASCADE,  related_name='followedto',blank=True,null=True)
    def __str__(self):
        return self.followed_by.firstname
    class Meta:
        unique_together = (('followed_by', 'followed_to'), )
    
class Post(models.Model):
    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    post_img = models.ImageField(blank=True,null=True,upload_to="posts/")
    caption = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(Profile,related_name="post_like",blank=True)

    def likeCount(self):
        
        return self.likes.count()
    @property
    def imageURL(self):
        try:
            url = self.post_img.url
        except:
            url=""
        return url

