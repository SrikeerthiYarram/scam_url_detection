from PyQt5.QtWidgets import QMessageBox
from app.dialogs.blacklist import load_blacklist,is_blacklisted,add_to_blacklist
from app.dialogs.whitelist import load_whitelist,is_whitelisted
from app.dialogs.rule_editor import evaluate_url
from app.dialogs.settings import SettingsDialog
from app.dialogs.logs import LogsDialog

class UIController:
    def __init__(self, main_window):
        
        self.main_window = main_window

        
        self.connect_ui()

    def connect_ui(self):
       
        self.main_window.check_btn.clicked.connect(self.check_url)
        self.main_window.url_input.returnPressed.connect(self.check_url)

     
        self.main_window.open_blacklist_action.triggered.connect(self.open_blacklist)
        self.main_window.open_watchlist_action.triggered.connect(self.open_watchlist)
        self.main_window.open_rule_editor_action.triggered.connect(self.open_rule_editor)
        self.main_window.open_settings_action.triggered.connect(self.open_settings)
        self.main_window.open_logs_action.triggered.connect(self.open_logs)
        self.main_window.about_action.triggered.connect(self.show_about)

    def check_url(self):
    url = self.main_window.url_input.text().strip()
    if not url:
        QMessageBox.warning(self.main_window, "Missing URL", "Please enter a URL to check.")
        return

    self.main_window.statusBar().showMessage("Checking...")
    self.main_window.check_btn.setEnabled(False)

    # 1️⃣ Check dynamic blacklist first
    blacklisted, domain = is_blacklisted(url)
    if blacklisted:
        result = {
            "url": url,
            "score": 10,
            "verdict": "Malicious",
            "matched_rules": [
                {"rule": "Blacklist match", "explanation": f"URL matches '{domain}'", "weight": 10}
            ]
        }
    else:
        # 2️⃣ Optional: check whitelist
        whitelisted = False
        if 'is_whitelisted' in globals():  # if you have a whitelist
            whitelisted = is_whitelisted(url)

        if whitelisted:
            result = {
                "url": url,
                "score": 0,
                "verdict": "Safe",
                "matched_rules": []
            }
        else:
            # 3️⃣ Run heuristic rules
            result = evaluate_url(url)  # your heuristics function

    self.main_window.display_result(result)
    self.main_window.check_btn.setEnabled(True)
    self.main_window.statusBar().showMessage("Check complete.")


        
        self.main_window.display_result(result)

       
        self.main_window.check_btn.setEnabled(True)
        self.main_window.statusBar().showMessage("Check complete.")

    def open_blacklist(self):
        dialog = BlacklistDialog(self.main_window)
        dialog.exec_()

    def open_watchlist(self):
        dialog = WatchlistDialog(self.main_window)
        dialog.exec_()

    def open_rule_editor(self):
        dialog = RuleEditorDialog(self.main_window)
        dialog.exec_()

    def open_settings(self):
        dialog = SettingsDialog(self.main_window)
        dialog.exec_()

    def open_logs(self):
        dialog = LogsDialog(self.main_window)
        dialog.exec_()

    def show_about(self):
        QMessageBox.information(
            self.main_window,
            "About",
        "Fake URL Detector"
        )
