import numpy as np

artists = np.array(["Drake", "Taylor Swift", "Kendrick Lamar", "Billie Eilish",
                    "The Weekend", "Doja Cat", "Post Malone", "Olivia Rodrigo",
                    "Bad Bunny", "SZA"])

# Streams (in millions) per artist over the last 6 months
# Each row = 1 artist, each column = 1 month
streams = np.array([
    [320, 280, 300, 410, 390, 450],
    [210, 390, 420, 380, 310, 500],
    [180, 200, 175, 220, 260, 300],
    [150, 160, 190, 210, 175, 220],
    [400, 370, 350, 330, 410, 480],
    [120, 140, 165, 180, 200, 175],
    [230, 210, 195, 220, 240, 260],
    [175, 190, 210, 230, 195, 215],
    [350, 320, 380, 410, 440, 390],
    [140, 165, 180, 200, 220, 195]
])

# Royalty rate per stream (in euro cents)
rate = np.array([0.4, 0.35, 0.42, 0.38, 0.41, 0.36, 0.39, 0.37, 0.40, 0.43])

print(f"The dimension of [streams] is : {streams.shape}")

# Flatten the 2D streams array into a single 1D vector
streams_flat = streams.reshape(60,)
print(f"The dimension of [streams_flat] is : {streams_flat.shape}")

# Sum streams across months (axis=1) to get each artist's 6-month total
streams_6months = streams.sum(axis=1)
print(f"The most listened to is : {artists[streams_6months.argmax()]}")
print(f"The least listened to is : {artists[streams_6months.argmin()]}")

# Average streams per month across all artists (axis=0)
average_per_month = streams.mean(axis=0).round(2)
print(f"The month with the most listens is month n°{average_per_month.argmax()+1}")

# Total revenue per artist = total streams × royalty rate (in euro cents)
revenues = streams_6months * rate
print(f"The artist who generated the most revenue is : {artists[revenues.argmax()]} with {(revenues.max()/100).round(2)}M euros")

# Build a 2-column table: [total streams, revenue] then filter artists above 1500M streams
tab = np.array([streams_6months, revenues]).T
tab = tab[(tab[:,0] > 1500)]
print(f"The artists with the most streams are : {'\n'.join(f'{i} - revenues : {j/100}M ' for i, j in zip(artists[streams_6months > 1500], tab[:,1]))}")