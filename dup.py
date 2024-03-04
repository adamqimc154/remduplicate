def remove_duplicates(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    unique_lines = list(set(lines)) 

    with open(output_file, 'w') as file:
        file.writelines(unique_lines)


input_file = 'input.txt'


output_file = 'output.txt'

remove_duplicates(input_file, output_file)

print("Duplicate file has been deleted and saved on output.txt.")
