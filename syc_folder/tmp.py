import json

def get_exclusive_items(file1_path, file2_path, output_path):
    # 1. Load data from both files
    with open(file1_path, 'r') as f1, open(file2_path, 'r') as f2:
        data1 = json.load(f1)
        data2 = json.load(f2)

    # 2. Create a set of video_names from the first file for fast lookup
    # Using a set is much faster than a list for large datasets
    existing_videos = {item['video_name'] for item in data1}

    # 3. Filter the second list
    # Keep the item if its video_name is NOT in the existing_videos set
    new_items = [item for item in data2 if item['video_name'] not in existing_videos]

    # 4. Save the results to the new file
    with open(output_path, 'w') as out_file:
        json.dump(new_items, out_file, indent=4)
    
    print(f"Process complete.")
    print(f"Items in File 1: {len(data1)}")
    print(f"Items in File 2: {len(data2)}")
    print(f"New items found and saved: {len(new_items)}")

import os
os.makedirs('./video_data/20251223_ground_and_setup_folder_extra', exist_ok=True)
# Run the function
get_exclusive_items('./video_data/20251216_ground_and_setup_folder/videos.json', './video_data/20251223_ground_and_setup_folder/videos.json', './video_data/20251223_ground_and_setup_folder_extra/videos.json')