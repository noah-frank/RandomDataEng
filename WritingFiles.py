# Python writing files (.txt, .json, .csv)

txt_data = "I like pizza!"

file_path = "./files/output.txt"

with open(file_path, "w") as file: # "w" = write
    file.write(txt_data)
    print(f"txt file '{file_path}' was created")

