#This is the better way to import because it reduces pageload.
from ascii import one, two
print(one())
print(two())

from art.pictures import three, four
print(three())
print(four())

from art.even_more_art.images import five
print(five())

from scene import six
print(six())



#This is the worst way to import because you're importing everything, so it increases pageload.
# import ascii
# print(ascii.one())
# print(ascii.two())

# import art.pictures
# print(art.pictures.three())
# print(art.pictures.four())

# import art.even_more_art.images
# print(art.even_more_art.images.five())

# import scene
# print(scene.six())