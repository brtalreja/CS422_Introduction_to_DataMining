#Using products.csv file as a dictionary to look-up values of transactions for canonical representation:
product_list = {}

with open('products.csv','r') as file:
    for row in file:
        row = row.replace('\n','').split(',')
        row = [i.strip() for i in row]
        product_list[row[0]] = row[1]

#All transaction files canonical representation:

for i in ('tr-1k','tr-5k','tr-20k','tr-75k'):
    with open(i+'-canonical.csv','w') as out_file:
        with open(i+'.csv','r') as in_file:
            for row in in_file:
                row = row.replace('\n','').split(',')
                row = [i.strip() for i in row]
                row = row[1:]
                transaction = ', '.join([product_list[i] for i in row])
                transaction += '\n'
                out_file.write(transaction)

