import numpy as np

class Pinhole_system:
    def __init__(self, Object_position, focal, Scale_pixel_unit, t_sensor):
        self.Object_position = Object_position
        self.focal = focal
        self.Scale_pixel_unit = Scale_pixel_unit
        self.t_sensor = t_sensor

    def pinhole_model(self):
        P = np.array([[self.focal, 0, 0, 0],[0, self.focal, 0, 0],[0, 0, 1, 0]])
        Object_coordinates = np.array([[float(self.Object_position[0])], [float(self.Object_position[1])], [float(self.Object_position[2])], [1]])
        image_matrix = P.dot(Object_coordinates)
        scale_factor = float(image_matrix[2])
        return   [float(image_matrix[0]) / scale_factor,  float(image_matrix[1]) / scale_factor, scale_factor]

    def Trans_image_to_sensor(self):
        A= np.array([[self.Scale_pixel_unit[0], 0, -self.Scale_pixel_unit[0] * self.t_sensor[0]], [0, self.Scale_pixel_unit[1], - self.Scale_pixel_unit[1] * self.t_sensor[1]], [0, 0, 1]])
        Image_coordinates = np.array([[self.pinhole_model()[0]], [self.pinhole_model()[1]], [1]])
        sensor_matrix = A.dot(Image_coordinates)
        return np.round(float(sensor_matrix[0]),0), np.round(float(sensor_matrix[1]),0)

# 1. world coordinates to object coordinates -> x_object, y_object, z_object

'''def Trans_world_to_object(x_world, y_world, z_world, R11 ,R12 ,R13 ,R21 ,R22 ,R23 ,R31 ,R32 ,R33 , tx, ty, tz):
    T = np.array([[R11, R12, R13, tx], [R21, R22, R23, ty], [R31, R32, R33, tz], [0, 0, 0, 1]])
    world_coordinates = np.array([[x_world], [y_world], [z_world], [1]])
    object_matrix = T.dot(world_coordinates)
    return float(object_matrix[0]), float(object_matrix[1]), float(object_matrix[2])

a =Trans_world_to_object(1,2,3,1,1,1,1,1,1,4,1,1,2,1,1)
print(a[0], a[1], a[2])'''

# 4. projection model: world to sensor coordinates -> (scale_factor, x_sensor, y_sensor)
'''
def projection_model(x_world, y_world, z_world, R11 ,R12 ,R13 ,R21 ,R22 ,R23 ,R31 ,R32 ,R33 , tx, ty, tz, S_x, S_y, theta, tx_sensor, ty_sensor, image_distance):
    fx = image_distance * S_x
    fy = image_distance * S_y/np.sin(theta)
    fs = - image_distance * S_x/np.tan(theta)
    cx = -S_x * (tx_sensor - ty_sensor/np.tan(theta))
    cy = -S_y * ty_sensor/np.sin(theta)
    G11 = R11 * fx + R21 * fs + R31 * cx
    G12 = R12 * fx + R22 * fs + R32 * cx
    G13 = R13 * fx + R23 * fs + R33 * cx
    G14 = fx * tx + fs * ty + cx * tz
    G21 = R21 * fy + R31 * cy
    G22 = R22 * fy + R32 * cy
    G23 = R23 * fy + R33 * cy
    G24 = fy * ty + cy * tz
    G31 = R31
    G32 = R32
    G33 = R33
    G34 = tz
    projection_matrix = np.array([[G31*x_world + G32*y_world + G33*z_world +G34], [G11*x_world + G12*y_world + G13*z_world + G14], [G21*x_world + G22*y_world + G23*z_world + G24]])
    return float(projection_matrix[0]), float(projection_matrix[1]) / float(projection_matrix[0]), float(projection_matrix[2]/ float(projection_matrix[0]))

d = projection_model(1,2,3,1,1,1,1,1,1,4,1,1,2,1,1, 1, 1, np.pi/2, 1, 1, 50)
print(d)'''