class lens:
    def __init__(self, focal, f_number):
        self.focal = focal
        self.f_number = f_number
    def lens_parameters(self):
        return float(self.focal), float(self.f_number)