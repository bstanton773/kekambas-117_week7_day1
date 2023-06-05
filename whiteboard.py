# Define a make_chocolate function that takes in (in order) small, big, goal
# The goal is the Total number of lbs of Chocolate you want to receive
# big is the number of large pieces of chocolate you have available
# big chocolate weighs 5 pounds
# small is the number of small pieces of chocolate you have available
# small chocolate weights 1 pounds
# We want to use as many large bars of chocolate as possible to reach our Goal weight
# the Function should return the number of small
# pieces of chocolate you need to use to reach your goal

def solution(small, big, goal):
    num_big_used = 0
    while big > 0 and (num_big_used + 1) * 5 <= goal:
        big -= 1
        num_big_used += 1
    
    num_small_used = 0

    new_goal = goal - (num_big_used * 5)
    while small > 0 and num_small_used < new_goal:
        small -= 1
        num_small_used += 1

    if (num_big_used*5) + (num_small_used) != goal:
        return -1
    return num_small_used

solution(4,1,5)
