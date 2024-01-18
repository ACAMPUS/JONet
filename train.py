import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO('ultralytics/cfg/models/v8/yolov8-goldyolo.yaml')
    model.load('yolov8n.pt') # loading pretrain weights
    model.train(data='dataset/tt100k_ori.yaml',
                cache=True,
                imgsz=640,
                epochs=300,
                batch=16,
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