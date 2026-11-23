import Person
import Man
import Hombre

# Create instances
guy_1 = Man.Man("Richard")
guy_2 = Hombre.Hombre("Diago")

# Adding an additional message into the respective classes method. 
guy_1.speak("It's a beautiful evening.")
guy_2.speak("Es una tarde hermosa.")
print("\n")

# Will output the default msg established in the Person class through the derived instances.
Person.Person.speak(guy_1)
Person.Person.speak(guy_2)