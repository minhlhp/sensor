import time
from noisuytt import noisuy
from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from pymodbus.constants import Defaults

Defaults.RetryOnEmpty = True
Defaults.Timeout = 5
Defaults.Retries = 5

client = ModbusClient(method='rtu', port='COM4', timeout=2, stopbits=1, bytesize=8, parity='N', baudrate=19200)
client.connect()


def Get_Data_Modbus():
    Device1 = client.read_holding_registers(address=16, count=1, unit=1)
    # Device2 = client.read_input_registers(address=16, count=2, unit=2)
    Temp1_In_Modbus = Device1.registers[0]
    print(Device1.__dict__)
    # print(Device2.__dict__)
    time.sleep(1)
    Temp1_Value = noisuy(4,20,0,1300,Temp1_In_Modbus)
    print(Temp1_Value)
    return Temp1_Value

Get_Data_Modbus()