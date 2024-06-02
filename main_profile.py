import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO

if __name__ == '__main__':
    # choose your yaml file
    model = YOLO('ultralytics/cfg/models/v3/yolov3-tiny.yaml')
    model.info(detailed=True)
    model.profile(imgsz=[640, 640])
    model.fuse()