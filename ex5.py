#More Variables program 1.1
#By Yonaton 2/26/17

#Define Variables
name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74.0 # inches
height_ft = round(height / 12.0) # feet
height_cm = round(height * 2.54) # centimeters
weight = 180.0 # lbs
weight_kg = weight * 0.45 # Kili=ograms
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

#Main Output
print "Let's talk about %s." % name
print "He's %s inches tall." % height
print "He's %s feet tall." % height_ft
print "He's %s centimeters tall." %height_cm
print "He's %s pounds heavy." % weight
print "He'd %s kilograms heavy." % weight_kg
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    age, height, weight, age + height + weight)
