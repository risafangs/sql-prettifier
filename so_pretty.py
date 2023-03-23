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

# separate big comma blocks into vertical lists
def split_comma_fields(text):
    text = re.sub(r',\s*', '\n, ', text)
    return text

output = split_comma_fields(output)

# display output in a code block
streamlit.text('✨🌟✨🌟✨🌟✨🌟✨🌟✨🌟✨🌟✨🌟')
streamlit.code(output, language='sql')
