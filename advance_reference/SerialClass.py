import serial
import serial.tools.list_ports
import binascii


class SerialAchieve:
    def __init__(self,band=115200,check="无校验位",data=8,stop=1):
        self.port = None
        # 获取可用串口
        self.port_list = list(serial.tools.list_ports.comports())
        assert (len(self.port_list) != 0),"无可用串口"

        self.bandRate = band
        self.checkbit = check
        self.databit = data
        self.stopbit = stop

        # 读写的数据
        self.read_data = None
        self.write_data = None

        pass
    def show_port(self):
        for i in range(0,len(self.port_list)):
            print(self.port_list[i])

    def show_other(self):
        print("波特率："+self.bandRate)
        print("校验位：" + self.checkbit)
        print("数据位：" + self.databit)
        print("停止位：" + self.stopbit)
    # 返回串口
    def get_port(self):
        return self.port_list
    # 打开串口
    def open_port(self,port):
        self.port = serial.Serial(port, self.bandRate,timeout = None)

    def delete_port(self):
        if self.port != None:
            self.port.close()
            print("关闭串口完成")
        else:
            pass

    def Read_data(self):   # self.port.read(self.port.in_waiting) 表示全部接收串口中的数据
        # self.read_data = self.port.read(self.port.in_waiting)   # 读取数据
        # print("call Read_data()")
        self.read_data = str(binascii.b2a_hex(self.port.read(self.port.inWaiting())))[2:-1]
        # return self.read_data.decode("utf-8")
        # print("返回数据：", self.read_data)
        return self.read_data
    def Write_data(self,data):
        if self.port.isOpen() == False:
            print("串口打开错误")
        else:
            print("发送数据：", bytes.fromhex(data))
            # self.port.write(data.encode("utf-8"))  # 返回的是写入的字节数
            self.port.write(bytes.fromhex(data))
if __name__ == '__main__':
    myser = SerialAchieve()
    myser.open_port("COM5")
    myser.delete_port()
    myser.show_port()



