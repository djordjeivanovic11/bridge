# import datetime
# import uuid
# from django.db import models

# from django.db import models
# from django.contrib.auth.models import User

# # Country model
# class Country(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name

# # College model
# class College(models.Model):
#     name = models.CharField(max_length=100)
#     state = models.CharField(max_length=2)

#     def __str__(self):
#         return self.name

# # Group model
# class Group(models.Model):
#     name = models.CharField(max_length=100)
#     country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=True)
#     college = models.ForeignKey(College, on_delete=models.CASCADE, null=True, blank=True)

#     def __str__(self):
#         return self.name

# # Post model (superclass)
# class Profile(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     id_user = models.IntegerField()
#     bio = models.TextField(blank=True)
#     profileimg = models.ImageField(upload_to='profile_images', default='blank-profile-picture.png')
#     location = models.CharField(max_length=100, blank=True)

#     def __str__(self):
#         return self.user.username

# class Post(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     user = models.CharField(max_length=100)
#     image = models.ImageField(upload_to='post_images')
#     caption = models.TextField()
#     created_at = models.DateTimeField(default=datetime.now)
#     no_of_likes = models.IntegerField(default=0)

#     def __str__(self):
#         return self.user

# class LikePost(models.Model):
#     post_id = models.CharField(max_length=500)
#     username = models.CharField(max_length=100)

#     def __str__(self):
#         return self.username

# class FollowersCount(models.Model):
#     follower = models.CharField(max_length=100)
#     user = models.CharField(max_length=100)

#     def __str__(self):
#         return self.user

# # Event model (subclass of Post)
# class Event(Post):
#     date = models.DateField()
#     location = models.CharField(max_length=255)

# # Opportunity model (subclass of Post)
# class Opportunity(Post):
#     deadline = models.DateField()

# # Comment model
# class Comment(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)

# # Like model
# class Like(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)

# # Follow model
# class Follow(models.Model):
#     follower = models.ForeignKey(User, related_name='follower', on_delete=models.CASCADE)
#     following = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)

# # Image model
# class Image(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     image = models.ImageField(upload_to='images/')

# # UserProfile model to extend User with additional profile information
# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     bio = models.TextField(null=True, blank=True)
#     profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

# # Notification model for user notifications
# class Notification(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     content = models.TextField()
#     timestamp = models.DateTimeField(auto_now_add=True)
#     is_read = models.BooleanField(default=False)