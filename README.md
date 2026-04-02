# 🐺 Engineering-Codex

Welcome to my central repository for mechatronics, control theory, and computational mathematics. 

This repository serves as an interactive, executable knowledge base. Instead of static notes, these modules are built using Jupyter/Colab notebooks (Python and Julia) to bridge the gap between theoretical mathematics and practical, computational implementation. The focus is heavily geared towards systems, modern control, dynamic modeling, and machine learning applications.

## 🗂️ Folder Structure & Navigation

The repository is organized logically by engineering and mathematical domains. Each sub-folder contains notebooks with derivations, proofs, and executable code examples.

### `01_Mathematics/`
The foundational math required for robotics, kinematics, and control systems.
* `01_Linear_Algebra/` (Vectors, Matrices, Tensors, Eigen-decomposition)
* `02_Calculus/` (Derivatives, Partial Differential Equations)
* `03_Optimization/` (Convex Optimization, Dynamic Programming (DP))
* `04_Computational_Methods/` (Numerical Integration, Root Finding, Algorithms)
* `05_Probability_and_Stats/` (Distributions, Stochastic Processes)

### `02_Control_Systems/`
From PID to advanced theoretical controllers.
* `01_Classical_Control/` (Root Locus, Frequency Response, Bode, PID)
* `02_Modern_Control/` (State-Space Representations, LQR, Pole Placement)
* `03_Nonlinear_Control/` (Lyapunov Stability, Sliding Mode Control)

### `03_Dynamic_Systems/`
Modeling the physics of moving bodies and observers.
* `01_Rigid_Body_Dynamics/` (Euler-Lagrange, Newton-Euler formulations)
* `02_Kinematics/` (Lie Groups: SO(3), SE(3), Quaternions, Rotations)
* `03_Estimation_and_Observers/` (Inertial Observers, Kalman Filters, Sensor Fusion)

### `04_Vibration_Systems/`
Mechanical vibrations and structural analysis.
* `01_Free_Vibrations/` (Single and Multi-Degree of Freedom Systems)
* `02_Forced_Vibrations/` (Harmonic Excitation, Damping Ratios)
* `03_Modal_Analysis/` (Mode Shapes, Frequency Response of Beams)

### `05_Machine_Learning/`
ML techniques applied to engineering and system identification.
* `01_Supervised_Learning/` (Regression, Neural Networks)
* `02_Reinforcement_Learning/` (Policy Gradients, Q-Learning for Control)

## 🛠️ How to Use This Repository

1.  **Environment:** The notebooks are designed to be run in Google Colab or a local Jupyter environment. 
2.  **Languages:** Ensure you have the appropriate kernels installed. Python environments generally require `numpy`, `scipy`, `matplotlib`, and `control`. Julia environments utilize `ControlSystems.jl` and `DifferentialEquations.jl`.
3.  **Execution:** Each notebook is self-contained. Run the cells sequentially to see the mathematical models simulated in real-time.

---
*Maintained by Janith Yapa*
