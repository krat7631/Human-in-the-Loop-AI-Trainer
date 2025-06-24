import csv
import os

def save_feedback(text, label):
    path = "data/user_feedback.csv"
    new_file = not os.path.exists(path)

    with open(path, "a", newline="") as f:
        writer = csv.writer(f)
        if new_file:
            writer.writerow(["comment", "label"])
        writer.writerow([text, label])
