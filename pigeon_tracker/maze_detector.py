import cv2


class MazeDetector:

    def __init__(self, min_val, max_val):
        self.min_val = min_val
        self.max_val = max_val

    def detect_maze(self, file_name):
        video = cv2.VideoCapture(file_name)
        ret, first_frame = video.read()

        canny = cv2.Canny(first_frame, self.min_val, self.max_val)

        cv2.imshow('canny', canny)


