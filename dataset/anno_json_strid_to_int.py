import json


anno_json=r'coco_ana.json'

with open(anno_json, 'r') as fr:
    anno_dict = json.load(fr)
    # 对标注文件annotations的image_id进行更改
    for annotations in anno_dict['images']:
        image_id = annotations['id']
        annotations['id'] = int(image_id)
    for ann in anno_dict['annotations']:
        id=ann['image_id']
        ann['image_id']=int(id)

# 分别保存更改后的标注文件和预测文件
with open('coco_ana_int.json', 'w') as fw:
    json.dump(anno_dict, fw, indent=4, ensure_ascii=False)