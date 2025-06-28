import random
import copy

class Hat(object):
    def __init__(self, **kwargs):
        self.contents = []
        for k,v in list(kwargs.items()):
            while v > 0:
                self.contents.append(k)
                v -= 1
        

    def draw(self, num):
        self.picked_colors = []
        self.range = (len(self.contents) - 1)
        if num > self.range:
            return self.picked_colors
        while self.range > 0:
            self.range = (len(self.contents) - 1)
            rand_num = random.randint(0,self.range)
            self.color_picked = self.contents.pop(rand_num)
            self.picked_colors.append(self.color_picked)
            num -= 1
            if num == 0:
                return self.picked_colors
            

    def expected(self, dict):
        self.expected_cont = []
        for k,v in list(dict.items()):
            while v > 0:
                self.expected_cont.append(k)
                v -= 1
        return self.expected_cont
    
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    N = num_experiments
    M = 0
    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        balls_drawn = hat_copy.draw(num_balls_drawn)
        expected_list = hat_copy.expected(expected_balls)
        found_balls = []
        
        for ball in expected_list:
            if ball in balls_drawn:
                found_ball_index = balls_drawn.index(ball)
                found_balls.append(balls_drawn.pop(found_ball_index))
            if len(found_balls) == len(expected_list):
                M += 1
            else:
                0
                
    print(M / N)
    return M / num_experiments
            




hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={"red":2,"green":1},
                  num_balls_drawn=5,
                  num_experiments=2000)
