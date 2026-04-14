# Data Cleaning with Copilot

For this exercise, use Copilot suggestions to help complete each step.

Note that sometimes Copilot has multiple suggestions, and you can cycle through them by using Alt+[ or Alt+] on Windows or Option+[ or Option+] on Mac.

Our overall goal in this exercise is to read in and reshape the data contained in the LCD_byRegionSex_2019.xlsx spreadsheet in the data folder of this repository, which has information about leading causes of death by region.

1. Start by reading in the data for the DAVIDSON region (the first sheet). You may need to open the spreadsheet to see where the data is contained. Try adding comments before you attempt to read the data in to get suggestions about how to deal with the sheet format.

2. Make sure that all rows contain data, and if not, clean them up.

3. Create more descriptive column names. Hint: name your columns <Group>_<Measure> (eg. "Male_Rate"). Have Copilot help you create a for loop to create a list of new column names.

4. Make a side-by-side bar chart that compares the rates of death for males vs. females. To do this, you could select the Male_Rate and Female_Rate columns, melt the DataFrame, and create your plot. You may want to use seaborn to help with this.

5. Now, create a function to read in the data for a different region and repeat the cleaning steps that you did above. Note that not all regions have the same number of rows, so you may need to adjust your code to deal with this. Hint: If you read in too many rows, you can drop those that have NaN in the Total_Rank column.





6. Finally, read in the data across all of the regions to create one DataFrame containing everything.

   <img width="1591" height="790" alt="image" src="https://github.com/user-attachments/assets/fe6a3551-1b7b-4f0b-8e8e-504685caecaa" />

