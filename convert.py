"""
Author's Note:

This is a custom Python script used to convert copied text data from the website oryzasnp.org into a table of records containing the rice's phenotype data. The data was obtained by manually perusing the database and copy-pasting the shown values.

This script was made in part of my 3+1 Research project, to make a classifier using Indonesian rice phenotype data.

This script assumes all acquired data are in the form of a loooooooooooong vertical list, and then stores the end product in CSV format.

This script is the backend script.
The frontend script is runscriptrun.py. Run that one.

(kurisu_na, 7-10 March 2016)
"""

"""
PART 1: mkRecordList()
Convert a loooooooooooooooong vector array-shaped data into a table of records associated with a variety.

Product of Part 1: A recordlist.csv file containing the tidy table of records.
"""

def mkRecordList(data, filename_open, tcol_count, variety_separator, eof_mark):
    # Open sesame!
    # 1. Open the file containing copied data in READ mode.
    fopen = open("Files/" + filename_open, "r")
    # 2. Makes a temporary file in WRITE mode, to save the list of records.
    ftemp = open("Files/recordlist.csv", "w")

    variety_count = 0
    line_count = 0
    line = ""

    while True:
        variety_count += 1 # Increments variety count.

        while True:
            row = [] # The variable which will store each row.
            for i in range(tcol_count): # Saves each line into the row array.
                line = fopen.readline()[:-1]
                if line == "": # Ignores blank lines.
                    continue
                if line == variety_separator or line == eof_mark: # Breaks the for loop if program finds variety_separator in the line.
                    break
                row.append(str(line))
            row.insert(0, str(variety_count)) # inserts variety_count in front of the list

            # Break Sequences:
            if line == eof_mark: # Breaks the while loop if program finds eof_mark in the line. Higher priority than variety_separator.
                break

            if line == variety_separator: # Breaks the while loop if program finds variety_separator in the line.
                break

            data.append(row)
            line_count += 1

        if line == eof_mark:
            break

    # This writes row as:
    # row[0],row[1],row[2],...,row[tcol_count]
    # in the file.
    for d in data:
        ftemp.write(",".join(d))
        ftemp.write("\n")

    # Close the files to save memory.
    fopen.close()
    ftemp.close()

""" END OF PART 1 """


"""
PART 2:
Make the table headers, which contains the field names and field descriptions.

Product of Part 2: Table headers are in the file specified in the beginning of the program.
"""

def mkTableHeaders(data, filename_save, field_name_index, field_desc_index, field_names_list):
    # Make the file specified in the beginning of the program in WRITE mode, to write the table headers first.
    fsave = open("Files/" + filename_save, "w")

    # Unique field names and their respective descriptions are stored as a dictionary, utilizing dictionary's unique keys.
    fields_dict = {}

    # Stores the list of field names and descriptions from the sorted dictionary.
    fields_list = []

    # Loops through the entire data array to find field names and pairs it with its description, while listing each field name.
    for d in data:
        field_name = d[field_name_index]
        if field_desc_index == 0: # no field description
            field_desc = "-"
        else:
            field_desc = d[field_desc_index]
        fields_dict[field_name] = field_desc

    # Sorts the dictionary's keys alphabetically, and saves them as tuples like (key,value) in a normal list in fields_list.
    fields_list = sorted(fields_dict.items())

    # Writes field names in the file.
    for i in range(len(fields_list)):
        field_names_list.append(fields_list[i][0]) # Saves field names into field_names_list.
        fsave.write(fields_list[i][0])
        if i < len(fields_list)-1:
            fsave.write(",")
        else:
            fsave.write("\n")

    if field_desc_index != 0:
        # Writes field description below their respective field names, if there are field descriptions.
        for i in range(len(fields_list)):
            fsave.write(fields_list[i][1])
            if i < len(fields_list)-1:
                fsave.write(",")
            else:
                fsave.write("\n")

    # Close the file to save memory.
    fsave.close()

""" END OF PART 2 """


"""
PART 3:
Combine the records of a same variety into a single record, and put them into the table.

Product of Part 3: A complete table of varieties with their respective attributes.
"""

def mkTable(data, filename_save, field_name_index, value_index, field_names_list):
    # Open the file specified in the beginning of the program in APPEND mode, to save the final table.
    fsave = open("Files/" + filename_save, "a")

    record = [""  for f in field_names_list] # Stores each record.
    current_record_no = 1 # Initialize current record number.

    # Loop through data[].
    for d in data:
        # Check current record number. Actions differ based on this variable.
        # If it's a different record: write record[] into file first, and increment current_record_no. Needs str() because all the items in data[] are stored as string.
        if int(d[0]) != current_record_no:
            fsave.write(",".join(record))
            fsave.write("\n")
            current_record_no = int(d[0])

        # Save data into record[].
        try:
            # Check for current record's field_name in field_names_list[], and returns the field_name's index.
            i = field_names_list.index(d[field_name_index])
            # Record data if the record has value in that field!
            record[i] = d[value_index]
        except ValueError:
            # Do nothing, the values will stay blank as first initialized.
            # pass
            print("Not Found")

    # Writes last record.
    fsave.write(",".join(record))
    fsave.write("\n")

    # Close the file to save memory.
    fsave.close()

""" END OF PART 3 """

""" That's all folks! """
