TwinTowers = 452
MyCityTallestBuilding = int(input("What's the height of your tallest building in metres?:"))
if TwinTowers > MyCityTallestBuilding:
    print("The KL Twin Towers is taller than your building!")
elif TwinTowers == MyCityTallestBuilding:
   print("You must live in KL too!")
else: 
    print("Damn, my city's tallest building is shorter than yours...")
