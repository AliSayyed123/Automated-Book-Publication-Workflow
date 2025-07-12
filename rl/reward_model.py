# rl/reward_model.py

def compute_reward(original: str, spun: str, human_feedback: str = None):
    reward = 0
    if human_feedback:
        reward += 1 if "accept" in human_feedback else -1
    if len(spun) > len(original):
        reward += 0.5
    if spun != original:
        reward += 0.5
    return reward
