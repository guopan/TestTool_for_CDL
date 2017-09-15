% 功能：读取CStreamingCapture程序输出的功率谱文件，并绘图展示

clear
close all
clc
spec_data = importdata("data_Spec.txt");

figure,plot(spec_data(1025:end));


%% 分距离门绘图
nLayers = length(spec_data)/512;
spec_data = reshape(spec_data,512,[]);
spec_data = flipud(spec_data);
xaxis = 200*(1:512)./512;
start = 1;
stop = 0;
for i = 1:nLayers
	figure(i+1);
	plot(xaxis(start:end-stop), spec_data(start:end-stop,i));
end
TileWindows;