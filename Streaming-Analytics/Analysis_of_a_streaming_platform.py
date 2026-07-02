import pandas as pd
import numpy as np

# --- Dataset 1 : users ---
users_data = {
    "user_id": [1, 2, 3, 4, 5, 6, 7, 8],
    "name": ["Nora", "Ilyes", "Salma", "Yanis", "Amel", "Karim", "Lina", "Bilal"],
    "country": ["FR", "DZ", np.nan, "FR", "DZ", "FR", np.nan, "DZ"],
    "subscription": ["premium", "free", "premium", "free", "premium", "free", "premium", "free"],
    "age": [24, 31, np.nan, 19, 45, 28, 22, np.nan]
}

# --- Dataset 2 : viewing history ---
watch_data = {
    "watch_id": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112],
    "user_id": [1, 2, 1, 3, 4, 5, 1, 6, 7, 2, 8, 3],
    "genre": ["Sci-Fi", "Comedy", "Sci-Fi", "Drama", "Comedy", "Drama",
              "Action", "Comedy", "Sci-Fi", "Comedy", "Action", np.nan],
    "duration_min": [45, 22, 50, 90, 25, 105, 40, 20, 48, np.nan, 33, 88],
    "rating": [8.5, 6.0, 9.0, 7.5, 5.5, np.nan, 8.0, 6.5, 7.0, 6.2, np.nan, 7.8]
}

users = pd.DataFrame(users_data)
watch = pd.DataFrame(watch_data)

# Count missing values per column in each DataFrame
missing_users = users.isnull().sum(axis=0)
missing_watch = watch.isnull().sum(axis=0)
print('missing values per column in users :\n', missing_users, '\n\n')
print('missing values per column in watch :\n', missing_watch, '\n\n')

# Fill missing 'country' with the most frequent value (mode)
users["country"] = users["country"].fillna(users["country"].mode()[0])
# Fill missing 'age' with the median (robust to outliers, unlike the mean)
users['age'] = users["age"].fillna(users["age"].median())

# Fill missing 'genre' with an explicit "Unknown" category
watch['genre'] = watch["genre"].fillna("Unknown")

# Replacing a score or duration with an arbitrary value (mean/median) would skew the analysis statistics
# whereas replacing a missing country with the mode has a minimal impact on the overall results.
# So instead of filling, we drop rows where 'rating' or 'duration_min' is missing.
watch = watch.dropna(axis=0, how="any", subset=["rating", "duration_min"])

# Left join: keep every watch record, and attach user info where available
full_data = watch.merge(right=users, on='user_id', how='left')

# Check for any NaNs introduced by the merge
missing = full_data.isna().sum()
print(missing)