<<<<<<< HEAD
from Bio import SeqIO
import statistics
import time
import csv
import os
class DNAFile:
    """
    A class for analyzing DNA sequences from a FASTA file.
    It calculates per-sequence GC content and summary statistics.
    """
    def __init__(self, filepath, name=None):
        self.filepath = filepath
        self.name = name  # store user-provided name
        self.sequences = [str(record.seq).upper() for record in SeqIO.parse(filepath, "fasta")]

    def count_sequences(self):
        return len(self.sequences)

    def lengths(self):
        return [len(seq) for seq in self.sequences]

    def gc_content(self, seq):
        if not seq:
            return 0
        gc = seq.count("G") + seq.count("C")
        return round((gc / len(seq)) * 100, 2)
    def average_gc_content(self):
        if not self.sequences:
            return 0
        return round(statistics.mean(self.gc_content(seq) for seq in self.sequences), 2)

    def analyze(self, report_every=1000):
        print("🧬 Starting analysis...")
        start = time.time()
        lengths = []
        gc_contents = []
        lengths = self.lengths()
        total = len(lengths)
        for i, seq in enumerate(self.sequences):
            if (i + 1) % report_every == 0:
                print(f"Processed {i + 1}/{total} sequences...")
        total = len(lengths)
        longest = max(lengths) if lengths else 0
        shortest = min(lengths) if lengths else 0
        avg_len = statistics.mean(lengths) if lengths else 0
        median_len = statistics.median(lengths) if lengths else 0
        avg_gc = statistics.mean(gc_contents) if gc_contents else 0
        elapsed = time.time() - start
        elapsed = time.time() - start
        print("\n✅ Analysis complete!")
        print(f"Total sequences: {total}")
        print(f"Longest: {max(lengths)} bp")
        print(f"Shortest: {min(lengths)} bp")
        print(f"Average length: {statistics.mean(lengths):.2f} bp")
        print(f"Median length: {statistics.median(lengths)} bp")
        print(f"Average GC content: {self.average_gc_content()}%")
        print(f"Time elapsed: {elapsed:.2f} seconds")
        # Save results for later
        self.results = [
            ["Total Sequences", total],
            ["Longest", longest],
            ["Shortest", shortest],
            ["Average Length", avg_len],
            ["Median Length", median_len],
            ["Average GC Content", avg_gc],
            ["Time Elapsed (seconds)", elapsed]
        ]
        # 🔽 Call the CSV saving function here
        self.save_to_csv()
    _file_counter = 0  # class variable to count how many results we saved    
    def save_to_csv(self, output_file=None):
        # 🔹 If no file name given, build one automatically based on the FASTA name
        if output_file is None:
            # Increment the class counter
             DNAFile._file_counter += 1
            # Use user's name if provided, otherwise make a generic name
             if self.name:
                 base_name = self.name.replace(" ", "_")  # clean spaces
             else:
                 base_name = f"result_{DNAFile._file_counter}"

             output_file = f"{base_name}.csv"
        # Save in the same folder as the FASTA file
        folder = os.path.dirname(self.filepath)
        full_path = os.path.join(folder, output_file)  
            
        with open(output_file, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Sequence_ID", "Length", "GC_Content(%)"])
            for record in SeqIO.parse(self.filepath, "fasta"):
                seq = str(record.seq).upper()
                writer.writerow([record.id, len(seq), self.gc_content(seq)])    
=======
from Bio import SeqIO
import statistics
import csv
import os
class DNAFile:
    """
    A class for analyzing DNA sequences from a FASTA file.
    It calculates per-sequence GC content and summary statistics.
    """
    def __init__(self, filepath, name=None):
        self.filepath = filepath
        self.name = name  # store user-provided name
        self.sequences = [str(record.seq).upper() for record in SeqIO.parse(filepath, "fasta")]

    def count_sequences(self):
        return len(self.sequences)

    def lengths(self):
        return [len(seq) for seq in self.sequences]

    def gc_content(self, seq):
        if not seq:
            return 0
        gc = seq.count("G") + seq.count("C")
        return round((gc / len(seq)) * 100, 2)
    def average_gc_content(self):
        if not self.sequences:
            return 0
        return round(statistics.mean(self.gc_content(seq) for seq in self.sequences), 2)

    def analyze(self):
        print("🧬 Starting analysis...")
       
        lengths = []
        gc_contents = []
        lengths = self.lengths()
        total = len(lengths)
        
        total = len(lengths)
        longest = max(lengths) if lengths else 0
        shortest = min(lengths) if lengths else 0
        avg_len = statistics.mean(lengths) if lengths else 0
        median_len = statistics.median(lengths) if lengths else 0
        avg_gc = statistics.mean(gc_contents) if gc_contents else 0
        
        print("\n✅ Analysis complete!")
        print(f"Total sequences: {total}")
        print(f"Longest: {max(lengths)} bp")
        print(f"Shortest: {min(lengths)} bp")
        print(f"Average length: {statistics.mean(lengths):.2f} bp")
        print(f"Median length: {statistics.median(lengths)} bp")
        print(f"Average GC content: {self.average_gc_content()}%")
        
        # Save results for later
        self.results = [
            ["Total Sequences", total],
            ["Longest", longest],
            ["Shortest", shortest],
            ["Average Length", avg_len],
            ["Median Length", median_len],
            ["Average GC Content", avg_gc],
            
        ]
        # 🔽 Call the CSV saving function here
        self.save_to_csv()
    _file_counter = 0  # class variable to count how many results we saved    
    def save_to_csv(self, output_file=None):
        # 🔹 If no file name given, build one automatically based on the FASTA name
        if output_file is None:
            # Increment the class counter
             DNAFile._file_counter += 1
            # Use user's name if provided, otherwise make a generic name
             if self.name:
                 base_name = self.name.replace(" ", "_")  # clean spaces
             else:
                 base_name = f"result_{DNAFile._file_counter}"

             output_file = f"{base_name}.csv"
        # Save in the same folder as the FASTA file
        folder = os.path.dirname(self.filepath)
        full_path = os.path.join(folder, output_file)  
            
        with open(output_file, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Sequence_ID", "Length", "GC_Content(%)"])
            for record in SeqIO.parse(self.filepath, "fasta"):
                seq = str(record.seq).upper()
                writer.writerow([record.id, len(seq), self.gc_content(seq)])    
>>>>>>> 5f73200 (Cleaned code: removed time and progress tracking)
        print(f"\n💾 Results saved to '{os.path.abspath(full_path)}'")