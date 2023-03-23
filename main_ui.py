import tkinter as tk
import variables
import menu_item
import get_network_info
import start_or_stop_scratch
import analyse_data


class Sniffer_UIs:
    root = tk.Tk()
    plist = tk.LabelFrame(root, text="数据流向", width=650, height=800, relief='groove', bd=2)
    p = tk.LabelFrame(root, text="原始数据", width=520, height=400, relief='groove', bd=2)
    des = tk.LabelFrame(root, text="协议详解", width=520, height=400, relief='groove', bd=2)
    plist_y_srcoll = tk.Scrollbar(plist, orient=tk.VERTICAL)
    lst_box = tk.Listbox(plist, bd=1, relief="groove", selectborderwidth=2, width=650, height=800,
                         listvariable=tk.StringVar(value=variables.header_info), activestyle="none", selectmode='singe')
    p_data_box = tk.Text(p, width=68, height=40, selectbackground="black")
    des_text = tk.Text(des, width=68, height=40)
    p_y_srcoll = tk.Scrollbar(p, orient=tk.VERTICAL)

    des_y_scroll = tk.Scrollbar(des, orient=tk.VERTICAL)

    def init_root(self):
        self.root.geometry('1200x800+200+30')  # '1200x800'
        self.root.resizable(width=False, height=False)
        m = tk.Menu(self.root)
        m.add_command(label="  保存文件  ", font=("黑体", 20, "bold"), command=menu_item.saved_note)
        m.add_command(label="  选择网卡  ", command=get_network_info.get_network_card_info)
        m.add_command(label="  开始嗅探  ", command=start_or_stop_scratch.start)
        m.add_command(label="  点击刷新  ", command=self.lst_box_update_display)
        m.add_command(label="关于软件", command=menu_item.about_us)
        self.root['menu'] = m  # 附加主菜单到窗口
        self.root.title('Network Sniffer')
        self.plist.place(x=0, y=0)
        self.plist.pack(side=tk.RIGHT, fill="y")
        self.plist.propagate(False)

        self.plist_y_srcoll.config(command=self.lst_box.yview)
        self.lst_box.config(yscrollcommand=self.plist_y_srcoll.set)
        self.plist.pack(side=tk.LEFT)
        self.lst_box.pack()
        self.plist_y_srcoll.pack(side=tk.RIGHT, fill="y")
        self.p_y_srcoll.pack(side=tk.RIGHT, fill="y")

        # ---------------------------------------------
        def selected_item_ip(event):
            if len(self.lst_box.curselection()) != 0:
                variables.which_pack_is_selected = self.lst_box.get(self.lst_box.curselection())
                self.analyse_packet()

        self.lst_box.bind('<Button-1>', selected_item_ip)

        self.p_data_box.config(yscrollcommand=self.p_y_srcoll.set)
        self.p_y_srcoll.config(command=self.p_data_box.yview)
        self.p_data_box.pack(side=tk.LEFT)
        self.p.pack()
        self.p.propagate(False)
        self.p_data_box.insert("insert", variables.pack_con)
        self.des_text.insert("insert", variables.analyse_info)

        self.des_y_scroll.pack(side=tk.RIGHT, fill="y")
        self.des_text.config(yscrollcommand=self.des_y_scroll.set)
        self.des_y_scroll.config(command=self.des_text.yview)

        self.des_text.pack()
        self.des.pack()
        self.des.propagate(False)

        self.root.mainloop()

    def lst_box_update_display(self):
        # print('正在刷新数据 。。。')

        self.lst_box.delete(0, tk.END)
        variables.dict_keys.clear()

        variables.dict_keys = list(variables.dict.keys())
        for index in range(len(variables.dict_keys)):
            self.lst_box.insert(tk.END, variables.dict_keys[index])
        self.lst_box.update()

    def p_con_update_display(self):
        variables.pack_con = variables.dict.setdefault(variables.which_pack_is_selected)
        # pack_data_len = len(variables.pack_con)
        # for index in range(pack_data_len):
        #     if index%12 == 0:

        self.p_data_box.delete('1.0', tk.END)
        self.p_data_box.insert(tk.END, variables.pack_con)
        self.p_data_box.update()

    def des_txt_update_display(self):
        analyse_data.analyse()
        analyse_data.connect_info()
        self.des_text.delete('1.0', tk.END)
        self.des_text.insert('insert', variables.analyse_info)
        self.des_text.update()

    def analyse_packet(self):
        self.p_con_update_display()
        self.des_txt_update_display()


if __name__ == '__main__':
    mu = Sniffer_UIs()
    mu.init_root()
