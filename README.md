# Microbit-SuperHeartBeatDetector
detect HPM through https://www.dfrobot.com.cn/goods-1339.html DF-gravity Module and publish it to Thingspeak,alarm when it gets high
<h1>整个流程：</h1>
<h2>首先：</h2>
1.在开机时初始化IO板，进行wifi联网（wifi名称、密码，连接成功和上传成功都会有显示）
2.灯带定义（有几颗LED灯、用哪个引脚配置）
3.记录心率变量初始化配置（item用来数字读取心率计跳动，sum用来记录10秒内的item变化了多少次以此来记录心率）
<h2>每xx时间循环：</h2>
1.设定每xx时间（如：一分钟）进行一次心率检测：
2.将item和sum清零
3.等待十秒
4.检测完成后会显示6倍的sum（10秒钟心跳次数x6=一分钟心跳次数BPM）
5.如果心率为xx范围时，会显示不同的表情图标（如愤怒、惊讶等）并播放相应的音乐和显示灯带来调节用户的心率
6.检测完成如果连接wifi则发送到thingspeak网页
7.记录一天的心率变化来反应情绪波动
8.当记录的心率超过一定数值（如100）时会连接IFTTT给指定用户发送提醒邮件注意调节心情
