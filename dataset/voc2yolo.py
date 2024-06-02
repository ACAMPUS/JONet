import os
import xml.etree.ElementTree as ET

def convert_voc_to_yolo(xml_folder, output_folder, classes):
    for file in os.listdir(xml_folder):
        if file.endswith(".xml"):
            xml_file = os.path.join(xml_folder, file)
            try:
                tree = ET.parse(xml_file)
                root = tree.getroot()
            except:
                print("xml_file: error:%s"%xml_file)
                continue
            if root.find("size/width") is None:
                print(xml_file)
            image_width = int(root.find("size/width").text)
            image_height = int(root.find("size/height").text)

            txt_file = os.path.join(output_folder, os.path.splitext(file)[0] + ".txt")
            with open(txt_file, "w") as f:
                for obj in root.findall("object"):
                    class_name = obj.find("name").text
                    if class_name not in classes:
                        continue
                    class_id = classes.index(class_name)

                    bbox = obj.find("bndbox")
                    xmin = float(bbox.find("xmin").text)
                    ymin = float(bbox.find("ymin").text)
                    xmax = float(bbox.find("xmax").text)
                    ymax = float(bbox.find("ymax").text)

                    x = (xmin + xmax) / 2 / image_width
                    y = (ymin + ymax) / 2 / image_height
                    width = (xmax - xmin) / image_width
                    height = (ymax - ymin) / image_height

                    f.write(f"{class_id} {x:.6f} {y:.6f} {width:.6f} {height:.6f}\n")

# 示例用法

######################   本地   ######################
# xml_folder = r"F:\dataset\voc-person-car\labels"
# output_folder = r"F:\dataset\voc-person-car\labels-yolo"

######################   server   ######################
xml_folder = r"./voc-person-car/labels"
output_folder = r"./voc-person-car/labels-yolo"
classes = ["car", "bicycle", "motorbike","person","bus"]  # 标注的类别列表
convert_voc_to_yolo(xml_folder, output_folder, classes)