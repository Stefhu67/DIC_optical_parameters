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
                self.focal = self.Lens_parameters['focal_mm']
                self.f_number = self.Lens_parameters['f_number']

                self.Camera_parameters = self.doc['Camera_data']
                self.sensor_size = self.Camera_parameters['sensor_size_mm']
                self.resolution = self.Camera_parameters['resolution']
                self.confusion_circle = self.Camera_parameters['confusion_circle_mm']

                self.Object_parameters = self.doc['Object_data']
                self.object_position = self.Object_parameters['Object_position']
                self.object_size = self.Object_parameters['Object_size_mm']
                self.object_depth = self.Object_parameters['Object_depth_mm']