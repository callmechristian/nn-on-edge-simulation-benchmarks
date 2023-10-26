import psutil
import time

# Define variables
interval_seconds = 0.1

# Get CPU information
print("Processor Info:")
print(f"Number of Cores: {psutil.cpu_count(logical=False)}")
print(f"Number of Logical CPUs: {psutil.cpu_count(logical=True)}")
print(f"CPU Frequency: {psutil.cpu_freq().current} MHz")

# Get CPU usage
cpu_percent = psutil.cpu_percent(interval=interval_seconds)
print("\nProcessor Usage:")
print(f"CPU Usage: {cpu_percent}%")

# Get memory (RAM) information
memory_info = psutil.virtual_memory()
print("\nMemory Info:")
print(f"Total RAM: {memory_info.total / (1024 ** 3):.2f} GB")
print(f"Available RAM: {memory_info.available / (1024 ** 3):.2f} GB")
print(f"Used RAM: {memory_info.used / (1024 ** 3):.2f} GB")

# Get memory usage
memory_info = psutil.virtual_memory()
print("\Memory Usage Info:")
print(f"Memory Usage: {memory_info.percent}%")

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

try:
    prev_disk_io = psutil.disk_io_counters()
    time.sleep(interval_seconds)
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

except KeyboardInterrupt:
    print("Monitoring stopped.")