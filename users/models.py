from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

# Create your models here.
class ProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile', validators=[FileExtensionValidator(['png', 'jpg'])])

    def __str__(self):
        return self.user.username
    
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_posts')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title