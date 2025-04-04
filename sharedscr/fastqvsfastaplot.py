#!/usr/bin/env python3

def parse_fastq(fastq_file):
    """
    Parse a FASTQ file and extract sequence identifiers and sequences.
    
    Args:
        fastq_file (str): Path to the FASTQ file
        
    Returns:
        dict: Dictionary with sequence identifiers as keys and sequence lengths as values
    """
    fastq_data = {}
    with open(fastq_file, 'r') as f:
        while True:
            # Read the four lines of a FASTQ entry
            header = f.readline().strip()
            if not header:
                break  # End of file
                
            seq = f.readline().strip()
            separator = f.readline().strip()  # The '+' line
            quality = f.readline().strip()
            
            if header.startswith('@'):
                # Extract the sequence identifier (everything before the first space)
                seq_id = header[1:].split(' ')[0]
                fastq_data[seq_id] = len(seq)
    
    return fastq_data

def parse_fasta(fasta_file):
    """
    Parse a FASTA file and extract sequence identifiers and sequences.
    
    Args:
        fasta_file (str): Path to the FASTA file
        
    Returns:
        dict: Dictionary with sequence identifiers as keys and sequence lengths as values
    """
    fasta_data = {}
    current_id = None
    current_seq = []
    
    with open(fasta_file, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
                
            if line.startswith('>'):
                # If we have a previous sequence, save it
                if current_id:
                    fasta_data[current_id] = len(''.join(current_seq))
                
                # Start a new sequence
                current_id = line[1:]  # Remove the '>'
                current_seq = []
            else:
                # Add this line to the current sequence
                current_seq.append(line)
        
        # Don't forget to save the last sequence
        if current_id:
            fasta_data[current_id] = len(''.join(current_seq))
    
    return fasta_data

def compare_sequences(fastq_file, fasta_file):
    """
    Compare sequence identifiers between FASTQ and FASTA files and generate a report.
    
    Args:
        fastq_file (str): Path to the FASTQ file
        fasta_file (str): Path to the FASTA file
        
    Returns:
        list: List of tuples containing (seq_id, fastq_length, in_fasta, fasta_length)
    """
    fastq_data = parse_fastq(fastq_file)
    fasta_data = parse_fasta(fasta_file)
    
    results = []
    
    for seq_id, fastq_length in fastq_data.items():
        if seq_id in fasta_data:
            in_fasta = "yes"
            fasta_length = fasta_data[seq_id]
        else:
            in_fasta = "no"
            fasta_length = "na"
        
        results.append((seq_id, fastq_length, in_fasta, fasta_length))
    
    return results

def plot_length_histograms(results, fastq_file):
    """
    Plot histograms of sequence lengths for FASTQ and FASTA files.
    
    Args:
        results (list): List of tuples containing (seq_id, fastq_length, in_fasta, fasta_length)
    """
    try:
        import matplotlib.pyplot as plt
        import numpy as np
        
        # Extract lengths
        fastq_lengths = [length for _, length, _, _ in results]
        
        # Extract FASTA lengths (only for sequences that are in FASTA with "yes")
        fasta_lengths = []
        matching_count = 0
        
        for _, _, in_fasta, fasta_length in results:
            if in_fasta == "yes":
                matching_count += 1
                fasta_lengths.append(fasta_length)
        
        # Create figure with two subplots
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)
        
        # Determine common bins for both histograms
        all_lengths = fastq_lengths.copy()
        if fasta_lengths:
            all_lengths.extend(fasta_lengths)
        min_length = min(all_lengths) if all_lengths else 0
        max_length = max(all_lengths) if all_lengths else 100
        bins = np.linspace(min_length, max_length, 30)
        
        # Plot FASTQ histogram
        ax1.hist(fastq_lengths, bins=bins, alpha=0.7, color='blue')
        ax1.set_title('FASTQ Sequence Lengths')
        ax1.set_ylabel('Frequency')
        ax1.grid(alpha=0.3)
        ax1.text(0.95, 0.95, f'Total: {len(fastq_lengths)} reads', 
                 transform=ax1.transAxes, ha='right', va='top',
                 bbox=dict(boxstyle='round', facecolor='white', alpha=0.7))
        
        # Plot FASTA histogram (only if there are matching sequences)
        if fasta_lengths:
            ax2.hist(fasta_lengths, bins=bins, alpha=0.7, color='green')
            ax2.set_title('FASTA Sequence Lengths (Matching Sequences Only)')
            ax2.set_xlabel('Length')
            ax2.set_ylabel('Frequency')
            ax2.grid(alpha=0.3)
            ax2.text(0.95, 0.95, f'Total: {matching_count} reads', 
                     transform=ax2.transAxes, ha='right', va='top',
                     bbox=dict(boxstyle='round', facecolor='white', alpha=0.7))
        else:
            ax2.text(0.5, 0.5, 'No matching sequences found in FASTA file', 
                     transform=ax2.transAxes, ha='center', va='center')
            ax2.set_xlabel('Length')
        
        # Ensure y-axes have the same scale
        y_max = max(ax1.get_ylim()[1], ax2.get_ylim()[1])
        ax1.set_ylim(0, y_max)
        ax2.set_ylim(0, y_max)
        
        # Adjust layout and save
        import os
        fastq_basename = os.path.basename(fastq_file)
        plot_filename = f"{fastq_basename}_histograms.png"
        plt.tight_layout()
        plt.savefig(plot_filename)
        print(f"Histogram plot saved as '{plot_filename}'")
        
        # Show plot
        plt.show()
        
    except ImportError:
        print("Warning: matplotlib not installed. Cannot generate histogram.")

def main():
    import argparse
    
    # Set up command line argument parsing
    parser = argparse.ArgumentParser(description='Compare sequence identifiers between FASTQ and FASTA files.')
    parser.add_argument('fastq_file', help='Path to the FASTQ file')
    parser.add_argument('fasta_file', help='Path to the FASTA file')
    parser.add_argument('--no-plot', action='store_true', help='Disable histogram plotting')
    parser.add_argument('--output', '-o', help='Output CSV file path (optional)')
    
    # Parse arguments
    args = parser.parse_args()
    
    # Run the comparison
    results = compare_sequences(args.fastq_file, args.fasta_file)
    
    # Create output
    output_lines = ["seqID,lenFASTQ,inFASTA,lenFASTA"]
    for seq_id, fastq_length, in_fasta, fasta_length in results:
        output_lines.append(f"{seq_id},{fastq_length},{in_fasta},{fasta_length}")
    
    # Write to file if specified, otherwise print to stdout
    if args.output:
        with open(args.output, 'w') as f:
            for line in output_lines:
                f.write(line + '\n')
        print(f"Results written to {args.output}")
    else:
        for line in output_lines:
            print(line)
    
    # Generate histograms unless disabled
    if not args.no_plot:
        plot_length_histograms(results, args.fastq_file)

if __name__ == "__main__":
    main()