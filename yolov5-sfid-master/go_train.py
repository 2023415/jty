import os
os.system("python train.py --data my_data.yaml --cfg yolov5s.yaml --weights pretrained/yolov5s.pt --epoch 100 --batch-size 4")
                           #配置文件             模型配置文件                                          一共跑100轮     四张图一批来跑

# os.system("python train.py --data my_data.yaml --cfg yolov5m.yaml --weights pretrained/yolov5m.pt --epoch 100 --batch-size 4")
# os.system("python train.py --data my_data.yaml --cfg yolov5l.yaml --weights pretrained/yolov5l.pt --epoch 100 --batch-size 4")

