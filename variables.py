which_is_checked = ''
which_pack_is_selected = ''
which_partern = ''
scratch_data = []
network_card_info_list = []
header_info = []
wait = False
pack_con = []
stop = False
available = 10
dict = {}
dict_keys = []
scracth_countor = 0
des_context = ""

analyse_info = ""

cur_dir = ""
save_data_file_name = ''
# 解析数据包内容所需字段

ethernet_header = ""
des_mac_addr = ""
src_mac_addr = ""
protocol_type = ""

ip_header = ""
ip_version = ""
ip_header_length = ""
diff_service = ""
ip_total_length = ""
ip_identification = ""
ip_flags = ""
ip_header_check_sum = ""
ip_alive_time = ""
ip_in_trans_protocol = ""
ip_src_ip_adrr = ""
ip_des_ip_adrr = ""

trans_layer_protocl = ""

tcp_info = ""
# TCP报文头部
tcp_header = ""
# TCP源端口
tcp_src_port = ""
# TCP目的端口
tcp_des_port = ""
# 序列号
tcp_serial_num = ""
# 确认号
tcp_ack_num = ""
# tcp报文头长度
tcp_header_length = ""
# 保留字段
tcp_reserved_segment = ""
# 标志符
tcp_identification = ""
# 拥塞控制窗口大小
tcp_window_size = ""
# 校验和
tcp_check_sum = ""
# 紧急指针
tcp_urg_pointer = ""
# 选择字段
tcp_opt_segment = ""

udp_header = ""

udp_src_port = ""
udp_des_port = ""

# udp_length是包括udp头部长度和udp数据长度
udp_length = ""
udp_check_sum = ""

# Intel(R) Wi-Fi 6E AX211 160MHz
