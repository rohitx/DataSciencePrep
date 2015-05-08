def macsong(animal, sound):
    print "Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!"
    print "And on that farm he had a " + animal+", Ee-igh, Ee-igh, Oh!"
    print "With a "+sound+", " +  sound +" here and a "+sound+", "+ sound + " there."
    print "Here a "+sound+", there a "+sound+", everywhere a "+sound+", "+ sound+"."
    print "Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!"
    return ""

animal = ["cow", "pig", "duck", "lamb", "chicks"]
sound = ["moo", "oink", "quack", "baa", "cluck"]


count = 0
while count < 5:
    print macsong(animal[count], sound[count])
    print ""
    count += 1

