# nn-on-edge-simulation-benchmarks

The test dataset for the pre-trained networks are 100 random classes out of ImageNet-1k.




# Setup
> [!IMPORTANT]
> Clone repo and run setup.py in a terminal to install all prerequisites. ~1GB

# Results [^1]
> [!TIP]
> The complete data analysis is found [here](https://colab.research.google.com/drive/1N10nkwOroTAoQyarE0EbAeVgEm9cesZK?usp=sharing).

From the following correlations graphs it's obvious that inference time is inversely correlated with the number of physical CPU cores available. This is not surprising, as having more physical CPU cores often leads to better parallelism and multitasking capabilities. In scenarios where multiple tasks or processes can be executed concurrently, a higher number of CPU cores can distribute the workload more efficiently, potentially reducing the overall inference time. This correlation aligns with the expected behavior in systems designed to leverage parallel processing, highlighting the impact of CPU core count on computational performance.

<img src="/plots/plot_correlations_configuration_aggregate.png" width="50%">
<img src="/plots/plot_correlations_res_usage_aggregate.png" width="50%">

We can see that MobileNet is superior to all other models in terms of efficiency, and has the best scores for 4GB RAM and 1 physical CPU core.

<img src="/plots/plot_power_efficiency_score_best_case.png" width="50%">

On a closer look, MobileNet actually dominates the leaderboard of efficiency with a score of 72. There is a slight efficiency drop between using 2GB RAM vs 4GB RAM, the latter being 4 units less. Justifiably, you can safely use the 2GB version as it is likely to lead to a percentually insignificant decrease in performance.

<img src="/plots/plot_power_efficiency_score_top20.png" width="50%">

Our hypothesis was that a model's performance is not impacted by the resource configurations, however this is only partly true. Doing a P-test on our data showed that the inference time is impacted by the configuration. [^2]

<img src="/plots/plot_ptest_aggregate.png" width="30%">

> [!NOTE]
> For a restricted analysis solely on ResNet50 for different configurations check [this](https://colab.research.google.com/drive/1a6TM5RRyMC_j9k_NlxVENhmbTkZLpLfr#scrollTo=AZikSZ_9iwb6) out

[^1]: Plots and data have been analysed in [this](https://colab.research.google.com/drive/1N10nkwOroTAoQyarE0EbAeVgEm9cesZK?usp=sharing) colab notebook.
[^2]: Mainly by the number of physical CPU cores available.
# Usage

Anything not mentioned here should be commented in the source files themselves.

## Sampling
`sample.ipynb` is for running each prediction and aggregating the results. Follow the example for ResNet50

The dataset is automatically downloaded and unzipped from google drive when you run `sample.ipynb`. **~700mb**

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

## Model Sizes

> [!NOTE]
> Total Size: 7236 MB (7.24 GB)

```
Xception: 88 MB
VGG16: 528 MB
VGG19: 549 MB
ResNet50: 98 MB
ResNet50V2: 98 MB
ResNet101: 171 MB
ResNet101V2: 171 MB
ResNet152: 232 MB
ResNet152V2: 232 MB
InceptionV3: 92 MB
InceptionResNetV2: 215 MB
MobileNet: 16 MB
MobileNetV2: 14 MB
DenseNet121: 33 MB
DenseNet169: 57 MB
DenseNet201: 80 MB
NASNetMobile: 23 MB
NASNetLarge: 343 MB
EfficientNetB0: 29 MB
EfficientNetB1: 31 MB
EfficientNetB2: 36 MB
EfficientNetB3: 48 MB
EfficientNetB4: 75 MB
EfficientNetB5: 118 MB
EfficientNetB6: 166 MB
EfficientNetB7: 256 MB
EfficientNetV2B0: 29 MB
EfficientNetV2B1: 34 MB
EfficientNetV2B2: 42 MB
EfficientNetV2B3: 59 MB
EfficientNetV2S: 88 MB
EfficientNetV2M: 220 MB
EfficientNetV2L: 479 MB
ConvNeXtTiny: 109.42 MB
ConvNeXtSmall: 192.29 MB
ConvNeXtBase: 338.58 MB
ConvNeXtLarge: 755.07 MB
ConvNeXtXLarge: 1310 MB
```
