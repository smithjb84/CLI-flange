import json
import argparse
from rich.console import Console
from rich.table import Table
import os

parser = argparse.ArgumentParser(
                    prog='Flange Library',
                    description='Script to quickly get dimensions of ASME Flange Sizes')
                    
parser.add_argument('size', help='Nominal Flange Size')
parser.add_argument('cl', help='Flange Class Size')
parser.add_argument('-s', '--series', help='Flange Series if Applicable', default='a')

args = parser.parse_args()

# Opening JSON file
f = open(os.path.dirname(os.path.realpath(__file__))+"\\ASME B16.47 Flanges.json")
data = json.load(f)

table = Table(title="Flange Dimensions")

table.add_column("ASME B16.47 "+args.size+"\""+" "+args.cl+"#"+" Series "+args.series.capitalize()+ " Flange", style="cyan", no_wrap=True)
table.add_column("Dimension", style="yellow")


selection = data["flange"][str(args.series).capitalize()][str(args.size)][str(args.cl)]
selection = data["flange"][str(args.series).capitalize()][str(args.size)][str(args.cl)]

for i in range(len(selection)):
    table.add_row(data["flange"]["verbose"][i], str(selection[i]))
    
console = Console()
console.print(table)