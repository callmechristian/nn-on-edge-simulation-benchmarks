import psutil
import time
import threading
import csv

class SystemMonitor:
    prev_disk_io = psutil.disk_io_counters()
    snapshots = []

    def __init__(self):
        self.monitoring_thread = None
        self.monitoring = False
        self.interval = 1

    def start(self, interval=1):
        """
        Start monitoring system resources at regular intervals.

        Args:
            interval (int, optional): The time interval in seconds at which system resource snapshots will be collected.
            Defaults to 1 second.

        Usage:
            1. Import the SystemMonitor class from your script where it's defined.

                from your_script import SystemMonitor

            2. Create an instance of the SystemMonitor class.

                monitor = SystemMonitor()

            3. Start the monitoring with the desired interval using the start_monitor method. Optionally, you can specify
            the monitoring interval in seconds as an argument. If not provided, the default interval of 1 second will
            be used.

                # Start monitoring with the default interval (1 second)
                monitor.start_monitor()

                # Start monitoring with a custom interval, e.g., 5 seconds
                monitor.start_monitor(interval=5)

            4. Once monitoring has started, the system resource snapshots will be collected at the specified interval.

            5. To stop the monitoring, you can use the stop_monitor method.

                monitor.stop_monitor()

        Example:
            from your_script import SystemMonitor

            # Create an instance of SystemMonitor
            monitor = SystemMonitor()

            # Start monitoring with a custom interval of 3 seconds
            monitor.start_monitor(interval=3)

            # Allow monitoring for a specific duration
            time.sleep(10) # can also just be another function call, not necessarily a sleep

            # Stop monitoring
            monitor.stop_monitor()
        """
        if self.monitoring:
            print("Monitoring is already running.")
            return

        self.interval = interval
        self.monitoring = True
        self.monitoring_thread = threading.Thread(target=self.monitoring_loop)
        self.monitoring_thread.start()
        print(f"Monitoring started with an interval of {interval} seconds.")

    def stop(self):
        if not self.monitoring:
            print("Monitoring is not running.")
            return

        self.monitoring = False
        self.monitoring_thread.join()
        disk_io = psutil.disk_io_counters()
        print("Monitoring stopped.")

    def monitoring_loop(self):
        prev_disk_io = psutil.disk_io_counters()
        while self.monitoring:
            self.read_system_resources()
            time.sleep(self.interval)
            self.totalTime = self.interval

    def read_system_resources(self):
        disk_io = psutil.disk_io_counters()

        cpu_percent = psutil.cpu_percent()
        memory_info = psutil.virtual_memory()
        
        # Calculate the difference in read and write counts
        read_count_diff = disk_io.read_count - self.prev_disk_io.read_count
        write_count_diff = disk_io.write_count - self.prev_disk_io.write_count
        
        # Calculate the difference in read and write bytes
        read_bytes_diff = disk_io.read_bytes - self.prev_disk_io.read_bytes
        write_bytes_diff = disk_io.write_bytes - self.prev_disk_io.write_bytes

        snapshot = {
            "timestamp": time.time(),
            "cpu_percent": cpu_percent,
            "memory_percent": memory_info.percent,
            "read_count": read_count_diff,
            "write_count": write_count_diff,
            "read_bytes": read_bytes_diff,
            "write_bytes": write_bytes_diff
        }
        
        self.snapshots.append(snapshot)
        self.prev_disk_io = disk_io

    def compute_and_print_average(self):
        if not self.snapshots:
            print("No snapshots available for computing the average.")
            return

        avg_snapshot = {}
        num_snapshots = len(self.snapshots)

        for key in self.snapshots[0]:
            if key == "timestamp":
                continue
            avg_snapshot[key] = sum(snapshot[key] for snapshot in self.snapshots) / num_snapshots

        # add total time to snapshot
        avg_snapshot.update({"total_time": self.totalTime})

        print("Average Snapshot:")
        print(avg_snapshot)

        # Get CPU information
        print("Processor Info:")
        print(f"Number of Cores: {psutil.cpu_count(logical=False)}")
        print(f"Number of Logical CPUs: {psutil.cpu_count(logical=True)}")
        print(f"CPU Frequency: {psutil.cpu_freq().current} MHz")

        # Get memory (RAM) information
        memory_info = psutil.virtual_memory()
        print("\nMemory Info:")
        print(f"Total RAM: {memory_info.total / (1024 ** 3):.2f} GB")
        print(f"Available RAM: {memory_info.available / (1024 ** 3):.2f} GB")
        print(f"Used RAM: {memory_info.used / (1024 ** 3):.2f} GB")

        # Gt swap (virtual memory) information
        swap_info = psutil.swap_memory()
        print("\nSwap (Virtual Memory) Info:")
        print(f"Total Swap: {swap_info.total / (1024 ** 3):.2f} GB")
        print(f"Used Swap: {swap_info.used / (1024 ** 3):.2f} GB")

        # Get disk usage information
        disk_info = psutil.disk_usage('/')
        print("\nDisk Storage Info:")
        print(f"Total Disk Space: {disk_info.total / (1024 ** 3):.2f} GB")
        print(f"Used Disk Space: {disk_info.used / (1024 ** 3):.2f} GB")
        print(f"Free Disk Space: {disk_info.free / (1024 ** 3):.2f} GB")
        print(f"Disk Usage Percentage: {disk_info.percent}%")

    
    def compute_and_return_average(self):
        '''
        Return the average system resources snapshot. <dict>

        snapshot = {
            "timestamp": time,
            "cpu_number_cores": cpu_number_cores,
            "cpu_number_cores_logical": cpu_number_cores_logical,
            "cpu_frequency": cpu_frequency,
            "ram_total": ram_total [GB],
            "ram_available": ram_available [GB],
            "ram_used": ram_used [GB],
            "swap_total": swap_total [GB],
            "swap_used": swap_used [GB],
            "cpu_percent": cpu_percent,
            "memory_percent": memory_info.percent,
            "read_count": read_count_diff,
            "write_count": write_count_diff,
            "read_bytes": read_bytes_diff,
            "write_bytes": write_bytes_diff,
            "total_time": total_time   
        }
        '''
        # Get memory (RAM) information
        memory_info = psutil.virtual_memory()

        # Gt swap (virtual memory) information
        swap_info = psutil.swap_memory()

        # Create AVG
        avg_snapshot = {}

        avg_snapshot.update({"cpu_number_cores": psutil.cpu_count(logical=False)})
        avg_snapshot.update({"cpu_number_cores_logical": psutil.cpu_count(logical=True)})
        avg_snapshot.update({"cpu_frequency": psutil.cpu_freq().current})
        avg_snapshot.update({"ram_total": "{:.2f}".format(memory_info.total / (1024 ** 3))})
        avg_snapshot.update({"ram_available": "{:.2f}".format(memory_info.available / (1024 ** 3))})
        avg_snapshot.update({"ram_used": "{:.2f}".format(memory_info.used / (1024 ** 3))})
        avg_snapshot.update({"swap_total": "{:.2f}".format(swap_info.total / (1024 ** 3))})
        avg_snapshot.update({"swap_used": "{:.2f}".format(swap_info.used / (1024 ** 3))})

        if not self.snapshots:
            print("No snapshots available for computing the average.")
            return
        
        num_snapshots = len(self.snapshots)

        for key in self.snapshots[0]:
            if key == "timestamp":
                continue
            avg_snapshot[key] = sum(snapshot[key] for snapshot in self.snapshots) / num_snapshots

        # added total monitoring time
        avg_snapshot.update({"total_time": self.totalTime})

        return avg_snapshot
    
    def write_snapshots_to_csv(self, filename, extensive=False):
        snapshots_to_write = self.snapshots if extensive else [self.compute_average_snapshot()]

        with open(filename, mode='w', newline='') as file:
            fieldnames = snapshots_to_write[0].keys()
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for snapshot in snapshots_to_write:
                writer.writerow(snapshot)

if __name__ == "__main__":
    # For command line interaction
    monitor = SystemMonitor()
    monitor.start(interval=1)

    # Allow monitoring for a specified duration (e.g., 10 seconds)
    time.sleep(3)

    # Stop the monitoring
    monitor.stop()
    monitor.compute_and_print_average()
