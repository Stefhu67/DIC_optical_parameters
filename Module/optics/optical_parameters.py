import numpy as np
import matplotlib.pyplot as plt

class Optical_parameter:
    def __init__(self, focal, f_number, distance_object, sensor_size_height, sensor_size_width, confusion_circle):
        self.focal = focal
        self.f_number = f_number
        self.distance_object = distance_object
        self.sensor_size_height = sensor_size_height
        self.sensor_size_width = sensor_size_width
        self.confusion_circle = confusion_circle

    def aov_function(self): 
        aov_height = np.degrees(2*np.arctan(self.sensor_size_height/(2*self.focal)))
        aov_width = np.degrees(2*np.arctan(self.sensor_size_width/(2*self.focal)))
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
        focal = self.sensor_size/(2*np.tan(np.radians(self.aov)/2))
        return np.round(focal,1)
    def F_number(self):
        F_number = self.focal_function()**2 * (self.second_plane-self.first_plane)/ (2*self.confusion_circle * self.first_plane * self.second_plane)
        return np.round(F_number, 1)


'''test1 = Optical_parameter(50,20,1000)

print(test1.Depth_Of_Field())

test2 = Inverse_optical_parameter(7.55, 509.64, 806.45, 1315.79)
print(test2.focal_function())
print(test2.F_number())'''


'''def aov_function(focal, sensor_size_height = 6.6, sensor_size_width = 8.8):  #6.6x8.8mm2, 2/3inch sensor format GH3
    aov_height = np.degrees(2*np.arctan(sensor_size_height/(2*focal)))
    aov_width = np.degrees(2*np.arctan(sensor_size_width/(2*focal)))
    return np.round(aov_height,2) , np.round(aov_width,2)

def focal_function(aov, sensor_size = 6.6):
    focal = sensor_size/(2*np.tan(np.radians(aov)/2))
    return focal

def Depth_Of_Field(focal, f_number, distance_object, confusion_circle = 0.03):  #distance_object a definir en mm
    Hyperfocal = focal**2 / (f_number * confusion_circle)
    if distance_object < Hyperfocal:
        DOF_=2 * Hyperfocal * distance_object**2 / (Hyperfocal**2-distance_object**2)
        DN= Hyperfocal*distance_object/(Hyperfocal+distance_object)
        DF=Hyperfocal*distance_object/(Hyperfocal-distance_object)
        return np.round(Hyperfocal, 2), np.round(DOF_, 2), np.round(DN, 2), np.round(DF, 2)
    else:
        print('not possible')
        return np.round(Hyperfocal, 2)

def F_number(focal, DOF, first_plane, second_plane, confusion_circle = 0.03):
    F_number = focal**2 * DOF / (2*confusion_circle * first_plane * second_plane)
    return np.round(F_number, 2)

def pinhole_model(x_object, y_object, z_object, focal):
    P = np.array([[focal, 0, 0, 0],[0, focal, 0, 0],[0, 0, 1, 0]])
    Object_coordinates = np.array([[x_object], [y_object], [z_object], [1]])
    image_matrix = P.dot(Object_coordinates)
    scale_factor = float(image_matrix[2])
    return   float(image_matrix[0]) / scale_factor,  float(image_matrix[1]) / scale_factor, scale_factor

pinhole = pinhole_model(80, 70, 1000, 50)
print(pinhole)'''

'''angle_view = aov_function(50)
print(angle_view)

focal_50 = focal_function(7.55)
print(focal_50)

DOF_ouverture20 = Depth_Of_Field(50, 20, 1000)  
print(DOF_ouverture20)

aperture_50 = F_number(50, 509.34, 806.45, 1315.79)
print(aperture_50)'''

'''
list_focal =[18,24,35,55,70,100,135,200,250] #focal en mm
list_aperture = [4, 4.5, 5, 5.6, 6.3, 6.7, 7.1, 8, 9, 9.5, 10, 11, 13, 14, 16, 18, 19, 20, 22, 25, 27] # 21 apertures
list_aov = []
list_DOF = []

for i in list_focal:
    list_aov.append(aov_function(i))
    dof = DOF(i, list_aperture[17])
    print(dof)

print(list_aov)

DOF_ouverture20 = DOF(55, 20)  
print(DOF_ouverture20)'''