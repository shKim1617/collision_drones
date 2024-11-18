from drone_class import create_drones
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

leader, follows = create_drones(1)
print(follows)
print(follows[0].get_state())

plt.ioff()
plt.show()

# 갑자기 머리를 돌리고 팔로우가 거기로 가는 형태로?
# 이건 너무 자연스럽다?

count = 0

def animate(frame):
    global count
        
    plt.cla()
    
    # 리더
    plt.scatter(leader.position[0], leader.position[1], color='red', label='Leader', s=200)
    # 팔로워1
    plt.scatter(follows[0].target_position[0], follows[0].target_position[1], color='black', label='target_position1', s=100)
    plt.scatter(follows[0].position[0], follows[0].position[1], color='blue', label='Follower 1', s=200)
    
    # 포메이션 라인 그리기
    plt.plot([leader.position[0], follows[0].position[0]], [leader.position[1], follows[0].position[1]], 'b--')
    
    # 리더 방향 화살표로 그리기
    plt.quiver(leader.position[0], leader.position[1], leader.direction[0], leader.direction[1], color='red', scale=10)
    
    if count < 5:
        leader.rotate_heading(np.pi/5)
        count += 1
        
    follows[0].update_all(leader.position, leader.direction)
    
    direction_to_target = follows[0].target_position - follows[0].position
    distance_to_target = np.linalg.norm(direction_to_target)
    
    if count >= 5:
        follows[0].position += (direction_to_target / distance_to_target)*0.25
    
    # 그래프 설정
    preset = 5
    plt.xlim(-preset, preset)
    plt.ylim(-preset, preset)
    plt.title("Drone Formation Movement without RL")
    plt.xlabel("X position")
    plt.ylabel("Y position")
    plt.legend()
    plt.grid(True)
    
# 애니메이션 실행
fig = plt.figure(figsize=(10, 10))
ani = FuncAnimation(fig, animate, frames=100, interval=200)
plt.show()