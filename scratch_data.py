from time import sleep
from winpcapy import WinPcapUtils

import variables


def packet_callback(win_pcap, param, header, pkt_data):
    dmac = ":".join(["%02x" % (b) for b in pkt_data[6:12]])
    smac = ":".join(["%02x" % (b) for b in pkt_data[0:6]])

    ip_frame = pkt_data[14:]
    src_ip = ".".join([str(b) for b in ip_frame[0xc:0x10]])
    dst_ip = ".".join([str(b) for b in ip_frame[0x10:0x14]])

    raw_data = ['%02X' % i for i in pkt_data]
    print("\n数据包内容", len(raw_data), "Bytes")
    print(raw_data)
    variables.scratch_data.append(raw_data)
    variables.scracth_countor = variables.scracth_countor + 1
    # variables.header_info.append(str("源MAC: " + smac+"  目的MAC: " + dmac+"   源IP: " + src_ip+"    目的IP:" + dst_ip))
    dict_key = str(
        str(variables.scracth_countor) + ": 源MAC: " + smac + " 目的MAC: " + dmac + " 源IP: " + src_ip + " 目的IP:" + dst_ip)
    variables.dict[dict_key] = raw_data
    print("\n数据流向")
    print(str(variables.scracth_countor) + "源MAC: " + smac, "    目的MAC: " + dmac, "   源IP: " + src_ip,
          "    目的IP:" + dst_ip)
    sleep(1)


def start():
    WinPcapUtils.capture_on(variables.which_is_checked, packet_callback)
