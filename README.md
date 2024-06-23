
一、数据集描述

MNIST数据集是一个经典的计算机视觉数据集，主要用于手写数字识别任务。以下是关于MNIST数据集的简单描述：

1.数据集来源与背景：
来源：该数据集由美国国家标准技术研究所（NIST）整理和标注，于1998年发布。
背景：数据集最初是为了证明在模式识别问题上，基于卷积神经网络（CNN）的方法可以取代基于手工特征的方法而创建的。
2.数据集规模与结构：
数据集包含70,000张28x28像素的灰度图像，其中训练集有60,000张图像，测试集有10,000张图像。
所有图像都是手写数字（0-9）的样本。
3.标注信息：
每张图像都带有标注，标注信息是0到9之间的一个数字，表示图像中的手写数字。
4.数据集应用：
MNIST数据集是机器学习和深度学习领域中最受欢迎的数据集之一，被广泛应用于各种图像分类算法的训练和测试。
它常被用作入门级的计算机视觉任务，帮助研究者和开发者了解图像识别算法的基本原理和性能评估。
5.数据预处理：
在使用MNIST数据集进行模型训练之前，通常需要进行一些预处理步骤，如数据归一化（将像素值缩放到0-1之间）和数据展开（将28x28的图像展平为784维的向量）。
6.模型性能：
MNIST数据集相对简单，许多算法和模型在该数据集上都能取得较好的性能。

