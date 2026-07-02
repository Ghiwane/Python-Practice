# Streaming Platform Analysis — Part 1 & 2 (Data Cleaning & Merging)

## 📌 Overview
This mini-project simulates a real-world scenario for a streaming platform: cleaning two raw datasets (`users` and `watch history`) and merging them into a single, analysis-ready DataFrame. It's a synthesis exercise covering the core Pandas data-cleaning toolkit.

## 📂 Datasets
- **`users`**: 8 users with `user_id`, `name`, `country`, `subscription` type, and `age`.
- **`watch`**: 12 watch records with `watch_id`, `user_id`, `genre`, `duration_min`, and `rating`.

Both datasets contain missing values (`NaN`), simulating real-world messy data.

## 🧹 Part 1 — Missing Values Handling

| Column | Strategy | Reasoning |
|---|---|---|
| `country` | Filled with **mode** | Categorical variable; the most frequent value is a reasonable default with minimal distortion. |
| `age` | Filled with **median** | Numerical variable; median is more robust to outliers than the mean. |
| `genre` | Filled with `"Unknown"` | Preserves the row while explicitly flagging missing category info. |
| `rating` / `duration_min` | **Dropped** (`dropna`) | These are core numerical variables used for statistical analysis later (Part 5). Imputing them with an arbitrary value (mean/median) would artificially skew those results, unlike filling a categorical field like `country`. |

## 🔗 Part 2 — Merging
- `watch` and `users` are merged on `user_id` using a **left join**, keeping every watch record and enriching it with user information.
- After merging, `full_data.isna().sum()` confirms no unexpected `NaN` values were introduced (which would indicate a `user_id` present in `watch` but missing from `users`).

## 🛠️ Concepts Used
- `isnull()` / `isna()` for missing value detection
- `fillna()` with `mode()` and `median()`
- `dropna()` with `subset` and `how="any"`
- `merge()` with `how="left"`

## ▶️ How to Run
```bash
python streaming_analysis.py
```