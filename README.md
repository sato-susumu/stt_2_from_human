# stt\_2\_from\_human

## 概要

stt_2_from_human は 音声認識結果 /stt トピック を受け取り、[RAI](https://github.com/RobotecAI/rai)の /from_human トピックに転送するシンプルなブリッジノードです。転送時にQoSや寿命を変更も行っています。

* **サブスクライブ元トピック**: `/stt` (`std_msgs/msg/String`)
* **パブリッシュ先トピック**: `/from_human` (`std_msgs/msg/String`)

## 依存関係

* ROS 2 Foxy/Humble 以降
* `rclpy`
* `std_msgs`

## ビルド方法
ワークスペースが ~/ros2_ws の場合

```bash
cd ~/ros2_ws
colcon build --packages-select stt_2_from_human
source install/setup.bash
```

## 実行方法

```bash
ros2 run stt_2_from_human stt_2_from_human
```

起動すると、ノード名 `stt_2_from_human` で `/stt` からのメッセージ受信と `/from_human` への再配信を開始します。

