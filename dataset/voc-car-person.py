# -*- coding: utf-8 -*-
# @Function:There are 20 classes in VOC data set. If you need to extract specific classes, you can use this program to extract them.

import os
import shutil

ann_filepath = r'./voc2012/VOCtrainval_11-May-2012/VOCdevkit/VOC2012/Annotations'
img_filepath = r'./voc2012/VOCtrainval_11-May-2012/VOCdevkit/VOC2012/JPEGImages/'
img_savepath = r'./voc-person-car/images/'
ann_savepath = r'./voc-person-car/labels/'
if not os.path.exists(img_savepath):
    os.mkdir(img_savepath)

if not os.path.exists(ann_savepath):
    os.mkdir(ann_savepath)
names = locals()
classes = ['aeroplane', 'bicycle', 'bird', 'boat', 'bottle',
           'bus', 'car', 'cat', 'chair', 'cow', 'diningtable',
           'dog', 'horse', 'motorbike', 'pottedplant',
           'sheep', 'sofa', 'train', 'tvmonitor', 'person']

for file in os.listdir(ann_filepath):
    print(file)

    fp = open(ann_filepath + '/' + file)  # 打开Annotations文件
    ann_savefile = ann_savepath + file
    fp_w = open(ann_savefile, 'w')
    lines = fp.readlines()

    ind_start = []
    ind_end = []
    lines_id_start = lines[:]

    lines_id_end = lines[:]


    classes3 = '\t\t<name>car</name>\n'
    classes4 = '\t\t<name>bicycle</name>\n'
    classes2 = '\t\t<name>motorbike</name>\n'
    classes1 = '\t\t<name>person</name>\n'
    classes5 = '\t\t<name>bus</name>\n'



    # 在xml中找到object块，并将其记录下来
    while "\t<object>\n" in lines_id_start:
        a = lines_id_start.index("\t<object>\n")
        ind_start.append(a)  # ind_start是<object>的行数
        lines_id_start[a] = "delete"

    while "\t</object>\n" in lines_id_end:
        b = lines_id_end.index("\t</object>\n")
        ind_end.append(b)  # ind_end是</object>的行数
        lines_id_end[b] = "delete"

    # names中存放所有的object块
    i = 0
    for k in range(0, len(ind_start)):
        names['block%d' % k] = []
        for j in range(0, len(classes)):
            if classes[j] in lines[ind_start[i] + 1]:
                a = ind_start[i]
                for o in range(ind_end[i] - ind_start[i] + 1):
                    names['block%d' % k].append(lines[a + o])
                break
        i += 1
        # print(names['block%d' % k])

    # xml头
    string_start = lines[0:ind_start[0]]

    # xml尾
    if ((file[2:4] == '09') | (file[2:4] == '10') | (file[2:4] == '11')):
        string_end = lines[(len(lines) - 11):(len(lines))]
        flag=1
    else:
        string_end = [lines[ind_end[-1]+1:len(lines)]]
        # string_end = lines[len(lines)-1]
        flag=2

    # 在给定的类中搜索，若存在则，写入object块信息
    a = 0
    for k in range(0, len(ind_start)):
        if classes3 in names['block%d' % k]:
            a += 1
            string_start += names['block%d' % k]
        if classes4 in names['block%d' % k]:
            a += 1
            string_start += names['block%d' % k]
        if classes2 in names['block%d' % k]:
            a += 1
            string_start += names['block%d' % k]
        if classes1 in names['block%d' % k]:
            a += 1
            string_start += names['block%d' % k]
        if classes5 in names['block%d' % k]:
            a += 1
            string_start += names['block%d' % k]

    if flag==1:
        string_start += string_end
    else:
        string_start += string_end[0]
    # print(string_start)
    for c in range(0, len(string_start)):
        fp_w.write(string_start[c])
    fp_w.close()
    # 如果没有我们寻找的模块，则删除此xml，有的话拷贝图片
    if a == 0:
        os.remove(ann_savepath + file)
    else:
        name_img = img_filepath + os.path.splitext(file)[0] + ".jpg"
        shutil.copy(name_img, img_savepath)
    fp.close()

