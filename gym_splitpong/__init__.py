from gym.envs.registration import register

register(
    id='splitpong-v0',
    entry_point='gym_splitpong.envs:SplitPongEnv',
)
# register(
    # id='foo-extrahard-v0',
    # entry_point='gym_foo.envs:FooExtraHardEnv',
# )
