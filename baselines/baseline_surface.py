#!/usr/bin/env python3

import argparse


def arguments():
    parser = argparse.ArgumentParser(description="Evaluate the simplest lemmatization strategy: Always use the word form.")
    parser.add_argument("FILE", type=argparse.FileType("r", encoding="utf-8"), help="Input file.")
    args = parser.parse_args()
    return args


def lemmatize_file(f):
    total, sur, norm, nw, sur_nc, norm_nc, nw_nc, nl = 0, 0, 0, 0, 0, 0, 0, 0
    for line in f:
        line = line.rstrip()
        if line == "":
            continue
        if line.startswith("<") and line.endswith(">"):
            continue
        if line.endswith("\tCLARIFY"):
            line = line[:-8]
        word, pos, udpos, norm_word, sur_lemma, norm_lemma = line.split("\t")
        total += 1
        if word.lower() == sur_lemma.lower():
            sur_nc += 1
        if word == sur_lemma:
            sur += 1
        if word.lower() == norm_lemma.lower():
            norm_nc += 1
        if word == norm_lemma:
            norm += 1
        if word.lower() == norm_word.lower():
            nw_nc += 1
        if word == norm_word:
            nw += 1
        if norm_word == norm_lemma:
            nl += 1
    return total, sur, norm, nw, sur_nc, norm_nc, nw_nc, nl


def main():
    args = arguments()
    total, sur, norm, norm_word, sur_nc, norm_nc, norm_word_nc, normlem = 0, 0, 0, 0, 0, 0, 0, 0
    t, s, n, nw, snc, nnc, nwnc, nl = lemmatize_file(args.FILE)
    total += t
    sur += s
    norm += n
    norm_word += nw
    sur_nc += snc
    norm_nc += nnc
    norm_word_nc += nwnc
    normlem += nl
    # print(total, sur, norm, norm_word)
    print("Normalized word form: %.2f%% accuracy (%.2f%% case-insensitive)" % (norm_word / total * 100, norm_word_nc / total * 100))
    print("Surface-oriented lemma: %.2f%% accuracy (%.2f%% case-insensitive)" % (sur / total * 100, sur_nc / total * 100))
    print("Normalized lemma: %.2f%% accuracy (%.2f%% case-insensitive)" % (norm / total * 100, norm_nc / total * 100))
    print("Normalized lemma based on normalized word forms: %.2f%%" % (normlem / total * 100))


if __name__ == "__main__":
    main()
