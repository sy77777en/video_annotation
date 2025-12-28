import os
import json
import random

def get_selected_videos(folder_path, json_path, num_to_pick):
    # 1. 直接读取 JSON，它本身就是一个文件名列表
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            exclude_list = json.load(f) 
            if not isinstance(exclude_list, list):
                print("错误：JSON 文件内容不是一个列表格式")
                return []
    except Exception as e:
        print(f"读取 JSON 出错: {e}")
        return []

    # 2. 获取文件夹内所有 .mp4 文件
    all_videos = [f for f in os.listdir(folder_path) if f.lower().endswith('.mp4')]
    
    # 3. 排除掉 list 里的文件
    exclude_set = set(exclude_list)
    available_videos = [v for v in all_videos if v not in exclude_set]
    
    # 4. 随机抽取指定的 number 数量
    if len(available_videos) < num_to_pick:
        print(f"警告：过滤后剩余 {len(available_videos)} 个视频，不足要求的 {num_to_pick} 个。将全部返回。")
        num_to_pick = len(available_videos)

    selected = random.sample(available_videos, num_to_pick)
    return selected

# --- 你的输入参数 ---
v_folder = '/data2/siyuanc4/flimai_sft'      # 视频文件夹
j_file = './exclude.json'  # JSON 文件路径
n = 110                      # 你想要的 number

result = get_selected_videos(v_folder, j_file, n)
print(result)
