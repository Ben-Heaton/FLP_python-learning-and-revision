import Songbird

bird_1 = Songbird.Songbird("Koko", "I'm Koko!")
print(bird_1.name, "ID", id(bird_1))
bird_1.sing()

bird_2 = Songbird.Songbird("Poko", "I'm Poko!")
print(bird_2.name, "ID", id(bird_2))
bird_2.sing()

bird_3 = Songbird.Songbird("Loko", "I'm Loko!")
print(bird_3.name, "ID", id(bird_3))
bird_3.sing()

# Not scrictly necessery here as when the interptretor shuts down, __del__ is called.
del bird_1
del bird_2
del bird_3