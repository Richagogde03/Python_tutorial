import csv

# reading from csv file using reader()
# it will give result in form of list
# with open("data.csv", 'r', newline='') as csvfile:
#     reader = csv.reader(csvfile)
#     for row in reader:
#         print(row)


# reading from csv file using DictReader()
# it will give result in the form of dictionary
# with open("data.csv", 'r') as csvfile2:
#     reader2 = csv.DictReader(csvfile2)
#     for row in reader2:
#         print(row)


# writing from csv file using .writer()
# if we use .writerow() it will print in single line
data_to_write = [
    ['Name', 'Age', 'City'],
    ['John', 23, 'Indore'],
    ['Bob', 25, 'Ujjain']
]

with open('data.csv', 'w', newline='') as csvfile3:
    writer1 = csv.writer(csvfile3)
    writer1.writerow(data_to_write)


# using append mode
# if we use writerows() it will print in differnt row
# with open('data2.csv', 'a', newline='') as csvfile4:
#     writer2 = csv.writer(csvfile4)
#     writer2.writerows(data_to_write)
