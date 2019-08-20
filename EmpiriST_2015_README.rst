===============================
The EmpiriST 2015 Gold Standard
===============================


Background
==========

The goal of the EmpiriST 2015 shared task was to encourage the developers of
NLP applications to adapt their tools and resources to the processing of
German Web pages and written German discourse in genres of computer-mediated
communication (CMC).  Examples for CMC genres are chats, forums, wiki talk
pages, tweets, blog comments, social networks, SMS and WhatsApp dialogues.

The shared task focuseed on tokenization and part-of-speech tagging as the
first and fundamental steps of most NLP pipelines. In the first part of the
task, participants received raw text files and had to submit tokenized
versions in one-token-per-line format. In the second part, participants
receive pre-tokenized text and had to annotated each token with a POS tag,
using the STTS_IBK tag set described in "tagset.txt".

See the website https://sites.google.com/site/empirist2015/ for further
information and detailed annotation guidelines.

This archive contains the official EmpiriST 2015 Gold Standard, with training
and test data for the tokenization and PoS tagging subtasks. Raw texts,
manually tokenized files and manual PoS annotation are provided for each part.
In addition, the official scorers and several other tools are included in the
form of Perl scripts.


License
=======

All files within this archive are published under the terms of the Creative
Commons BY-SA 3.0 license. You receive a copy of the license text in the file
"COPYING".

If you use these data in your research, please cite the EmpiriST 2015 task
description paper (a BibTeX entry can be found in the file "reference.bib").

    Beißwenger, Michael; Bartsch, Sabine; Evert, Stefan; Würzner, Kay-Michael
    (2016).  EmpiriST 2015: A shared task on the automatic linguistic
    annotation of computer-mediated communication and web corpora.  In
    Proceedings of the 10th Web as Corpus Workshop (WAC-X) and the EmpiriST
    Shared Task, pages 78-90, Berlin, Germany.


Contents
========

The evaluation data for the EmpiriST shared task are taken from various
sources and are divided into a **Web corpora** subset (monologic texts) and a
**CMC** subset (dialogic texts such as chats, tweets, short messages etc.).

Training and test data for each subset are provided in separate directories:

``train_cmc/``

    CMC training data.

``train_web/``

    Web corpora training data.

``test_cmc/``

    CMC test data.

``test_web/``

    Web corpora test data.

Each of these directories has the same structure with three subdirectories,
containing raw, tokenized and tagged texts with exactly the same filenames:
    
``raw/*.txt``

    The raw source texts, as plain UTF-8 encoded text files with Unix line
    breaks. Text files are structured into segments separated by blank lines
    (i.e. two subsequent line breaks), which correspond to postings in the CMC
    subset and to paragraph-like units in the Web corpora subset. Additional
    meta-information may be included in the form of emtpy XML elements (e.g. a
    timestamp for each posting in the CMC subset).

``tokenized/*.txt``

    For each text file in ``raw/``, this directory contains a manually
    tokenized file with the same name. The format is plain UTF-8 encoded text
    with Unix line breaks. Tokens are separated by single line breaks, i.e. the
    file has a one-token-per-line format. As in the raw source texts,
    posting/paragraph boundaries are marked by blank lines (i.e. two subsequent
    line breaks), and empty XML elements containing metadata are preserved on
    separate lines.

``tagged/*.txt``

    For each text file in ``raw/`` and tokenized file in ``tokenized/``, this
    directory contains a manually POS-tagged file with the same name. Its
    format corresponds to the tokenized files (in particular, plain UTF-8
    encoded text with Unix line breaks), except that every token is followed by
    a TAB stop (``\t``, ASCII decimal code 9) and its part-of-speech tag on the
    same line. The tags used are listed in the file ``tagset.txt``; see the
    annotation guidelines for a detailed explanation.

Several other files and utilities can be found in the top-level directory:    

``README.rst``

    This README file.

``COPYING``

    A copy of the CC-BY-SA 3.0 license.

``reference.bib``

    A BibTeX entry for the EmpiriST task description paper.  Please cite this
    paper if you make use of the gold standard in your published research.
    
``tagset.txt``

    A concise description of the STTS_IBK tag set used for PoS annotation.
    
``tools/compare_tokenization.perl``

``tools/compare_tagging.perl``

    Perl scripts for evaluating tokenization and tagging results according
    to the official EmpiriST metrics. (Some users may need to install the Perl
    module Algorithm::Diff from CPAN.)

``tools/validate_tokenization.perl``

``tools/validate_tagging.perl``

    Perl scripts for validating the format of system output files before
    submission to the shared task.

``tools/normalize_text.perl``

    A Perl script for text cleanup and whitespace tokenization (used as a
    basis for the manual tokenization of the gold standard).

``tools/line_count.perl``

    Perl script for counting the number of tokens in one-word-per-line files
    (automatically skips empty lines and XML elements).


Sources
=======

The CMC data include samples from the following CMC genres and sources:

``TWEETS``

    Some tweets taken from the Twitter channel of an academy project, some
    tweets taken from the Twitter channel of a lecturer in German Linguistics,
    used for discussions with students accompanying a university class)

``SOCIAL CHAT``

    Postings selected from the Dortmund Chat Corpus, http://www.chatkorpus.tu-dortmund.de

``PROFESSIONAL CHAT``

    Postings selected from the Dortmund Chat Corpus, http://www.chatkorpus.tu-dortmund.de

``WIKIPEDIA TALK PAGES``

    Samples from talk pages of the German Wikipedia

``WHATSAPP CONVERSATIONS``

    Postings taken from the data set collected by the project "WhatsApp,
    Deutschland?", http://www.whatsup-deutschland.de/

``BLOG COMMENTS``

    Comments posted on weblogs under a CC license

The Web corpora training data include text samples obtained from various Web
pages that are licensed under CC-BY-SA 3.0 or a compatible (more permissive)
licence.

URLs of the original pages are embedded in the metadata tag on the first line
of each text file in the form ``<article id="..." url="SOURCE URL"/>``.
    

Authors
=======

The shared task (ST) has been prepared by members of the DFG scientific network
Empirikom (therefore: "EmpiriST"):
Sabine Bartsch, Michael Beißwenger, Stefan Evert and Kay-Michael Würzner

Its preparation has parially been funded by the German Society for Language
Technology and Computational Linguistics (GSCL). The shared task is endorsed
by the ACL Special Interest Group on the Web as Corpus and by the GSCL Special
Interest Group on Social Media / Computer-Mediated Communication.
