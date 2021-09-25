import numpy as np
import matplotlib.pyplot as plt

class Optical_parameter:
    def __init__(self, focal, f_number, distance_object, sensor_size, confusion_circle):
        self.focal = focal
        self.f_number = f_number
        self.distance_object = distance_object
        self.sensor_size = sensor_size
        self.confusion_circle = confusion_circle

    def aov_function(self): 
        aov_height = np.degrees(2*np.arctan(float(self.sensor_size[0])/(2*self.focal)))
        aov_width = np.degrees(2*np.arctan(float(self.sensor_size[1])/(2*self.focal)))
        return np.round(aov_height,2) , np.round(aov_width,2)
    
    def Depth_Of_Field(self):
        Hyperfocal = self.focal**2 / (self.f_number * self.confusion_circle)
        if self.distance_object < Hyperfocal:
            DOF_=2 * Hyperfocal * self.distance_object**2 / (Hyperfocal**2-self.distance_object**2)
            DN= Hyperfocal*self.distance_object/(Hyperfocal+self.distance_object)
            DF=Hyperfocal*self.distance_object/(Hyperfocal-self.distance_object)
            return np.round(Hyperfocal, 2), np.round(DOF_, 2), np.round(DN, 2), np.round(DF, 2)
        else:
            DN= Hyperfocal*self.distance_object/(Hyperfocal+self.distance_object)
            print('The depth of field is infinite')
            return np.round(Hyperfocal, 2), np.round(DN, 2)


class Inverse_optical_parameter:
    def __init__(self, aov, first_plane, second_plane, sensor_size, confusion_circle):
        self.aov = aov
        self.first_plane = first_plane
        self.second_plane = second_plane
        self.sensor_size = sensor_size
        self.confusion_circle = confusion_circle
    def focal_function(self):
        focal = float(self.sensor_size[0])/(2*np.tan(np.radians(self.aov)/2))
        return np.round(focal,1)
    def F_number(self):
        F_number = self.focal_function()**2 * (self.second_plane-self.first_plane)/ (2*self.confusion_circle * self.first_plane * self.second_plane)
        return np.round(F_number, 1)

'''test1 = Optical_parameter(50,20,1000)

print(test1.Depth_Of_Field())

test2 = Inverse_optical_parameter(7.55, 509.64, 806.45, 1315.79)
print(test2.focal_function())
print(test2.F_number())'''