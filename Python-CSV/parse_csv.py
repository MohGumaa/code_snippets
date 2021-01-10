import csv

with open('names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open('new_names.csv', 'w') as new_file:
        fieldnames = ['first_name', 'last_name']

        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')

        csv_writer.writeheader()

        for line in csv_reader:
            # del line['email']
            # We can create dic with key  f, l name and pass it
            my_dic = {'first_name': line.get('first_name'), 'last_name': line.get('last_name')}
            csv_writer.writerow(my_dic)
