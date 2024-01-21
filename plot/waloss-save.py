import numpy as np
import torch
import pandas as pd
import matplotlib.pyplot as plt


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


def calculate_wasserstein_loss(center_distances, scale):
    wasserstein_losses = []

    for distance in center_distances:
        pred = torch.tensor([0, 0, scale, scale])  # Example predicted bbox
        target = torch.tensor([distance, 0, scale, scale])  # Example target bbox
        wasserstein_losses.append(wasserstein_loss(pred, target).item())

    return wasserstein_losses


def save_to_excel(data, filename):
    df = pd.DataFrame(data, columns=['Center Distance', 'Scale 4x4', 'Scale 8x8', 'Scale 16x16', 'Scale 32x32'])
    df.to_excel(filename, index=False)


def plot_and_save_wasserstein_loss():
    bbox_scales = [4, 8, 16, 32]
    center_distances = np.arange(0, max(bbox_scales), 0.1)
    data = {'Center Distance': center_distances}

    for scale in bbox_scales:
        wasserstein_losses = calculate_wasserstein_loss(center_distances, scale)
        data[f'Scale {scale}x{scale}'] = wasserstein_losses

    plot_wasserstein_loss_vs_distance(center_distances, data)
    save_to_excel(data, 'wasserstein_loss_data.xlsx')


def plot_wasserstein_loss_vs_distance(center_distances, data):
    plt.figure(figsize=(10, 6))

    for scale in ['Scale 4x4', 'Scale 8x8', 'Scale 16x16', 'Scale 32x32']:
        plt.plot(center_distances, data[scale], label=scale)

    plt.xlabel('Center Distance')
    plt.ylabel('Wasserstein Loss')
    plt.legend()
    plt.title('Wasserstein Loss vs Center Distance for Different Bbox Scales')
    plt.grid(False)
    # plt.show()
    plt.savefig('wasserstein_loss_full_size.png', dpi=1000)

if __name__ == "__main__":
    plot_and_save_wasserstein_loss()
