import json
import cv2 as cv
import numpy as np

json_dict = json.load(open('front_new_res.json', 'r'))
# print(json_dict['data'][0]['joint_full']['predictions'])

kp_dict = json_dict['data'][0]['joint_full']['predictions'][0]['keypoints']

kp_arr = np.array(kp_dict)
kp_arr = kp_arr.reshape(143, 3)
kp_mat = np.mat(kp_arr)
# print(kp_arr)

px = list(kp_mat[:, 0])
py = list(kp_mat[:, 1])
s = list(kp_mat[:, 2])
# print(x, y, s)


def show_point(img, x, y):
    points_num = 143

    for points in range(points_num):
        pos = (int(x[points-1]), int(y[points-1]))
        if pos[0] > 0 and pos[1] > 0:
            cv.circle(img, pos, 5, (0, 0, 255), -1)  # 为肢体点画红色实心圆
    return img


image = cv.imread('front_new_pre.jpg')
sp = image.shape
print(sp)
show_point(image, px, py)
cv.imwrite("front_new_pt.png", image)
