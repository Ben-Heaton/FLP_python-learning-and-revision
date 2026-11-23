import Person

class Hombre(Person.Person):
    ''' A derived class to define Hombre properties. '''
    
    def speak(self, msg):
        print(self.name, ':\n\tHola!', msg)