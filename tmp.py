import os
import json
import random
import shutil

def copy_selected_videos(video_folder, json_path, number, output_folder='selected_videos'):
    # 1. 加载排除列表 (JSON 仅包含文件名列表)
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            exclude_list = json.load(f)
    except Exception as e:
        print(f"读取 JSON 失败: {e}")
        return

    # 2. 扫描文件夹并过滤
    exclude_set = set(exclude_list)
    available_videos = [
        f for f in os.listdir(video_folder) 
        if f.lower().endswith('.mp4') and f not in exclude_set
    ]

    # 3. 确定抽取数量
    if len(available_videos) < number:
        print(f"可用视频不足，仅有 {len(available_videos)} 个。")
        number = len(available_videos)
    
    selected_videos = random.sample(available_videos, number)

    # 4. 创建目标文件夹并复制
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"已创建目标文件夹: {output_folder}")

    for video in selected_videos:
        src = os.path.join(video_folder, video)
        dst = os.path.join(output_folder, video)
        shutil.copy2(src, dst)  # copy2 会保留元数据
        print(f"已复制: {video}")

    print(f"\n任务完成！成功复制 {len(selected_videos)} 个视频到 '{output_folder}'")

# --- 修改这里的参数 ---
copy_selected_videos(
    video_folder = '/data2/siyuanc4/flimai_sft',  # 你的视频来源文件夹
    json_path    = './exclude.json',  # exclude.json 的路径
    number       = 20,                 # 你想要 copy 的数量
    output_folder = './selected_results_2' # 结果存放的文件夹
)