![image](https://github.com/fengyarui1/Handwritten-digit-recognition/assets/163635050/f86ad819-8e7a-47bf-bdf1-d752a2b0766e)# Handwritten-digit-recognition
图 1以下是所使用的MNIST数据集

7.调用数据集：
在getData.py中
import input_data # 调用input_data
mnist = input_data.read_data_sets('MNIST_data/', one_hot=True)
print('type of "mnist" is %s' % (type(mnist)))#获取训练数据的类型
print('number of train data is %d' % (mnist.train.num_examples))#输出训练数据多少个
print('number of test data is %d' % (mnist.test.num_examples))#输出测试数据有多少个



二、工具描述

Python中的tkinter库是用于创建图形用户界面（GUI）应用程序的标准库。以下是关于tkinter库的简单描述，按照清晰的结构进行分点表示和归纳：

1.概述：
tkinter是Python的标准GUI库，它允许开发者使用Python代码创建跨平台的GUI应用程序。
作为Python标准库的一部分，它无需额外安装，可以直接在Python环境中使用。
2.主要功能：
创建GUI界面：tkinter可以用来创建基本的图形用户界面，包括窗口、按钮、文本框等。
添加组件：提供了各种可视化组件，如按钮（Button）、标签（Label）、文本框（Entry）、列表框（Listbox）等，用于构建用户界面。
布局管理：提供了几种布局管理器，如pack、grid和place，用于控制组件在窗口中的位置和大小。
事件处理：支持事件处理机制，允许开发者为控件绑定事件处理函数，以响应用户的操作，如点击按钮或键盘输入。
3.特点：
简单易学：tkinter提供了简单的API和易于理解的语法，使得初学者可以快速上手开发GUI应用程序。
跨平台性：tkinter是跨平台的，可以在多个操作系统上运行，包括Windows、macOS和Linux等。
内置控件丰富：tkinter提供了许多常见的GUI控件，可以方便地创建各种GUI界面。
4.示例组件：
Label：用于显示文本或图像的标签。
Button：用户可点击的按钮，可以绑定点击事件。
Entry：单行文本框，用于接收用户输入。
Text：多行文本框，支持更复杂的文本编辑和显示。
Listbox：列表框，用于显示可选择的列表项。

tkinter是Python中用于创建GUI应用程序的重要库，它提供了丰富的控件和布局管理器，支持事件处理机制，并且具有简单易学和跨平台的特点。无论是初学者还是经验丰富的开发者，都可以使用tkinter来快速构建交互式的图形界面应用程序。

在PyCharm中可以直接安装，打开终端输入pip install tkinter即可。






三、方法描述

1.图像处理-Pillow

Pillow是一个Python图像处理库，由Python Imaging Library（PIL）的一个分支演变而来。Pillow提供了广泛的图像处理功能，包括但不限于图像的打开、操作和保存。通过使用Pillow，用户可以轻松地进行图像的缩放、裁剪、旋转、颜色转换以及应用各种图像滤镜等操作。此外，Pillow还支持图像格式的转换，如将JPEG图像转换为PNG格式。由于其强大的功能和易用性，Pillow已成为Python社区中广泛使用的图像处理库之一。


2.深度学习-卷积神经网络

卷积神经网络（Convolutional Neural Network，CNN）是一种在计算机视觉领域取得了巨大成功的深度学习模型。它们的设计灵感来自于生物学中的视觉系统，旨在模拟人类视觉处理的方式。在过去的几年中，CNN已经在图像识别、目标检测、图像生成和许多其他领域取得了显著的进展，成为了计算机视觉和深度学习研究的重要组成部分。

(1)图像原理
图像在计算机中是一堆按顺序排列的数字，数值为0到255。0表示最暗，255表示最亮。 如下图：、

![image](https://github.com/fengyarui1/Handwritten-digit-recognition/assets/163635050/5bb94b71-bf12-455f-bd50-3de8a5d95f7a)
图 2图像原理
上图是只有黑白颜色的灰度图，而更普遍的图片表达方式是RGB颜色模型，即红、绿、蓝三原色的色光以不同的比例相加，以产生多种多样的色光。RGB颜色模型中，单个矩阵就扩展成了有序排列的三个矩阵，也可以用三维张量去理解。
其中的每一个矩阵又叫这个图片的一个channel（通道），宽, 高, 深来描述。

(2)什么是卷积神经网络？
在传统神经网络中，我们要识别下图红色框中的图像时，我们很可能识别不出来，因为这六张图的位置都不通，计算机无法分辨出他们其实是一种形状或物体。



 传统神经网络原理如下图：
![image](https://github.com/fengyarui1/Handwritten-digit-recognition/assets/163635050/9e4b8090-eac1-4a69-add7-40637431b664)

图 3传统神经网络原理
我们希望一个物体不管在画面左侧还是右侧，都会被识别为同一物体，这一特点就是不变性。为了实现平移不变性，卷积神经网络（CNN）等深度学习模型在卷积层中使用了卷积操作，这个操作可以捕捉到图像中的局部特征而不受其位置的影响。

(3)什么是卷积？
在卷积神经网络中，卷积操作是指将一个可移动的小窗口（称为数据窗口，如下图绿色矩形）与图像进行逐元素相乘然后相加的操作。这个小窗口其实是一组固定的权重，它可以被看作是一个特定的滤波器（filter）或卷积核。这个操作的名称“卷积”，源自于这种元素级相乘和求和的过程。这一操作是卷积神经网络名字的来源。
简而言之，卷积操作就是用一个可移动的小窗口来提取图像中的特征，这个小窗口包含了一组特定的权重，通过与图像的不同位置进行卷积操作，网络能够学习并捕捉到不同特征的信息。
![image](https://github.com/fengyarui1/Handwritten-digit-recognition/assets/163635050/f31d4eda-d5f4-43fe-aa46-7fc1eeec4aa1)

图 4卷积过程

(4)卷积神经网络的构造

1)输入层
输入层接收原始图像数据。图像通常由三个颜色通道（红、绿、蓝）组成，形成一个二维矩阵，表示像素的强度值。
2)卷积和激活
卷积层将输入图像与卷积核进行卷积操作。然后，通过应用激活函数（如ReLU）来引入非线性。这一步使网络能够学习复杂的特征。
3)池化层
池化层通过减小特征图的大小来减少计算复杂性。它通过选择池化窗口内的最大值或平均值来实现。这有助于提取最重要的特征。
4)多层堆叠
CNN通常由多个卷积和池化层的堆叠组成，以逐渐提取更高级别的特征。深层次的特征可以表示更复杂的模式。
5)全连接和输出
最后，全连接层将提取的特征映射转化为网络的最终输出。这可以是一个分类标签、回归值或其他任务的结果。


































四、识别手写字体

1.手写字体图片

首先在电脑自带的画图工具中，通过调整图片属性改变像素为28*28，用画笔工具书写数字0-9，并依次保存在文件夹中。
在程序设计的进程中，识别的图片都是28*28像素的，同时也考虑到了识别多个数字的可能，因此在书写多个数字时，也要严格按照每个数字都是28*28像素的。因此n个数字的图片的像素为28n*28像素。

2.识别单个图片

在上一节的介绍中，每个图片都是通过卷积池化后来识别的，简单来说就是通过识别每张图片每个数字的轮廓，再通过对MNIST库的深度学习后进行比对，找到相似的数字最后输出结果。因为只是相似，所以在识别数字的过程中难免出现差错，这也在意料之内。
在testImg.py中，convolute_pool(img)函数就是卷积池化的过程，最后这个函数返回predint[0]的值就是识别的数字。


