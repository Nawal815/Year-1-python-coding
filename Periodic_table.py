#Periodic table program

#----------------------
#Subprograms
#----------------------
def periodic_table(element):
    match element:
        #Alkali metals:
        #Lithium
        case "Li" | "lithium":
            print("Symbol: Li")
            print("Element: Lithium")
            print("Atomic weight: 6.94")
            print("Group: Alkali metals")
        #Sodium
        case "Na" | "sodium":
            print("Symbol: Na")
            print("Element: Sodium")
            print("Atomic weight: 22.99")
            print("Group: Alkali metals")
        #Potassium
        case "K" | "potassium":
            print("Symbol: K")
            print("Element: Potassium")
            print("Atomic weight: 39.098")
            print("Group: Alkali metals")
        #Halogens:
        #Flourine
        case "F" | "flourine":
            print("Symbol: F")
            print("Element: Flourine")
            print("Atomic weight: 18.998")
            print("Group: Halogens")
        #Chlorine
        case "Cl" | "chlorine":
            print("Symbol: Cl")
            print("Element: Chlorine")
            print("Atomic weight: 35.45")
            print("Group: Halogens")
        #Bromine
        case "Br" | "bromine":
            print("Symbol: Br")
            print("Element: Bromine")
            print("Atomic weight: 79.904")
            print("Group: Halogens")
        #Any other element
        case _:
            print("Element is not in the catalogue.")
        

#----------------------
#Main Program
#----------------------
lookup = input("ENter the symbol or name of an element:")
periodic_table(lookup)

