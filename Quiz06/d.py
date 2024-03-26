class Logger:
    def __init__(self, log_level = "INFO"):
        self.log_level = log_level

    def log(self, message):
        raise NotImplementedError("Subclasses must implement the log method")

class ConsoleLogger(Logger):
    def log(self, message):
        print(f"[{self.log_level}] {message}")

class FileLogger(Logger):
    def __init__(self, log_level = "INFO", file_path = "app.log"):
        super().__init__(log_level)
        self.file_path = file_path

    def log(self, message):
        with open(self.file_path, "a") as file:
            file.write(f"[{self.log_level}] {message}\n")

class Application:
    def __init__(self, logger):
        self.logger = logger

    def run(self):
        self.logger.log("Application started")
        #application
        self.logger.log("Application finished")

if __name__ == "__main__":
    console_logger = ConsoleLogger(log_level = "DEBUG")
    app = Application(logger=console_logger)
    app.run()

    file_logger = FileLogger(log_level = "ERROR", file_path  = "error.log")
    app = Application(logger = file_logger)
    app.run()