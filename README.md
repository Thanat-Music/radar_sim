# Radar Simulation Project

## Overview
This project is a radar simulation developed from scratch using Python. The main purpose is to research and study the physics and mathematics behind radar technology. The current version simulates objects on a 2D plane and uses "photons" to measure the distance between objects and the radar.

## Features
- **2D Plane Simulation**: Objects are represented on a 2D plane.
- **Photon-Based Distance Measurement**: Sends photons from the radar to measure distances to objects.

## Current Issues
- **Distance Measurement Error**: Due to the precision of the time simulation and Python's performance limitations, there is an error rate in the distance measurements.
- **Photon Contact Point**: The point of contact between the photon and objects from each radar is not overlapped, making it difficult to apply known algorithms for accurate measurement.

## Next Steps
- **Performance Improvement**: Switch to C++ to enhance performance.
- **Wave Simulation**: Implement wave simulation for a more accurate representation of radar behavior.

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/radar-simulation.git
    ```
2. Navigate to the project directory:
    ```bash
    cd radar-simulation
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Run the simulation:
    ```bash
    python main.py
    ```

## Usage
- The simulation currently places objects on a 2D plane and sends photons to measure the distance between them and the radar.
- Results will display the measured distances, along with any errors due to precision issues.

## Contributing
If you notice any issues or have suggestions for improvement, feel free to open an issue or submit a pull request. Your feedback is highly appreciated.

## License
This project is licensed under the MIT License.

## Contact
If you have any questions, suggestions, or have found a mistake, please feel free to contact me. Your insights are greatly valued.
Email: musiz.thanat@gmial.comm

