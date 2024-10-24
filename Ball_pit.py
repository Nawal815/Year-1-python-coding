
#Ball pit program

#subprogram
#function to return the volume fo the ball pit
def ball_pit_volume(ball_pit_radius, ball_pit_height):
    pi = 3.14
    return pi * (ball_pit_radius * ball_pit_radius) * ball_pit_height

#function to return the volume of a ball
def ball_volume(ball_radius):
    pi = 3.14
    return (4 / 3) * pi * (ball_radius * ball_radius * ball_radius)


#Main program
ball_pit_radius = 1 #meters
ball_pit_height = 0.2 #meters
ball_radius = 0.05 #meters
packing_density = 0.75 #volume taken up by the balls
balls = (ball_pit_volume(ball_pit_radius, ball_pit_height) / ball_volume(ball_radius)) * packing_density
print ("You need", balls, "balls to fill the ball pit")