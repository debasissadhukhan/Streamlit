import streamlit as st
import time
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

matplotlib.use('TkAgg')
st.title('My first app')
st.write("Here's our first attempt at using data to create a table:")
df = pd.DataFrame({
    'first column': [1, 2, 3, 8],
    'second column': [10, 20, 30, 44]
})
fig, ax = plt.subplots()
sns.lineplot(x='first column', y='second column', data=df, ax=ax)
st.write(fig)
"""  
option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You Selected', option
"""
option = st.sidebar.selectbox(
    'Which number do you like best?',
    df['first column'])

'You selected:', option

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    # Update the progress bar with each iteration.
    latest_iteration.text(f'Iteration {i + 1}')
    bar.progress(i + 1)
    time.sleep(0.1)
