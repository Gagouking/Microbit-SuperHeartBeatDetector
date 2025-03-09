# Microbit-SuperHeartBeatDetector
detect HPM through https://www.dfrobot.com.cn/goods-1339.html DF-gravity Module and publish it to Thingspeak,alarm when it gets high
<h1>整个流程：</h1>
<h2>首先：</h2>
<p>1.在开机时初始化IO板，进行wifi联网（wifi名称、密码，连接成功和上传成功都会有显示）</p>
<p>2.灯带定义（有几颗LED灯、用哪个引脚配置）</p>
<p>3.记录心率变量初始化配置（item用来数字读取心率计跳动，sum用来记录10秒内的item变化了多少次以此来记录心率）</p>
<h2>每xx时间循环：</h2>
<p>1.设定每xx时间（如：一分钟）进行一次心率检测</p>
<p>2.将item和sum清零</p>
<p>3.等待十秒</p>
<p>4.检测完成后会显示6倍的sum（10秒钟心跳次数x6=一分钟心跳次数BPM）</p>
<p>5.如果心率为xx范围时，会显示不同的表情图标（如愤怒、惊讶等）并播放相应的音乐和显示灯带来调节用户的心率</p>
<p>6.检测完成如果连接wifi则发送到thingspeak网页</p>
<p>7.记录一天的心率变化来反应情绪波动</p>
<p>8.当记录的心率超过一定数值（如100）时会连接IFTTT给指定用户发送提醒邮件注意调节心情</p>
<h1>The whole process:</h1>
<h2>First of all:</h2>
<p>1. Initialize the IO board at the time of boot and carry out wifi networking (wifi name, password, successful connection and successful upload will be displayed)</p>

<p>2. Definition of the strip (how many LEDs are there, which pin configuration is used)</p>

<p>3. Record the heart rate variable initialization configuration (item is used to digitally read the beats of the heart rate monitor, and sum is used to record how many times the item has changed within 10 seconds to record the heart rate)</p>

<h2>Every xx time loop:</h2>
<p>1. Set a heart rate check every xx time (e.g., one minute).</p>

<p>2. Reset item and sum 2. Zeros out item and sum</p>

<p>3. Wait for ten seconds</p>

<p>4. After the test is completed, 6 times the sum will be displayed (10 seconds of heartbeats x 6 = BPM of one minute of heartbeats)</p>

<p>5. If the heart rate is in the xx range, different emoji icons (such as anger, surprise, etc.) will be displayed, and the corresponding music and light strips will be displayed to adjust the user's heart rate</p>

<p>6. The detection is complete, if the wifi is connected, then send to the thingspeak web page</p>

<p>7. Record changes in heart rate throughout the day to reflect mood swings</p>

<p>8. When the recorded heart rate exceeds a certain value (such as 100), IFTTT will be connected to send a reminder email to the specified user, pay attention to adjust the mood</p>
