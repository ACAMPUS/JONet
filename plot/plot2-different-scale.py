import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams

config = {
    "font.family": 'serif',
    "font.size": 18,
    "mathtext.fontset": 'stix',
    "font.serif": ['SimSun'],
}
rcParams.update(config)

def calculate_iou(bbox1, bbox2):
    x1, y1, w1, h1 = bbox1
    x2, y2, w2, h2 = bbox2

    intersection_x = max(0, min(x1 + w1 / 2, x2 + w2 / 2) - max(x1 - w1 / 2, x2 - w2 / 2))
    intersection_y = max(0, min(y1 + h1 / 2, y2 + h2 / 2) - max(y1 - h1 / 2, y2 - h2 / 2))

    intersection = intersection_x * intersection_y
    union = w1 * h1 + w2 * h2 - intersection

    iou = intersection / union
    return iou

bbox_size = [4, 8, 16, 32]  # 不同尺度下的bbox大小
center_distances = np.linspace(0, max(bbox_size), 100)

plt.figure(figsize=(10, 8))

for size in bbox_size:
    bbox1 = [0, 0, size, size]
    bbox2 = [0, 0, size, size]

    ious = [calculate_iou(bbox1, [distance, distance, size, size]) for distance in center_distances]

    plt.plot(center_distances, ious, label=f'{size}x{size}',linewidth=2)

plt.xlabel('Center Distance')
plt.ylabel('IOU')
# plt.title('IOU vs Center Distance for Bboxes of Different Scales')
plt.legend()
plt.grid(False)
plt.show()
