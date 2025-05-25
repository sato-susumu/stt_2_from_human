# stt_2_from_human/bridge_node.py

import rclpy
from rclpy.node import Node
from rclpy.duration import Duration
from std_msgs.msg import String
from rclpy.qos import QoSProfile, ReliabilityPolicy, DurabilityPolicy

# —— 定数 —— 
TOPIC_STT = '/stt'
TOPIC_FROM = '/from_human'
QOS_DEPTH = 1
TIMEOUT_SEC = 10

class STT2FromHumanBridge(Node):
    def __init__(self):
        super().__init__('stt_2_from_human')

        # 起動時ログ
        self.get_logger().info(f'STT→Human bridge starting: subscribe to "{TOPIC_STT}", publish to "{TOPIC_FROM}"')

        # /stt をサブスクライブする QoS
        sub_qos = QoSProfile(
            depth=QOS_DEPTH,
            reliability=ReliabilityPolicy.RELIABLE,
            durability=DurabilityPolicy.VOLATILE,
        )
        self.subscription = self.create_subscription(
            String,
            TOPIC_STT,
            self.stt_callback,
            sub_qos
        )

        # /from_human をパブリッシュする QoS
        pub_qos = QoSProfile(
            depth=QOS_DEPTH,
            reliability=ReliabilityPolicy.RELIABLE,
            durability=DurabilityPolicy.TRANSIENT_LOCAL,
        )
        # メッセージの寿命を 10 秒に設定
        pub_qos.lifespan = Duration(seconds=TIMEOUT_SEC, nanoseconds=0)

        self.publisher = self.create_publisher(
            String,
            TOPIC_FROM,
            pub_qos
        )

        # 準備完了ログ
        self.get_logger().info('Bridge node ready. Waiting for incoming messages…')

    def stt_callback(self, msg: String):
        # 受信ログ
        self.get_logger().info(f'Received on {TOPIC_STT}: "{msg.data}", forwarding to {TOPIC_FROM}…')
        # 受け取ったメッセージをそのまま転送
        self.publisher.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = STT2FromHumanBridge()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('KeyboardInterrupt received, shutting down.')
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
