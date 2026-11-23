import Person

class Man(Person.Person):
    ''' A derived class to define Man properties. '''
    
    def speak(self, msg):
        print(self.name, ':\n\tHello!', msg)