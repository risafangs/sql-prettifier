# imports

import streamlit


# visual start

streamlit.header('Prettier SQL for All!')
streamlit.text('Paste your ugly all-caps SQL into the box below and experience magical transformation.')

# form
sql_input = streamlit.text_area(sql_input, placeholder="Input query text here", label_visibility=hidden)

