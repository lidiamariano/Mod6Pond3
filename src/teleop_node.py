import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import sys
import select
import termios
import tty

class TeleopNode(Node):
    def __init__(self):
        super().__init__('teleop_node')
        self.publisher = self.create_publisher(Twist, 'cmd_vel', 10)
        self.speed = 0.5
        self.angular_speed = 1.0
        self.get_logger().info('Teleop Node has been started.')
        self.print_instructions()

    def print_instructions(self):
        print("Use os seguintes comandos para movimentar o Turtlebot3:")
        print("  - 'w': Move para frente")
        print("  - 's': Move para trás")
        print("  - 'a': Gira para esquerda")
        print("  - 'd': Gira para direita")
        print("  - ' ': Para")
        print("  - 'Ctrl+C': Sair")
        print()  
        
    def get_key(self):
        tty.setraw(sys.stdin.fileno())
        select.select([sys.stdin], [], [], 0)
        key = sys.stdin.read(1)
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, termios.tcgetattr(sys.stdin))
        return key

    def run(self):
        try:
            while rclpy.ok():
                key = self.get_key()
                twist = Twist()

                if key == 'w':
                    twist.linear.x = self.speed
                elif key == 's':
                    twist.linear.x = -self.speed
                elif key == 'a':
                    twist.angular.z = self.angular_speed
                elif key == 'd':
                    twist.angular.z = -self.angular_speed
                elif key == ' ':
                    twist.linear.x = 0.0
                    twist.angular.z = 0.0
                elif key == '\x03':  # Ctrl+C
                    break

                self.publisher.publish(twist)
                self.get_logger().info(f'Published - Linear: {twist.linear.x}, Angular: {twist.angular.z}\n')  # Adiciona uma quebra de linha
        except Exception as e:
            self.get_logger().error(f'Exception: {e}')
        finally:
            twist = Twist()
            self.publisher.publish(twist)
            self.get_logger().info('Teleop Node has been stopped.')

def main(args=None):
    rclpy.init(args=args)
    teleop_node = TeleopNode()
    teleop_node.run()
    teleop_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()