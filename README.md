# Addis Taxi Route Finder 🚖📍

## Project Overview
**Addis Taxi Route Finder** is a Python-based intelligent navigation tool designed to help users find the optimal taxi route between various stations in Addis Ababa. By leveraging the **A* Search Algorithm**, the application calculates the most efficient path based on distance and heuristics, visualizing the result on an interactive graph.

Whether you are a commuter looking for the best route or a developer interested in pathfinding algorithms, this project serves as a practical demonstration of graph theory and interactive data visualization.

## Key Features 🌟
- **Optimal Pathfinding**: Uses the A* algorithm to find the shortest path between two stations.
- **Interactive Interface**: Built with [Streamlit](https://streamlit.io/) for a user-friendly web experience.
- **Graph Visualization**: Visualizes the station network and the calculated path using **NetworkX** and **Matplotlib**.
- **Customizable Data**: Station connections and heuristics are loaded from external files, making it easy to update or expand the network.

## Tech Stack 🛠️
- **Python 3.x**: Core programming language.
- **Streamlit**: For creating the web interface.
- **NetworkX**: For graph creation, manipulation, and study of the structure.
- **Matplotlib**: For plotting the graph and the routes.

## Project Structure 📂
```
AddisTaxiRoute/
├── app.py                # Main application entry point (Streamlit app)
├── data/
│   └── stations.json     # Graph data (nodes and edges representing stations)
├── src/
│   ├── a_star.py         # Implementation of the A* search algorithm
│   ├── graph.py          # Graph class to handle data loading and structure
│   └── heuristics.py     # Heuristic functions for pathfinding
├── requirements.txt      # List of project dependencies
└── README.md             # Project documentation
```

## Setup & Installation 🚀

Follow these steps to get the project running on your local machine.

### 1. Clone the Repository
```bash
git clone <repository-url>
cd AddisTaxiRoute
```

### 2. Create a Virtual Environment (Optional but Recommended)
It's good practice to use a virtual environment to manage dependencies.
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
Install the required packages using pip:
```bash
pip install -r requirements.txt
```

### 4. Run the Application
Start the Streamlit app:
```bash
streamlit run app.py
```
The application should automatically open in your default web browser at `http://localhost:8501`.

## How It Works 🧠

1. **Graph Initialization**: The `Graph` class in `src/graph.py` loads the station data from `data/stations.json`.
2. **User Input**: The user selects a **Start Station** and a **Goal Station** via the Streamlit interface.
3. **Path Calculation**: When the "Find Optimal Route" button is clicked, the app calls the `a_star` function from `src/a_star.py`.
4. **Heuristics**: The algorithm uses a heuristic function (in `src/heuristics.py`) to estimate the cost to reach the goal, prioritizing paths that seem more promising.
5. **Visualization**: If a path is found, it is highlighted on a graph plot displayed within the app.

## Contributing 🤝
Contributions are welcome! If you'd like to improve the heuristics, add more stations, or enhance the UI, feel free to fork the repository and submit a pull request.

## License 📄
This project is open-source and available under the MIT License.
