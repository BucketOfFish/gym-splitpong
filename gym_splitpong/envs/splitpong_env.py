import gym
from gym import error, spaces, utils
from gym.utils import seeding
from gym.envs.classic_control import rendering

class SplitPongEnv(gym.Env):

    metadata = {'render.modes': ['human']}

    ##################
    # Initialization #
    ##################

    def __init__(self):
        self.side = 0 # 0 = left, 1 = right, 2 = dual
        self.leftPaddlePos = 100
        self.rightPaddlePos = 100
        self.ballXPos = 50
        self.ballYPos = 100
        self.ballDirection = 0 # 0 = left, 1 = right
        self.YVel = 0
        self.viewer = None
        self.game_width = 100
        self.game_height = 200

    #################
    # Taking a Step #
    #################

    def _step(self, action):
        assert 1 == 1

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
