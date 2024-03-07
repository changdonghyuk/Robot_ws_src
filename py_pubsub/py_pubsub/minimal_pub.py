
from rclpy.node import Node
from stm32.getchar import Getchar
from std_msgs.msg import String # topic 설정 

sp  = serial.Serial('/dev/ttyACM0', 115200, timeout=1)

class Sub_led_msg(Node):

    def __init__(self):
        super().__init__('sub_led_msg')
        self.publisher_ = self.create_publisher(String, 'led_ctrl', 1)
      

    def get led msg(self):
        
        
        if msg.data =='LED ON':
        	print("Send '1')
        	sp.write(b'1') 
        elif msg.data =='LED OFF':
        	print("Send '0')
        	sp.write(b'0') 
        else pass


def main(args=None):
   

    node = Sub_led_msg()

    rclpy.spin(node)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__': # 명시적 __name__ main 이라면 그것이 메인이다
    main()
