import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pandas_profiling import ProfileReport

import steamlit as st

st.header("Analysis to Excel files  ")

june_file = pd.read_excel("June_Report.xlsx")
may_file = pd.read_excel("MaY_Report.xlsx")

st.header("June Report")
st.write(june_file)

st.header("May Report")
st.write(may_file)

st.line_chart(june_file)

st.line_chart(may_file)