from Module import *
import argparse

deck = Deck('./deck.yaml')
Yaml_parameters = deck.doc

Lens_parameters = Yaml_parameters['Lens_data']
Camera_parameters = Yaml_parameters['Camera_data']
Geometrical_parameters = Yaml_parameters['Geometrical_data']
Object_parameters = Yaml_parameters['Object_data']

focal = float(Lens_parameters['focal_mm'])
f_number = float(Lens_parameters['f_number'])

sensor_size_height = float(Camera_parameters['sensor_size_height_mm'])
sensor_size_width = float(Camera_parameters['sensor_size_width_mm'])
confusion_circle = float(Camera_parameters['confusion_circle_mm'])

object_distance = float(Geometrical_parameters['object_distance_mm'])
aov = float(Geometrical_parameters['angle_of_view_deg'])
first_plane = float(Geometrical_parameters['first_sharp_plane_mm'])
second_plane = float(Geometrical_parameters['second_sharp_plane_mm'])

object_position = Object_parameters['Object_position']

test1 = Optical_parameter(focal,f_number,object_distance, sensor_size_height, sensor_size_width, confusion_circle)
print(test1.aov_function())
print(test1.Depth_Of_Field())

test2 = Inverse_optical_parameter(aov, first_plane, second_plane, sensor_size_height, confusion_circle)
print(test2.focal_function())
print(test2.F_number())

test3 = Pinhole_system(object_position,focal)
print(test3.pinhole_model())

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