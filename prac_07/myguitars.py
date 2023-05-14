import csv

def main():
    guitars = []
    in_file = open('guitars.csv', 'r')
    in_file.readline()
    for line in in_file:
        parts = line.strip().split
