import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO('ultralytics/cfg/models/v8/yolov8-ASF-no-scale+nwd+dyhead.yaml')
    model.load('yolov8n.pt') # loading pretrain weights
    model.train(data='dataset/voc-car-person.yaml',
                cache=True,
                imgsz=640,
                epochs=300,
                batch=64,
                close_mosaic=10,
                workers=12,
                device='0',
                optimizer='SGD', # using SGD
                # resume='', # last.pt path
                # amp=False, # close amp
                # fraction=0.2,
                project='runs/train',
                name='exp',
                patience=30,

                )
