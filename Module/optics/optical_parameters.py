import numpy as np
import matplotlib.pyplot as plt

class Optical_operation:
    def __init__(self, Lens, Camera, Objet):
        self.Lens = Lens
        self.Camera = Camera
        self.Objet = Objet
    def Field_of_view(self):
        focal = self.Lens[0]
        sensor_size = self.Camera[0]
        aov_x = np.degrees(2*np.arctan(sensor_size[0]/(2*focal)))
        aov_y = np.degrees(2*np.arctan(sensor_size[1]/(2*focal)))   
        return aov_x, aov_y
    def Depth_Of_Field(self):
        focal = self.Lens[0]
        f_number = self.Lens[1]
        confusion_circle = self.Camera[2]
        Hyperfocal = focal**2 / (f_number * confusion_circle)
        object_position = self.Objet[0]
        if object_position[2] < Hyperfocal:
            DOF_=2 * Hyperfocal * object_position[2]**2 / (Hyperfocal**2-object_position[2]**2)
            DN= Hyperfocal*object_position[2]/(Hyperfocal+object_position[2])
            DF=Hyperfocal*object_position[2]/(Hyperfocal-object_position[2])
            return np.round(Hyperfocal, 2), np.round(DOF_, 2), np.round(DN, 2), np.round(DF, 2)
        else:
            DN= Hyperfocal*object_position[2]/(Hyperfocal+object_position[2])
            print('The depth of field is infinite')
            return np.round(Hyperfocal, 2), np.round(DN, 2)

class Inverse_optical_operation:
    def __init__(self, Objet, Camera):
        self.Objet = Objet
        self.Camera = Camera
    def focal_function(self):
        aov_x = self.Objet[3]
        aov_y = self.Objet[4]
        sensor_size = self.Camera[0]
        focal_x = sensor_size[0]/(2*np.tan(np.radians(aov_x[0]-aov_x[1])/2))
        focal_y = sensor_size[1]/(2*np.tan(np.radians(aov_y[0]-aov_y[1])/2))
        return min(np.round(focal_x,1), np.round(focal_y,1))
    def F_number(self):
        confusion_circle = self.Camera[2]
        depth = self.Objet[2]
        object_position = self.Objet[0]
        F_number = self.focal_function()**2 * depth/ (2*confusion_circle * object_position[2] * (object_position[2]+depth))
        return np.round(F_number, 1)