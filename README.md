# empirist-corpus

## Introduction

[EmpiriST 2015 shared task](https://sites.google.com/site/empirist2015/)

[harmonised testsuite for POS Tagging of German social media data](https://www.cl.uni-heidelberg.de/~rehbein/tweeDe.mhtml)

## Annotation

The following subsections give a bit of additional information about
the annotation process.

### Tokenization and part-of-speech tagging

[Beißwenger et al.
(2016:47)](https://www.aclweb.org/anthology/W16-2606) describe the
annotation process as follows:

> All data sets were manually tokenized and PoS tagged by multiple
> annotators, based on the official
> [tokenization](doc/EmpiriST_Guideline-Tokenisierung.pdf) […] and
> [tagging](doc/EmpiriST_Guideline-PoS.pdf)
> [guidelines](doc/EmpiriST_Guideline-Ergaenzungsdokument.pdf) […].
> Cases of disagreement were then adjudicated by the task organizers to
> produce the final gold standard.

### Sentence splitting

[Rehbein et al.
(2018:20)](https://www.oeaw.ac.at/fileadmin/subsites/academiaecorpora/PDF/konvens18_03.pdf)
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

The EmpiriST 2015 shared task was organized by Michael Beißwenger,
Sabine Bartsch, Stefan Evert and Kay-Michael Würzner.

Ines Rehbein, Josef Ruppenhofer and Victor Zimmermann added sentence
boundaries and automatically mapped the STTS pos tags to UD pos tags.

Thomas Proisl, Natalie Dykes, Philipp Heinrich, Besim Kabashi and
Stefan Evert added normalization and lemmatization.

## References

  * Beißwenger, Michael, Sabine Bartsch, Stefan Evert, and Kai-Michael
    Würzner. 2016. “EmpiriST 2015: A shared task on the automatic
    linguistic annotation of computer-mediated communication and web
    corpora.” In *Proceedings of the 10th Web as Corpus Workshop
    (WAC-X) and the EmpiriST Shared Task*, 44–56, Berlin. Association
    for Computational Linguistics.
    [PDF](https://www.aclweb.org/anthology/W16-2606).
  * Rehbein, Ines, Josef Ruppenhofer, and Victor Zimmermann. 2018. “A
    harmonised testsuite for POS tagging of German social media data.”
    In *Proceedings of the 14th Conference on Natural Language
    Processing (KONVENS 2018)*, 18–28, Wien.
    [PDF](https://www.oeaw.ac.at/fileadmin/subsites/academiaecorpora/PDF/konvens18_03.pdf).
