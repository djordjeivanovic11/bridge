from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from itertools import chain
import random
from django.forms import CommentEditForm, PostEditForm

def index(request):
    # Get the user's country from their profile
    user_profile = Profile.objects.get(user=request.user)
    user_country = user_profile.country

    # Get the most recent posts from people in the user's country
    recent_posts = Post.objects.filter(user__userprofile__country=user_country).order_by('-created_at')

    return render(request, 'index.html', {'recent_posts': recent_posts})


# def create_post(request):
#     if request.method == 'POST':
#         user = request.user  # Assuming you have user authentication enabled
#         content = request.POST.get('content', '')
        
#         if content:
#             new_post = Post.objects.create(user=user, content=content)
#             return HttpResponse("Post created successfully!")
#         else:
#             return HttpResponse("Content cannot be empty for a post.")
#     else:
#         return render(request, 'create_post.html')
    
# @login_required
# def edit_post(request, post_id):
#     post = get_object_or_404(Post, id=post_id, user=request.user)
#     if request.method == 'POST':
#         form = PostEditForm(request.POST, instance=post)
#         if form.is_valid():
#             form.save()
#             return redirect('index')  # Redirect to the feed or wherever you want
#     else:
#         form = PostEditForm(instance=post)
#     return render(request, 'edit_post.html', {'form': form, 'post': post})

# @login_required
# def like_post(request, post_id):
#     post = get_object_or_404(Post, id=post_id)
#     if request.user in post.likes.all():
#         post.likes.remove(request.user)
#         liked = False
#     else:
#         post.likes.add(request.user)
#         liked = True
#     post.save()
#     return JsonResponse({'liked': liked, 'likes_count': post.likes.count()})

# def like(request):
#     if request.method == 'POST':
#         post_id = request.POST.get('post_id', '')
#         post = Post.objects.get(id=post_id)

#         # Assuming you have a ManyToManyField for likes in your Post model
#         post.likes.add(request.user)

#         return HttpResponse("Liked successfully!")
#     else:
#         return HttpResponse("Invalid request method for liking a post.")

# def comment(request):
#     if request.method == 'POST':
#         post_id = request.POST.get('post_id', '')
#         content = request.POST.get('content', '')

#         if content:
#             post = Post.objects.get(id=post_id)
#             comment = Comment.objects.create(user=request.user, post=post, content=content)
#             return HttpResponse("Commented successfully!")
#         else:
#             return HttpResponse("Content cannot be empty for a comment.")
#     else:
#         return HttpResponse("Invalid request method for commenting on a post.")
    
# @login_required
# def edit_comment(request, comment_id):
#     comment = get_object_or_404(Comment, id=comment_id, user=request.user)
#     if request.method == 'POST':
#         form = CommentEditForm(request.POST, instance=comment)
#         if form.is_valid():
#             form.save()
#             return redirect('index')  # Redirect to the feed or wherever you want
#     else:
#         form = CommentEditForm(instance=comment)
#     return render(request, 'edit_comment.html', {'form': form, 'comment': comment})

# def connect(request):
#     if request.method == 'POST':
#         other_user_id = request.POST.get('user_id', '')
#         other_user = Profile.objects.get(id=other_user_id)

#         # Assuming you have a ManyToManyField for connections in your UserProfile model
#         request.user.userprofile.connections.add(other_user)

#         return HttpResponse("Connected with user successfully!")
#     else:
#         return HttpResponse("Invalid request method for connecting with a user.")

# @login_required(login_url='signin')
# def index(request):
#     user_object = User.objects.get(username=request.user.username)
#     user_profile = Profile.objects.get(user=user_object)

#     user_following_list = []

#     user_following = FollowersCount.objects.filter(follower=request.user.username)

#     for users in user_following:
#         user_following_list.append(users.user)

#     # Suggestions
#     all_users_in_country = User.objects.filter(profile__country=user_profile.country)
#     user_following_all = [user.user for user in user_following]

#     new_suggestions_list = [user for user in all_users_in_country if user not in user_following_all and user != user_object]
#     random.shuffle(new_suggestions_list)
#     final_suggestions_list = new_suggestions_list[:5]

#     suggestions_username_profile_list = Profile.objects.filter(user__in=final_suggestions_list)

#     # Get the most recent posts from people in the user's country
#     recent_posts = Post.objects.filter(user__userprofile__country=user_profile.country).order_by('-created_at')

