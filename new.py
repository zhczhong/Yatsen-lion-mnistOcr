import matplotlib.pyplot as plt
import pylab
import cv2
import numpy as np
from PIL import Image

def __getYData(data,y1,y2):
    """
    y1必须小于y2
    获取data数组内，第1个维度y1-y2的数据
    返回一个numpy数组,shape = [y2-y1][len(data[0])]
    """
    w,h = data.shape
    back_data = np.zeros((y2-y1,len(data[0])))
    y_index = 0
    while y_index != y2 - y1:
        for x in range(h):
            back_data[y_index][x] = data[y_index + y1][x]
        y_index += 1
    return back_data

def __getXData(data,x1,x2):
    """
    x1必须小于x2
    获取data数组内，第2个维度x1-x2的数据
    返回一个numpy数组,shape = [len(data)][x2-x1]
    """
    w,h = data.shape
    back_data = np.zeros((len(data),x2-x1))
    x_index = 0
    while x_index != x2 - x1:
        for y in range(w):
            back_data[y][x_index] = data[y][x_index + x1]
        x_index += 1
    return back_data
    

def findWordRect(img,min_height = 12):
    """
    img为需要处理的图像
    min_height 为字符区域的最小高度
    返回参数为一个字典的列表
    字典内:
    'x1','y1'为左上角坐标
    'x2','y2'为右下角坐标
    """
    # 获取图像大小
    w,h = img.size
    img = img.getdata()
    img = np.array(img,dtype = np.uint8)
    img = np.reshape(img,(h,w,3))
    # debug
    # print(w,h)
    # 显示读取的图片
    # plt.imshow(img)                                    
    # pylab.show()
    # 设置是卷积核
    fil = np.array([[ 0,-1, 0],                        
                    [ -1, 4, -1],
                    [  0, -1, 0]])
    #使用opencv的卷积函数
    res = cv2.filter2D(img,-1,fil) 
    img = Image.fromarray(res)
    img = img.convert('L')
    # debug
    # img.show()
    data = img.getdata()
    data = np.array(data,dtype = np.uint8)
    data = np.reshape(data,(h,w))
    # x_data = np.zeros((w,1))
    y_data = np.zeros((h,1))
    for x_line in range(w):
        for y_line in range(h):
            # x_data[x_line] += data[y_line][x_line]
            y_data[y_line] += data[y_line][x_line]
    # debug
    #print(x_data)
    #print(y_data)
    sum = 0
    for i in range(h):
        sum += y_data[i]
    # arg_x = sum / w
    arg_y = sum / h
    y_result = []
    # 字符区块的最大高度
    # 区域越黑则值越大
    max_height = 0
    for i in range(h):
        if arg_y > y_data[i]:
            if max_height >= min_height:
                y_result.append({'y1':i - max_height,'y2' : i})
            max_height = 0
            continue
        else:
            max_height += 1           
    result = []
    for one_dic in y_result:
        d = __getYData(data,one_dic['y1'],one_dic['y2'])
        check_d = np.zeros((w,1))
        for x in range(w):
            for y in range(one_dic['y2']-one_dic['y1']):
                check_d[x] += d[y][x]
        for i in range(w):
            if check_d[i] > w/h:
                for j in range(w):
                    if check_d[w-j-1] > w/h:
                        result.append({'x1':i,'y1':one_dic['y1'],'x2':w-j-1,'y2':one_dic['y2']})
                        break
                    else:
                        continue
                break
            else:
                continue
    return result

if __name__ == '__main__':
    e1 = cv2.getTickCount()
    img = Image.open("1.jpg")
    result = findWordRect(img)
    e2 = cv2.getTickCount()
    time = (e2 - e1)/ cv2.getTickFrequency()
    print(result)
    print(time)
    for one_dic in result:
        new_img = img.crop((one_dic['x1'],one_dic['y1'],one_dic['x2'],one_dic['y2']))
        new_img.show()
