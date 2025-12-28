import json
import shutil
import os
import glob
import random

# --- Configurations ---
label_path = '/compute/trinity-2-25/siyuanc4/video_annotation/video_labels/cam_motion-cam_setup-20251227_ground_and_setup_folder/all_labels.json'
target_folder = '/data2/siyuanc4/camerabench_pro/videos'
# IMPORTANT: Where the original camerabench mp4 files are stored
source_video_dir = './videos' 
filmai_dir = '/data2/siyuanc4/filmai/videos'

video_types = {"camerabench_cut": 15, "camerabench_no_cut": 15, "flim": 30}

# Load labels
with open(label_path, 'r') as f:
    label_data = json.load(f)

pos_videos = label_data["cam_motion.has_shot_transition_cam_motion"]["pos"]
neg_videos = label_data["cam_motion.has_shot_transition_cam_motion"]["neg"]

# Get list of filenames for flim (removing path to just get name)
flim_paths = glob.glob(os.path.join(filmai_dir, '*.mp4'))
flim_videos = [os.path.basename(p) for p in flim_paths]

for video_type, number in video_types.items():
    print(f"Processing {video_type}...")
    save_folder = os.path.join(target_folder, video_type)
    os.makedirs(save_folder, exist_ok=True)

    # 1. Select the random subset
    if video_type == 'camerabench_cut':
        selected = random.sample(pos_videos, min(len(pos_videos), number))
        src_root = source_video_dir
    elif video_type == 'camerabench_no_cut':
        selected = random.sample(neg_videos, min(len(neg_videos), number))
        src_root = source_video_dir
    else:
        selected = random.sample(flim_videos, min(len(flim_videos), number))
        src_root = filmai_dir

    # 2. Copy the files
    for filename in selected:
        # Some JSONs might store paths, ensure we only have the filename
        base_name = os.path.basename(filename)
        src_path = os.path.join(src_root, base_name)
        dst_path = os.path.join(save_folder, base_name)
        
        if os.path.exists(src_path):
            shutil.copy(src_path, dst_path)
        else:
            print(f"Warning: File not found: {src_path}")

print("Done! Videos have been organized.")

  
