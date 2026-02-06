def main():
      userMass = input("Input a mass (kg): ")
      
      parsedMass = int(userMass)
      
      print(calculateEnergy(parsedMass))
      

def calculateEnergy(mass):
      speedOfLight = 300000000
      
      energy = mass * speedOfLight * speedOfLight
      
      return energy


main()