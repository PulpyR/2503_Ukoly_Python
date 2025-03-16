import math

class Locality:
    def __init__(self, name, locality_coefficient):
        self.name = name
        self.locality_coefficient = locality_coefficient

class Property:
    def __init__(self, locality):
        self.locality = locality

from enum import Enum
class Estate_type(Enum):
    LAND = "land"
    BUILDING_SITE = "building site"
    FORREST = "forrest"
    GARDEN = "garden"

class Estate(Property):
    def __init__(self, locality, estate_type, area):
        
        if estate_type not in Estate_type:
            raise ValueError("Špatně zadaný koeficient typu pozemku (estate type)")

        super().__init__(locality)
        self.estate_type = estate_type
        self.area = area
           
    def calculate_tax(self):
        if self.estate_type == "land":
            return self.area * 0.85 * self.locality.locality_coefficient
        elif self.estate_type == "building site":
            return self.area * 9 * self.locality.locality_coefficient
        elif self.estate_type == "forrest":
            return self.area * 0.35 * self.locality.locality_coefficient
        else: #diky enum eliminovany jiné možnosti, zbývá "garden"
            return self.area * 2 * self.locality.locality_coefficient


class Residence(Property):
    def __init__(self, locality, area, commercial: bool):
        super().__init__(locality)
        self.area = area
        self.commercial = commercial
    def calculate_tax(self):
        if self.commercial == False:
            return self.area * self.locality.locality_coefficient * 15
        else:
            return self.area * self.locality.locality_coefficient * 15 *2
    
        
#objekty třídy Locality:
lokalita_1 = Locality("Lokalita 1", 2)
lokalita_Manetin = Locality("Manětín", 0.8)
lokalita_Brno = Locality("Brno", 3)


#objekty třídy Property:
property_1 = Estate(lokalita_1,"forrest", 500)
property_2 = Estate(lokalita_Manetin, "land", 900)
property_3 = Residence(lokalita_Manetin, 120, False)
property_4 = Residence(lokalita_Brno, 90, True)

#výstupy pro jednotlivé nemovitosti
print(f"Daň z nemovitosti property_1 je {math.ceil(property_1.calculate_tax())} Kč")
print(f"Daň z nemovitosti property_2 je {math.ceil(property_2.calculate_tax())} Kč")
print(f"Daň z nemovitosti property_3 je {math.ceil(property_3.calculate_tax())} Kč")
print(f"Daň z nemovitosti property_4 je {math.ceil(property_4.calculate_tax())} Kč")


