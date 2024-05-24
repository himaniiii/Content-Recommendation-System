import sqlparse
from sqlparse.sql import Where, IdentifierList, Identifier, Token
from sqlparse.tokens import Keyword, DML, Wildcard
import mysql.connector

def set_table_column_mappings(query):
    if "Movie_TV_Data" in query:
        return {
            "imdb_movie_data": ["Rank", "Title" ,"Genre", "Release_Year", "Rating", "Votes"],
            "tv": ["Title","Rating", "Age", "Release_Year", "Netflix", "Hulu", "Prime", "Disney"]
        }
    elif "Series_Info" in query:
        return {
            "action_series": ["Title","Rating", "Number_of_votes", "Release_Year"],
            "adventure_series": ["Title", "Rating", "Number_of_votes", "Release_Year"],
            "animation_series": ["Title", "Rating", "Number_of_votes", "Release_Year"]
        }
    elif "Social_Media_Info" in query:
        return {
            "instagram": ["Rank","Influence_Score", "Followers", "ChannelInfo", "TotalLikes"],
            "youtube": ["Rank","Youtuber","Subscribers", "Video_Views", "Category","Created_Year"]
        }
    else:
        return {}

def identify_components(parsed_query, table_column_mapping):
    components = {table: {"columns": [], "conditions": []} for table in table_column_mapping}
    in_select = False
    select_all = False

    for token in parsed_query.tokens:
        if token.ttype is DML and token.value.upper() == 'SELECT':
            in_select = True
        elif token.ttype is Keyword and token.value.upper() in ['FROM', 'WHERE']:
            in_select = False

        if in_select:
            if isinstance(token, IdentifierList):
                for identifier in token.get_identifiers():
                    if isinstance(identifier, Token) and identifier.ttype is Wildcard:
                        select_all = True
                        break
                    col_name = identifier.get_name()
                    for table, cols in table_column_mapping.items():
                        if col_name in cols:
                            components[table]["columns"].append(col_name)
            elif isinstance(token, Identifier):
                if token.ttype is Wildcard:
                    select_all = True
                    break
                col_name = token.get_name()
                for table, cols in table_column_mapping.items():
                    if col_name in cols:
                        components[table]["columns"].append(col_name)

            if select_all:
                for table in components:
                    components[table]["columns"] = table_column_mapping[table]
                break

        if isinstance(token, Where):
            where_conditions = str(token)
            for table, cols in table_column_mapping.items():
                for col in cols:
                    if col in where_conditions:
                        components[table]["conditions"].append(where_conditions)
                        break

    return components

def get_connection(database_name):
    try:
        return mysql.connector.connect(
            host='localhost',
            user='root',
            password='Himani@12',
            database=database_name
        )
    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

def execute_query(query, database_name):
    connection = get_connection(database_name)
    if connection is not None:
        try:
            cursor = connection.cursor()
            cursor.execute(query)
            results = cursor.fetchall()
            cursor.close()
            connection.close()
            return results
        except mysql.connector.Error as e:
            print(f"Error executing query: {e}")
            return []
    else:
        return []
    
def build_query(global_table):
   
    column_names = input("Enter the columns you want to search, use '*' for all columns or list them separated by commas: ")
    conditions = input("Enter any conditions for the 'WHERE' clause (e.g., 'Age = 8 and Category = \'PG'\'), or leave blank if none: ")

    if column_names.strip() == '*':
        column_names = "*"

    query = f"SELECT {column_names} FROM {global_table}"
    if conditions:
        query += f" WHERE {conditions}"

    return query

global_table = input("Enter the global table you want to search in: ")
query = build_query(global_table)
parsed = sqlparse.parse(query)[0]
table_column_mapping = set_table_column_mappings(global_table)
components = identify_components(parsed, table_column_mapping)

sub_queries = []
for table, details in components.items():
    if details["columns"]:
        select_clause = ", ".join(details["columns"])
        where_clause = " AND ".join(details["conditions"]) if details["conditions"] else ""
        sub_query = f"SELECT {select_clause} FROM {table} {where_clause}"
        sub_queries.append(sub_query)

combined_results = []
for i, sub_query in enumerate(sub_queries, start=1):
    results = execute_query(sub_query, 'iia')
    combined_results.extend(results)
    print(f"Results for Sub-Query {i}:", results)

print("Combined Results:", combined_results)
