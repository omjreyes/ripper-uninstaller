import os
import shutil
import winreg

class AppManager:
    def __init__(self, logger):
        self.logger = logger

    def get_installed_apps(self):
        # Fetch installed apps using registry
        apps = []
        registry_paths = [
            (winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall"),
            (winreg.HKEY_CURRENT_USER, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall"),
        ]
        for reg, path in registry_paths:
            try:
                with winreg.OpenKey(reg, path) as key:
                    for i in range(winreg.QueryInfoKey(key)[0]):
                        sub_key = winreg.EnumKey(key, i)
                        with winreg.OpenKey(key, sub_key) as subkey:
                            try:
                                name = winreg.QueryValueEx(subkey, "DisplayName")[0]
                                apps.append(name)
                            except FileNotFoundError:
                                pass
            except Exception as e:
                self.logger.log("System", f"Error accessing registry: {e}")
        return apps

    def uninstall_app(self, app_name):
        paths = self.get_installation_paths(app_name)
        if not paths:
            self.logger.log(app_name, "No install locations found. Uninstaller might not exist.")
        else:
            for path in paths:
                try:
                    if os.path.exists(path):
                        shutil.rmtree(path)
                        self.logger.log(app_name, f"Deleted {path}")
                except Exception as e:
                    self.logger.log(app_name, f"Error deleting {path}: {e}")

    def get_installation_paths(self, app_name):
        # Fetch installation paths from registry (or other methods)
        return get_installation_paths(app_name)

    def repair_app(self, app_name):
        # Custom repair logic
        self.logger.log(app_name, "Repair started.")
        try:
            # Add repair logic here
            self.logger.log(app_name, "Repair completed.")
        except Exception as e:
            self.logger.log(app_name, f"Repair failed: {e}")