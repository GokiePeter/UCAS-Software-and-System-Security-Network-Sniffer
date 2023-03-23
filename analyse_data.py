import variables


def analyse():
    variables.ethernet_header = variables.pack_con[0:14]
    variables.ip_header = variables.pack_con[14:34]
    type_judge = variables.pack_con[23]
    if type_judge == '06':
        variables.tcp_header = variables.pack_con[34:54]
    elif type_judge == '11':
        variables.udp_header = variables.pack_con[34:42]

    variables.des_mac_addr = ':'.join(str(b) for b in variables.ethernet_header[0:6])
    variables.src_mac_addr = ':'.join(str(b) for b in variables.ethernet_header[6:12])
    variables.protocol_type = ':'.join(str(b) for b in variables.ethernet_header[12:14])
    variables.ip_version = ''
    if variables.ip_header[0] == '45':
        variables.ip_version = '4'
    else:
        variables.ip_version = '6'
    variables.ip_header_length = '20'

    variables.diff_service = variables.ip_header[1]
    variables.ip_total_length = str(int(variables.ip_header[2] + variables.ip_header[3], 16))
    variables.ip_identification = variables.ip_header[4] + variables.ip_header[5]
    variables.ip_flags = variables.ip_header[6]
    variables.ip_header_check_sum = "0x" + variables.ip_header[10] + variables.ip_header[11]
    variables.ip_alive_time = str(int(variables.ip_header[8], 16))
    if variables.ip_header[9] == "06":
        variables.ip_in_trans_protocol = "TCP"
    else:
        variables.ip_in_trans_protocol = "UDP"

    variables.ip_src_ip_adrr = '.'.join(str(int(con, 16)) for con in variables.ip_header[12:16])
    variables.ip_des_ip_adrr = '.'.join(str(int(con, 16)) for con in variables.ip_header[16:20])
    if variables.ip_in_trans_protocol == "TCP":
        variables.tcp_src_port = str(int(variables.tcp_header[0] + variables.tcp_header[1], 16))
        variables.tcp_des_port = str(int(variables.tcp_header[2] + variables.tcp_header[3], 16))
        variables.tcp_serial_num = str(
            int(variables.tcp_header[4] + variables.tcp_header[5] + variables.tcp_header[6] + variables.tcp_header[7],
                16))
        variables.tcp_ack_num = str(
            int(variables.tcp_header[8] + variables.tcp_header[9] + variables.tcp_header[10] + variables.tcp_header[11],
                16))

        bin_str = "{0:b}".format(int(variables.tcp_header[12] + variables.tcp_header[13]), 16)

        variables.tcp_header_length = str(int(bin_str[0:4], 2)) + bin_str[0:4]
        variables.tcp_reserved_segment = bin_str[4:10]

        variables.tcp_identification = bin_str[10:16]
        variables.tcp_window_size = str(int(variables.tcp_header[8] + variables.tcp_header[9], 16))
        variables.tcp_check_sum = "0x" + variables.tcp_header[10] + variables.tcp_header[11]
        variables.tcp_urg_pointer = variables.tcp_header[12] + variables.tcp_header[13]
        variables.tcp_opt_segment = ''


    elif variables.ip_in_trans_protocol == "UDP":
        variables.udp_src_port = str(int(variables.udp_header[0] + variables.udp_header[1], 16))
        variables.udp_des_port = str(int(variables.udp_header[2] + variables.udp_header[3], 16))
        variables.udp_length = str(int(variables.udp_header[4] + variables.udp_header[5], 16))
        variables.udp_check_sum = "0x" + variables.udp_header[6] + variables.udp_header[7]


def connect_info():
    ethernet_info = "-------------------------------帧信息-------------------------------\n" + "源MAC地址:" + variables.src_mac_addr + "\n目的MAC地址:" + variables.des_mac_addr + "\n协议类型:" + variables.protocol_type
    tcp_info = ""
    udp_info = ""
    type_judge = variables.pack_con[23]
    ip_info = "\n---------------------------- IP头部信息-----------------------------\n" + "IP头部长度:" + variables.ip_header_length + \
              "\nIP版本号:" + variables.ip_version + "\n区分服务: " + \
              variables.diff_service + "\nIP数据包总长度:" + variables.ip_total_length + "\n标识位:" + variables.ip_identification + \
              "\n标志:" + variables.ip_flags + "\n首部校验和:" + variables.ip_header_check_sum + "\n生存时间:" + variables.ip_alive_time + \
              "\n传输层协议:" + variables.ip_in_trans_protocol + "\n源IP地址:" + variables.ip_src_ip_adrr + "\n目的IP地址:" + variables.ip_des_ip_adrr

    if variables.ip_in_trans_protocol == "TCP":
        tcp_info = "\n----------------------------传输层协议信息--------------------------\n" + "协议类型: TCP\n" + \
                   "源端口号: " + variables.tcp_src_port + "\n目的端口号: " + variables.tcp_des_port + \
                   "\n序列号: " + variables.tcp_serial_num + "\n确认号: " + variables.tcp_ack_num + \
                   "\nTCP头部长: " + variables.tcp_header_length + "\n保留字段: " + variables.tcp_reserved_segment + \
                   "\n标志位: " + variables.tcp_identification + "\n窗口大小: " + variables.tcp_window_size + \
                   "\n校验和: " + variables.tcp_check_sum + "\n紧急指针: " + variables.tcp_urg_pointer + \
                   "\n选项字段: " + variables.tcp_opt_segment
        variables.trans_layer_protocl = tcp_info
    elif variables.ip_in_trans_protocol == "UDP":
        udp_info = "\n----------------------------传输层协议信息--------------------------\n" + "协议类型: UDP\n" + \
                   "源端口号: " + variables.udp_src_port + "\n目的端口号: " + variables.udp_des_port + "\n长度: " + variables.udp_length + \
                   "\nUDP校验和: " + variables.udp_check_sum
        variables.trans_layer_protocl = udp_info
    variables.analyse_info = ethernet_info + ip_info + variables.trans_layer_protocl
