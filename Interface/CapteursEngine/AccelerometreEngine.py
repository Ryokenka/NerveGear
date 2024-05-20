import serial


ser = serial.Serial('COM7', 115200, timeout=0.5)

while True:
	data = ser.readline().decode('utf-8').strip()
	print(data)

ser.close()