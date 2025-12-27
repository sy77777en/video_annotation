import os
import json
import shutil
from pathlib import Path

def organize_small_labels(json_path, source_video_dir, base_output_dir, threshold=30):
    # 1. 初始化路径
    source_dir = Path(source_video_dir)
    output_base = Path(base_output_dir)
    
    # 2. 读取 JSON 数据
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    print(f"开始处理 JSON，目标阈值：少于 {threshold} 个样本...")

    processed_labels = 0
    copied_videos = 0

    # 3. 遍历每个 label
    for label_key, content in data.items():
        pos_cases = content.get("pos", [])
        
        # 检查 positive cases 数量是否少于 30
        if 0 < len(pos_cases) < threshold:
            # 创建子文件夹（以 label 名命名）
            # 注意：label 名可能包含点号，Path 会处理好
            label_folder = output_base / label_key
            label_folder.mkdir(parents=True, exist_ok=True)
            
            print(f"正在处理 Label: {label_key} (共 {len(pos_cases)} 个视频)")

            # 4. 复制视频文件
            for video_name in pos_cases:
                # 兼容处理：有些 JSON 里的名字可能带路径，我们只取文件名
                pure_video_name = os.path.basename(video_name)
                source_path = source_dir / pure_video_name
                target_path = label_folder / pure_video_name

                if source_path.exists():
                    shutil.copy2(source_path, target_path) # copy2 保留元数据
                    copied_videos += 1
                else:
                    print(f"  ⚠️ 找不到视频: {pure_video_name}")
            
            processed_labels += 1

    print("\n--- 处理完成 ---")
    print(f"总共创建了 {processed_labels} 个 Label 文件夹")
    print(f"总共复制了 {copied_videos} 个视频文件")

# --- 配置区 ---
if __name__ == "__main__":
    organize_small_labels(
        json_path="./video_labels/cam_motion-cam_setup-20251227_ground_and_setup_folder/all_labels.json",      # 你的 JSON 文件路径
        source_video_dir="./videos",     # 视频源文件夹
        base_output_dir="./rare_label_videos",# 输出的根目录
        threshold=50                    # 阈值
    )
