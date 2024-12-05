import os

def open_firewall_port(port, name="OpenPort", protocol="TCP"):
    command = f'netsh advfirewall firewall add rule name="{name}" dir=in action=allow protocol={protocol} localport={port}'
    result = os.system(command)
    if result == 0:
        print(f"Cổng {port} đã được mở thành công trên Firewall!")
    else:
        print("Đã xảy ra lỗi khi mở cổng.")

if __name__ == "__main__":
    port = input("Nhập số cổng cần mở: ")
    name = input("Nhập tên quy tắc (mặc định: OpenPort): ") or "OpenPort"
    protocol = input("Nhập giao thức (TCP/UDP, mặc định: TCP): ") or "TCP"
    open_firewall_port(port, name, protocol)