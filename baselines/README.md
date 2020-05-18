# Baselines for the EmpiriST-Lemma task

This directory provides reference implementations for the baselines of the EmpiriST lemmatization tasks. All systems are trained or optimized on the TIGER treebank and the EmpiriST training set, then evaluated on the EmpiriST test set.

Evaluation results of the current versions can be found at the bottom of this page.


## Baseline implementations

### cwb-lemmatize-smor v1.2

`cwb-lemmatize-smor` applies SMOR lemmatization to a [CWB](http://cwb.sourceforge.net/)-indexed corpus, which must include part-of-speech annotation. It applies various heuristics for capitalization differences, tagset adjustment, lemma disambiguation and unknown words.  It can optionally adjust the lemmatization to TIGER conventions (`--tiger`) and to the quirks of the EmpiriST tagset and conventions (`--tiger --empirist`).

The prerequisites listed below must be installed.  Then run `perl cwb-lemmatize-smor -h` for a brief usage summary.

- [IMS Corpus Workbench](http://cwb.sourceforge.net/developers.php#svn), version 3.4.19 or newer
- CWB/Perl interface (latest version from [SVN](http://cwb.sourceforge.net/developers.php#svn)); packages `CWB` and `CWB-CL` are required
- [SMOR](https://www.cis.uni-muenchen.de/~schmid/tools/SMOR/); the command-line utility `smor-lemmatizer` must be in the standard search path

`cwb-lemmatize-smor` is made available under the same terms as Perl itself, in particular the [Artistic Licence](https://www.perlfoundation.org/artistic-license-10.html).


## Evaluation results

All baselines are evaluated in four different settings (but results are not always available for all settings):

1. **surf-surf**: surface form ➞ surface-oriented lemma
2. **surf-surf nocase**: surface form ➞ surface-oriented lemma (case-insensitive)
3. **surf-norm**: surface form ➞ normalized lemma
4. **norm-norm**: normalized word ➞ normalized lemma

The primary evaluation result is the score for setting 1 (surf-surf).

|                              | surf-surf | surf-surf nc | surf-norm | norm-norm |
|:-----------------------------|----------:|-------------:|----------:|----------:|
| Use word form                |     66.18 |        71.63 |     65.44 |     71.29 |
| Lookup EmpiriST              |     85.75 |              |     85.22 |           |
| Lookup TIGER                 |     93.27 |              |     92.53 |           |
| Lookup TIGER + EmpiriST      |     94.52 |              |     93.92 |           |
|                              |           |              |           |           |
| TreeTagger                   |     80.80 |              |     80.34 |           |
| TreeTagger + post-processing |     92.01 |              |     91.74 |           |
| RNNTagger                    |     92.71 |              |     92.06 |           |
|                              |           |              |           |           |
| **statistical lemmatizers**  |           |              |           |           |
| OpenNLP EmpiriST             |     76.17 |        92.78 |     75.81 |           |
| OpenNLP TIGER + EmpiriST     |     78.51 |        97.51 |     78.13 |           |
| mate-tools EmpiriST          |     71.00 |        86.36 |     70.55 |           |
| mate-tools TIGER + EmpiriST  |     76.83 |        94.30 |     76.26 |           |
|                              |           |              |           |           |
| **SMOR morphology**          |           |              |           |           |
| `cwb-lemmatize-smor` v1.0    |     74.01 |              |     74.04 |           |
|  + TIGER post-processing     |     89.21 |              |     89.22 |           |
|  + unknown-word heuristics   |     96.96 |              |     96.20 |           |
| `cwb-lemmatize-smor` v1.2    |           |              |           |           |
|  + heuristic & disambiguation|     83.44 |        84.88 |     82.80 |     83.98 |
|  + TIGER adaptations         |     97.30 |        98.62 |     96.66 |     97.95 |
|  + EmpiriST adaptations      | **97.81** |    **98.73** | **96.94** | **98.62** |
