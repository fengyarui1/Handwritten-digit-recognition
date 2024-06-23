from PIL import Image
import tensorflow as tf
from matplotlib import pyplot as plt
import cutPic
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

def imageprepare(img):
    img = Image.open(img) #读取图片，路劲为相对路径，注意是28*28像素
    plt.imshow(img)  #显示需要识别的图片
    #plt.show()
    img = img.convert('L')    #RGB转成灰色
    tv = list(img.getdata())#返回img的像素序列
    tva = [(255-x)*1.0/255.0 for x in tv]#得到每一个像素点的灰度，最大1为黑，最小0为白
    return tva


def weight_variable(shape):
    initial = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial)


def bias_variable(shape):
    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial)


def conv2d(x, W):
    return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')


def max_pool_2x2(x):
    return tf.nn.max_pool(x, ksize=[1,2,2,1], strides=[1, 2, 2, 1], padding='SAME')


def convolute_pool(img):
    tf.reset_default_graph()
    result = imageprepare(img)

    x = tf.placeholder(tf.float32, [None, 784])
    y_ = tf.placeholder(tf.float32, [None, 10])
    # 第一层卷积
    W_conv1 = weight_variable([5, 5, 1, 32])
    b_conv1 = bias_variable([32])

    x_image = tf.reshape(x, [-1, 28, 28, 1])

    h_conv1 = tf.nn.relu(conv2d(x_image, W_conv1) + b_conv1)
    h_pool1 = max_pool_2x2(h_conv1)

    # 第二层卷积
    W_conv2 = weight_variable([5, 5, 32, 64])
    b_conv2 = bias_variable([64])

    h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) + b_conv2)
    h_pool2 = max_pool_2x2(h_conv2)

    # 密集卷积层
    W_fc1 = weight_variable([7 * 7 * 64, 1024])
    b_fc1 = bias_variable([1024])

    h_pool2_flat = tf.reshape(h_pool2, [-1, 7 * 7 * 64])
    h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)

    # dropout
    rate = 1-tf.placeholder("float")
    h_fc1_drop = tf.nn.dropout(h_fc1, rate)

    # 输出
    W_fc2 = weight_variable([1024, 10])
    b_fc2 = bias_variable([10])

    y_conv = tf.nn.softmax(tf.matmul(h_fc1_drop, W_fc2) + b_fc2)  # 添加softmax层

    # 模型评估
    cross_entropy = -tf.reduce_sum(y_ * tf.log(y_conv))
    train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)
    correct_prediction = tf.equal(tf.argmax(y_conv, 1), tf.argmax(y_, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))

    saver = tf.train.Saver()  # 定义saver

    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        saver.restore(sess, 'SAVE/model.ckpt')

        prediction = tf.argmax(y_conv, 1)  # 返回对于y_conv预测到的标签值，与真实标签相比较比较是否匹配
        predint = prediction.eval(feed_dict={x: [result], rate: 1.0}, session=sess)  # 得出测试的结果
        return predint[0]






