import random
import numpy as np
import matplotlib.pyplot as plt

def gamblers_ruin():
    gambling_money = 50  # Starting money
    gambling_goal = 100  # Winning goal
    gambling_simulations = []

    # Continue betting until money is depleted or goal is reached
    while 1 <= gambling_money < gambling_goal:
        bet_size = 1
        # Randomly decide win (+1) or lose (-1)
        w_or_l = random.choice([-1, 1])
        gambling_money += bet_size * w_or_l
        gambling_simulations.append(gambling_money)
    
    return gambling_simulations

# Simulate and plot the gambling process
simulation_results = gamblers_ruin()

plt.plot(simulation_results)
plt.yticks(np.arange(-20, 120, 10))  # Custom y-ticks
plt.axhline(y=0, color='r', linestyle='-')  # Loss boundary
plt.axhline(y=100, color='black', linestyle='-')  # Goal boundary
plt.xlabel('Number of bets')
plt.ylabel('Winnings')
plt.title('Gambling Simulation')
plt.show()
