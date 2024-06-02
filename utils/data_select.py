import os
import random
import shutil

# 定义源目录和目标目录的路径：

source_dir = "./voc-person-car/"
train_dir = "/root/dataset/voc-person-car/train"
val_dir = "/root/dataset/voc-person-car/val"

# 创建目标目录：
os.makedirs(os.path.join(train_dir, "images"), exist_ok=True)
os.makedirs(os.path.join(train_dir, "labels"), exist_ok=True)
os.makedirs(os.path.join(val_dir, "images"), exist_ok=True)
os.makedirs(os.path.join(val_dir, "labels"), exist_ok=True)


# 获取images目录中所有的图片文件名，并随机打乱顺序：
image_files = [file for file in os.listdir(os.path.join(source_dir, "images")) if file.endswith(".jpg")]
random.shuffle(image_files)


# 选取2700张图片作为训练集，复制到train目录：
train_images = image_files[:8696]
for image in train_images:
    image_path = os.path.join(source_dir, "images", image)
    txt_path = os.path.join(source_dir, "labels-yolo", os.path.splitext(image)[0] + ".txt")
    if not os.path.exists(image_path) or (not os.path.exists(txt_path)):
        print(txt_path)
        continue
    shutil.copy(image_path, os.path.join(train_dir, "images"))
    shutil.copy(txt_path, os.path.join(train_dir, "labels"))


# 选取900张图片作为测试集，复制到val目录：
val_images = image_files[8696:]
for image in val_images:
    image_path = os.path.join(source_dir, "images", image)
    txt_path = os.path.join(source_dir, "labels-yolo", os.path.splitext(image)[0] + ".txt")
    if not os.path.exists(image_path) or (not os.path.exists(txt_path)):
        print(txt_path)
        continue
    shutil.copy(image_path, os.path.join(val_dir, "images"))
    shutil.copy(txt_path, os.path.join(val_dir, "labels"))
