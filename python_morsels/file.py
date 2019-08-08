# import csv
# import sys

# old_filename, new_filename = sys.argv[1:]

# """
# bad
# """
# with open(old_filename, newline="") as old_file:
#     reader = csv.reader(old_file, delimiter="|")
#     rows = [line for line in reader]

# with open(new_filename, mode="wt", newline="") as new_line:
#     writer = csv.writer(new_line)
#     writer.writerrows(rows)


# """
# better
# """
# with open(old_filename, newline="") as  old_file:
#     reader = csv.reader(old_file, delimiter="|")
#     with open(new_filename, mode="wt", newline="") as new_file:
#         csv.writer(new_file).writerrows(reader)


"""
For example any of these should work (all specify input delimiter as pipe and the last two additionally specifies the quote character as single quote):

$ python fix_csv.py --in-delimiter="|" cars.csv cars-fixed.csv
$ python fix_csv.py cars.csv cars-fixed.csv --in-delimiter="|"
$ python fix_csv.py --in-delimiter="|" --in-quote="'" cars.csv cars-fixed.csv
$ python fix_csv.py --in-quote="'" --in-delimiter="|" cars.csv cars-fixed.csv
"""



from argparse import ArgumentParser
import csv

"""
 "--" indicates that this is an optional variable
"""

parser = ArgumentParser()
parser.add_argument('old_filename')
parser.add_argument('new_filename')
parser.add_argument('--in-delimiter', dest='delim')
parser.add_argument('--in-quote', dest='quote')
args = parser.parse_args()

with open(args.old_filename, newline='') as old_file:
    arguments = {}
    if args.delim:
        arguments['delimiter'] = args.delim
    if args.quote:
        arguments['quotechar'] = args.quote
    if not args.delim and not args.quote:
        arguments['dialect'] = csv.Sniffer().sniff(old_file.read())
        old_file.seek(0)
    reader = csv.reader(old_file, **arguments)
    rows = list(reader)

with open(args.new_filename, mode='wt', newline='') as new_file:
    writer = csv.writer(new_file)
    writer.writerows(rows)