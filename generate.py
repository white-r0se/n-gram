import argparse
import pickle
import numpy as np

def generate_new_word(prefix, d):
    if (prefix in d):
        index = np.random.choice(len(d[prefix]), p=[tup[1] for tup in d[prefix]])
        return d[prefix][index][0]
    else:
        return None

def generation(line, d, n):
    count = 0
    while (True):
        new_word = generate_new_word((line[-2], line[-1]), d)
        if (new_word == None):
            break
        line.append(new_word)
        count += 1
        if count == n:
            break
    print(" ".join(line))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--model', dest="model", required=True)
    parser.add_argument('--prefix', dest="prefix", nargs="+", default=None)
    parser.add_argument('--length', dest="length", type=int, default=10)
    args = parser.parse_args()

    with open(args.model, 'rb') as f:
        d = pickle.load(f)

    if (args.prefix == None):
        prefix = [list(d.keys())[np.random.randint(len(d))][np.random.randint(2)]]
    else:
        prefix = args.prefix
    if (len(prefix) == 1):
        next_words = []
        for key in d:
            if (prefix[0] == key[0]):
                next_words.append(key[1])
            elif (prefix[0] == key[1]):
                next_words.append(d[key][np.random.randint(len(d[key]))][0])
        prefix.append(np.random.choice(next_words))

    generation(prefix, d, args.length)



    