import yaml, sys
import numpy as np
import os.path

class Deck():
    def __init__(self, inputhpath):
        if not os.path.exists(inputhpath):
            print("File " + inputhpath)
            sys.exit(1)
        else:
            with open(inputhpath,'r') as f:
                ## Container of the tags parsed from the yaml file
                self.doc = yaml.load(f, Loader=yaml.BaseLoader)
                self.Lens_parameters = self.doc['Lens_data']
                self.Camera_parameters = self.doc['Camera_data']
                self.Geometrical_parameters = self.doc['Geometrical_data']
                self.Object_parameters = self.doc['Object_data']
                self.focal = float(self.Lens_parameters['focal_mm'])
                self.f_number = float(self.Lens_parameters['f_number'])
                self.sensor_size = self.Camera_parameters['sensor_size_mm']
                self.confusion_circle = float(self.Camera_parameters['confusion_circle_mm'])
                self.resolution = self.Camera_parameters['resolution']
                self.Scale_pixel_unit = [np.round(float(self.resolution[0])/float(self.sensor_size[0]), 0), np.round(float(self.resolution[1])/float(self.sensor_size[1]),0)]
                self.t_sensor = [-float(self.sensor_size[0])/2, -float(self.sensor_size[1])/2]
                self.object_distance = float(self.Geometrical_parameters['object_distance_mm'])
                self.aov = float(self.Geometrical_parameters['angle_of_view_deg'])
                self.first_plane = float(self.Geometrical_parameters['first_sharp_plane_mm'])
                self.second_plane = float(self.Geometrical_parameters['second_sharp_plane_mm'])
                self.object_position = self.Object_parameters['Object_position']
                self.Object_size = self.Object_parameters['Object_size_mm']
                self.angle_of_view_x = np.degrees(2*np.arctan((float(self.object_position[0])+float(self.Object_size[0])/2)/float(self.object_position[2]))) - np.degrees(2*np.arctan((float(self.object_position[0])-float(self.Object_size[0])/2)/float(self.object_position[2])))
                self.angle_of_view_y = np.degrees(2*np.arctan((float(self.object_position[1])+float(self.Object_size[1])/2)/float(self.object_position[2]))) - np.degrees(2*np.arctan((float(self.object_position[1])-float(self.Object_size[1])/2)/float(self.object_position[2])))

#faire des class ex: lentille, objet
