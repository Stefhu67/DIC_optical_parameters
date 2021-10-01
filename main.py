from Module import *
import argparse

deck = Deck('./deck.yaml')
Yaml_parameters = deck.doc

Lens = lens(deck.focal, deck.f_number).lens_parameters()
Camera = camera(deck.sensor_size, deck.resolution, deck.confusion_circle).camera_parameters()
Objet = objet(deck.object_position, deck.object_size, deck.object_depth).object_parameter()

print(Lens)
print(Camera)
print(Objet)

test = Optical_operation(Lens,Camera,Objet)
print(test.Field_of_view())
print(test.Depth_Of_Field())

test1 = Inverse_optical_operation(Objet, Camera)
print(test1.focal_function())
print(test1.F_number())

'''
test3 = Pinhole_system(deck.object_position,deck.focal,deck.Scale_pixel_unit,deck.t_sensor)
print(test3.pinhole_model())
print(test3.Trans_image_to_sensor())'''