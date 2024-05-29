import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_srvs.srv import Empty
from rclpy.qos import QoSProfile

class TurtlebotController(Node):
    def __init__(self):
        super().__init__('turtlebot_controller')
        qos = QoSProfile(depth=10)
        self.publisher = self.create_publisher(Twist, 'cmd_vel', qos)
        self.subscription = self.create_subscription(Twist, 'cmd_vel', self.listener_callback, qos)
        self.stop_service = self.create_service(Empty, 'stop_robot', self.stop_robot_callback)
        self.get_logger().info('Turtlebot Controller has been started.')

    def listener_callback(self, msg):
        self.publisher.publish(msg)
        self.get_logger().info(f'Published: Linear: {msg.linear.x}, Angular: {msg.angular.z}')

    def stop_robot_callback(self, request, response):
        twist = Twist()
        self.publisher.publish(twist)
        self.get_logger().info('Robot stopped.')
        return response

def main(args=None):
    rclpy.init(args=args)
    turtlebot_controller = TurtlebotController()
    rclpy.spin(turtlebot_controller)
    turtlebot_controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
