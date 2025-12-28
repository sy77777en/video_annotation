import os
import json
import random

def select_videos(folder_path, json_path):
    # 1. 读取 JSON 配置文件
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            config = json.load(f)
            # 根据你描述的格式，这里假设 json 是一个 dict
            # 里面包含一个列表 (exclude_list) 和一个数字 (number)
            exclude_list = config.get('list', [])  
            count_to_pick = config.get('number', 0)
    except FileNotFoundError:
        print(f"错误：找不到配置文件 {json_path}")
        return []

    # 2. 获取文件夹内所有 .mp4 文件
    all_videos = [f for f in os.listdir(folder_path) if f.lower().endswith('.mp4')]
    
    # 3. 过滤掉在排除列表中的视频
    exclude_set = set(exclude_list)
    available_videos = [v for v in all_videos if v not in exclude_set]
    
    print(f"总视频数: {len(all_videos)}")
    print(f"排除视频数: {len(exclude_set)}")
    print(f"剩余可选数: {len(available_videos)}")

    # 4. 随机抽取
    if len(available_videos) == 0:
        print("没有可抽取的视频。")
        return []
    
    # 如果要求的数量超过剩余数量，取最大可用数
    actual_pick_count = min(count_to_pick, len(available_videos))
    selected_videos = random.sample(available_videos, actual_pick_count)
    
    return selected_videos

# --- 使用示例 ---
video_dir = '/data2/siyuanc4/flimai_sft'   # 你的视频文件夹
config_file = './exclude.json'   # JSON 文件的实际路径

result = select_videos(video_dir, config_file)

print("\n最终选中的视频列表：")
for i, name in enumerate(result, 1):
    print(f"{i}. {name}")
