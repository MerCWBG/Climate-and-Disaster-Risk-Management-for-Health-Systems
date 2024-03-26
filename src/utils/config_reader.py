import yaml
import os
import logging
import datetime


class Logger:
    def __init__(self, directory=None, file_name=None):
        self.directory = directory
        self.file_name = file_name
        self.logger = None  # Logger object

        # Set up logger if file_name is provided
        if self.file_name:
            self.setup_logger()

    def setup_logger(self):
        # If no directory is provided, use the current directory
        if self.directory is None:
            self.directory = os.getcwd()

        # Get the timestamp of the process
        # timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        timestamp = None

        # Combine directory, file name, and timestamp to get the complete path
        log_file_path = os.path.join(
            self.directory, f"{self.file_name}_{timestamp}.log"
        )

        # Remove the existing log file if it exists
        if os.path.exists(log_file_path):
            os.remove(log_file_path)

        # Create the directory if it doesn't exist
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)

        # Create logger
        self.logger = logging.getLogger("my_logger")
        self.logger.setLevel(logging.DEBUG)

        # Create file handler
        file_handler = logging.FileHandler(log_file_path)
        file_handler.setLevel(logging.DEBUG)

        # Create formatter and add it to the handler
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
        )
        file_handler.setFormatter(formatter)

        # Add the handler to the logger
        self.logger.addHandler(file_handler)

    def info(self, message):
        if not self.logger:
            raise ValueError(
                "Logger not initialized. Use setup_logger() or provide a file_name."
            )
        self.logger.info(message)
        print(f"INFO: {message}")

    def warning(self, message):
        if not self.logger:
            raise ValueError(
                "Logger not initialized. Use setup_logger() or provide a file_name."
            )
        self.logger.warning(message)
        print(f"WARNING: {message}")

    def error(self, message):
        if not self.logger:
            raise ValueError(
                "Logger not initialized. Use setup_logger() or provide a file_name."
            )
        self.logger.error(message)
        print(f"ERROR: {message}")

    def critical(self, message):
        if not self.logger:
            raise ValueError(
                "Logger not initialized. Use setup_logger() or provide a file_name."
            )
        self.logger.critical(message)
        print(f"CRITICAL: {message}")

    def debug(self, message):
        if not self.logger:
            raise ValueError(
                "Logger not initialized. Use setup_logger() or provide a file_name."
            )
        self.logger.debug(message)
        print(f"DEBUG: {message}")

    def get_logger_file(self):
        if self.logger:
            for handler in self.logger.handlers:
                if isinstance(handler, logging.FileHandler):
                    return handler.baseFilename
        else:
            raise ValueError(
                "Logger not initialized. Use setup_logger() or provide a file_name."
            )


class ConfigReader:
    @staticmethod
    def replace_none(data):
        """Replace 'None' or 'none' strings with None."""
        if isinstance(data, dict):
            for key, value in data.items():
                if isinstance(value, str):
                    if value.lower() == "none":
                        data[key] = None
                elif isinstance(value, (list, dict)):
                    data[key] = ConfigReader.replace_none(value)
        elif isinstance(data, list):
            for i, item in enumerate(data):
                data[i] = ConfigReader.replace_none(item)
        return data

    @staticmethod
    def read_yaml_file(file_path):
        """Read YAML file and return parsed data."""
        with open(file_path, "r") as f:
            yaml_data = yaml.safe_load(f)
            return ConfigReader.replace_none(yaml_data)
