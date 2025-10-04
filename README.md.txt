# 🧬 DNA FASTA Analyzer

A simple yet efficient **Python tool** to analyze DNA FASTA files.  
It calculates basic genome statistics such as sequence count, GC content, and sequence lengths,  
and automatically saves the results in a clean **CSV file**.

---

## 🚀 Features

- Reads one or more DNA sequences from a FASTA file  
- Calculates:
  - Total number of sequences
  - Shortest, longest, average, and median lengths
  - GC content per sequence and average GC content
- Automatically generates a CSV results file  
- Smart file naming (custom name or auto-generated)

---

## 🧰 Requirements

Install Biopython before running:
```bash
pip install biopython
Example usage
from dna_analyzer import DNAFile

example = DNAFile(r"C:\Users\QBS-OM\OneDrive\Desktop\my github projects\dna analyzer\gene.fasta", name="example")
example.analyze(report_every=1000)
Expected output:
🧬 Starting analysis...

✅ Analysis complete!
Total sequences: 1
Longest: 1608 bp
Shortest: 1608 bp
Average length: 1608.00 bp
Median length: 1608 bp
Average GC content: 40.11%
Time elapsed: 0.00 seconds

💾 Results saved to 'C:\Users\QBS-OM\OneDrive\Desktop\my github projects\dna analyzer\example.csv'
CSV Output

The CSV file contains:
| Sequence_ID | Length | GC_Content(%) |
| ----------- | ------ | ------------- |
| Sequence1   | 1608   | 40.11         |
Author & License

© 2025 Haneen Alrifai

This project is licensed under the MIT License.