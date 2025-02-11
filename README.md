# Q-Learning Visualization

A graphical visualization of the Q-Learning algorithm implemented in Python using Tkinter.

## Overview

This application demonstrates Q-Learning, a model-free reinforcement learning algorithm, by visualizing an agent finding the optimal path from the top-left corner to the bottom-right corner of a grid. Users can interact with the environment by placing obstacles that the agent must learn to avoid.

## Features

- Interactive 6x6 grid environment
- Visual representation of the Q-Learning process
- Ability to place obstacles by clicking on squares
- Real-time visualization of the agent's path
- Start/Stop controls for the learning process

## How it Works

1. **Environment Setup**
   - The grid is initialized as a 6x6 matrix
   - The agent (red square) starts in the top-left corner
   - The goal is to reach the bottom-right corner
   - Reward of 100 is given when reaching the goal
   - Learning rate (gain) is set to 0.5

2. **User Interaction**
   - Click on any square to create an obstacle (black square)
   - Click "Start" to begin the learning process
   - Click "Stop" to pause the learning

3. **Visual Elements**
   - Red square: Current position of the agent
   - Blue squares: Visited positions with learned Q-values
   - Black squares: Obstacles placed by the user
   - White squares: Unvisited positions

## Running the Application

```python
from QAgentVisualizer import QAgentVisualizer

app = QAgentVisualizer(size=6)
app.create_window()
```

## Technical Details

The Q-Learning implementation uses:
- A Q-matrix of size (36, 4) for storing action values
- Four possible actions: UP (0), RIGHT (1), DOWN (2), LEFT (3)
- State transitions occur every 10ms
- Numpy arrays for efficient matrix operations

## Screenshots

1. Initial State
![screenshot from 2018-02-11 12-57-31](https://user-images.githubusercontent.com/23728874/36073141-f3da8b18-0f2b-11e8-8260-09ecbed82b56.png)

2. Adding Obstacles
![screenshot from 2018-02-11 12-57-51](https://user-images.githubusercontent.com/23728874/36073160-27328056-0f2c-11e8-815c-b10336d3b5f0.png)

3. Learning in Progress
![screenshot from 2018-02-11 12-58-21](https://user-images.githubusercontent.com/23728874/36073163-32f70a1a-0f2c-11e8-95ef-d91929a3bd4a.png)