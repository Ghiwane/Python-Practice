from Player import Player
from League import League


championship = League("Python Championship")

Ghiwane = Player("Ghiwane", [85, 92, 78], "Gold")
Jimmy = Player("Jimmy", [60, 55, 70], "Bronze")
Messi = Player("Messi", [90, 88, 95], "Gold")
Rose = Player("Rose", [72, 68, 75], "Silver")

print("--- 1. Registering Players ---")
championship.new_player(Ghiwane)
championship.new_player(Jimmy)
championship.new_player(Messi)
championship.new_player(Rose)

print("\n--- 2. Security Test (Duplicate) ---")

championship.new_player(Ghiwane)

print("\n--- 3. Full Ranking ---")
for player in championship.ranking():
    print(player)

print("\n--- 4. Finalists Only ---")
finalists = championship.finalists()
if finalists:
    for f in finalists:
        print(f"- {f.name} ({f.statut()})")
else:
    print("No finalists at the moment.")