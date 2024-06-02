import matplotlib.pyplot as plt
import numpy as np
import torch


def wasserstein_loss(pred, target, eps=1e-7, constant=12.8):
    b1_x1, b1_y1, b1_x2, b1_y2 = pred.chunk(4, -1)
    b2_x1, b2_y1, b2_x2, b2_y2 = target.chunk(4, -1)
    w1, h1 = b1_x2 - b1_x1, b1_y2 - b1_y1 + eps
    w2, h2 = b2_x2 - b2_x1, b2_y2 - b2_y1 + eps

    b1_x_center, b1_y_center = b1_x1 + w1 / 2, b1_y1 + h1 / 2
    b2_x_center, b2_y_center = b2_x1 + w2 / 2, b2_y1 + h2 / 2
    center_distance = (b1_x_center - b2_x_center) ** 2 + (b1_y_center - b2_y_center) ** 2 + eps
    wh_distance = ((w1 - w2) ** 2 + (h1 - h2) ** 2) / 4

    wasserstein_2 = center_distance + wh_distance
    return torch.exp(-torch.sqrt(wasserstein_2) / constant)

def calculate_iou(bbox1, bbox2):
    # 计算IOU（交并比）
    x1, y1, w1, h1 = bbox1
    x2, y2, w2, h2 = bbox2

    intersection = max(0, min(x1 + w1, x2 + w2) - max(x1, x2)) * max(0, min(y1 + h1, y2 + h2) - max(y1, y2))
    union = w1 * h1 + w2 * h2 - intersection

    iou = intersection / union
    return iou

def plot_iou_distance(bboxes, num_points=100):
    # 生成横坐标，即两个bbox中心点的距离
    distances = np.linspace(0,  max(bboxes[0][0], bboxes[3][0]), num_points)

    # 计算每个尺寸下的IOU
    ious = []
    for distance in distances:
        iou_values = [calculate_iou((0, 0, w, h), (distance, 0, w, h)) for w, h in bboxes]
        ious.append(iou_values)

    # 绘制图表
    ious = np.array(ious).T  # 转置矩阵，使每列对应一种bbox尺寸
    plt.plot(distances, ious[0], label='4x4')
    plt.plot(distances, ious[1], label='8x8')
    plt.plot(distances, ious[2], label='16x16')
    plt.plot(distances, ious[3], label='32x32')

    # 添加标签和标题
    plt.xlabel('Center Distance')
    plt.ylabel('IOU')
    plt.title('IOU vs Center Distance for Bounding Boxes of Different Sizes')
    plt.legend()

    # 显示图表
    plt.show()

# 示例bbox
bboxes = [(4, 4), (8, 8), (16, 16), (32, 32)]

# 绘制图表
plot_iou_distance(bboxes)
