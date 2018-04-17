from clk_test import answer         # light sensor
from DHT22 import hum, tem          # temperature and humidity sensor
from test_PIR import a              # pir sensor


while True:
    answer = answer + 0
    hum = hum + 0
    tem = tem + 0
    a = a + 0

    print(answer)
    print(hum)
    print(tem)
    print(a)
