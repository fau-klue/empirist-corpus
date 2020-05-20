# EmpiriST corpus

## Introduction

The EmpiriST corpus is a manually annotated corpus consisting of
German web pages and German computer-mediated communication (CMC),
i.e. written discourse. Examples for CMC genres are monologic and
dialogic tweets, social and professional chats, threads from Wikipedia
talk pages, WhatsApp interactions and blog comments. Here is an
overview of the sizes of the corpus and its subsets in tokens:

|              |    CMC |    Web |  Total |
|--------------|--------|--------|--------|
| **Training** |  5,109 |  4,944 | 10,053 |
| **Test**     |  5,237 |  7,568 | 12,805 |
| **Total**    | 10,346 | 12,512 | 22,858 |

The dataset was originally created by [Beißwenger et al.
(2016)](https://www.aclweb.org/anthology/W16-2606) for the [EmpiriST
2015 shared task](https://sites.google.com/site/empirist2015/) and
featured manual tokenization and part-of-speech tagging. Subsequently,
[Rehbein et al.
(2018)](https://www.oeaw.ac.at/fileadmin/subsites/academiaecorpora/PDF/konvens18_03.pdf)
incorporated the dataset into their [harmonised testsuite for POS
tagging of German social media
data](https://www.cl.uni-heidelberg.de/~rehbein/tweeDe.mhtml),
manually added sentence boundaries and automatically mapped the
part-of-speech tags to [UD pos
tags](https://universaldependencies.org/u/pos/all.html). In our own
annotation efforts ([Proisl et al.,
2020](http://www.lrec-conf.org/proceedings/lrec2020/pdf/2020.lrec-1.754.pdf)),
we manually normalized and lemmatized the data and converted the
corpus into a “vertical” format suitable for importing into the Open
Corpus Workbench, CQPweb, SketchEngine, or similar corpus tools.

## Annotation

Here is a one-sentence posting illustrating the corpus format. The
seven columns are: Word form, [STTS IBK
tag](https://sites.google.com/site/empirist2015/home/annotation-guidelines),
[UD POS tag](https://universaldependencies.org/u/pos/all.html), [USAS
tag](http://ucrel.lancs.ac.uk/usas/), normalized form,
surface-oriented lemma, normalized lemma.

    <posting id="cmc_train_003_099" author="quaki" origid="1-114">
    <s>
    die       ART     DET     Z5           die       der       der
    viecha    NN      NOUN    L2           Viecher   Viech     Viech
    reissen   VVFIN   VERB    A1.1.2/MWU:7 reißen    reissen   reißen
    imma      ADV     ADV     N6           immer     imma      immer
    die       ART     DET     Z5           die       der       der
    müllsäcke NN      NOUN    O2           Müllsäcke Müllsack  Müllsack
    auf       PTKVZ   PART    A1.1.2/MWU:3 auf       auf       auf
    hmmmm     ITJ     INTJ    Z4           hm        hmmmm     hm
    </s>
    </posting>

The following subsections give a bit of additional information about
the annotation process.

### Tokenization and part-of-speech tagging

[Beißwenger et al. (2016:
47)](https://www.aclweb.org/anthology/W16-2606) describe the
annotation process as follows:

> All data sets were manually tokenized and PoS tagged by multiple
> annotators, based on the official
> [tokenization](doc/EmpiriST_Guideline-Tokenisierung.pdf) […] and
> [tagging](doc/EmpiriST_Guideline-PoS.pdf)
> [guidelines](doc/EmpiriST_Guideline-Ergaenzungsdokument.pdf) […].
> Cases of disagreement were then adjudicated by the task organizers to
> produce the final gold standard.

### Sentence splitting

[Rehbein et al. (2018:
20)](https://www.oeaw.ac.at/fileadmin/subsites/academiaecorpora/PDF/konvens18_03.pdf)
used the following rules to guide the segmentation:

> * Hashtags and URLs at the beginning or the end of the tweet that
>   are not integrated in the sentence are separated and form their
>   own unit […].
> * Emoticons are treated as non-verbal comments to the text and are
>   thus integrated in the utterance.
> * Interjections (*Aaahh*), inflectives (*\*grins\**), fillers (*ähm*)
>   and acronyms typical for CMC (*lol*, *OMG*) are also not separated
>   but considered as part of the message.

### Normalization and lemmatization

The data were individually normalized and lemmatized by four student
annotators according to the [lemmatization
guidelines](doc/Lemmatisierungsrichtlinien.pdf). Unclear cases were
decided in group meetings with the team leaders.

## Authors

The corpus data was collected, tokenized and part-of-speech tagged by
the organizers of the EmpiriST 2015 shared task: Michael Beißwenger,
Sabine Bartsch, Stefan Evert and Kay-Michael Würzner.

Ines Rehbein, Josef Ruppenhofer and Victor Zimmermann added sentence
boundaries and automatically mapped the STTS pos tags to UD pos tags.

Thomas Proisl, Natalie Dykes, Philipp Heinrich, Besim Kabashi and
Stefan Evert added normalization and lemmatization.

<!-- ## Utilities -->

<!-- Extract the training set: -->

<!--     xsltproc -o empirist_train.vrt utils/extract_train.xsl empirist.vrt -->

<!-- Extract the test set: -->

<!--     xsltproc -o empirist_test.vrt utils/extract_test.xsl empirist.vrt -->


## References

  * Beißwenger, Michael, Sabine Bartsch, Stefan Evert, and Kai-Michael
    Würzner. 2016. “EmpiriST 2015: A shared task on the automatic
    linguistic annotation of computer-mediated communication and web
    corpora.” In *Proceedings of the 10th Web as Corpus Workshop
    (WAC-X) and the EmpiriST Shared Task*, 44–56, Berlin. Association
    for Computational Linguistics.
    [PDF](https://www.aclweb.org/anthology/W16-2606).
  * Proisl, Thomas, Natalie Dykes, Philipp Heinrich, Besim Kabashi,
    Andreas Blombach, and Stefan Evert. 2020. “EmpiriST Corpus 2.0:
    Adding Manual Normalization, Lemmatization and Semantic Tagging to
    a German Web and CMC Corpus.” In *Proceedings of the 12th Language
    Resources and Evaluation Conference (LREC 2020)*, 6144–6150,
    Marseille. European Language Resources Association.
    [PDF](http://www.lrec-conf.org/proceedings/lrec2020/pdf/2020.lrec-1.754.pdf).
  * Rehbein, Ines, Josef Ruppenhofer, and Victor Zimmermann. 2018. “A
    harmonised testsuite for POS tagging of German social media data.”
    In *Proceedings of the 14th Conference on Natural Language
    Processing (KONVENS 2018)*, 18–28, Wien.
    [PDF](https://www.oeaw.ac.at/fileadmin/subsites/academiaecorpora/PDF/konvens18_03.pdf).
