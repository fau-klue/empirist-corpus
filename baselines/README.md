# Baselines for the EmpiriST-Lemma task

## cwb-lemmatize-smor

`cwb-lemmatize-smor` applies SMOR lemmatization to a [CWB](http://cwb.sourceforge.net/)-indexed corpus, which must include part-of-speech annotation. It can optionally adjust the lemmatization to TIGER conventions or to the EmpiriST tagset and conventions.

The prerequisites listed below must be installed.  Then run `perl cwb-lemmatize-smor -h` for a brief usage summary.

- [IMS Corpus Workbench](http://cwb.sourceforge.net/developers.php#svn), version 3.4.19 or newer
- CWB/Perl interface (latest version from [SVN](http://cwb.sourceforge.net/developers.php#svn)); packages `CWB` and `CWB-CL` are required
- [SMOR](https://www.cis.uni-muenchen.de/~schmid/tools/SMOR/); the command-line utility `smor-lemmatizer` must be in the standard search path

`cwb-lemmatize-smor` is made available under the same terms as Perl itself, in particular the [Artistic Licence](https://www.perlfoundation.org/artistic-license-10.html).
