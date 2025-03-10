# In jupyter notebook the library DataPrep is taking too much time to load/install.
# But DataPrep lib is working fine in VS Code editor.

import pandas as pd

# !pip install --upgrade pip    ----> running in terminal
# !pip install dataprep         ----> running in terminal

from dataprep.eda import create_report

# Example dataset (replace with your actual DataFrame)
df = pd.read_csv("Spotify_data.csv")

report = create_report(df)
report.show()  
report.save("data_prep_report.html")

# Generate EDA report
report = create_report(df)
report.save("eda_report.html")  # Report has been saved to eda_report.html!

create_report(df).show_browser()














