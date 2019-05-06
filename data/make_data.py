import csv
import random

def main():
    print("\nReading file...")
    all_lines = []
    with open('english_rock.csv', encoding='utf8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            all_lines.append(row)
    print("\nRead file...")
    print("\nTotal lines ", len(all_lines))

    random.shuffle(all_lines)

    train_lines = all_lines[:int(0.8 *len(all_lines))]
    val_lines = all_lines[int(0.8 * len(all_lines)):int(0.9 * len(all_lines))]
    test_lines = all_lines[int(0.9 * len(all_lines)):]

    print("\nCreating train file...")
    train_keys = train_lines[0].keys()
    with open('train_rock.csv', 'w', encoding='utf8') as csv_file:
        csv_writer = csv.DictWriter(csv_file, train_keys)
        csv_writer.writeheader()
        csv_writer.writerows(train_lines)
    print("\nCreated train file...")

    print("\nCreating val file...")
    val_keys = val_lines[0].keys()
    with open('val_rock.csv', 'w', encoding='utf8') as csv_file:
        csv_writer = csv.DictWriter(csv_file, val_keys)
        csv_writer.writeheader()
        csv_writer.writerows(val_lines)
    print("\nCreated val file...")

    print("\nCreating test file...")
    test_keys = test_lines[0].keys()
    with open('test_rock.csv', 'w', encoding='utf8') as csv_file:
        csv_writer = csv.DictWriter(csv_file, test_keys)
        csv_writer.writeheader()
        csv_writer.writerows(test_lines)
    print("\nCreated val file...")

if __name__ == '__main__':
    main()