import matplotlib.pyplot as plt
import numpy as np
import torch

def calculate_iou(bbox1, bbox2):
    # 计算IOU（交并比）
    x1, y1, w1, h1 = bbox1
    x2, y2, w2, h2 = bbox2

    intersection = max(0, min(x1 + w1, x2 + w2) - max(x1, x2)) * max(0, min(y1 + h1, y2 + h2) - max(y1, y2))
    union = w1 * h1 + w2 * h2 - intersection

    iou = intersection / union
    return iou

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

def plot_comparison(bboxes, num_points=100):
    # 生成横坐标，即两个bbox中心点的距离
    distances = np.linspace(0, 32, num_points)

    # 计算每个尺寸下的IOU和Wasserstein Loss
    ious = []
    losses = []
    for distance in distances:
        bbox_distance = torch.tensor([distance, 0, bboxes[0][0], bboxes[0][1]])  # 使用第一个bbox的尺寸
        iou_values = [calculate_iou(torch.tensor([0, 0, w, h]), bbox_distance) for w, h in bboxes]
        loss_values = [wasserstein_loss(torch.tensor([0, 0, w, h]), bbox_distance) for w, h in bboxes]
        ious.append(iou_values)
        losses.append(loss_values)

    # 绘制图表
    ious = np.array(ious).T  # 转置矩阵，使每列对应一种bbox尺寸
    losses = np.array(losses).T
    fig, ax1 = plt.subplots()

    color = 'tab:red'
    ax1.set_xlabel('Center Distance')
    ax1.set_ylabel('IOU', color=color)
    ax1.plot(distances, ious[0], label='4x4 IOU', color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()
    color = 'tab:blue'
    ax2.set_ylabel('Wasserstein Loss', color=color)
    ax2.plot(distances, losses[0], label='4x4 Wasserstein Loss', color=color)
    ax2.tick_params(axis='y', labelcolor=color)

    fig.tight_layout()
    plt.title('IOU and Wasserstein Loss vs Center Distance for 4x4 Bounding Box')
    plt.show()

# 示例bbox
bboxes = [(4, 4), (8, 8), (16, 16), (32, 32)]

# 绘制图表
plot_comparison(bboxes)
