import numpy as np
class objet:
    def __init__(self, center_position, object_size, object_depth):
        self.center_position = center_position
        self.object_size = object_size
        self.object_depth =object_depth
    def object_parameter(self):
        position = [float(self.center_position[0]), float(self.center_position[1]), float(self.center_position[2])]
        size_XY = [float(self.object_size[0]), float(self.object_size[1])]
        depth = float(self.object_depth)
        angle_max_min_x = [np.degrees(2*np.arctan((float(self.center_position[0])+float(self.object_size[0])/2)/float(self.center_position[2]))), np.degrees(2*np.arctan((float(self.center_position[0])-float(self.object_size[0])/2)/float(self.center_position[2])))]
        angle_max_min_y = [np.degrees(2*np.arctan((float(self.center_position[1])+float(self.object_size[1])/2)/float(self.center_position[2]))), np.degrees(2*np.arctan((float(self.center_position[1])-float(self.object_size[1])/2)/float(self.center_position[2])))]
        return position, size_XY, depth, angle_max_min_x, angle_max_min_y