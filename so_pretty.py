# imports

import streamlit


# visual start

streamlit.header('Prettier SQL for All!')
streamlit.text('Paste your ugly all-caps SQL into the box below and experience magical transformation.')

# form
input_form = streamlit.form("ugly_sql")
input_form.slider("Inside the form")
streamlit.slider("Outside the form")

# Now add a submit button to the form:
input_form.form_submit_button("submit")
