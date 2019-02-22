import cv2


def show_frame(file_name, frame):
    cap = cv2.VideoCapture(file_name)
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame)

    result_tuple = cap.read()
    cap.release()
    return result_tuple


class ColorTracker:

    def __init__(self, lower_color_boundary, upper_color_boundary, hsv=True, tracking_mask=True, original=True,
                 scaling=1.0):
        self.scaling = scaling
        self.original = original
        self.tracking_mask = tracking_mask
        self.hsv = hsv

        self.lower_color_boundary = lower_color_boundary
        self.upper_color_boundary = upper_color_boundary

        self.current_frame_number = 0
        self.video = None
        self.length = 0
        self.fps = 0

    def track_video(self, file_name, initial_frame):
        self.current_frame_number = 0
        self.video = cv2.VideoCapture(file_name)

        self.length = int(self.video.get(cv2.CAP_PROP_FRAME_COUNT))
        self.fps = self.video.get(cv2.CAP_PROP_FPS)

        self._skip_to_frame(initial_frame)
        movements = self._track_color()

        return {'movements': movements, 'fps': self.fps, 'start': initial_frame, 'length': self.length}

    def _skip_to_frame(self, frame_number):
        while self.video.isOpened():
            if self.current_frame_number >= frame_number:
                break

            self.video.grab()
            self.current_frame_number += 1

    def _track_color(self):
        object_movement = []
        while self.video.isOpened():
            ret, image = self.video.read()
            self.current_frame_number += 1

            if self.current_frame_number % 100 == 0:
                self.update_progress_bar()

            if ret:

                if self.scaling < 1.0:
                    image = cv2.resize(image, None, fx=self.scaling, fy=self.scaling, interpolation=cv2.INTER_LINEAR)

                hsv_frame = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
                color_tracking_mask = cv2.inRange(hsv_frame, self.lower_color_boundary, self.upper_color_boundary)

                _, contours, _ = cv2.findContours(color_tracking_mask, cv2.RETR_EXTERNAL,
                                                  cv2.CHAIN_APPROX_SIMPLE)

                # find biggest contour
                # biggest means max area
                if len(contours) > 0:
                    tracked_object = max(contours, key=cv2.contourArea)
                    x, y, w, h = cv2.boundingRect(tracked_object)
                    object_movement.append((x, y))
                    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), thickness=3)

                if self.hsv:
                    cv2.imshow('hsv', hsv_frame)

                if self.tracking_mask:
                    cv2.imshow('tracking_mask', color_tracking_mask)

                if self.original:
                    cv2.imshow('original', image)
            else:
                print("skipping frame " + str(self.current_frame_number))

            if cv2.waitKey(1) & 0xFF == ord('q') or self.current_frame_number >= self.length:
                break

        print("video closed")
        self.video.release()
        cv2.destroyAllWindows()
        return object_movement

    def update_progress_bar(self):

        progress = int(self.current_frame_number / self.length * 100)

        progress_tenth = int(progress / 10)
        progress_bar = "[" + "#" * progress_tenth + " " * (10 - progress_tenth) + "] " + str(progress) + "%"
        print(progress_bar)

        pass