#     return render(request, 'index.html', {'user_profile': user_profile, 'recent_posts': recent_posts, 'suggestions_username_profile_list': suggestions_username_profile_list})

# def create_event(request):
#     if request.method == 'POST':
#         # Similar logic as create_post
#         return HttpResponse("Event created successfully!")
#     else:
#         return render(request, 'create_event.html')

# def create_opportunity(request):
#     if request.method == 'POST':
#         # Similar logic as create_post
#         return HttpResponse("Opportunity created successfully!")
#     else:
#         return render(request, 'create_opportunity.html')

# def show_profile(request):
#     user_id = request.GET.get('user_id', '')
#     user_profile = Profile.objects.get(id=user_id)
#     return render(request, 'user_profile.html', {'user_profile': user_profile})

# @login_required
# def edit_profile(request):
#     if request.method == 'POST':
#         form = UserProfileEditForm(request.POST, instance=request.user.profile)
#         if form.is_valid():
#             form.save()
#             return redirect('profile')  # Redirect to the user's profile page
#     else:
#         form = UserProfileEditForm(instance=request.user.profile)
#     return render(request, 'edit_profile.html', {'form': form})

# def search_people(request):
#     if request.method == 'GET':
#         query = request.GET.get('q', '')
#         user_results = User.objects.filter(username__icontains=query) | User.objects.filter(email__icontains=query)
#         return render(request, 'search_people.html', {'query': query, 'user_results': user_results})
#     else:
#         return HttpResponse("Invalid request method for searching people.")


# def filter_events(request):
#     countries = Country.objects.all()
#     colleges = College.objects.all()

#     if request.method == 'GET':
#         selected_country = request.GET.get('country', '')
#         selected_college = request.GET.get('college', '')

#         events = Event.objects.all()

#         if selected_country:
#             events = events.filter(target_country__id=selected_country)

#         if selected_college:
#             events = events.filter(target_university__id=selected_college)

#         return render(request, 'filtered_events.html', {'events': events, 'countries': countries, 'colleges': colleges, 'selected_country': selected_country, 'selected_college': selected_college})

#     return render(request, 'filtered_events.html', {'countries': countries, 'colleges': colleges})

# def filter_opportunities(request):
#     countries = Country.objects.all()
#     colleges = College.objects.all()

#     if request.method == 'GET':
#         selected_country = request.GET.get('country', '')
#         selected_college = request.GET.get('college', '')

#         opportunities = Opportunity.objects.all()

#         if selected_country:
#             opportunities = opportunities.filter(target_country__id=selected_country)

#         if selected_college:
#             opportunities = opportunities.filter(target_university__id=selected_college)

#         return render(request, 'filtered_opportunities.html', {'opportunities': opportunities, 'countries': countries, 'colleges': colleges, 'selected_country': selected_country, 'selected_college': selected_college})

#     return render(request, 'filtered_opportunities.html', {'countries': countries, 'colleges': colleges})

# def search_posts(request):
#     countries = Country.objects.all()
#     colleges = College.objects.all()

#     if request.method == 'GET':
#         selected_country = request.GET.get('country', '')
#         selected_college = request.GET.get('college', '')

#         # Get posts filtered by selected country and college
#         posts = Post.objects.all()

#         if selected_country:
#             posts = posts.filter(user__profile__country__id=selected_country)

#         if selected_college:
#             posts = posts.filter(user__student__college__id=selected_college)

#         # Order posts by date from most recent to least recent
#         posts = posts.order_by('-created_at')

#         return render(request, 'search_posts.html', {'posts': posts, 'countries': countries, 'colleges': colleges, 'selected_country': selected_country, 'selected_college': selected_college})

#     return render(request, 'search_posts.html', {'countries': countries, 'colleges': colleges})


# def search_people_by_country(request):
#     countries = Country.objects.all()
#     selected_country = None

#     if request.method == 'GET':
#         selected_country_id = request.GET.get('country', '')
        
#         if selected_country_id:
#             selected_country = get_object_or_404(Country, id=selected_country_id)
#             people = Profile.objects.filter(country=selected_country).order_by('college', 'country__name')
#         else:
#             people = Profile.objects.none()

#         paginator = Paginator(people, 10)  # Show 10 people per page

