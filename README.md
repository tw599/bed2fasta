# About
Convert bed files or genomic range coordinates to DNA sequence in FASTA format

```
chr1 3267236 3267637 Peak1  +
chr2 3277942 3628373 Peak2  +
chr3 5784393 5782838 Peak3  +
chr4 17847283 17248934 Peak4  +
chr5 9213894 9438234 Peak5  +
```

Input bed file must have 6 columns:

```
Column 1: chromosome
Column 2: Start site
Column 3: End site
Column 4: Peak ID/Name
Column 5: Blank
Column 6: Strand (+/-)
```

# Usage

```
python bed2fasta.py 
```
