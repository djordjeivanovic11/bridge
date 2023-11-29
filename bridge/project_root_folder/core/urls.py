from django.urls import path
from .views import (
    index,
    # create_post,
    # like,
    # comment,
    # connect,
    # suggestions,
    # create_event,
    # create_opportunity,
    # show_profile,
    # search_people,
    # filter_events,
    # filter_opportunities,
    # search_posts,
    # search_people_by_country,
)

urlpatterns = [
    path('', index, name='index')
#     path('create_post/', create_post, name='create_post'),
#     path('like/', like, name='like'),
#     path('comment/', comment, name='comment'),
#     path('connect/', connect, name='connect'),
#     path('suggestions/', suggestions, name='suggestions'),
#     path('create_event/', create_event, name='create_event'),
#     path('create_opportunity/', create_opportunity, name='create_opportunity'),
#     path('show_profile/', show_profile, name='show_profile'),
#     path('search_people/', search_people, name='search_people'),
#     path('filter_events/', filter_events, name='filter_events'),
#     path('filter_opportunities/', filter_opportunities, name='filter_opportunities'),
#     path('search_posts/', search_posts, name='search_posts'),
#     path('search_people_by_country/', search_people_by_country, name='search_people_by_country'),
]
