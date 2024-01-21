import matplotlib.pyplot as plt
import numpy as np
import torch
import pandas as pd

def iou(box1, box2):
    x1, y1, w1, h1 = box1
    x2, y2, w2, h2 = box2

    x_intersection = max(0, min(x1 + w1, x2 + w2) - max(x1, x2))
    y_intersection = max(0, min(y1 + h1, y2 + h2) - max(y1, y2))

    intersection = x_intersection * y_intersection
    union = w1 * h1 + w2 * h2 - intersection

    return intersection / union

def calculate_iou(center_distances, scale):
    iou_values = []

    for distance in center_distances:
        box1 = [0, 0, scale, scale]
        box2 = [distance, 0, scale, scale]
        iou_values.append(iou(box1, box2))

    return iou_values

def save_to_excel(data, filename):
    df = pd.DataFrame(data, columns=['Center Distance', 'Scale 4x4', 'Scale 8x8', 'Scale 16x16', 'Scale 32x32'])
    df.to_excel(filename, index=False)

def plot_and_save_iou():
    bbox_scales = [4, 8, 16, 32]
    center_distances = np.arange(0, max(bbox_scales), 0.1)
    data = {'Center Distance': center_distances}

    for scale in bbox_scales:
        iou_values = calculate_iou(center_distances, scale)
        data[f'Scale {scale}x{scale}'] = iou_values

    plot_iou_vs_distance(center_distances, data)
    save_to_excel(data, 'iou_data.xlsx')

def plot_iou_vs_distance(center_distances, data):
    plt.figure(figsize=(10, 6))

    for scale in ['Scale 4x4', 'Scale 8x8', 'Scale 16x16', 'Scale 32x32']:
        plt.plot(center_distances, data[scale], label=scale)

    plt.xlabel('Center Distance')
    plt.ylabel('IOU')
    plt.legend()
    plt.title('IOU vs Center Distance for Different Bbox Scales')
    plt.grid(True)
    # plt.show()  # save与show不可一起调用，如果想保存就不要调用show，否则保存的是一张空白图
    plt.savefig('iou_plot.png', dpi=1000)  # 保存图像，设置dpi为1000

if __name__ == "__main__":
    plot_and_save_iou()
