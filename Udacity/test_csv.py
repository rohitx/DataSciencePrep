import csv

# create file input object f_in to work with example.csv file
f_in = open('example.csv', 'r')
# create file output object f_out to write to the new 'out_data.csv'
f_out = open('out.csv', 'w')

# create csv readers and writers based on our file object
reader_in = csv.reader(f_in, delimiter=',')
#reader_in = csv.reader(f_in, delimiter=',')
#writer_out = csv.reader(f_out, delimiter=',')
writer_out = csv.writer(f_out, delimiter=',')

# skip the first line because it contains headers
reader_in.next()

# We see that the output is in terms of columns rather than rows
for line in reader_in:
    type_chocolate = line[0]
    line_1 = [type_chocolate, line[1], line[2], line[3], line[4]]
    writer_out.writerow(line_1)
    writer_out.writerow(line_2)