import math
from fractions import Fraction


# creates a Mainsequencestar with 0.08 - 50 Solarmasses
def createMainSequenceStar(mass):
    """Creates the properties of a main sequence star with a given Mass in Sunmasses

        Parameters:
        mass(float): Mass of the Star

        Returns:
        dict: properties of the Star

    """
    Star = {'Mass': mass}
    if mass < 1:
        Star['Radius'] = pow(mass, 0.8)
    else:
        Star['Radius'] = pow(mass, 0.5)
    Star['Circumference'] = 2 * math.pi * Star['Radius']
    Star['Area'] = 4 * math.pi * pow(Star['Radius'], 2)
    Star['Volume'] = Fraction(4, 3) * math.pi * pow(Star['Radius'], 3)
    Star['Density'] = Star['Mass'] / Star['Volume']
    Star['Luminosity'] = pow(Star['Mass'], 3.5)
    Star['Surface Temperature'] = pow(Star['Luminosity'] / pow(Star['Radius'], 2), 0.25)*5778
    Star['Lifetime'] = Star['Mass'] / Star['Luminosity'] * 10

    Star['inner Habitable Zone'] = math.sqrt(Star['Luminosity'] / 1.1)
    Star['outer Habitable Zone'] = math.sqrt(Star['Luminosity'] / 0.53)
    for i in Star:
        print(i, Star[i])

    return Star


if __name__ == "__main__":
    import sys
    createMainSequenceStar(float(sys.argv[1]))
