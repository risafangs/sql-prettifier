# imports

import streamlit
import re

# visual start

streamlit.header('Prettier SQL for All!')

# form stuff

label_text = "Paste your SQL into the box below and experience magical transformation."
sql_input = streamlit.text_area(label=label_text)

# stop the screaming
output = sql_input.lower()

# break a large query into small query blocks and store each block by itself
# use select statement to break?

# separate big comma blocks into vertical lists
def split_comma_fields(text):
    text = re.sub(r',\s*', '\n, ', text)
    return text

output = split_comma_fields(output)

# pull out tables and aliases and store them 
def extract_table_aliases(query):
    # Initialize an empty dictionary to store table name and alias
    table_dict = {}

    # use from/join keywords and whitespaces to find table names and their aliases
    # should also optionally look for 'as' keyword and disregard
    pattern = re.compile(r'(?:from|join)\s+(\w+)(?:\s+(?:as\s+)?(\w+))?')

    # Use re.findall() to find all matches of the pattern in the SQL query
    matches = re.findall(pattern, query)

    # Loop through the matches and store the table name and alias in the dictionary
    for match in matches:
        table_name = match[0]
        alias = match[1] if match[1] else table_name
        table_info[alias] = table_name

    return table_dict

# in each query component block, replace use of alias with full table name 

# display output in a code block
streamlit.text('✨🌟✨🌟✨🌟✨🌟✨🌟✨🌟✨🌟✨🌟')
streamlit.code(output, language='sql')
