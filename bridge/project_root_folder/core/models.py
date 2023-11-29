from django.db import models
from django.contrib.auth.models import User


# Country model
class Country(models.Model):
    name = models.CharField(max_length=100)
    models.CharField(max_length=2)


    def __str__(self):
        return self.name + self.flag
    
# Citizen model
class Citizen(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

# College model
class College(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    state = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.name}, {self.country}"

# Student model
class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    college = models.ForeignKey(College, on_delete=models.CASCADE )

# Group model
class Group(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='core/group_images/')
    description = models.TextField(max_length=700)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True )
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=True)
    college = models.ForeignKey(College, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
    
# Member model
class Member(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE )

# Socials model
class Socials(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    instagram = models.CharField(max_length=100, blank=True)
    facebook = models.CharField(max_length=100, blank=True)
    linkedin = models.CharField(max_length=120, blank=True)

    def __str__(self):
        return f"Socials for {self.user.username}"

# ProfileQuestions model
class ProfileQuestions(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    question1 = models.TextField()
    question2 = models.TextField()
    question3 = models.TextField()

    def __str__(self):
        return f"Profile Questions for {self.user.username}"
    
# Profile model 
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE )
    image = models.ImageField(upload_to='core/profile_pictures/', default='core/default_profile')
    bio = models.TextField(blank=True)
    socials = models.OneToOneField(Socials, on_delete=models.CASCADE)
    location = models.CharField(max_length=100, blank=True)
    questions = models.OneToOneField(ProfileQuestions, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    
# Follow model
class Bridge(models.Model):
    follower = models.ForeignKey(User, related_name='follower', on_delete=models.CASCADE)
    following = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)

# Post model
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='core/post_images/')
    caption = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='post_likes', blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.caption[:20]}"

# Comment model
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

# Like model
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

# Event model
class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=700)
    date = models.DateField()
    image = models.ImageField(upload_to='core/event_image/')
    target_group = models.ForeignKey(Group, on_delete=models.CASCADE)
    target_country = models.ForeignKey(Country, on_delete=models.CASCADE)
    target_university = models.ForeignKey(College, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)

# Opportunity model (subclass of Event)
class Opportunity(Event):
    linked_application = models.CharField(max_length=120)
    deadline = models.DateField()