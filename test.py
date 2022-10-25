from pymodbus.client.sync import ModbusTcpClient
from pymodbus.transaction import ModbusRtuFramer as ModbusFramer

client = ModbusTcpClient("192.168.1.254", port=8880, framer=ModbusFramer)
success = client.connect()
def Get_Data_Modbus():
    read = client.read_holding_registers(address=16, count=1, unit=1)
    Temp1_In_Modbus = read.registers[0]
    print(Temp1_In_Modbus)
    # print(read)
Get_Data_Modbus()
