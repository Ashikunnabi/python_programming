""" Comma Separated Value """
import csv


with open("05.information.csv", 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    for line in csv_reader:
        print(line)
        
    '''
    print("====================Only Emails=================")
    for email in csv_reader:
        print(email[2])
    '''
    
    '''
    print("====================CSV WRITING=================")
    with open("05.new.csv", 'w') as new_file:
        csv_writer = csv.writer(new_file, delimiter='\t')
        
        for new in csv_reader:
            csv_writer.writerow(new)
    '''
    
