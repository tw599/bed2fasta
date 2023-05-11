import argparse
from Bio import SeqIO

# Create argument parser
parser = argparse.ArgumentParser(description='Transform a 6-column genomic BED file into a FASTA file')
parser.add_argument('input_bed', metavar='input.bed', type=str, help='Path to input BED file')
parser.add_argument('output_fasta', metavar='output.fasta', type=str, help='Path to output FASTA file')
parser.add_argument('genome_fasta', metavar='genome.fasta', type=str, help='Path to genome FASTA file')
args = parser.parse_args()

# Parse genome sequences into a dictionary
genome_dict = SeqIO.to_dict(SeqIO.parse(args.genome_fasta, "fasta"))

# Read BED file and extract regions from genome dictionary
with open(args.input_bed) as f, open(args.output_fasta, 'w') as output:
    for line in f:
        chrom, start, end, name, score, strand = line.strip().split('\t')
        seq = genome_dict[chrom][int(start):int(end)].seq
        output.write(f'>{name}\n{seq}\n')
