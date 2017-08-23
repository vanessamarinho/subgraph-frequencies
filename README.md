# Subgraph Frequencies
subgraph-frequencies v1.0

Code to calculate the frequencies of all directed subgraphs involving three nodes from textual networks as described in http://ieeexplore.ieee.org/document/7839612/

## Usage

Calculate the frequencies of all directed subgraphs from the co-occurrence network extracted from the file input.txt:

```
python get_frequencies.py -a input.txt output.csv
```

## Options

```
Usage: python get_frequencies.py -a|-r <inputfile> [<outputfile>]
Options:
  -a             It returns the absolute frequency of all subgraphs (i.e. raw count).
  -r             It returns the relative frequency of all subgraphs.

Input:
  <inputfile>    Input text file.
  <outputfile>   Output text file in a CSV format. If not defined, the code will output to stdout.

```

## Example

Given the following text sample:

```
To be or not to be that is the question

```

The respective co-occurrence network (the nodes represent the words and the directed edges connect adjacent words) obtained from the text sample is:

![Co-occurrence network](co-occurrence.png?raw=true "Co-occurrence network for the sentence 'To be or not to be that is the question'")

The output would be the following:

For -a:

For -r:

Each value in the output corresponds to the frequency of one subgraph, as presented in the mapping below:

![Mapping between frequencies and subgraphs](output.png?raw=true "Mapping between each frequency and its respective subgraph")