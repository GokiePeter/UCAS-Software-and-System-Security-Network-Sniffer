import datetime
import os
import tkinter as tk
from random import random
from tkinter.messagebox import showinfo
import variables


def about_us():
    about = tk.Tk()
    about.withdraw()
    showinfo("提示", "欢迎使用Network Sniffer！")


def save_file():
    variables.cur_dir = os.path.abspath('.')
    variables.save_data_file_name = datetime.datetime.now().strftime('%Y-%m-%d-T') + '-R1-' + str(
        int(random() * 1000)) + '-R2-' + str(int(random() * 1000)) + '.txt'
    con_list = list(variables.dict.values())
    save_data_file = open(variables.save_data_file_name, 'w')
    con_list_length = len(con_list)
    if con_list_length != 0:
        for index in range(con_list_length):
            save_data_file.write(str(con_list[index]))
            save_data_file.write('\n')
    con_list.clear()
    save_data_file.close()


def saved_note():
    save_file()
    save_note_pad = tk.Tk()
    save_note_pad.withdraw()
    print("本次数据已保存到:\n" + variables.cur_dir + "\\" + "\n" + variables.save_data_file_name)
    showinfo("提示", "本次数据已保存到:\n" + variables.cur_dir + "\n\\" + variables.save_data_file_name)
