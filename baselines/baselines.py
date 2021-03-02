#!/usr/bin/env python3

import argparse
import collections


def arguments():
    parser = argparse.ArgumentParser(description="Given a word form and a POS tag, return the most frequent lemma from TIGER. Fallback 1: Ignore case. Fallback 2: Return word form.")
    parser.add_argument("-t", "--tiger", type=argparse.FileType("r", encoding="utf-8"), required=True, help="Path to TIGER corpus")
    parser.add_argument("-d", "--trainfile", type=argparse.FileType("r", encoding="utf-8"), help="Training data")
    parser.add_argument("-i", "--ignore-case", action="store_true", help="Ignore case")
    parser.add_argument("INPUT", type=argparse.FileType("r", encoding="utf-8"), help="Test data")
    args = parser.parse_args()
    return args


def read_tiger(f):
    dic = collections.defaultdict(collections.Counter)
    dic_lc = collections.defaultdict(collections.Counter)
    for line in f:
        line = line.rstrip()
        if line == "":
            continue
        fields = line.split("\t")
        token = fields[1]
        lemma = fields[2]
        pos = fields[4]
        if lemma == "--":
            continue
        if pos == "PROAV":
            pos = "PAV"
        dic[(token, pos)][lemma] += 1
        dic_lc[(token.lower(), pos)][lemma] += 1
    return dic, dic_lc


def read_train(fh):
    norm_dic = collections.defaultdict(collections.Counter)
    norm_dic_lc = collections.defaultdict(collections.Counter)
    word_slemma_dic = collections.defaultdict(collections.Counter)
    word_slemma_dic_lc = collections.defaultdict(collections.Counter)
    word_nlemma_dic = collections.defaultdict(collections.Counter)
    word_nlemma_dic_lc = collections.defaultdict(collections.Counter)
    norm_slemma_dic = collections.defaultdict(collections.Counter)
    norm_slemma_dic_lc = collections.defaultdict(collections.Counter)
    norm_nlemma_dic = collections.defaultdict(collections.Counter)
    norm_nlemma_dic_lc = collections.defaultdict(collections.Counter)
    for line in fh:
        line = line.rstrip()
        if line == "":
            continue
        if line.startswith("<") and line.endswith(">"):
            continue
        word, pos, udpos, semtag, norm_word, sur_lemma, norm_lemma, *rest = line.split("\t")
        if pos == "PIDAT":
            pos = "PIAT"
        norm_dic[word][norm_word] += 1
        norm_dic_lc[word.lower()][norm_word] += 1
        word_slemma_dic[(word, pos)][sur_lemma] += 1
        word_slemma_dic_lc[(word.lower(), pos)][sur_lemma] += 1
        word_nlemma_dic[(word, pos)][norm_lemma] += 1
        word_nlemma_dic_lc[(word.lower(), pos)][norm_lemma] += 1
        norm_slemma_dic[(norm_word, pos)][sur_lemma] += 1
        norm_slemma_dic_lc[(norm_word.lower(), pos)][sur_lemma] += 1
        norm_nlemma_dic[(norm_word, pos)][norm_lemma] += 1
        norm_nlemma_dic_lc[(norm_word.lower(), pos)][norm_lemma] += 1
    return norm_dic, norm_dic_lc, word_slemma_dic, word_slemma_dic_lc, word_nlemma_dic, word_nlemma_dic_lc, norm_slemma_dic, norm_slemma_dic_lc, norm_nlemma_dic, norm_nlemma_dic_lc


def lemmatize_surface(fh, ignore_case, use_normalized=False):
    total, nw, sur, nl = 0, 0, 0, 0
    for line in fh:
        line = line.rstrip()
        if line == "":
            continue
        if line.startswith("<") and line.endswith(">"):
            continue
        word, pos, udpos, semtag, norm_word, sur_lemma, norm_lemma, *rest = line.split("\t")
        if use_normalized:
            word = norm_word
        total += 1
        if ignore_case:
            if word.lower() == norm_word.lower():
                nw += 1
            if word.lower() == sur_lemma.lower():
                sur += 1
            if word.lower() == norm_lemma.lower():
                nl += 1
        else:
            if word == norm_word:
                nw += 1
            if word == sur_lemma:
                sur += 1
            if word == norm_lemma:
                nl += 1
    return total, nw, sur, nl


