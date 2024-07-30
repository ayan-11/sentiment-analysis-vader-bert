def combine_files(file_names, output_file):
    with open(output_file, 'w') as outfile:
        for file_name in file_names:
            with open(file_name, 'r') as infile:
                outfile.write(infile.read())

file_names = ["StopWords_Auditor.txt", "StopWords_Currencies.txt", "StopWords_DatesandNumbers.txt", "StopWords_Generic.txt", "StopWords_GenericLong.txt", "StopWords_Geographic.txt", "StopWords_Names.txt"]

output_file = "StopWords.txt"

combine_files(file_names, output_file)
print("Files combined successfully!")
