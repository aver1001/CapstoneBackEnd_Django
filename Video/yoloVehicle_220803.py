import cv2
from python.histo_compare import *
import copy


# import bunhopan

def yoloVehicle(img, y_dict, classes, yolo_model, cnt,isfirst=True):
    hide_img = np.copy(img)
    height, width, channels = img.shape
    blob = cv2.dnn.blobFromImage(img, 1.0 / 256, (416, 416), (0, 0, 0), swapRB=True, crop=False)

    layer_names = yolo_model.getLayerNames()
    out_layers = [layer_names[i - 1] for i in yolo_model.getUnconnectedOutLayers()]

    yolo_model.setInput(blob)
    output3 = yolo_model.forward(out_layers)

    class_ids, confidences, boxes = [], [], []
    for output in output3:
        for vec85 in output:
            scores = vec85[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.7:

                centerx, centery = int(vec85[0] * width), int(vec85[1] * height)
                w, h = int(vec85[2] * width), int(vec85[3] * height)
                x, y = int(centerx - w / 2), int(centery - h / 2)
                if w > h*1.8: # Before 2
                    continue
                    
                if 'Vehicle_Car' == classes[class_id]:
                    if (w * h) <= 4500: # +1500
                        continue
                if 'Vehicle_Bus' == classes[class_id]:
                    if (w * h) <= 8000: # +3500
                        continue
                if 'Vehicle_Unknown' == classes[class_id]:
                    if (w * h) <= 5250: # +1000
                        continue

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
    TL = ""
    temp_dict = {}
    road_dict = {} #new
    rm_cnt=0 #new
    if isfirst == True:
        tl_area = 0
        for i in range(len(boxes)):
            if i in indexes:
                x, y, w, h = boxes[i]
                text = str(classes[class_ids[i]])
                if 'Left' in text or 'Right' in text: #new
                    road_dict[rm_cnt]={'pos': [x, y, w, h],
                                    'type': text,
                                   'state': None} #new
                    rm_cnt+=1
                if text != 'RoadMark_StopLine':
                    cv2.rectangle(hide_img, (x, y), (x + w, y + h), (0, 0, 0), cv2.FILLED)
                if 'Vehicle' in text:
                    y_dict[cnt] = {'pos': [x, y, w, h],
                                   'type': text}
                    cnt += 1
        temp_dict = copy.deepcopy(y_dict)
    else:
        # if y_dict:
        #     cnt = max(y_dict.keys()) + 1
        # else:
        #     cnt = 0
        cnt+=1
        tl_area = 0

        checked = []

        ## yolo model detect pos

        for i in range(len(boxes)):
            if i in indexes:
                x, y, w, h = boxes[i]
                acc = []
                mid = (x + (w // 2), y + (h // 2))
                text = str(classes[class_ids[i]])
                if 'Left' in text or 'Right' in text: #new
                    road_dict[rm_cnt]={'pos': [x, y, w, h],
                                    'type': text} #new
                    rm_cnt+=1 #new
                if text != 'RoadMark_StopLine':
                    cv2.rectangle(hide_img, (x, y), (x + w, y + h), (0, 0, 0), cv2.FILLED)
                if 'Vehicle' in text:
                    for key, value in y_dict.items():
                        value = value['pos']
                        dx, dy, dw, dh = value[0], value[1], value[2], value[3]
                        if dx <= 0 or dy <= 0 or x <= 0 or y <= 0:
                            continue
                        dmid = (dx + (dw // 2), dy + (dh // 2))
                        acc.append((key, abs(mid[0] - dmid[0]) + abs(mid[1] - dmid[1]), [dx, dy, dw, dh]))

                    try:
                        acc.sort(key=lambda x: x[1])
                    except:
                        continue

                    for key, pos, (dx, dy, dw, dh) in acc:

                        if isSame(img[y:y + h, x:x + w], img[dy:dy + dh, dx:dx + dw]):
                            temp_dict[key] = {'pos': [x, y, w, h],
                                              'type': text,
                                              'state': None}
                            del y_dict[key]
                            break


                    else:
                        temp_dict[cnt] = {'pos': [x, y, w, h],
                                          'type': text,
                                          'state': None}
                        cnt += 1

    return temp_dict, hide_img, cnt, road_dict #new

    # else:
    #     if y_dict:
    #         cnt = list(y_dict.keys())[-1]+1
    #     else:
    #         cnt=0
    #     tl_area=0

    #     checked=[]
    #     for i in range(len(boxes)):
    #         if i in indexes:
    #             x,y,w,h=boxes[i]
    #             mid = (x+(w//2),y+(h//2))
    #             text=str(classes[class_ids[i]])

    #             if 'Vehicle' in text:
    #                 # if w*h>=10000:
    #                 #     g_image=img[y:y+h,x:x+w]
    #                     # try:
    #                     #     bh = bunhopan.findCarnum(g_image)
    #                     #     print(bh)
    #                     # except:
    #                     #     continue
    #                 for key,value in y_dict.items():
    #                     dx,dy,dw,dh = value[0],value[1],value[2],value[3]
    #                     if dx<=0 or dy<=0 or x<=0 or y<=0:
    #                         continue
    #                     if isSame(img[y:y+h,x:x+w],img[value[1]:value[1]+value[3],value[0]:value[0]+value[2]]):
    #                         y_dict[key]=[x,y,w,h,text]
    #                         checked.append(key)
    #                         break
    #                 else:
    #                     y_dict[cnt]=[x,y,w,h,text]
    #                     checked.append(cnt)
    #                     cnt+=1

    #             if 'Traffic' in text and tl_area<w*h:
    #                 TL=text+'  '+str(confidences[i])
    #                 tl_area=w*h

    #     for key in list(y_dict.keys()):
    #         if key not in checked:
    #             del y_dict[key]

    # return y_dict, TL