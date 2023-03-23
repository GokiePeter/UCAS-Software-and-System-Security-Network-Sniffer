import tkinter as tk
import variables
from winpcapy import WinPcapDevices

# print("---------------网卡-------------------")

with WinPcapDevices() as devices:
    for device in devices:
        print("网卡名：" + str(device.name), "   网卡描述信息：" + str(device.description))
        str_network_card = str(device.description)
        variables.network_card_info_list.append(str(str_network_card[2:len(str_network_card) - 1]))


def get_network_card_info():
    network_info = tk.Tk()
    network_info.title("提示：")
    network_info.geometry("400x350+550+200")
    lf = tk.LabelFrame(network_info, text="请双击选择嗅探网卡:", width=420, height=350, relief='groove', bd=2)
    lf.pack()

    network_info.propagate(False)

    net_info_box = tk.Listbox(lf, width=50, height=15, selectmode='singe', activestyle='none')
    for item in variables.network_card_info_list:
        net_info_box.insert(tk.END, item)
    net_info_box.propagate(False)
    net_info_box.pack()

    def selected_item(event):
        if len(net_info_box.curselection()) != 0:
            # print(net_info_box.curselection(), type(net_info_box.curselection()))
            # print(net_info_box.get(net_info_box.curselection()))
            variables.which_is_checked = net_info_box.get(net_info_box.curselection())

    net_info_box.bind('<Double-Button-1>', selected_item)

    def clo_win():
        network_info.destroy()

    tk.Button(lf, text="确定", command=clo_win).pack()

    network_info.mainloop()


def close_widow(root):
    root.protocol('WM_DELETE_WINDOW', root.destroy)


def set_value(num):
    variables.which_is_checked = num
