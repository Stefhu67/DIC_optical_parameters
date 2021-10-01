import numpy as np

class camera:
    def __init__(self, sensor_size, resolution, confusion_circle):
        self.sensor_size = sensor_size
        self.resolution = resolution
        self.confusion_circle = confusion_circle
    def camera_parameters(self):
        return [float(self.sensor_size[0]), float(self.sensor_size[1])], [float(self.resolution[0]), float(self.resolution[1])] , float(self.confusion_circle), [np.round(float(self.resolution[0])/float(self.sensor_size[0]), 0), np.round(float(self.resolution[1])/float(self.sensor_size[1]),0)]
