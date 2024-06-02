import matplotlib.pyplot as plt
import numpy as np

def calculate_iou(bbox1, bbox2):
    x1, y1, w1, h1 = bbox1
    x2, y2, w2, h2 = bbox2

    intersection_x = max(0, min(x1 + w1 / 2, x2 + w2 / 2) - max(x1 - w1 / 2, x2 - w2 / 2))
    intersection_y = max(0, min(y1 + h1 / 2, y2 + h2 / 2) - max(y1 - h1 / 2, y2 - h2 / 2))

    intersection = intersection_x * intersection_y
    union = w1 * h1 + w2 * h2 - intersection

    iou = intersection / union
    return iou

# Bbox尺度相同，大小为4x4
bbox_size = 4
bbox1 = [0, 0, bbox_size, bbox_size]
bbox2 = [0, 0, bbox_size, bbox_size]

# 中心点距离范围
distances = np.linspace(0, 2 * bbox_size, 100)
ious = []

for distance in distances:
    bbox2[0] = distance
    iou = calculate_iou(bbox1, bbox2)
    ious.append(iou)

# 绘制图像
plt.plot(distances, ious, label='IOU')
plt.xlabel('Center Distance')
plt.ylabel('IOU')
plt.title('IOU vs Center Distance for 4x4 Bboxes')
plt.legend()
plt.show()
