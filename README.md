# nn-on-edge-simulation-benchmarks

# Setup
Run setup.py in a terminal to install all prerequisites. ~1GB

# Usage

## Sampling
**sample.ipynb** is for running each prediction and aggregating the results. Follow the example for ResNet50

## Extending
**SS_model.py** is the base class for all models
**[model].py** files inherit the base class and must redefine all methods. Output a prediction

1. **utils/Table.py** utility class for saving data
3. **utils/SystemMonitor.py** is the system monitor class
4. **utils/coninous-system-monitor.py** is a continous system resource monitor
5. **utils/get-system-snapshot.py** gets the current system resources in that tenth of a second when it's called

## __Table.py Usage__

**Append Rows to an Existing DataFrame**

To append rows to an existing Pandas DataFrame saved in a given file, use the append_to_df function. This function takes two arguments: filename (the name of the file containing the DataFrame) and data (a list of lists where each inner list represents a row to be appended to the DataFrame).

**Example:**

```python
Table.append_to_df("existing_dataframe.csv", data_to_append)
```

**Create an Empty DataFrame**

To create an empty Pandas DataFrame with custom column names and save it to a given file, use the create_empty_df function. This function takes two arguments: filename (the name of the file to save the DataFrame to) and column_names (a list of strings containing the column names for the DataFrame).

**Example:**

```python
column_names = ["name", "age", "occupation"]
Table.create_empty_df("new_dataframe.csv", column_names)
```

**Append Data to Samples**

The script also provides a function to append data to a predefined DataFrame structure. It collects system resource snapshots and appends them along with other data to the DataFrame. This function requires a few arguments, including filename, model_name, monitor, and model_class.

**Example:**

```python
Table.append_data_to_samples("Samples1.csv", "ModelName", monitor_instance, model_instance)
```


### **Command-Line Usage**

The script can also be executed from the command line with the following commands:

**To create an empty DataFrame:**

```shell
python3 utils/Table.py create <filename>.csv <column_names>
```
**To append rows to an existing DataFrame:**

```shell
python3 utils/Table.py append <filename>.csv <row1_value> <row2_value> ...
```
## SystemMonitor Class

The `SystemMonitor` class provides a utility for monitoring system resources at regular intervals. It collects data such as CPU usage, memory usage, disk I/O, and more.

### Usage

1. **Import the `SystemMonitor` class from your script where it's defined:**

    ```python
    from utils.SystemMonitor import SystemMonitor
    ```

2. **Create an instance of the `SystemMonitor` class:**

    ```python
    monitor = SystemMonitor()
    ```

3. **Start Monitoring:**

   - Use the `start` method to begin monitoring. You can specify the monitoring interval in seconds (default is 1 second).

   - Example:

     ```python
     # Start monitoring with the default interval (1 second)
     monitor.start()

     # Start monitoring with a custom interval, e.g., 5 seconds
     monitor.start(interval=5)
     ```

4. **Stop Monitoring:**

   - To stop the monitoring, use the `stop` method:

     ```python
     monitor.stop()
     ```

5. **Collect and Analyze Data:**

   - The `SystemMonitor` class collects system resource data at the specified interval. You can access and analyze this data as needed.

6. **Compute and Print Average:**

   - Use the `compute_and_print_average` method to compute the average system resource snapshots and print the results.

7. **Return Average Snapshot:**

   - Use the `compute_and_return_average` method to obtain the average system resource snapshot as a dictionary.

8. **Write Snapshots to CSV:**

   - Use the `write_snapshots_to_csv` method to write collected snapshots to a CSV file. You can specify whether to write extensive snapshots or just the average snapshot.

### Command-Line Usage

You can also interact with the `SystemMonitor` class from the command line:

- To start monitoring from the command line:

    ```shell
    python3 your_script.py start
    ```

- To stop monitoring from the command line:

    ```shell
    python3 your_script.py stop
    ```

- To write snapshots to a CSV file from the command line:

    ```shell
    python3 your_script.py write_snapshots filename.csv [extensive]
    ```

   The `[extensive]` flag is optional and determines whether to write extensive snapshots or just the average snapshot to the CSV file.
