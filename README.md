# nn-on-edge-simulation-benchmarks

# Setup
Run setup.py in a terminal to install all prerequisites. ~1GB

# Usage
**sample.ipynb** is for running each predicion and aggregating the results

each **[model].py** file outputs a prediction

1. **utils/create-table.py** creates an empty dataframe storage file
2. **utils/append-table.py** appends a row to the table created by create-table.py (must contain same number of columns)
3. **utils/SystemMonitor.py** is the system monitor class
4. **utils/coninous-system-monitor.py** is a continous system resource monitor
5. **utils/get-system-snapshot.py** gets the current system resources in that tenth of a second when it's called

