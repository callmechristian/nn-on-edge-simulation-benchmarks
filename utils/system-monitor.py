import psutil
import time

# Function to print real-time system resource utilization
def monitor_system_resources(interval_seconds):
    try:
        prev_disk_io = psutil.disk_io_counters()
        
        while True:
            # Get CPU usage
            cpu_percent = psutil.cpu_percent(interval=interval_seconds)
            print(f"CPU Usage: {cpu_percent}%")

            # Get memory usage
            memory_info = psutil.virtual_memory()
            print(f"Memory Usage: {memory_info.percent}%")

            disk_io = psutil.disk_io_counters()
            
            # Calculate the difference in read and write counts
            read_count_diff = disk_io.read_count - prev_disk_io.read_count
            write_count_diff = disk_io.write_count - prev_disk_io.write_count
            
            # Calculate the difference in read and write bytes
            read_bytes_diff = disk_io.read_bytes - prev_disk_io.read_bytes
            write_bytes_diff = disk_io.write_bytes - prev_disk_io.write_bytes

            print("\nDisk Usage in interval " + str(interval_seconds) + "s:")
            print(f"Read Count per second: {read_count_diff / interval_seconds}")
            print(f"Write Count per second: {write_count_diff / interval_seconds}")
            print(f"Read Bytes per second: {read_bytes_diff / interval_seconds} bytes")
            print(f"Write Bytes per second: {write_bytes_diff / interval_seconds} bytes")
                
            prev_disk_io = disk_io

            print(f"\n================================\n")

            time.sleep(interval_seconds)

            prev_disk_io = psutil.disk_io_counters()

    except KeyboardInterrupt:
        print("Monitoring stopped.")

if __name__ == "__main__":
    interval_seconds = 1  # Adjust the monitoring interval as needed
    monitor_system_resources(interval_seconds)