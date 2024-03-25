import os
import random
import shutil

# 定义源目录和目标目录的路径：

source_dir = "/root/dataset/SODA-D/img_split/train"
train_dir = "/root/dataset/new-soda/train"
val_dir = "/root/dataset/new-soda/val"

# 创建目标目录：
os.makedirs(os.path.join(train_dir, "images"), exist_ok=True)
os.makedirs(os.path.join(train_dir, "labels"), exist_ok=True)
os.makedirs(os.path.join(val_dir, "images"), exist_ok=True)
os.makedirs(os.path.join(val_dir, "labels"), exist_ok=True)


# 获取images目录中所有的图片文件名，并随机打乱顺序：
image_files = [file for file in os.listdir(os.path.join(source_dir, "images")) if file.endswith(".jpg")]
random.shuffle(image_files)


# 选取2700张图片作为训练集，复制到train目录：
train_images = image_files[:2700]
for image in train_images:
    image_path = os.path.join(source_dir, "images", image)
    txt_path = os.path.join(source_dir, "labels", os.path.splitext(image)[0] + ".txt")
    shutil.copy(image_path, os.path.join(train_dir, "images"))
    shutil.copy(txt_path, os.path.join(train_dir, "labels"))


# 选取900张图片作为测试集，复制到val目录：
val_images = image_files[2700:3600]
for image in val_images:
    image_path = os.path.join(source_dir, "images", image)
    txt_path = os.path.join(source_dir, "labels", os.path.splitext(image)[0] + ".txt")
    shutil.copy(image_path, os.path.join(val_dir, "images"))
    shutil.copy(txt_path, os.path.join(val_dir, "labels"))
