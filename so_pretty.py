# imports

import streamlit


# visual start

streamlit.header('Prettier SQL for All!')

# form stuff

label_text = "Paste your SQL into the box below and experience magical transformation."
sql_input = streamlit.text_area(label=label_text)

# stop the screaming
output = sql_input.lower()



# display output in a code block
streamlit.text('✨🌟✨🌟✨')
streamlit.code(output, language='sql')
