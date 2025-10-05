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
```
---
## Example
```bash
example=DNAFile(r"C:\Users\QBS-OM\OneDrive\Desktop\my github projects\dna analyzer\gene.fasta", name="gene_analysis_example")
example.analyze()
output
🧬 Starting analysis...

✅ Analysis complete!
Total sequences: 3
Longest: 1615 bp
Shortest: 0 bp
Average length: 1074.33 bp
Median length: 1608 bp
Average GC content: 26.68%

💾 Results saved to 'C:\Users\QBS-OM\OneDrive\Desktop\my github projects\dna analyzer\gene_analysis_example.csv'
```
## Author & License
© 2025 Haneen Alrifai

This project is licensed under the MIT License.
