import tkinter as tk
from tkinter import ttk
import psutil

def search_ports():
    keyword = entry.get()
    result_text.delete(1.0, tk.END)

    connections = psutil.net_connections()
    for conn in connections:
        if conn.status == 'LISTEN':
            local_address = conn.laddr
            pid = conn.pid

            try:
                process = psutil.Process(pid)
                process_name = process.name()
                port = str(local_address.port)

                if keyword.lower() in process_name.lower() or keyword == port:
                    result_text.insert(tk.END, f"端口: {port}  进程名: {process_name}\n")
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass

# 创建主窗口
window = tk.Tk()
window.title("端口进程检索")

# 创建标签和输入框
label = tk.Label(window, text="请输入进程名称或者端口号:")
label.pack()

# 创建一个框架来容纳输入框和按钮
frame = tk.Frame(window)
frame.pack(pady=10)

entry = tk.Entry(frame)
entry.pack(side=tk.LEFT, padx=5)

# 创建搜索按钮
button = tk.Button(frame, text="Search", command=search_ports)
button.pack(side=tk.LEFT, padx=5)

# 创建结果文本框和滚动条
result_frame = tk.Frame(window)
result_frame.pack()

scrollbar = ttk.Scrollbar(result_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

result_text = tk.Text(result_frame, yscrollcommand=scrollbar.set)
result_text.pack()

scrollbar.config(command=result_text.yview)

# 默认显示全部端口信息
search_ports()

# 运行主循环
window.mainloop()