![image](https://github.com/fengyarui1/Handwritten-digit-recognition/assets/163635050/d6515774-f541-4434-ace7-aac4cec4536b)
![image](https://github.com/fengyarui1/Handwritten-digit-recognition/assets/163635050/dc33ec5f-42be-4652-8d54-f410a198bd47)

图 5所要识别的图片和卷积池化后的图片


3.识别多个图片

考虑到程序每次只能识别一个数字，那么是否能识别多个数字呢？
在第一段其实就说了通过图画工具来写多个数字，而且n个数字的图片像素必须严格为28n*28。那么我们很快就能想到识别多个数字也就是把n个数字图片等分为n个28*28像素的小图片，通过调用testImg.py来依次识别。
那么切割图片的工作就由cutPic.py来完成。
![image](https://github.com/fengyarui1/Handwritten-digit-recognition/assets/163635050/d4964905-3859-41f1-ad6f-19f955dc7c3d)

图 6cut（）函数

切割完的小图片都保存在了pic文件夹中。
![image](https://github.com/fengyarui1/Handwritten-digit-recognition/assets/163635050/5d74423e-a9cc-4b46-8907-467fbce2a538)

图 7被切割成4个小图片















五、GUI界面的设计

设计GUI界面主要是为了用户使用程序更加便捷高效。如果没有一个界面而只是呈现大段代码，那么除了对于设计者来说，其他人除非找到了输入输出的部分，才能够运行设计好的程序。那么在我的设计初期，就构思用户是否能直接打开图片，就能显示识别的数字。

1.界面描述

首先，打开界面会有一个欢迎提示。在页面中间会有一个按钮供用户打开图片。其次，在识别完图片之后，会将结果输出到界面中。最后，考虑到整体的美观，添加一些内容，把识别的图片也呈现在屏幕上。

2.代码讲解

GUI界面的代码为imgGUI.py。
(1)函数process_image()
这个函数是将识别分割好的图片依次呈现到屏幕上的。在设想这一步的初期，预期是可以每打开一次图片就可以呈现一次分割好图片的内容，但是在完成第一次识别后，第二次识别完成后的图片堆叠在第一次的结果上了。那么就通过遍历 image_container的所有子元素并销毁它们，来清除旧的图片，这样每次识别就只输出新的内容了。
![image](https://github.com/fengyarui1/Handwritten-digit-recognition/assets/163635050/bc9b98eb-87b0-4f52-96d9-be019beb354f)

图 8更新输出内容

在识别自己写好的数字图片的时候，有时候会报错“cannot write mode RGBA as JEPG”，添加这段代码“img = Image.open(img_path).convert('RGB')”，将图片转换为RGB模式。

(2)函数show_result()
在每张识别分割好的图片后添加识别的结果。

(3)函数open_image_file()
打开图片路径。

(4)函数create_gui()
设计一个Label显示欢迎界面。设计一个按钮调用open_image_file()来打开图像。


3.效果呈现
(1)打开界面
![image](https://github.com/fengyarui1/Handwritten-digit-recognition/assets/163635050/4957fe91-3738-4e78-bd83-94a0e39c6167)


(2)点击按钮打开文件夹
![image](https://github.com/fengyarui1/Handwritten-digit-recognition/assets/163635050/6a41294c-00b4-4966-b477-8d457920e4b0)


(3)识别单个数字
![image](https://github.com/fengyarui1/Handwritten-digit-recognition/assets/163635050/35ca9d83-6fcf-4fb5-927c-02b98ba156f3)



(4)识别多个数字
![image](https://github.com/fengyarui1/Handwritten-digit-recognition/assets/163635050/e17bf68e-2df3-4496-91d9-b66b6d9962df)
![image](https://github.com/fengyarui1/Handwritten-digit-recognition/assets/163635050/c75b47d0-2e5b-4e91-94f9-f587db5d6b59)




(5)pic文件夹的更新
![image](https://github.com/fengyarui1/Handwritten-digit-recognition/assets/163635050/48f4a7da-da16-476f-87c2-546ac77bdca6)








六、参考资料

源代码参考：
https://github.com/NH4L/handwrittenNumberRecognition
https://github.com/fz007-hhh/MyHandWriting
卷积神经网络的讲解：
https://blog.csdn.net/Morganfs/article/details/124121625
修改图片尺寸和像素工具：
https://www.gaitubao.com/
