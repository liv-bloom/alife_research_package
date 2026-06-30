import random
import os

def simulate_physarum(steps=100, grid_size=50):
    # Extremely simplified headless physarum model for quicktest reproducibility
    grid = [[0.0 for _ in range(grid_size)] for _ in range(grid_size)]
    agents = [{"x": random.randint(0, grid_size-1), "y": random.randint(0, grid_size-1)} for _ in range(200)]
    
    for step in range(steps):
        for agent in agents:
            # Move randomly (simplified sensory check)
            agent["x"] = (agent["x"] + random.choice([-1, 0, 1])) % grid_size
            agent["y"] = (agent["y"] + random.choice([-1, 0, 1])) % grid_size
            # Deposit trace
            grid[agent["y"]][agent["x"]] += 1.0
            
        # Decay trace
        for y in range(grid_size):
            for x in range(grid_size):
                grid[y][x] *= 0.9
                
    # Calculate stats for statistical verification (R5S)
    total_trace = sum(sum(row) for row in grid)
    density = total_trace / (grid_size*grid_size)
    print(f"Simulation completed: {steps} steps on {grid_size}x{grid_size} grid.")
    print(f"Metrics: Trace density = {density:.4f}")
    
    # Simple verification logic
    if 0.5 < density < 2.0:
        print("Result: Stable trace distribution achieved.")
    else:
        print("Result: Anomaly in trace density.")

if __name__ == "__main__":
    simulate_physarum()
