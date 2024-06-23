from PIL import Image


def cut(img_file, dx, dy):#dx,dy分别表示宽度和高度
    img = Image.open(img_file)
    n = 1
    x1 = 0
    y1 = 0
    x2 = dx
    y2 = dy#定义坐标
    while x2 <= img.size[1]:#纵向，控制x1,x2
        while y2 <= img.size[0]:#横向,控制y1,y2
            new_pic = 'pic/pic' + str(n) + '.jpg'
            img2 = img.crop((y1, x1, y2, x2))
            img2.save(new_pic)
            y1 += dy
            y2 = y1 + dy
            n += 1

        x1 = x1 + dx
        x2 = x1 + dx
        y1 = 0
        y2 = dy#当完成一行图像的切割后，重置 y1 和 y2 并增加 x1 和 x2，以开始下一行的切割。
    return n - 1#函数返回 n - 1，即切割出的图像数量。


def main(img):

    #img = 'testPic.jpg'
    n = cut(img, 28, 28)
    return n



