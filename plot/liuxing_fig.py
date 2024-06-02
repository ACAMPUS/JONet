# 怎么做两条不同量纲的折线置于一个图中
# GPT-3.5-Turbo
# Poe
# 要将两条具有不同量纲的折线图置于一个图中，可以通过以下步骤实现：
# 根据每个折线图的数据，创建两个单独的坐标轴。
# 将第一个折线图绘制在第一个坐标轴上。确保坐标轴的范围和刻度适合第一个折线图的数据。
# 创建第二个坐标轴，并将其放置在第一个坐标轴的右侧。确保第二个坐标轴的范围和刻度适合第二个折线图的数据。
# 将第二个折线图绘制在第二个坐标轴上。
# 添加合适的图例，以区分两个折线图。
# 下面是一个示例代码，使用Python的Matplotlib库来实现将两条不同量纲的折线图置于一个图中：
# python
# 复制
import matplotlib.pyplot as plt
from matplotlib import rcParams
import numpy as np

config = {
    "font.family": 'serif',
    "font.size": 12,
    "mathtext.fontset": 'stix',
    "font.serif": ['SimSun'],
}
rcParams.update(config)


# 第一个折线图的数据
x1 = [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
y1 = [4427.28, 2152.16, 1917.16, 1786.48, 1916.16, 1911.08, 2088.16, 2664.2, 2849.2, 2808.24]

# 第二个折线图的数据
x2 = [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
y2 = [13.25,	15.29,	18.56,	15.04,12.78,	21.29,	33.87,	20.19,	19.52,	15.24]

fig, ax1 = plt.subplots()

# 绘制第一个折线图
ax1.plot(x1, y1, color='blue', marker='o')
ax1.set_xlabel('年份')
ax1.set_ylabel('猪饲料价格指数（元/吨）')

# 创建第二个坐标轴
ax2 = ax1.twinx()

# 绘制第二个折线图
ax2.plot(x2, y2, color='red', marker='o')
ax2.set_ylabel('生猪价格（元/千克）')

# 添加图例
ax1.legend(['猪饲料价格指数'], loc=(0.2, 0.9),frameon=False)
ax2.legend(['生猪价格'], loc='upper right',frameon=False)
plt.savefig("fig",dpi=300)
plt.show()

