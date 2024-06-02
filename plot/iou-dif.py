import matplotlib.pyplot as plt
import numpy as np

def iou(box1, box2):
    x1, y1, w1, h1 = box1
    x2, y2, w2, h2 = box2

    x_intersection = max(0, min(x1 + w1, x2 + w2) - max(x1, x2))
    y_intersection = max(0, min(y1 + h1, y2 + h2) - max(y1, y2))

    intersection = x_intersection * y_intersection
    union = w1 * h1 + w2 * h2 - intersection

    return intersection / union

def plot_iou_vs_distance():
    bbox_scales = [4, 8, 16, 32]

    for scale in bbox_scales:
        center_distances = np.arange(0, 32, 0.1)
        iou_values = []

        for distance in center_distances:
            box1 = [0, 0, scale, scale]
            box2 = [distance, 0, scale, scale]
            iou_values.append(iou(box1, box2))

        plt.plot(center_distances, iou_values, label=f'Scale {scale}x{scale}')

    plt.xlabel('Center Distance')
    plt.ylabel('IOU')
    plt.legend()
    plt.title('IOU vs Center Distance for Different Bbox Scales')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    plot_iou_vs_distance()
