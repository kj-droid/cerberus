
# Cerberus Firewall Main Script

import json
import os

class CerberusFirewall:
    def __init__(self, config_path="config.json"):
        self.rules = []
        self.config_path = config_path
        self.load_config()

    def load_config(self):
        if os.path.exists(self.config_path):
            with open(self.config_path, 'r') as f:
                config = json.load(f)
                print(f"Config loaded: {config}")
        else:
            print("No configuration file found.")

    def add_rule(self, rule):
        self.rules.append(rule)
        print(f"Rule added: {rule}")

    def show_rules(self):
        print("Current Rules:")
        for rule in self.rules:
            print(rule)

if __name__ == "__main__":
    firewall = CerberusFirewall()
    firewall.add_rule("Allow all outbound traffic on port 80")
    firewall.show_rules()
