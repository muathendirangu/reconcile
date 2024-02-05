# reconcile
a cli a tool that reads in two CSV files (termed "source" and "target"), reconciles the records, and produces a report detailing the differences between the two.

**Reconciliation Report Generation**

This Python script allows you to generate a reconciliation report in CSV format by comparing two CSV files (source and target). The report includes information about records missing in the target, missing in the source, and discrepancies of data in records.

### Prerequisites

Make sure you have Python3 installed on your machine. You can download it from [Python's official website](https://www.python.org/downloads/).

### Usage

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/muathendirangu/reconcile.git
   cd reconcile
   ```

3. **Run the Program:**

   Execute the script with the appropriate command-line arguments:

   ```bash
   python reconciliation_script.py -s source.csv -t target.csv -o output_report.csv
   ```

   - `-s` or `--source`: Path to the source CSV file.
   - `-t` or `--target`: Path to the target CSV file.
   - `-o` or `--output`: Path to the output reconciliation report CSV file.


### Output

After running the script, you will see the reconciliation report generated in CSV format at the specified output path. Additionally, the script will print information about records missing in the source and target, as well as the number of discrepancies found.

### Notes

- Ensure that the source and target CSV files have the same structure, including the field names.
- Make sure to provide valid file paths for the source, target, and output files.
- Adjust the number of processes and chunk size based on your system's capabilities for optimal performance.
