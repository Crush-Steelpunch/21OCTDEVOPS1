## Classes
#
#class Keyword:
#
#    attribute = 'data in'
#
#    def funcname():
#        pass #code here


class Dog:

    def __init__(self,energy="high"):
        self.energy = energy

    def printtheattr(self):
        print(energy)
        print(self.energy)

    def speak(self):
        print('Woof')


energy = 'this is a var'


havoc = Dog('hypermanic')
print(havoc.energy)
havoc.speak()

clifford = Dog()
print(clifford.energy)
clifford.speak()

clifford.printtheattr()

# login example class

#class login():
#
#    username = 'user'
#    password = 'passwd'
#    url = 'url'
#
#    def getloginofcloud():
#        pass