#         page = request.GET.get('page')
#         try:
#             people = paginator.page(page)
#         except PageNotAnInteger:
#             # If the page is not an integer, deliver the first page
#             people = paginator.page(1)
#         except EmptyPage:
#             # If the page is out of range (e.g. 9999), deliver the last page of results
#             people = paginator.page(paginator.num_pages)

#     return render(request, 'search_people_by_country.html', {'countries': countries, 'selected_country': selected_country, 'people': people})

# @login_required
# # create model Notifications
# def ShowNotifications(request):
#     user = request.user
#     notifications = Notification.objects.filter(user=user).order_by('-date')
#     context = {
#         'notifications':notifications,
#     }
#     return render(request, 'blog/notifications.html', context)
    

# # this might be neccessary 
# # from friend.models import FriendList, FriendRequest

# def get_user(user_id):
#     try:
#         return User.objects.get(pk=user_id)
#     except User.DoesNotExist:
#         return None

# def check_authentication(request):
#     if not request.user.is_authenticated:
#         return HttpResponse("You must be authenticated.")
#     return None

# def friends_list_view(request, user_id):
#     error_message = check_authentication(request)
#     if error_message:
#         return error_message

#     this_user = get_user(user_id)
#     if not this_user:
#         return HttpResponse("That user does not exist.")

#     try:
#         friend_list = FriendList.objects.get(user=this_user)
#     except FriendList.DoesNotExist:
#         return HttpResponse(f"Could not find a friends list for {this_user.username}")

#     if request.user != this_user and request.user not in friend_list.friends.all():
#         return HttpResponse("You must be friends to view their friends list.")

#     friends = [(friend, request.user.profile.is_mutual_friend(friend.profile)) for friend in friend_list.friends.all()]
#     context = {'this_user': this_user, 'friends': friends}
#     return render(request, "friend/friend_list.html", context)


# def friend_requests(request, user_id):
#     error_message = check_authentication(request)
#     if error_message:
#         return error_message

#     account = get_user(user_id)
#     if not account or account != request.user:
#         return HttpResponse("You can't view another user's friend requests.")

#     friend_requests = FriendRequest.objects.filter(receiver=account, is_active=True)
#     context = {'friend_requests': friend_requests}
#     return render(request, "friend/friend_requests.html", context)

# @login_required
# def send_friend_request(request):
#     receiver_user_id = request.POST.get("receiver_user_id")
#     if not receiver_user_id:
#         return HttpResponse("Unable to send a friend request.")

#     receiver = get_user(receiver_user_id)
#     if not receiver:
#         return HttpResponse("Unable to send a friend request.")

#     friend_requests = FriendRequest.objects.filter(sender=request.user, receiver=receiver)
#     try:
#         friend_requests.get(is_active=True)
#         return HttpResponse("You already sent them a friend request.")
#     except FriendRequest.DoesNotExist:
#         FriendRequest.objects.create(sender=request.user, receiver=receiver)
#         return HttpResponse("Friend request sent.")

# @login_required
# def accept_friend_request(request, friend_request_id):
#     friend_request = get_user(friend_request_id)
#     if not friend_request or friend_request.receiver != request.user:
#         return HttpResponse("Unable to accept that friend request.")

#     friend_request.accept()
#     return JsonResponse({"response": "Friend request accepted."})

# @login_required
# def remove_friend(request, receiver_user_id):
#     removee = get_user(receiver_user_id)
#     if not removee:
#         return JsonResponse({"response": "Unable to remove that friend."})

#     friend_list = FriendList.objects.get(user=request.user)
#     friend_list.unfriend(removee)
#     return JsonResponse({"response": "Successfully removed that friend."})

# @login_required
# def decline_friend_request(request, friend_request_id):
#     friend_request = get_user(friend_request_id)
#     if not friend_request or friend_request.receiver != request.user:
#         return JsonResponse({"response": "Unable to decline that friend request."})

#     friend_request.decline()
#     return JsonResponse({"response": "Friend request declined."})

# @login_required
# def cancel_friend_request(request, receiver_user_id):
#     receiver = get_user(receiver_user_id)
#     if not receiver:
#         return JsonResponse({"response": "Unable to cancel that friend request."})

#     friend_requests = FriendRequest.objects.filter(sender=request.user, receiver=receiver, is_active=True)
#     if not friend_requests.exists():
#         return JsonResponse({"response": "Nothing to cancel. Friend request does not exist."})

#     for friend_request in friend_requests:
#         friend_request.cancel()

#     return JsonResponse({"response": "Friend request cancelled."})

