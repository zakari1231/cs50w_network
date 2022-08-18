from django.contrib.auth.models import AbstractUser
from django.db import models
from django import forms


class User(AbstractUser):
    pass


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.CharField(max_length=500, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    like = models.ManyToManyField(
        User,  blank=True, related_name="liked_user")

    def __str__(self):
        return self.user.username


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    follower = models.ManyToManyField(
        User,  blank=True, related_name="follower_user")
    following = models.ManyToManyField(
        User,  blank=True, related_name="following_user")
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.user.username


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth',)
