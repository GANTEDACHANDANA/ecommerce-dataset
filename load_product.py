import pandas as pd
import sqlite3

# Step 1: Load the CSV
df = pd.read_csv('archive/products.csv')  # make sure path matches

# Step 2: Connect to SQLite DB
conn = sqlite3.connect('ecommerce.db')
cursor = conn.cursor()

# Step 3: Create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,
    cost REAL,
    category TEXT,
    name TEXT,
    brand TEXT,
    retail_price REAL,
    department TEXT,
    sku TEXT,
    distribution_center_id INTEGER
)
''')

# Step 4: Load CSV into DB
df.to_sql('products', conn, if_exists='replace', index=False)

# Step 5: Verify the data
cursor.execute('SELECT COUNT(*) FROM products')
print("✅ Total products loaded:", cursor.fetchone()[0])

print("🧾 Sample rows:")
for row in cursor.execute('SELECT * FROM products LIMIT 5'):
    print(row)

conn.close()
