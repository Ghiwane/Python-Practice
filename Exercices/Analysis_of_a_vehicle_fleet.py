import numpy as np

models = np.array(["Tesla Model 3", "Renault Clio", "Peugeot 308", "BMW Serie 3",
                   "Toyota Yaris", "Audi A4", "Ford Fiesta", "Mercedes Classe C",
                   "Volkswagen Golf", "Citroën C3"])

# Kilométrage actuel de chaque véhicule (en km)
mileage = np.array([45000, 120000, 87000, 23000, 156000,
                    61000, 98000, 34000, 142000, 75000])

# Consommation moyenne (en L/100km) — 0 pour les électriques
consumption = np.array([0.0, 5.8, 6.2, 7.1, 4.9,
                        7.8, 5.5, 8.2, 6.0, 5.1])

print (f"The three first models are : {', '.join(map(str, models[:3]))}")

print(f"The mileage of vehicles in even-numbered positions : {', '.join(map(str, mileage[0::2]))}")

print(f"These ones must undergo a vehicle inspection : {', '.join(map(str, models[mileage>100000]))}")

greedy_thermal = (consumption > 7) & (consumption != 0)
print(f"these ones are too greedy : {', '.join(f'{i} : {j}' for i, j in zip(models[greedy_thermal], consumption[greedy_thermal]))}")

mileage[mileage>150000] = 150000
print(f"150,000 km is the administrative limit: {', '.join(map(str, mileage))}" )

print(f"The average of mileage is : {np.mean(mileage):.2f}")

mileage_miles= np.round(mileage*0.621371, 0)
print(f"The mileage in miles : {', '.join(map(str, mileage_miles))}")

efficient_vehicle= (consumption<6) & (mileage < 100000)

print(f"The most effective ones are : {', '.join(models[efficient_vehicle])}")