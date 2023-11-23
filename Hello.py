import streamlit as st
import re
import pandas as pd

def count_keyword_occurrences(text, keyword_list):
    # Lowercase the text and the keywords for consistency
    text = text.lower()
    keyword_list = [keyword.lower() for keyword in keyword_list]

    # Count occurrences
    occurrences = {keyword: len(re.findall(r"\b" + re.escape(keyword) + r"\b", text)) for keyword in keyword_list}
    return occurrences

# Function to convert DataFrame to markdown
def df_to_markdown(df):
    markdown = ' | ' + ' | '.join(df.columns) + ' |\n' + ' | ' + ' | '.join(['---'] * len(df.columns)) + ' |\n'
    for index, row in df.iterrows():
        markdown += ' | ' + ' | '.join(str(cell) for cell in row) + ' |\n'
    return markdown

# Title for the app
st.title('Pepper Content \n'
         '### Keyword Frequency Counter')

# Instructions
st.write('Please input your entire article and all the target keywords. '
         'Then hit Submit to analyse the keyword frequency.')

# Creating a text area for the user to input a large piece of text
text_input = st.text_area('Paste your article here:', height=300)

# Creating a text input for the user to enter a list of key phrases separated by commas
keyword_input = st.text_area('Enter the full list of keywords, separated by commas:', height=150)

# Submit button
submit_button = st.button('Submit')

if submit_button:
    # Split keywords by commas and strip whitespace
    keyword_list = [keyword.strip() for keyword in keyword_input.split(',')]

    if text_input and keyword_list:
        # Count occurrences
        occurrences = count_keyword_occurrences(text_input, keyword_list)

        # Convert the dictionary into a pandas DataFrame
        df = pd.DataFrame(list(occurrences.items()), columns=['Keyword', 'Frequency'])

        # Convert the DataFrame to markdown
        markdown_table = df_to_markdown(df)

        # Display results in a Markdown-formatted table
        st.write('Frequency of each key phrase in Markdown format:')
        st.markdown(markdown_table, unsafe_allow_html=True)
    else:
        st.error('Please make sure you have entered the text and keywords.')
