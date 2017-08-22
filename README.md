# Subgraph Frequencies
subgraph-frequencies v1.0

Code to calculate the frequencies of all subgraphs involving three nodes as described in http://ieeexplore.ieee.org/document/7839612/

## Usage

Calculate the frequencies of all subgraphs from the file input.txt:

```
python get_frequencies.py -a input.txt output.txt
```

### Options

```
Usage: python get_frequencies.py -a|-r <inputfile> [<outputfile>]
Options:
  -a             It returns the absolute frequency of all subgraphs (i.e. raw count)
  -r             It returns the relative frequency of all subgraphs.

Input:
  <inputfile>    Input text file.
  <outputfile>   Output text file. If not defined, the code will output to stdout)

```



Text sample:

```
To be or not to be that is the question

```

The respective co-occurrence network obtained from the text sample is: