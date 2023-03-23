import threading
import scratch_data
from winpcapy import WinPcapUtils


def start():
    # print(threading.current_thread())
    t = threading.Thread(target=scratch_data.start)
    t.setDaemon(True)
    t.start()


def stop():
    WinPcapUtils.stop
