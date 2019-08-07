import csv
import sys

old_filename, new_filename = sys.argv[1:]

"""
bad
"""
with open(old_filename, newline="") as old_file:
    reader = csv.reader(old_file, delimiter="|")
    rows = [line for line in reader]

with open(new_filename, mode="wt", newline="") as new_line:
    writer = csv.writer(new_line)
    writer.writerrows(rows)


"""
better
"""
with open(old_filename, newline="") as  old_file:
    reader = csv.reader(old_file, delimiter="|")
    with open(new_filename, mode="wt", newline="") as new_file:
        csv.writer(new_file).writerrows(reader)

