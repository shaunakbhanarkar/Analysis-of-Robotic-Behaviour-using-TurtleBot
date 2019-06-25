import rospy
from geometry_msgs.msg import Twist
import copy
from math import pi

#Tiles are 2*2 feet

def move_circle():

    rospy.init_node('Node1',anonymous=True)

    #Copy the initial position
    ##initial_turtlebot_odom_pose = copy.deepcopy(turtlebot_odom_pose)
    
    # Create a publisher which can "talk" to Turtlesim and tell it to move
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
    
    #First Circle 
    # Create a Twist message and add linear x and angular z values
    move_cmd = Twist()
    move_cmd.linear.x = 0.1      #ye maine li hai
    move_cmd.angular.z = 0.2     # radius = 0.5m v=rw

    # Save current time and set publish rate at 10 Hz
    now = rospy.Time.now()
    rate = rospy.Rate(100)

    # For the next 15.708 seconds publish cmd_vel move commands to Turtlesim
    while rospy.Time.now() < now + rospy.Duration.from_sec(10*pi):
        pub.publish(move_cmd)
        rate.sleep()

    #Stopping First Circle
    move_cmd.linear.x = 0.0     #ye maine li hai
    move_cmd.angular.z = 0.0     # radius = 0.5m v=rw
    pub.publish(move_cmd)




    #First Rotation 
    # Create a Twist message and add linear x and angular z values
    #move_cmd = Twist()
    move_cmd.linear.x = 0.0      #ye maine li hai
    move_cmd.angular.z = 0.2     # radius = 0.5m v=rw

    # Save current time and set publish rate at 10 Hz
    now = rospy.Time.now()
    rate = rospy.Rate(100)

    # For the next 3.927 seconds publish cmd_vel move commands to Turtlesim
    while rospy.Time.now() < now + rospy.Duration.from_sec(1.25*pi*2):
        pub.publish(move_cmd)
        rate.sleep()

    #Stopping First Rotation
    move_cmd.linear.x = 0.0     #ye maine li hai
    move_cmd.angular.z = 0.0     # radius = 0.5m v=rw
    pub.publish(move_cmd)



    #First Diagonal Cross 
    # Create a Twist message and add linear x and angular z values
    #move_cmd = Twist()
    move_cmd.linear.x = 0.1      #ye maine li hai
    move_cmd.angular.z = 0.0     # radius = 0.5m v=rw

    # Save current time and set publish rate at 10 Hz
    now = rospy.Time.now()
    rate = rospy.Rate(100)

    # For the next 5 seconds publish cmd_vel move commands to Turtlesim
    while rospy.Time.now() < now + rospy.Duration.from_sec(5*2):
        pub.publish(move_cmd)
        rate.sleep()

    #Stopping First Diagonal Cross
    move_cmd.linear.x = 0.0     #ye maine li hai
    move_cmd.angular.z = 0.0     # radius = 0.5m v=rw
    pub.publish(move_cmd)


    #Second Rotation 
    # Create a Twist message and add linear x and angular z values
    #move_cmd = Twist()
    move_cmd.linear.x = 0.0      #ye maine li hai
    move_cmd.angular.z = -0.2     # radius = 0.5m v=rw

    # Save current time and set publish rate at 10 Hz
    now = rospy.Time.now()
    rate = rospy.Rate(100)

    # For the next 3.927 seconds publish cmd_vel move commands to Turtlesim
    while rospy.Time.now() < now + rospy.Duration.from_sec(1.25*pi *2):
        pub.publish(move_cmd)
        rate.sleep()

    #Stopping Second Rotation
    move_cmd.linear.x = 0.0     #ye maine li hai
    move_cmd.angular.z = 0.0     # radius = 0.5m v=rw
    pub.publish(move_cmd)


    #Second Circle 
    # Create a Twist message and add linear x and angular z values
    #move_cmd = Twist()
    move_cmd.linear.x = 0.1      #ye maine li hai
    move_cmd.angular.z = -0.2     # radius = 0.5m v=rw

    # Save current time and set publish rate at 10 Hz
    now = rospy.Time.now()
    rate = rospy.Rate(100)

    # For the next 15.708 seconds publish cmd_vel move commands to Turtlesim
    while rospy.Time.now() < now + rospy.Duration.from_sec(10*pi):
        pub.publish(move_cmd)
        rate.sleep()

    #Stopping Second Circle
    move_cmd.linear.x = 0.0     #ye maine li hai
    move_cmd.angular.z = 0.0     # radius = 0.5m v=rw
    pub.publish(move_cmd)


    #Third Rotation 
    # Create a Twist message and add linear x and angular z values
    #move_cmd = Twist()
    move_cmd.linear.x = 0.0      #ye maine li hai
    move_cmd.angular.z = -0.2     # radius = 0.5m v=rw

    # Save current time and set publish rate at 10 Hz
    now = rospy.Time.now()
    rate = rospy.Rate(100)

    # For the next 3.927 seconds publish cmd_vel move commands to Turtlesim
    while rospy.Time.now() < now + rospy.Duration.from_sec(1.25*pi *2):
        pub.publish(move_cmd)
        rate.sleep()

    #Stopping Third Rotation
    move_cmd.linear.x = 0.0     #ye maine li hai
    move_cmd.angular.z = 0.0     # radius = 0.5m v=rw
    pub.publish(move_cmd)



    #Second Diagonal Cross 
    # Create a Twist message and add linear x and angular z values
    #move_cmd = Twist()
    move_cmd.linear.x = 0.1      #ye maine li hai
    move_cmd.angular.z = 0.0     # radius = 0.5m v=rw

    # Save current time and set publish rate at 10 Hz
    now = rospy.Time.now()
    rate = rospy.Rate(100)

    # For the next 5 seconds publish cmd_vel move commands to Turtlesim
    while rospy.Time.now() < now + rospy.Duration.from_sec(5*2):
        pub.publish(move_cmd)
        rate.sleep()

    #Stopping Second Diagonal Cross
    move_cmd.linear.x = 0.0     #ye maine li hai
    move_cmd.angular.z = 0.0     # radius = 0.5m v=rw
    pub.publish(move_cmd)

    #Fourth Rotation 
    # Create a Twist message and add linear x and angular z values
    #move_cmd = Twist()
    move_cmd.linear.x = 0.0      #ye maine li hai
    move_cmd.angular.z = 0.2     # radius = 0.5m v=rw

    # Save current time and set publish rate at 10 Hz
    now = rospy.Time.now()
    rate = rospy.Rate(100)

    # For the next 3.927 seconds publish cmd_vel move commands to Turtlesim
    while rospy.Time.now() < now + rospy.Duration.from_sec(1.25*pi *2):
        pub.publish(move_cmd)
        rate.sleep()

    #Stopping Fourth Rotation
    move_cmd.linear.x = 0.0     #ye maine li hai
    move_cmd.angular.z = 0.0     # radius = 0.5m v=rw
    pub.publish(move_cmd)

    #Calculate final distance
    ##distance_moved = abs(0.5 * sqrt(((turtlebot_odom_pose.pose.pose.position.x-initial_turtlebot_odom_pose.pose.pose.position.x) ** 2)+((turtlebot_odom_pose.pose.pose.position.y-initial_turtlebot_odom_pose.pose.pose.position.y) ** 2)))

    ##print("Total Distance Moved = ", distance_moved)


if __name__ == '__main__':
    try:
        move_circle()
    except rospy.ROSInterruptException:
        pass