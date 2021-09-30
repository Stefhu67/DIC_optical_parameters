from Module import *
import argparse

deck = Deck('./deck.yaml')
Yaml_parameters = deck.doc

print(deck.Object_size)
print(deck.angle_of_view_x)
print(deck.angle_of_view_y)

test1 = Optical_parameter(deck.focal,deck.f_number,deck.object_distance, deck.sensor_size, deck.confusion_circle)
print(test1.aov_function())
print(test1.Depth_Of_Field())

test2 = Inverse_optical_parameter(deck.angle_of_view, deck.first_plane, deck.second_plane, deck.sensor_size, deck.confusion_circle)
print(test2.focal_function())
print(test2.F_number())

test3 = Pinhole_system(deck.object_position,deck.focal,deck.Scale_pixel_unit,deck.t_sensor)
print(test3.pinhole_model())
print(test3.Trans_image_to_sensor())

'''Lens_parameters = Yaml_parameters['Lens_data']
Camera_parameters = Yaml_parameters['Camera_data']
Geometrical_parameters = Yaml_parameters['Geometrical_data']
Object_parameters = Yaml_parameters['Object_data']

focal = float(Lens_parameters['focal_mm'])
f_number = float(Lens_parameters['f_number'])

sensor_size = Camera_parameters['sensor_size_mm']
confusion_circle = float(Camera_parameters['confusion_circle_mm'])
resolution = Camera_parameters['resolution']
Scale_pixel_unit = [np.round(float(resolution[0])/float(sensor_size[0]), 0), np.round(float(resolution[1])/float(sensor_size[1]),0)]
t_sensor = [-float(sensor_size[0])/2, -float(sensor_size[1])/2]

print(Scale_pixel_unit)

object_distance = float(Geometrical_parameters['object_distance_mm'])
aov = float(Geometrical_parameters['angle_of_view_deg'])
first_plane = float(Geometrical_parameters['first_sharp_plane_mm'])
second_plane = float(Geometrical_parameters['second_sharp_plane_mm'])

object_position = Object_parameters['Object_position']
angle_of_view = np.degrees(2*np.arctan(float(object_position[0])/float(object_position[2])))
'''


'''if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="python main.py -d './mydata/deck.yaml'")

    parser.add_argument("-d", "--mydeck", 
                    action="store",
                    dest="deck",
                    type=str,
                    help="provide the path to your deck file (please see README.md)",
                    default="./deck.yaml",
                    required=True)

    args = parser.parse_args()
    print(args)
    if args.deck:
        try:
            f = open(args.deck)
        except IOError:
            print("The provided path does not seem to exist.")
            sys.exit(1)
        finally:
            f.close()

    test1 = Optical_parameter(50,20,1000)
    print(test1.aov_function())
    print(test1.Depth_Of_Field())

    test2 = Inverse_optical_parameter(7.55, 509.64, 806.45, 1315.79)
    print(test2.focal_function())
    print(test2.F_number())

    test3 = Pinhole_system([8,7,10],50)
    print(test3.pinhole_model())'''