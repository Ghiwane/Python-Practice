import pandas as pd
import numpy as np

data = {
    "order_id": [1001, 1002, 1003, 1004, 1005, 1002, 1006, 1007, 1008, 1004],
    "customer": ["Lea", "Karim", "Lea", "Sophie", "Karim", "Karim", "Nadia", "Sophie", "Yanis", "Sophie"],
    "category": ["Electronics", "Clothing", "Electronics", "Books", "Clothing", "Clothing", "Electronics", "Books", np.nan, "Books"],
    "payment_method": ["card", "paypal", "card", "card", "paypal", "paypal", np.nan, "card", "paypal", "card"],
    "amount": [250.0, 45.0, 120.0, 15.5, 45.0, 45.0, 380.0, 22.0, 60.0, 15.5],
    "order_date": ["12-03-2024", "05-03-2024", "28-02-2024", "20-02-2024", "05-03-2024", "05-03-2024", "01-03-2024", "18-02-2024", "22-02-2024", "20-02-2024"]
}

# Build the DataFrame and use order_id as the index
orders = pd.DataFrame(data, index=data["order_id"])
orders = orders.drop(columns="order_id")


# Q1: Check how many fully duplicated rows exist, then drop them keeping the first occurrence
print(f'There is {orders.duplicated().sum()} duplicates')
orders = orders.drop_duplicates(keep='first')


# Rebuild a sortable date string in "YYYY-MM-DD" format from "DD-MM-YYYY"
orders['sortable_date'] = orders['order_date'].apply(lambda x: x.split('-')[2] + '-' + x.split('-')[1] + '-' + x.split('-')[0])
# Now sorting is chronologically correct; descending + keep='first' gives the most recent order per customer
print(orders.sort_values(by='sortable_date', ascending=False).drop_duplicates(subset='customer', keep='first'))
orders = orders.drop(columns='sortable_date')  # cleanup, we don't need it anymore


# Q3: Fill missing values in payment_method and category
orders['payment_method'] = orders['payment_method'].replace(np.nan, 'unknow')
orders['category'] = orders['category'].replace(np.nan, 'Other')
print(orders, "\n\n")


# Q4: Rename columns for consistency
orders = orders.rename({'payment_method': 'payment', 'order_date': 'date'}, axis=1)
print(orders, '\n\n')


# Q5: Split the date string into day, month, year columns using lambda + split
orders['day'] = orders['date'].apply(lambda x: x.split('-')[0])
orders['month'] = orders['date'].apply(lambda x: x.split('-')[1])
orders['year'] = orders['date'].apply(lambda x: x.split('-')[2])
orders = orders.drop('date', axis=1)  # original date column no longer needed
print(orders, '\n\n')


# Q6: Count orders made in February using conditional indexing
nb_february = orders[orders['month'] == '02']
print(f"There is {len(nb_february)} orders in february\n\n")


# Q7: Create a new column classifying orders as 'high' or 'low' based on amount, row by row
orders['amount_category'] = orders["amount"].apply(lambda x: 'high' if x > 100.0 else 'low')
print(orders, '\n\n')


# Q8: Total amount spent per customer, then find the top spender — using groupby
# groupby('customer') groups all rows sharing the same customer value together
# ['amount'].sum() then sums the amount column within each group
totals_per_customer = orders.groupby('customer')['amount'].sum()
print(totals_per_customer, '\n\n')


# Q9: Descriptive statistics of amount, restricted to 'high' orders only
print(orders[orders["amount_category"] == 'high'].describe())