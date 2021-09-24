from Module import *

test1 = Optical_parameter(50,20,1000)
print(test1.aov_function())
print(test1.Depth_Of_Field())

test2 = Inverse_optical_parameter(7.55, 509.64, 806.45, 1315.79)
print(test2.focal_function())
print(test2.F_number())

test3 = Pinhole_system([8,7,10],50)
print(test3.pinhole_model())