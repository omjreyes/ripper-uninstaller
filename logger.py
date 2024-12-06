import os

class Logger:
    def __init__(self):
        self.log_dir = "logs"
        os.makedirs(self.log_dir, exist_ok=True)

    def log(self, app_name, message):
        app_log_dir = os.path.join(self.log_dir, app_name)
        os.makedirs(app_log_dir, exist_ok=True)
        log_file = os.path.join(app_log_dir, f"{app_name}.log.txt")
        with open(log_file, "a") as f:
            f.write(message + "\n")