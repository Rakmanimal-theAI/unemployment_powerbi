import pandas as pd

# The file is technically an HTML table saved as .xls, so we use read_html
employ = pd.read_html("HLF001101_20260326_013727_85.xls", header=2)[0]

# 1. Clean Unemployment Data (Matrix format -> Long format)
# Rename first column to Date
employ.rename(columns={employ.columns[0]: 'Date'}, inplace=True)

# Drop the last 3 columns (North Island, South Island, Total) and the 4th column (Index 3, redundant header)
cols_to_drop = list(employ.columns[-3:])
if len(employ.columns) > 3:
    cols_to_drop.append(employ.columns[3])
employ.drop(columns=cols_to_drop, inplace=True)

# Melt to long format: Date, Region, Unemployment
df_unemp = employ.melt(id_vars='Date', var_name='Region', value_name='Unemployment %')

# Clean numeric data (convert to number, coerce errors to NaN, then drop empty rows)
df_unemp['Unemployment %'] = pd.to_numeric(df_unemp['Unemployment %'], errors='coerce')
df_unemp.dropna(subset=['Unemployment %'], inplace=True)

CPI = pd.read_excel("graphdata.xlsx", sheet_name="CPI", skiprows=43)
df_cpi = pd.DataFrame({'Date': CPI.iloc[:, 1], 'Inflation': CPI.iloc[:, 2]})

bank_bill = pd.read_excel("graphdata.xlsx", sheet_name="90DAY", skiprows=4)
df_ocr = pd.DataFrame({'Date': bank_bill.iloc[:, 1], 'Interest Rate': bank_bill.iloc[:, 3]})

GDP = pd.read_excel("graphdata.xlsx", sheet_name="GDP", skiprows=4)
df_gdp = pd.DataFrame({'Date': GDP.iloc[:, 1], 'GDP': GDP.iloc[:, 2]})

# 1. Convert all date columns to Datetime and then to Period (Quarterly)
for name, df in [("Unemployment %", df_unemp), ("CPI", df_cpi), ("Interest Rate", df_ocr), ("GDP", df_gdp)]:
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df.dropna(subset=['Date'], inplace=True)
    df['Quarter'] = df['Date'].dt.to_period('Q')
    if not df.empty:
        print(f"{name} Range: {df['Date'].min().date()} to {df['Date'].max().date()} ({len(df)} rows)")
    else:
        print(f"WARNING: {name} is empty after date parsing!")

# 2. Aggregate OCR (Monthly) to Quarterly
# Taking the mean of the months in the quarter to align with other metrics
df_ocr_q = df_ocr.groupby('Quarter', as_index=False)['Interest Rate'].mean()

# 3. Merge to find the common window (Inner Join)
merged = df_unemp[['Quarter', 'Region', 'Unemployment %']].merge(df_cpi[['Quarter', 'Inflation']], on='Quarter', how='inner')
merged = merged.merge(df_ocr_q[['Quarter', 'Interest Rate']], on='Quarter', how='inner')
merged = merged.merge(df_gdp[['Quarter', 'GDP']], on='Quarter', how='inner')

# 4. Format the date as requested: 2000-Q1
merged['Date'] = merged['Quarter'].apply(lambda x: f"{x.year}-Q{x.quarter}")

# Display result
final_df = merged[['Date', 'Unemployment %', 'Inflation', 'Interest Rate', 'GDP', 'Region']]

if not final_df.empty:
    print(final_df.head())
    print(f"Data Window: {final_df['Date'].iloc[0]} to {final_df['Date'].iloc[-1]}")
else:
    print("Merged Data is Empty! Check the date ranges printed above.")

final_df.to_csv("cleaned_unemployed_data.csv")
