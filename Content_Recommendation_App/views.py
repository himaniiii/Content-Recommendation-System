# views.py
from django.shortcuts import render
from .database_utils import run_query
import pandas as pd
import mysql.connector

# Database Configuration for the application
DB_CONFIG_GLOBAL = {
    'user': 'root',
    'password': 'Himani@12',
    'host': 'localhost',
    'database': 'global_data',
    'raise_on_warnings': True
}

DB_CONFIG_LOCAL = {
    'user': 'root',
    'password': 'Himani@12',
    'host': 'localhost',
    'database': 'iia',
    'raise_on_warnings': True
}

def home(request):
    return render(request, 'home.html')

def fetch_series_data(request, series_type):
    table_mappings = {
        "instagram": "instagram",
        "imdb": "imdb_movie_data",
        "tv": "tv",
        "youtube": "youtube",
        "movie_tv_data": "Movie_TV_Data",
        "social_media_info": "Social_Media_Info",
        "series_info": "Series_Info",
        "action": "action_series",
        "adventure": "adventure_series",
        "animation": "animation_series"
    }

    table_name = table_mappings.get(series_type, f"{series_type}_series")
    query = f"SELECT * FROM {table_name} LIMIT 10;"

    data, column_names = run_query(query, table_name)
    template_name = f"{series_type}_series.html"
    return render(request, template_name, {'data': data, 'columns': column_names})

def fetch_action_series(request):
    return fetch_series_data(request, 'action')

def fetch_adventure_series(request):
    return fetch_series_data(request, 'adventure')

def fetch_animation_series(request):
    return fetch_series_data(request, 'animation')

def fetch_instagram_content(request):
    return fetch_series_data(request, 'instagram')

def fetch_youtube_content(request):
    return fetch_series_data(request, 'youtube')

def fetch_tv_series(request):
    return fetch_series_data(request, 'tv')

def fetch_imdb_content(request):
    return fetch_series_data(request, 'imdb')

def fetch_movie_tv_data(request):
    return fetch_series_data(request, 'movie_tv_data')

def fetch_social_media_info(request):
    return fetch_series_data(request, 'social_media_info')

def fetch_series_info(request):
    return fetch_series_data(request, 'series_info')

def fetch_sorted_series(request):
    content_type = request.GET.get('content_type')
    sort_by = request.GET.get('sort_by')

    global_tables = ['Movie_TV_Data', 'Social_Media_Info', 'Series_Info']
    local_tables = ['imdb_movie_data', 'tv', 'instagram', 'youtube', 
                    'action_series', 'adventure_series', 'animation_series']

    column_mappings = {
        "action": {
            'table_name': 'action_series',
            'database': 'iia' if 'action_series' in local_tables else 'global_data'
        },
        "adventure": {
            'table_name': 'adventure_series',
            'database': 'iia' if 'adventure_series' in local_tables else 'global_data'
        },
        "animation": {
            'table_name': 'animation_series',
            'database': 'iia' if 'animation_series' in local_tables else 'global_data'
        },
        "instagram": {
            'table_name': 'instagram',
            'database': 'iia' if 'instagram' in local_tables else 'global_data'
        },
        "imdb": {
            'table_name': 'imdb_movie_data',
            'database': 'iia' if 'imdb_movie_data' in local_tables else 'global_data'
        },
        "tv": {
            'table_name': 'tv',
            'database': 'iia' if 'tv' in local_tables else 'global_data'
        },
        "youtube": {
            'table_name': 'youtube',
            'database': 'iia' if 'youtube' in local_tables else 'global_data'
        },
        "Movie_TV_Data": {
            'table_name': 'Movie_TV_Data',
            'database': 'global_data' 
        },
        "Social_Media_Info": {
            'table_name': 'Social_Media_Info',
            'database': 'global_data' 
        },
        "Series_Info": {
            'table_name': 'Series_Info',
            'database': 'global_data'
        },
    }

    mapping = column_mappings.get(content_type)
    if not mapping:
        return render(request, "error.html", {'error': 'Invalid content type'})

    table_name = mapping['table_name']
    database_name = mapping['database']

    print(database_name)

    if sort_by:
        query = f"SELECT * FROM {table_name} ORDER BY {sort_by} DESC LIMIT 300;"
    else:
        query = f"SELECT * FROM {table_name} LIMIT 300;"
    print(query)
    data, column_names = run_query(query, table_name)
    template_name = f"{content_type}_series.html"
    return render(request, template_name, {'data': data, 'columns': column_names})

