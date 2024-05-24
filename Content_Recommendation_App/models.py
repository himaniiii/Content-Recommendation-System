from django.db import models



class ActionSeries(models.Model):
    Title = models.TextField(blank=True, null=True)
    Release_Year = models.DateField(blank=True, null=True)
    Genre = models.TextField(blank=True, null=True)
    Cast = models.TextField(blank=True, null=True)
    Rating = models.FloatField(blank=True, null=True)
    Certificate = models.TextField(blank=True, null=True)
    Number_of_votes = models.BigIntegerField(blank=True, null=True)


class AdventureSeries(models.Model):
    Title = models.TextField(blank=True, null=True)
    Release_Year = models.DateField(blank=True, null=True) # Note: This should probably be an IntegerField
    Genre = models.TextField(blank=True, null=True)
    Cast = models.TextField(blank=True, null=True)
    Rating = models.FloatField(blank=True, null=True)
    Certificate = models.TextField(blank=True, null=True)
    Number_of_Votes = models.BigIntegerField(blank=True, null=True)


class AnimationSeries(models.Model):
    Title = models.TextField(blank=True, null=True)
    Release_Year = models.DateField(blank=True, null=True)
    Genre = models.TextField(blank=True, null=True)
    Cast = models.TextField(blank=True, null=True)
    Rating = models.FloatField(blank=True, null=True)
    Certificate = models.TextField(blank=True, null=True)
    Number_of_votes = models.BigIntegerField(blank=True, null=True)


class Content(models.Model):
    Title = models.TextField(blank=True, null=True)
    Release_Year = models.DateField(blank=True, null=True)
    Genre = models.TextField(blank=True, null=True)
    Cast = models.TextField(blank=True, null=True)
    Rating = models.FloatField(blank=True, null=True)
    Certificate = models.TextField(blank=True, null=True)
    Number_of_votes = models.BigIntegerField(blank=True, null=True)


class IMDBMovieData(models.Model):
    Rank = models.BigIntegerField(blank=True, null=True)
    Title = models.TextField(blank=True, null=True)
    Genre = models.TextField(blank=True, null=True)
    Director = models.TextField(blank=True, null=True)
    Actors = models.TextField(blank=True, null=True)
    Release_Year = models.DateField(blank=True, null=True)
    Rating = models.FloatField(blank=True, null=True)
    Votes = models.BigIntegerField(blank=True, null=True)
    Metascore = models.FloatField(blank=True, null=True)



class Influencer(models.Model):
    Movie_Rank = models.BigIntegerField(blank=True, null=True)
    Channel_Info = models.TextField(blank=True, null=True)
    Influencer_Score = models.BigIntegerField(blank=True, null=True)
    Posts = models.FloatField(blank=True, null=True)
    Followers = models.FloatField(blank=True, null=True)
    Avg_Likes = models.FloatField(blank=True, null=True)
    _60_Day_Eng_rate = models.FloatField(blank=True, null=True)
    New_Post_Avg_Like = models.FloatField(blank=True, null=True)
    Total_Likes = models.FloatField(blank=True, null=True)
    Youtuber = models.TextField(blank=True, null=True)
    Subscribers = models.BigIntegerField(blank=True, null=True)
    Video_Views = models.BigIntegerField(blank=True, null=True)
    Category = models.TextField(blank=True, null=True)
    Title = models.TextField(blank=True, null=True)
    Uploads = models.BigIntegerField(blank=True, null=True)
    Country = models.TextField(blank=True, null=True)
    Channel_Type = models.TextField(blank=True, null=True)
    Video_Views_Rank = models.BigIntegerField(blank=True, null=True)
    Country_Rank = models.BigIntegerField(blank=True, null=True)
    Channel_Type_Rank = models.BigIntegerField(blank=True, null=True)
    Video_Views_For_The_Last_30_Days = models.BigIntegerField(blank=True, null=True)
    Subscriber_For_Last_30_Days = models.BigIntegerField(blank=True, null=True)
    Created_Year = models.BigIntegerField(blank=True, null=True)



class tv_table(models.Model):
    uid = models.BigIntegerField(blank=True, null=True)
    Title = models.TextField(blank=True, null=True)
    Release_Year = models.DateField(blank=True, null=True)
    Age = models.TextField(blank=True, null=True)
    IMDb = models.FloatField(blank=True, null=True)
    Rotten_Tomatoes = models.TextField(blank=True, null=True)
    Netflix = models.BigIntegerField(blank=True, null=True)
    Hulu = models.BigIntegerField(blank=True, null=True)
    Prime_Video = models.BigIntegerField(blank=True, null=True)
    Disney_plus = models.BigIntegerField(blank=True, null=True)

class Instagram(models.Model):
    Rank = models.BigIntegerField(blank=True, null=True)
    Channel_Info = models.TextField(blank=True, null=True)
    Influence_Score = models.FloatField(blank=True, null=True)
    Posts = models.TextField(blank=True, null=True)
    Followers = models.TextField(blank=True, null=True)
    Avg_Likes = models.TextField(blank=True, null=True)
    _60_Day_Eng_Rate = models.TextField(blank=True, null=True)
    New_Post_Avg_Like = models.TextField(blank=True, null=True)
    Total_Likes = models.TextField(blank=True, null=True)


class UserInteraction(models.Model):
    Movie_Rank = models.BigIntegerField(blank=True, null=True)
    Movie_Title = models.TextField(blank=True, null=True)
    Movie_Genre = models.TextField(blank=True, null=True)
    Movie_Director = models.TextField(blank=True, null=True)
    Movie_Actors = models.TextField(blank=True, null=True)
    Release_Year = models.DateField(blank=True, null=True)
    Movie_Rating = models.FloatField(blank=True, null=True)
    Movie_Votes = models.BigIntegerField(blank=True, null=True)
    Movie_Metascore = models.BigIntegerField(blank=True, null=True)
    Type = models.TextField(blank=True, null=True)
    TV_ID = models.BigIntegerField(blank=True, null=True)
    TV_Title = models.TextField(blank=True, null=True)
    TV_Age = models.TextField(blank=True, null=True)
    IMDB = models.FloatField(blank=True, null=True)
    Rotten_Tomatoes = models.FloatField(blank=True, null=True)
    Netflix = models.BigIntegerField(blank=True, null=True)
    Hulu = models.BigIntegerField(blank=True, null=True)
    Prime_Video = models.BigIntegerField(blank=True, null=True)
    Disney = models.BigIntegerField(blank=True, null=True)



class YouTube(models.Model):
    Rank = models.IntegerField(blank=True, null=True)
    Youtuber = models.TextField(blank=True, null=True)
    Subscriber = models.BigIntegerField(blank=True, null=True)
    Video_Views = models.BigIntegerField(blank=True, null=True)
    Category = models.TextField(blank=True, null=True)
    Title = models.TextField(blank=True, null=True)
    Uploads = models.BigIntegerField(blank=True, null=True)
    Country = models.TextField(blank=True, null=True)
    Channel_Type = models.TextField(blank=True, null=True)
    Video_Views_Rank = models.BigIntegerField(blank=True, null=True)
    Country_Rank = models.BigIntegerField(blank=True, null=True)
    Channel_Type_Rank = models.BigIntegerField(blank=True, null=True)
    Video_Views_For_The_Last_30_days = models.BigIntegerField(blank=True, null=True)
    Subscriber_For_Last_30_Days = models.BigIntegerField(blank=True, null=True)
    Created_Year = models.DateField(blank=True, null=True)
