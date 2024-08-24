print("Give mass in talent, lots,pounds")
talents=float(input("then give talents"))
lots=float(input("then give lots "))
pounds=float(input("then give pounds "))

lotsInGR=13,3
poundInGR = 32*lotsInGR
talentsInGR = 20*poundInGR

mass =talents* lotsInGR +pounds*poundInGR+lotsInGR+pounds*poundInGR

Kg=int(mass//1000)
grams= mass%1000
print("")
print(str(Kg)+"kilograms and " + str(round(grams,2))+"grams")
print(f{Kg} kilogrms and {grams:.2f} grams")"