def Similarity(inp):
    SIMILARITY_THRESHOLD = 0.5

    def fetch_data(query, database):
        connection = mysql.connector.connect(**DB_CONFIG[database])
        cursor = connection.cursor()
        cursor.execute(query)
        data = pd.DataFrame(cursor.fetchall(), columns=cursor.column_names)
        cursor.close()
        connection.close()
        return data

    text_columns = ['Title', 'Release_Year', 'Genre', 'Cast', 'Rating', 'Certificate', 'Youtuber', 'ChannelInfo']

    DB_CONFIG = {
        'global_data': {
            'user': 'root',
            'password': 'Himani@12',
            'host': 'localhost',
            'database': 'global_data',
            'raise_on_warnings': True
        },
        'iia': {
            'user': 'root',
            'password': 'Himani@12',
            'host': 'localhost',
            'database': 'iia',
            'raise_on_warnings': True
        }
    }

    # Fetch data from tables in both databases
    imdb_data = fetch_data("SELECT * FROM imdb_movie_data", 'iia')
    tv_data = fetch_data("SELECT * FROM tv", 'iia')
    action_series = fetch_data("SELECT * FROM action_series", 'iia')
    adventure_series = fetch_data("SELECT * FROM adventure_series", 'iia')
    animation_series = fetch_data("SELECT * FROM animation_series", 'iia')
    movie_tv_data = fetch_data("SELECT * FROM Movie_TV_Data", 'global_data')
    social_media_info = fetch_data("SELECT * FROM Social_Media_Info", 'global_data')
    series_info = fetch_data("SELECT * FROM Series_Info", 'global_data')
    instagram_data = fetch_data("SELECT *, ChannelInfo AS Title FROM instagram", 'iia')
    youtube_data = fetch_data("SELECT *, Youtuber AS Title FROM youtube", 'iia')

    # Combine data and add a SeriesType column
    combined_data = pd.concat([
        imdb_data.assign(SeriesType='IMDB'),
        tv_data.assign(SeriesType='TV'),
        action_series.assign(SeriesType='Action'),
        adventure_series.assign(SeriesType='Adventure'),
        animation_series.assign(SeriesType='Animation'),
        movie_tv_data.assign(SeriesType='Movie_TV_Data'),
        social_media_info.assign(SeriesType='Social_Media_Info'),
        series_info.assign(SeriesType='Series_Info'),
        instagram_data.assign(SeriesType='Instagram'),
        youtube_data.assign(SeriesType='YouTube')
    ], ignore_index=True)

    combined_data['combined_text'] = combined_data[text_columns].apply(lambda row: ', '.join(row.values.astype(str)), axis=1)

    # Similarity comparison
    matching_results = []

    for idx, row in combined_data.iterrows():
        series_type = row['SeriesType']
        title = row['Title']
        similarity_scores = []

        for col in text_columns:
            input_tokens = set(inp.lower().split())
            title_tokens = set(str(title).lower().split())
            similarity = len(input_tokens.intersection(title_tokens)) / len(input_tokens.union(title_tokens))
            similarity_scores.append(similarity)

        average_similarity = sum(similarity_scores) / len(similarity_scores)

        if average_similarity >= SIMILARITY_THRESHOLD:
            matching_results.append((series_type, title, average_similarity))

    # Sort and return results
    sorted_results = sorted(matching_results, key=lambda x: x[2], reverse=True)
    return sorted_results



def your_search_view_name(request):
    if 'search_query' in request.GET:
        search_query = request.GET.get('search_query')
        similarity_results = Similarity(search_query)

        template_name = "search_results.html"
        return render(request, template_name, {
            'similarity_results': similarity_results, 
            'search_query': search_query
        })
    else:
        return render(request, 'search_results.html')

    
def global_data(request, content_type):
    content_mappings = {
        "movie_tv_data": {
            "table_name": "Movie_TV_Data",
            "database": "global_data",
            "sort_column": "Movie_Rank"
        },
        "series_info": {
            "table_name": "Series_Info",
            "database": "global_data",
            "sort_column": "Rating"
        },
        "social_media_info": {
            "table_name": "Social_Media_Info",
            "database": "global_data",
            "sort_column": "channel_type_rank"
        },
        # Local database tables
        "imdb_movie_data": {
            "table_name": "imdb_movie_data",
            "database": "iia",
            "sort_column": "Rank"
        },
        "tv": {
            "table_name": "tv",
            "database": "iia",
            "sort_column": "Rating"
        },
        "instagram": {
            "table_name": "instagram",
            "database": "iia",
            "sort_column": "Rank"
        },
        "youtube": {
            "table_name": "youtube",
            "database": "iia",
            "sort_column": "Subscribers"
        },
        "action_series": {
            "table_name": "action_series",
            "database": "iia",
            "sort_column": "Rating"
        },
        "adventure_series": {
            "table_name": "adventure_series",
            "database": "iia",
            "sort_column": "Rating"
        },
        "animation_series": {
            "table_name": "animation_series",
            "database": "iia",
            "sort_column": "Rating"
        }
    }

    # Get the specific mapping for the requested content type
    mapping = content_mappings.get(content_type)

    if mapping:
        table_name = mapping["table_name"]
        database_name = mapping["database"]
        sort_column = mapping["sort_column"]
        query = f"SELECT * FROM {table_name} ORDER BY {sort_column} DESC LIMIT 10;"

        # Call the run_query function with the correct database
        data, column_names = run_query(query, database_name)
        template_name = f"{content_type}.html"
        return render(request, template_name, {'data': data, 'columns': column_names})
    else:
        # Handle the case where the content type is not recognized
        return render(request, "error.html", {'error': 'Invalid content type'})