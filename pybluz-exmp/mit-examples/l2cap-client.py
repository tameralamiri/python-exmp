
import bluetooth

sock=bluetooth.BluetoothSocket(bluetooth.L2CAP)

bd_addr = "00:01:95:1A:9E:03"
port = 0x1001

sock.connect((bd_addr, port))

sock.send("hello!!")

sock.close()
