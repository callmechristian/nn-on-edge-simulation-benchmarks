# nn-on-edge-simulation-benchmarks

# Setup
Run setup.py in a terminal to install all prerequisites. ~1GB

# Usage
sample.ipynb is for running each predicion and aggregating the results

each [model].py file outputs a prediction

utils/create-table.py creates an empty dataframe storage file
utils/append-table.py appends a row to the table created by create-table.py (must contain same number of columns)
utils/SystemMonitor.py is the system monitor class
utils/coninous-system-monitor.py is a continous system resource monitor
utils/get-system-snapshot.py gets the current system resources in that tenth of a second when it's called

