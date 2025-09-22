import psutil

class SystemStats:
    def __init__(self, config_path="tools_config"):
        self.config_path = config_path
        self.load_config()

    def load_config(self):
        def load_config(self):
            # Provide the absolute path to the configuration file
            config_path = os.path.join(os.path.dirname(__file__), self.config_path)

            # Read configuration from the file
            with open(config_path, 'r') as config_file:
                self.primary_drive = config_file.readline().strip()

    def get_memory_usage(self):
        memory_stats = psutil.virtual_memory()
        return (memory_stats.used / memory_stats.total) * 100

    def get_cpu_usage(self):
        return psutil.cpu_percent()

    def get_disk_usage(self):
        disk_stats = psutil.disk_usage(self.primary_drive)
        return (disk_stats.used / disk_stats.total) * 100