def lemmatize_train(fh, norm_dic, norm_dic_lc, slemma_dic, slemma_dic_lc, nlemma_dic, nlemma_dic_lc, ignore_case, use_normalized=False):
    total, nw, sur, nl = 0, 0, 0, 0
    unk_cased = {"nw": 0, "sur": 0, "nl": 0}
    unk_uncased = {"nw": 0, "sur": 0, "nl": 0}
    for line in fh:
        line = line.rstrip()
        if line == "":
            continue
        if line.startswith("<") and line.endswith(">"):
            continue
        word, pos, udpos, semtag, norm_word, sur_lemma, norm_lemma, *rest = line.split("\t")
        if use_normalized:
            word = norm_word
        total += 1
        normalized, slemma, nlemma = word, word, word
        if word in norm_dic:
            normalized = norm_dic[word].most_common(1)[0][0]
            unk_cased["nw"] += 1
        elif word.lower() in norm_dic_lc:
            normalized = norm_dic_lc[word.lower()].most_common(1)[0][0]
            unk_uncased["nw"] += 1
        if (word, pos) in slemma_dic:
            slemma = slemma_dic[(word, pos)].most_common(1)[0][0]
            unk_cased["sur"] += 1
        elif (word.lower(), pos) in slemma_dic_lc:
            slemma = slemma_dic_lc[(word.lower(), pos)].most_common(1)[0][0]
            unk_uncased["sur"] += 1
        if (word, pos) in nlemma_dic:
            nlemma = nlemma_dic[(word, pos)].most_common(1)[0][0]
            unk_cased["nl"] += 1
        elif (word.lower(), pos) in nlemma_dic_lc:
            nlemma = nlemma_dic_lc[(word.lower(), pos)].most_common(1)[0][0]
            unk_uncased["nl"] += 1
        if ignore_case:
            if normalized.lower() == norm_word.lower():
                nw += 1
            if slemma.lower() == sur_lemma.lower():
                sur += 1
            if nlemma.lower() == norm_lemma.lower():
                nl += 1
        else:
            if normalized == norm_word:
                nw += 1
            if slemma == sur_lemma:
                sur += 1
            if nlemma == norm_lemma:
                nl += 1
    return total, nw, sur, nl, unk_cased, unk_uncased


