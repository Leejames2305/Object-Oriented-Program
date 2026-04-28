# %%
import pandas as pd

# pd.options.display.max_rows = 5
xlsx = pd.ExcelFile('A6-merge.xlsx')

print(type(xlsx))
print(xlsx.sheet_names)


# %%
sr = [1, 2]
sheets = []

for i, s in enumerate(xlsx.sheet_names):
    print(s)
    sheets += [xlsx.parse(s, skiprows=sr[i])]
print(sheets)

print("========== Tidying up ===========")
for s in sheets:
    s['item name'] = s['item name'].str.strip()
print(sheets)

print("========== Extracting Apple Data ===========")
mask = (sheets[0]['item name'] == 'apple')
df_wm = sheets[0][mask]
print(df_wm)


# %%
# Combine transactions for 'apple' in both purchase and sales sheets in 'A6-merge.xlsx' using pd.concat with ignore_index=True, sort=False.
# Store the results in new data frame with rows sorted by date/time
print("=========== Combining Apple Data ===========")
mask_purchase = (sheets[0]['item name'] == 'apple')
mask_sales = (sheets[1]['item name'] == 'apple')
df_purchase = sheets[0][mask_purchase]
df_sales = sheets[1][mask_sales]
df_apple = pd.concat([df_purchase, df_sales], ignore_index=True, sort=False)
df_apple = df_apple.sort_values(by='date/time')
df_apple = df_apple.fillna(0, inplace=False)
print(df_apple)


# %%
