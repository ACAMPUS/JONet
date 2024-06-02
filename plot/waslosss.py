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


def plot_wasserstein_loss_vs_distance():
    bbox_scales = [4, 8, 16, 32]

    for scale in bbox_scales:
        center_distances = np.arange(0, scale, 0.1)
        wasserstein_losses = []

        for distance in center_distances:
            pred = torch.tensor([0, 0, scale, scale])  # Example predicted bbox
            target = torch.tensor([distance, 0, scale, scale])  # Example target bbox
            wasserstein_losses.append(wasserstein_loss(pred, target).item())

        plt.plot(center_distances, wasserstein_losses, label=f'Scale {scale}x{scale}')

    plt.xlabel('Center Distance')
    plt.ylabel('Wasserstein Loss')
    plt.legend()
    plt.title('Wasserstein Loss vs Center Distance for Different Bbox Scales')
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    plot_wasserstein_loss_vs_distance()
