import pandas as pd
import pandas_gbq

df = pd.read_csv('data.csv', encoding='cp1252')

# Sjednocení formátu StockCode a Description
df['StockCode'] = df['StockCode'].astype(str).str.upper()
df['Description'] = df['Description'].str.upper().str.strip()
df['Description'] = df['Description'].str.strip()

# Pokud řádek nemá název, pokusíme se ho doplnit z jiných řádků se stejným StockCode (pokud se žádný název nenajde, změníme z None na 'UNKNOWN')
mapping = df.dropna(subset=['Description']).drop_duplicates('StockCode')
mapping = mapping.set_index('StockCode')['Description']
df['Description'] = df['Description'].fillna(df['StockCode'].map(mapping))
df['Description'] = df['Description'].fillna('UNKNOWN')

# Vyplnění chybějících hodnot v CustomerID nulou (neregistrovaní zákazníci)
df['CustomerID'] = df['CustomerID'].fillna(0)

# Pokud InvoiceNo začíná na 'C', znamená to, že se jedná o stornovaný doklad, a tyto řádky odstraníme
df['InvoiceNo'] = df['InvoiceNo'].astype(str)
df = df[~df['InvoiceNo'].str.startswith('C')]

# Odstranění řádků s nulovým nebo záporným množstvím (Quantity) a cenou (UnitPrice)
df = df[df['Quantity'] > 0]
df = df[df['UnitPrice'] > 0]

# Sjednocení názvů zemí a odstranění nejasných záznamů
df['Country'] = df['Country'].replace('RSA', 'South Africa')
df['Country'] = df['Country'].replace('EIRE', 'Ireland')
df = df[~df['Country'].isin(['Unspecified', 'European Community'])]

# Převod InvoiceDate na datetime a vytvoření nových sloupců pro rok, měsíc, den v týdnu a hodinu
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
df['Year'] = df['InvoiceDate'].dt.year
df['Month'] = df['InvoiceDate'].dt.month
df['DayOfWeek'] = df['InvoiceDate'].dt.day_name()
df['Hour'] = df['InvoiceDate'].dt.hour

# Vytvoření sloupce TotalSum jako součin Quantity a UnitPrice, zaokrouhleného na 2 desetinná místa
df['TotalSum'] = df['Quantity'] * df['UnitPrice']
df['TotalSum'] = df['TotalSum'].round(2)

# Převod datových typů pro optimalizaci a kompatibilitu s Google BigQuery
df['InvoiceNo'] = df['InvoiceNo'].astype(str)
df['StockCode'] = df['StockCode'].astype(str)
df['Description'] = df['Description'].astype(str)
df['Quantity'] = df['Quantity'].astype(int)
df['UnitPrice'] = df['UnitPrice'].astype(float)
df['CustomerID'] = df['CustomerID'].fillna(0).astype(int)
df['Country'] = df['Country'].astype(str)
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
df['Year'] = df['Year'].astype(int)
df['Month'] = df['Month'].astype(int)
df['DayOfWeek'] = df['DayOfWeek'].astype(str)
df['Hour'] = df['Hour'].astype(int)
df['TotalSum'] = df['TotalSum'].astype(float)

# Nahrání dat do Google BigQuery    

project_id = 'sqltest-489613' 
dataset_table = 'ecommerce_analysis.sales' 

pandas_gbq.to_gbq(df, dataset_table, project_id=project_id, if_exists='replace')

print(f"✅ Data byla úspěšně nahrána do BigQuery do tabulky {dataset_table}")








