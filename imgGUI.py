import tkinter as tk
from tkinter import filedialog, messagebox, Label, Frame,font
from PIL import Image, ImageTk

# 假设 convolute_pool 函数存在于 testImg.py 中，并且它执行图像处理
from testImg import convolute_pool
from cutPic import main


def process_image(root, image_path):
    try:
        for widget in image_container.winfo_children():
            widget.destroy()
        n = main(image_path)  # 切割图片并返回数量
        for i in range(1, n + 1):
            img_path = 'pic/pic' + str(i) + '.jpg'
            # 打开图片并立即转换为RGB模式
            img = Image.open(img_path).convert('RGB')
            photo = ImageTk.PhotoImage(img)

            # 创建一个新的 Frame 来放置图片和结果
            frame = Frame(image_container)
            frame.pack(side=tk.TOP, fill=tk.X, pady=10)

            # 创建一个 Label 来显示图片
            image_label = Label(frame, image=photo)
            image_label.image = photo  # 保持对图片的引用，防止被垃圾回收
            image_label.pack(side=tk.LEFT, padx=10, pady=10)

            # 调用 convolute_pool 对图片进行识别，并显示结果
            result = convolute_pool(img_path)
            show_result(frame, result, i)
    except Exception as e:
        messagebox.showerror("Error", str(e))


def show_result(frame, result, img_num):
    # 创建一个 Label 来显示结果
    result_label = Label(frame, text=f"图片 {img_num} 识别的数字为：{result}")
    result_label.pack(side=tk.LEFT, padx=10, pady=10)


def open_image_file():
    file_path = filedialog.askopenfilename(filetypes=[("JPEG files", "*.jpg;*.jpeg")])
    if file_path:
        process_image(root, file_path)


def create_gui():
    global root,image_container
    root = tk.Tk()
    root.title("手写体数字识别")
    root.geometry("400x450")  # 调整窗口大小以适应多张图片
    # 添加一个标题Label
    title_font = font.Font(family='Helvetica', size=16, weight='bold')
    title_label = tk.Label(root, text="欢迎使用手写体数字识别！",font=title_font)
    title_label.pack(pady=20)  # 设置垂直间距
    # 创建一个按钮来打开图像文件
    button = tk.Button(root, text="点击按钮打开图像", command=open_image_file)
    button.pack(pady=20)
    # 创建一个容器来持有图片和结果的 Frame
    image_container = Frame(root)
    image_container.pack(fill=tk.BOTH, expand=True, pady=(20,0))  # 使其填充整个窗口


    root.mainloop()


if __name__ == '__main__':
    create_gui()