import argparse
import pickle

def tokenize_file(name):
    with open(name, "r", encoding="utf-8") as file:
        words = file.read()
    return words.split()

def clear_data(words):
    return [("".join(filter(str.isalpha, word))).lower() for word in words]

def calc_prob(d):
    for prefix in d:
        sum_counts = sum([tup[1] for tup in d[prefix]])
        d[prefix] = [(tup[0], tup[1]/sum_counts) for tup in d[prefix]]

def learn(words):
    d = {}
    for i in range(2, len(words)):
        prefix = (words[i-2], words[i-1])
        if (prefix in d):
            for j in range(len(d[prefix])):
                if (words[i] == d[prefix][j][0]):
                    d[prefix][j] = (d[prefix][j][0], \
                    d[prefix][j][1] + 1)
                    break
            else:
                d[prefix].append((words[i], 1))
        else:
            d[prefix] = [(words[i], 1)]
    calc_prob(d)
    return d

def main_train(args):
    if (args.input_dir == None):
        line = input()
        tok = line.split()
    else:
        tok = tokenize_file(args.input_dir)
    cleared_data = clear_data(tok)
    d = learn(cleared_data)

    with open(args.model, 'wb') as f:
        pickle.dump(d, f)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--input-dir', dest="input_dir", default=None)
    parser.add_argument('--model', dest="model", default="model.pickle")
    args = parser.parse_args()
    main_train(args)



