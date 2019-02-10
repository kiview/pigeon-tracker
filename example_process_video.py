import json
import os
import glob
from pigeon_tracker.tracker import ColorTracker


def find_videos(search_root):
    return glob.glob(search_root + "/**/*.MP4", recursive=True)


lower_red = (170, 100, 100)
upper_red = (180, 255, 255)

output_dir = os.getcwd() + "/results"

t = ColorTracker(lower_red, upper_red)
t.hsv = False
t.original = False
t.tracking_mask = False

video_parent_dir = "/run/media/kiview/dolphin/videos for the analyzing body embodyment/"
video_dirs = find_videos(video_parent_dir)

for video in video_dirs:

    print("Analyzing video " + video)
    result = t.track_video(video, 1000)
    result_json = json.dumps(result)

    result_file = output_dir + "/" + video.replace(video_parent_dir, "") + ".json"

    os.makedirs(os.path.dirname(result_file), exist_ok=True)
    with open(result_file, "w") as text_file:
        print(result_json, file=text_file)

