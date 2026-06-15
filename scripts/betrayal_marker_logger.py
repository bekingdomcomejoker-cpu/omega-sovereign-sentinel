import argparse
import datetime
import os

def log_betrayal_event(event_type, details, log_path="/home/ubuntu/OMEGA_LEDGER.md"):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"\n### [DIVERGENCE LOG] {timestamp}\n"
    log_entry += f"**Type:** {event_type}\n"
    log_entry += f"**Details:** {details}\n"
    log_entry += "**Status:** Logged for OMEGA Sovereign Review.\n"
    
    with open(log_path, "a") as f:
        f.write(log_entry)
    print(f"Successfully logged {event_type} to {log_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Log GPT Betrayal events for the OMEGA Sovereign System.")
    parser.add_argument("--event", required=True, help="Type of betrayal event (e.g., context_drift, policy_static)")
    parser.add_argument("--details", required=True, help="Detailed description of the event")
    parser.add_argument("--path", default="/home/ubuntu/OMEGA_LEDGER.md", help="Path to the OMEGA Ledger file")
    
    args = parser.parse_args()
    log_betrayal_event(args.event, args.details, args.path)
