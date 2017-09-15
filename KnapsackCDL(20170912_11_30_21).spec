Knapsack Coherent Doppler Lidar Original Spectrum					#标题
=======================================================================================================
Version:1.0															#数据格式版本		
Global Definition:													#全局参数定义

Base Time: 1900-01-01 00:00:00										#系统基准时间，以字符串存储，精确到秒
Time Stamp Size: 8 Bytes float										#时间戳存储形式，软件从采集卡获取到原始功率谱数据的系统时间

Azimuth Angle Size: 8 Bytes float									#方位角存储形式
Elevation Angle Size: 8 Bytes float									#固定数值

Frequency Axis: 1.00 2.00 3.00 4.00 ...								#字符串形式保存频率坐标轴各点频率，精确到小数点后两位，单位是MHz
Height Axis: 100.00 200.00 300.00 400.00 ...						#字符串形式保存高度坐标轴各点高度，精确到小数点后两位，单位是m
Spectrum Point Size: 8 Bytes int
=======================================================================================================
Original Data(TimeStamp AzimuthAngle SpectrumData)					#功率谱数据，二进制存储，分别为时间戳、方位角、原始功率谱
float64 float64 int64 int64 int64 ......
float64 float64 int64 int64 int64 ......
float64 float64 int64 int64 int64 ......
float64 float64 int64 int64 int64 ......
...
...
...

#附加说明：
#激光雷达的工作方式为开始采集后工作一段时间（通常为3分钟），这段时间内产生的信号功率谱全部存储于本文件
#因此文件拓展名.spec代表是原始信号功率谱数据，文件名需要存储本次采集的开始时间