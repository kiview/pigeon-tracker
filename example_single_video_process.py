from pigeon_tracker.tracker import ColorTracker

lower_red = (170, 100, 100)
upper_red = (180, 255, 255)

t = ColorTracker(lower_red, upper_red)
t.hsv = False
t.original = False
t.tracking_mask = False
t.scaling = 0.3

t.track_video("example-videos/pigeon_video.mp4", 1000)
