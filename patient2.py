import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load your dataset
data = pd.read_csv('covid.csv')  # Update the path with your dataset's location

state_info_df = pd.read_excel('state_info.xlsx') 

def app():
    st.header('COVID-19 State wise Status')
    select = st.selectbox('Please select a state', data['state'])  # Dropdown menu with state names
    # Filter data based on the selected state
    state_data = data[data['state'] == select]

    st.subheader(f'COVID-19 pandemic in {select}')
    #state_info_text = state_info_df(state_info_df['State']) == [select]['Information'].values
    state_info_text = state_info_df[state_info_df['State'] == select]['Information'].values

    if len(state_info_text) > 0:
        st.write(state_info_text[0])
    else:
        st.write("Information not available for this state.")
    st.write(f'Total population: {state_data["population"].values[0]}')
    st.write(f'Total confirmed cases: {state_data["confirmed"].values[0]}')

    
    # Plotting
    st.subheader('COVID-19 Cases Summary')
    fig, ax = plt.subplots(figsize=(10, 6))
    categories = ['Active', 'Discharged', 'Deaths']
    counts = [state_data['active'].values[0], state_data['passive'].values[0], state_data['deaths'].values[0]]
    ax.bar(categories, counts, color=['blue', 'green', 'red'])
    ax.set_title(f'COVID-19 Cases in {select}')
    ax.set_ylabel('Count')
    st.pyplot(fig)
