import numpy as np
import cv2

img = cv2.imread('sample.png')  # 读取图片
imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 图片灰度化

mid = cv2.medianBlur(imgGrey, ksize=9)  # 选择性加入
blur = cv2.GaussianBlur(mid, ksize=(5, 5), sigmaX=7)  # 高斯模糊
_, thrash = cv2.threshold(blur, 220, 255, cv2.THRESH_BINARY_INV)  # 图形二值化
contours, _ = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)  # 寻找边缘
cv2.imshow("Grey", imgGrey)  # 可不记
cv2.imshow("thrash", thrash)  # 可不记
cv2.imshow("img", img)  # 显示原图像
for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)  # 无限逼近法来绘制棱
    cv2.drawContours(img, [approx], 0, (0, 0, 255), 3)   # 将绘制的棱和图片混合
    x = approx.ravel()[0]
    y = approx.ravel()[1] - 5  # 建立坐标系
    if len(approx) == 3:
        cv2.putText(img, "Triangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))  # 检测三角形
    elif len(approx) == 4:
        x1, y1, w, h = cv2.boundingRect(approx)  # 检测四边形（分为矩形和正方形）
        aspectRatio = float(w)/h
        print(aspectRatio)
        if 0.95 <= aspectRatio <= 1.05:
            cv2.putText(img, "square", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))  # 检测正方形
        else:
            cv2.putText(img, "rectangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))  # 检测矩形
    elif len(approx) == 5:
        cv2.putText(img, "Pentagon", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))  # 五边形
    elif len(approx) == 6:
        cv2.putText(img, "hexagon", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))  # 六边形
    elif len(approx) == 7:
        cv2.putText(img, "Heptagon", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))  # 七边形
    elif len(approx) == 10:
        cv2.putText(img, "Star", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))  # 星形（十条边）
    else:
        cv2.putText(img, "Circle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))  # 用排除法最后检测为圆形

cv2.imshow("shapes", img)  # 显示后期图像
cv2.waitKey(0)
cv2.destroyAllWindows()  # 必要函数
