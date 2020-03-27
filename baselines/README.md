# Baselines for the EmpiriST-Lemma task

This directory provides reference implementations for the baselines of the EmpiriST lemmatization tasks. All systems are trained or optimized on the TIGER treebank and the EmpiriST training set, then evaluated on the EmpiriST test set.

Evaluation results of the current versions can be found at the bottom of this page.


## Baseline implementations

### cwb-lemmatize-smor

`cwb-lemmatize-smor` applies SMOR lemmatization to a [CWB](http://cwb.sourceforge.net/)-indexed corpus, which must include part-of-speech annotation. It can optionally adjust the lemmatization to TIGER conventions or to the EmpiriST tagset and conventions.

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

| A | surf-surf | surf-surf nc | surf-norm | norm-norm |
|:--|----------:|-------------:|----------:|----------:|
| x |   xx      |  x           |  xx       |           |


