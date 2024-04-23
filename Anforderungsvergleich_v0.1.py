from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt

filename1 = filedialog.askopenfilename()
df1 = pd.read_excel(filename1)
filename2 = filedialog.askopenfilename()
df2 = pd.read_excel(filename2)

merged_df = pd.merge(df2, df1, on='Projektnummer', how='left', indicator=True)
new_entries = merged_df[merged_df['_merge'] == 'left_only'][['Projektnummer', 'Projektbezeichnung_x']]
new_entries.columns = ['Projektnummer', 'Projektbezeichnung']

print("New Entries:")
print(new_entries)
print("Here is a Change in Fork 1")

output_excel_path = "new_entries.xlsx"
new_entries.to_excel(output_excel_path, index=False)
print(f"\nResult exported to {output_excel_path}")

input("Press Enter to exit...")
