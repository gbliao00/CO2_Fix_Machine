import serial
ser=serial.Serial('COM3', 9600, timeout=1)
ser.write("S\r\n".encode())
ser.read(22) # 小括號內可以填入一次要讀取的byte數
result=ser.read(22)
print(result)
ser.write("E\r\n".encode())
ser.close()
