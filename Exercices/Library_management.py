import pandas as pd

data = {
    "book_id": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "title": ["1984", "Le Petit Prince", "Dune", "L'Étranger", "Fondation",
              "Les Misérables", "Neuromancer", "La Peste", "Hyperion", "Candide"],
    "genre": ["Sci-Fi", "Fiction", "Sci-Fi", "Fiction", "Sci-Fi",
              "Fiction", "Sci-Fi", "Fiction", "Sci-Fi", "Fiction"],
    "borrower_id": [501, 502, 501, 503, 504, 502, 505, 503, 501, 506],
    "days_borrowed": [12, 5, 21, 3, 8, 45, 15, 7, 30, 2],
    "late_fee": [0, 0, 4.5, 0, 0, 22.5, 2.5, 0, 12, 0]
}

# Build the DataFrame and use book_id as the index instead of a default range
library = pd.DataFrame(data, index=data["book_id"])
library = library.drop(columns="book_id")

# Basic overview: shape and first rows
print(library.shape)
print(library.head(5), '\n\n')

# Display a single column as a Series
print(library['title'], '\n\n')

# Count how many books belong to each genre
print(library['genre'].value_counts(), '\n\n')

# Select specific row(s) and column(s) by label using loc
print(library.loc[[105], ['title', 'genre']], '\n\n')

# Select rows/columns by integer position using iloc
print(library.iloc[0:3, 0:2], '\n\n')

# Conditional indexing: keep only Sci-Fi books
sci_fi_books = library[library['genre'] == "Sci-Fi"]
print(sci_fi_books, '\n\n')

# Conditional indexing: keep only books with an outstanding late fee
late_books = library[library['late_fee'] >0]
print(late_books[['title', 'late_fee']], '\n\n')

# Conditional indexing: keep only loans that lasted more than 20 days
borrowed_books = library[library['days_borrowed'] > 20]
print(borrowed_books[['title', 'days_borrowed']], '\n\n')

# Quick descriptive statistics (mean, std, min, max, quartiles) on one column
print("The statistics of the loans : ")
print(library['days_borrowed'].describe(), '\n\n')

# Manually sum a column by looping over its values (Series are iterable)
fee=0
for amount in library["late_fee"]:
    fee += amount
print(f"The total amount of fees collected by the library : {fee}\n\n")

# Accumulate total days borrowed per borrower_id using a dictionary
totals = {}
for i in range(len(library)):
    bid = library['borrower_id'].iloc[i]
    days = library['days_borrowed'].iloc[i]
    if bid in totals:
        totals[bid] += days
    else:
        totals[bid] = days

# Find the borrower with the highest cumulative number of days borrowed
best_borrower = max(totals, key=totals.get)
print(f"Borrower {best_borrower} borrowed {totals[best_borrower]} days in total")