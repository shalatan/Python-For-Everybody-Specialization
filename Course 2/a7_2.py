"""
Write a program that prompts for a file name, then opens that file and reads
through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines
and compute the average of those values and produce an output as shown below.
Do not use the sum() function or a variable named sum in your solution.
You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
"""

fname = input("Enter file name: ")
fh = open(fname)
total = 0.0
count = 0.0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        n = line.find(":")
        new = line[n+1:]
        total = total + float(new)
        count = count+1
        avg = total/count
print("Average spam confidence:",avg)
