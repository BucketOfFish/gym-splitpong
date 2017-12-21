import gym
from gym import error, spaces, utils
from gym.utils import seeding
from gym.envs.classic_control import rendering
import numpy as np

class SplitPongEnv(gym.Env):

    metadata = {'render.modes': ['human']}

    ##################
    # Initialization #
    ##################

    def __init__(self):

        self.side = 0 # 0 = left, 1 = right, 2 = dual
        self.leftPaddlePos = 100
        self.rightPaddlePos = 100
        self.paddleSize = 10
        self.ballXPos = 50
        self.ballYPos = 100
        self.ballXVel = 1
        self.ballYVel = 0

        self.viewer = None
        self.game_width = 100
        self.game_height = 200

        self.action_space = spaces.MultiDiscrete([[-1,1], [-1,1]])
        self.observation_space = spaces.Box(np.array([0, 0, 0, 0]), np.array([self.game_height, self.game_height, self.game_width, self.game_height])) # paddle1, paddle2, ballX, ballY

    #################
    # Taking a Step #
    #################

    def _step(self, action):

        assert self.action_space.contains(action), "%r (%s) invalid"%(action, type(action))
        self.leftPaddlePos += action[0]
        self.rightPaddlePos += action[1]

        self.ballXPos += self.ballXVel
        self.ballYPos += self.ballYVel
        self.ballYPos = self.ballYPos % self.game_height

        done = False
        reward = 0.0

        if self.ballXPos == 0:
            self.ballYVel = np.random.uniform(-5,5)
            if abs(self.leftPaddlePos-self.ballYPos) < self.paddleSize:
                reward = 1.0
                self.ballXVel *= -1
            else:
                reward = -1.0
                self.ballXPos = self.game_width/2

        if self.ballXPos == self.game_width:
            self.ballYVel = np.random.uniform(-5,5)
            if abs(self.rightPaddlePos-self.ballYPos) < self.paddleSize:
                reward = 1.0
                self.ballXVel *= -1
            else:
                reward = -1.0
                self.ballXPos = self.game_width/2

        self.state = (self.leftPaddlePos, self.rightPaddlePos, self.ballXPos, self.ballYPos)
        return np.array(self.state), reward, done, {}

    #############
    # Resetting #
    #############

    def _reset(self):
        self.leftPaddlePos = 100
        self.rightPaddlePos = 100
        self.ballXPos = 50
        self.ballYPos = 100

    ####################
    # Screen Rendering #
    ####################

    def _render(self, mode='human', close=False):

        if close:
            if self.viewer is not None:
                self.viewer.close()
                self.viewer = None
            return

        horizontalSpacing = 20

        if self.viewer is None:
            self.viewer = rendering.Viewer(self.game_width + 2*horizontalSpacing, self.game_height)

            # ball = rendering.Point()
            ball = rendering.make_circle(2)
            ball.set_color(1,0,0)
            self.ballTrans = rendering.Transform()
            ball.add_attr(self.ballTrans)
            self.viewer.add_geom(ball)

            # leftPaddle = rendering.Point()
            leftPaddle = rendering.make_circle(2)
            self.leftTrans = rendering.Transform()
            leftPaddle.add_attr(self.leftTrans)
            self.viewer.add_geom(leftPaddle)

            # rightPaddle = rendering.Point()
            rightPaddle = rendering.make_circle(2)
            self.rightTrans = rendering.Transform()
            rightPaddle.add_attr(self.rightTrans)
            self.viewer.add_geom(rightPaddle)

        self.ballTrans.set_translation(self.ballXPos+horizontalSpacing, self.ballYPos)
        self.leftTrans.set_translation(horizontalSpacing, self.leftPaddlePos)
        self.rightTrans.set_translation(self.game_width+horizontalSpacing, self.rightPaddlePos)

        return self.viewer.render(return_rgb_array = mode=='rgb_array')
