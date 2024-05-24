"""Content_Recommendation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Content_Recommendation_App.views import home,fetch_action_series,fetch_adventure_series,fetch_animation_series,fetch_imdb_content,fetch_instagram_content,fetch_series_data,fetch_tv_series,fetch_youtube_content, fetch_sorted_series, your_search_view_name, fetch_movie_tv_data, fetch_series_info, fetch_social_media_info


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home, name='home'),
    path('', home, name='root'),
    path('action-series/',fetch_action_series, name='fetch_action_series'),
    path('adventure-series/', fetch_adventure_series, name='fetch_adventure_series'),
    path('animation-series/', fetch_animation_series, name='fetch_animation_series'),
    path('instagram-series/', fetch_instagram_content, name='fetch_instagram_content'),
    path('youtube-series/', fetch_youtube_content, name='fetch_youtube_content'),
    path('tv-series/', fetch_tv_series, name='fetch_tv_series'),
    path('imdb-series/', fetch_imdb_content, name='fetch_imdb_content'),
    path('movie_tv_data/', fetch_movie_tv_data, name='fetch_movie_tv_data'),
    path('series_info/', fetch_series_info, name='fetch_series_info'),
    path('social_media_info/', fetch_social_media_info, name='fetch_social_media_info'),
    path('fetch_sorted_series/',fetch_sorted_series, name='fetch_sorted_series'),
    path('search/', your_search_view_name, name='your_search_view_name'),
]


# if ((dropdown_1 = "sorting") and (dropdown_2 = "action"):
#       