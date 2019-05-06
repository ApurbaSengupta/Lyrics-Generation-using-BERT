import argparse
from nltk.translate.bleu_score import sentence_bleu
import warnings

warnings.simplefilter("ignore", UserWarning)

def bleuScore(gold, pred):
    cumulativeBlue, totalSentences = 0, len(gold)

    for line in gold:
        assert line in pred
        reference = [gold[line].split(' ')]
        candidate = pred[line].split(' ') 
        cumulativeBlue += sentence_bleu(reference, candidate, weights=(.334, 0.333, 0.333, 0))

    return cumulativeBlue / totalSentences

def accuracy(gold, pred):
    num_correct, num_total = 0, 0
    for line1 in gold:
        assert line1 in pred
        if gold[line1] == pred[line1]:
            num_correct += 1
        num_total += 1

    accuracy = num_correct / num_total

    return accuracy

def loadData(name):
    data = {}
    with open(name) as file:
        for line in file:
            line1, line2 = line.strip().split('\t')
            data[line1] = line2

    return data

def main(args):
    gold = loadData(args.goldfile)
    pred = loadData(args.predfile)

    assert len(gold) == len(pred)

    print(f'Accuracy: {accuracy(gold, pred):.2f}')
    print(f'BLEU score: {bleuScore(gold, pred):.2f}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--goldfile', type=str, required=True)
    parser.add_argument('--predfile', type=str, required=True)

    args = parser.parse_args()
    main(args)