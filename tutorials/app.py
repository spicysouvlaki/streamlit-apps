import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd

st.title("my first app")

st.write("here's our first dataframe")

df = pd.DataFrame({
        "first": [1,2,3,4],
        "second": [10 * x for x in [1,2,3,4]],

})

# this is equivalent
st.write(df)
# to this (with the right opts turned on)
df


chart_data = pd.DataFrame(
    np.random.rand(20,3),
    columns=['a','b','c']
)

st.line_chart(chart_data)


"""
everything as pretty straightforwad up to here.

This was some crazy black magic. I totally did not expect that
to actually happen.

I expected that mapping data onto san francisco would be
much much more difficult.


// mapping these doc strings is pretty annoying
"""
if st.checkbox('show datafram'):
    map_data = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
        columns=['lat', 'lon'])

    st.map(map_data)


option = st.selectbox(
    'Whic number do you lik e best?',
    df['first']
)

'You slected: ', option

import time

'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'