def main():
    args = arguments()
    tiger, tiger_lc = read_tiger(args.tiger)
    norm_dic, norm_dic_lc, word_slemma_dic, word_slemma_dic_lc, word_nlemma_dic, word_nlemma_dic_lc, norm_slemma_dic, norm_slemma_dic_lc, norm_nlemma_dic, norm_nlemma_dic_lc = read_train(args.trainfile)
    # for x in slemma_dic:
    #     if x in tiger:
    #         x_top = slemma_dic[x].most_common(1)[0][0]
    #         y_top = tiger[x].most_common(1)[0][0]
    #         if x_top != y_top:
    #             print(x, x_top, y_top)
    print("Surface tokens")
    total, norm_word, sur_lemmma, norm_lemma = lemmatize_surface(args.INPUT, args.ignore_case)
    # print(" ", total, norm_word, sur_lemmma, norm_lemma)
    print("  Normalized word: %.2f%% accuracy" % (norm_word / total * 100))
    print("  Surface-oriented lemma: %.2f%% accuracy" % (sur_lemmma / total * 100))
    print("  Normalized lemma: %.2f%% accuracy" % (norm_lemma / total * 100))
    args.INPUT.seek(0)
    print("Normalized tokens")
    total, norm_word, sur_lemmma, norm_lemma = lemmatize_surface(args.INPUT, args.ignore_case, use_normalized=True)
    # print(" ", total, norm_word, sur_lemmma, norm_lemma)
    print("  Normalized word: %.2f%% accuracy" % (norm_word / total * 100))
    print("  Surface-oriented lemma: %.2f%% accuracy" % (sur_lemmma / total * 100))
    print("  Normalized lemma: %.2f%% accuracy" % (norm_lemma / total * 100))
    args.INPUT.seek(0)
    print("Train EmpiriST")
    print("  Surface tokens")
    total, norm_word, sur_lemmma, norm_lemma, unk_cased, unk_uncased = lemmatize_train(args.INPUT, norm_dic, norm_dic_lc, word_slemma_dic, word_slemma_dic_lc, word_nlemma_dic, word_nlemma_dic_lc, args.ignore_case)
    print("    Normalized word: %.2f%% accuracy; unknown: %.2f%%" % (norm_word / total * 100, (1 - (unk_cased["nw"] + unk_uncased["nw"]) / total) * 100))
    print("    Surface-oriented lemma: %.2f%% accuracy; unknown: %.2f%%" % (sur_lemmma / total * 100, (1 - (unk_cased["sur"] + unk_uncased["sur"]) / total) * 100))
    print("    Normalized lemma: %.2f%% accuracy; unknown: %.2f%%" % (norm_lemma / total * 100, (1 - (unk_cased["nl"] + unk_uncased["nl"]) / total) * 100))
    args.INPUT.seek(0)
    print("  Normalized tokens")
    total, norm_word, sur_lemmma, norm_lemma, unk_cased, unk_uncased = lemmatize_train(args.INPUT, norm_dic, norm_dic_lc, norm_slemma_dic, norm_slemma_dic_lc, norm_nlemma_dic, norm_nlemma_dic_lc, args.ignore_case, use_normalized=True)
    print("    Normalized word: %.2f%% accuracy; unknown: %.2f%%" % (norm_word / total * 100, (1 - (unk_cased["nw"] + unk_uncased["nw"]) / total) * 100))
    print("    Surface-oriented lemma: %.2f%% accuracy; unknown: %.2f%%" % (sur_lemmma / total * 100, (1 - (unk_cased["sur"] + unk_uncased["sur"]) / total) * 100))
    print("    Normalized lemma: %.2f%% accuracy; unknown: %.2f%%" % (norm_lemma / total * 100, (1 - (unk_cased["nl"] + unk_uncased["nl"]) / total) * 100))
    args.INPUT.seek(0)
    print("Train TIGER")
    print("  Surface tokens")
    total, norm_word, sur_lemmma, norm_lemma, unk_cased, unk_uncased = lemmatize_train(args.INPUT, {}, {}, tiger, tiger_lc, tiger, tiger_lc, args.ignore_case)
    # print(" ", total, norm_word, sur_lemmma, norm_lemma)
    print("    Normalized word: %.2f%% accuracy; unknown: %.2f%%" % (norm_word / total * 100, (1 - (unk_cased["nw"] + unk_uncased["nw"]) / total) * 100))
    print("    Surface-oriented lemma: %.2f%% accuracy; unknown: %.2f%%" % (sur_lemmma / total * 100, (1 - (unk_cased["sur"] + unk_uncased["sur"]) / total) * 100))
    print("    Normalized lemma: %.2f%% accuracy; unknown: %.2f%%" % (norm_lemma / total * 100, (1 - (unk_cased["nl"] + unk_uncased["nl"]) / total) * 100))
    args.INPUT.seek(0)
    print("  Normalized tokens")
    total, norm_word, sur_lemmma, norm_lemma, unk_cased, unk_uncased = lemmatize_train(args.INPUT, {}, {}, tiger, tiger_lc, tiger, tiger_lc, args.ignore_case, use_normalized=True)
    # print(" ", total, norm_word, sur_lemmma, norm_lemma)
    print("    Normalized word: %.2f%% accuracy; unknown: %.2f%%" % (norm_word / total * 100, (1 - (unk_cased["nw"] + unk_uncased["nw"]) / total) * 100))
    print("    Surface-oriented lemma: %.2f%% accuracy; unknown: %.2f%%" % (sur_lemmma / total * 100, (1 - (unk_cased["sur"] + unk_uncased["sur"]) / total) * 100))
    print("    Normalized lemma: %.2f%% accuracy; unknown: %.2f%%" % (norm_lemma / total * 100, (1 - (unk_cased["nl"] + unk_uncased["nl"]) / total) * 100))
    args.INPUT.seek(0)
    print("Train TIGER + EmpiriST")
    for k, v in tiger.items():
        word_slemma_dic[k] += v
        norm_slemma_dic[k] += v
    for k, v in tiger_lc.items():
        word_slemma_dic_lc[k] += v
        norm_slemma_dic_lc[k] += v
    for k, v in tiger.items():
        word_nlemma_dic[k] += v
        norm_nlemma_dic[k] += v
    for k, v in tiger_lc.items():
        word_nlemma_dic_lc[k] += v
        norm_nlemma_dic_lc[k] += v
    print("  Surface tokens")
    total, norm_word, sur_lemmma, norm_lemma, unk_cased, unk_uncased = lemmatize_train(args.INPUT, norm_dic, norm_dic_lc, word_slemma_dic, word_slemma_dic_lc, word_nlemma_dic, word_nlemma_dic_lc, args.ignore_case)
    # print(" ", total, norm_word, sur_lemmma, norm_lemma)
    print("    Normalized word: %.2f%% accuracy; unknown: %.2f%%" % (norm_word / total * 100, (1 - (unk_cased["nw"] + unk_uncased["nw"]) / total) * 100))
    print("    Surface-oriented lemma: %.2f%% accuracy; unknown: %.2f%%" % (sur_lemmma / total * 100, (1 - (unk_cased["sur"] + unk_uncased["sur"]) / total) * 100))
    print("    Normalized lemma: %.2f%% accuracy; unknown: %.2f%%" % (norm_lemma / total * 100, (1 - (unk_cased["nl"] + unk_uncased["nl"]) / total) * 100))
    args.INPUT.seek(0)
    print("  Normalized tokens")
    total, norm_word, sur_lemmma, norm_lemma, unk_cased, unk_uncased = lemmatize_train(args.INPUT, norm_dic, norm_dic_lc, norm_slemma_dic, norm_slemma_dic_lc, norm_nlemma_dic, norm_nlemma_dic_lc, args.ignore_case, use_normalized=True)
    # print(" ", total, norm_word, sur_lemmma, norm_lemma)
    print("    Normalized word: %.2f%% accuracy; unknown: %.2f%%" % (norm_word / total * 100, (1 - (unk_cased["nw"] + unk_uncased["nw"]) / total) * 100))
    print("    Surface-oriented lemma: %.2f%% accuracy; unknown: %.2f%%" % (sur_lemmma / total * 100, (1 - (unk_cased["sur"] + unk_uncased["sur"]) / total) * 100))
    print("    Normalized lemma: %.2f%% accuracy; unknown: %.2f%%" % (norm_lemma / total * 100, (1 - (unk_cased["nl"] + unk_uncased["nl"]) / total) * 100))


if __name__ == "__main__":
    main()
