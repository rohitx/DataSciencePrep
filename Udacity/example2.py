import csv
# We will test the actual data on smaller snippet of data

# create file input object f_in to work with example.csv file
f_in= open('turnstile_110528.txt', 'r')
# create file output object f_out to write to the new 'out_data.csv'
f_out = open('updated_turnstile_110528.txt', 'w')

# create csv readers and writers based on our file object
reader_in = csv.reader(f_in, delimiter=',')
writer_out = csv.writer(f_out, delimiter=',')

# We see that the output is in terms of columns rather than rows
for line in reader_in:
    header1 = line[0]
    header2 = line[1]
    header3 = line[2]
    for k in range(3, len(line)-1, 5):
        writer_out.writerow([header1, header2, header3] + [line[i].strip() for i in range(k, k+5)])

f_in.close()
f_out.close()
