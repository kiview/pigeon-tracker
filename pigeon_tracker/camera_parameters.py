import numpy as np
import yaml


class CameraParameters(object):
    camera_matrix = None
    dist_coefs = None
    rms = None

    def __init__(self, camera_matrix, dist_coefs, rms):
        self.camera_matrix = camera_matrix
        self.dist_coefs = dist_coefs
        self.rms = rms

    @staticmethod
    def read_yaml(filepath):
        with open(filepath) as fp:
            c = yaml.load(fp)
            camera_matrix = np.array(c['camera_matrix'])
            dist_coefs = np.array(c['dist_coefs'])
            rms = float(c['rms'])
            return CameraParameters(camera_matrix, dist_coefs, rms)


