# imports

import streamlit


# visual start

streamlit.header('Prettier SQL for All!')
streamlit.text('Paste your ugly all-caps SQL into the box below and experience magical transformation.')

# form
label_text = "You know what to do"
sql_input = streamlit.text_area(label=label_text)

print(sql_input.lower())
