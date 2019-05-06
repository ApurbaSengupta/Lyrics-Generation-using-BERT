import csv
import random
import argparse

def main(args):
    all_lines = []
    all_pairs = []
    with open(args.datafile, encoding='utf8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            lines = row['lyrics'].split('\n')
            for i in range(len(lines) - 1):
                all_pairs.append((lines[i], lines[i + 1]))
                all_lines.append(lines[i])
            all_lines.append(lines[len(lines) - 1])

    sampled_data_x = {}
    sampled_data_y = {}
    correct_pairs = random.sample(all_pairs, 100)
    for line1, line2 in correct_pairs:
        sampled_data_y[line1] = line2
        sampled_data_x[line1] = [line2]
        sampled_data_x[line1].extend(random.sample(all_lines, 9))

    with open('predfile', 'w') as file:
        for line1, line2s in sampled_data_x.items():
            line2 = random.choice(line2s)
            file.write(f'{line1}\t{line2}\n')
    with open('goldfile', 'w') as file:
        for line1, line2 in sampled_data_y.items():
            file.write(f'{line1}\t{line2}\n')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--datafile', type=str, required=True)

    args = parser.parse_args()
    main(args)