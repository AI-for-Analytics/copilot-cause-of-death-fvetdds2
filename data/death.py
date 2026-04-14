import pandas as pd
df = pd.read_excel("data/LCD_byRegionSex_2019.xlsx", sheet_name="DAVIDSON", skiprows=2, engine="openpyxl" )
# clean up rows with missing data
df = df.dropna(subset=["DAVIDSON"])
#reset index
df = df.reset_index(drop=True)
print(df.shape)
