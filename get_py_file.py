import csv, shutil

csv_file = open("./file_name.csv", "r", encoding="ms932", errors="", newline="" )
py_names = open("./file_names.csv", "w", encoding="ms932", errors="", newline="")
f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
for i in f:
    print(i[0])
    text = i[0].rstrip("src") + "py"
    if i[0] != "file_name":
        # shutil.copy("./src/" + i[0], "./python_files/" + text)
        py_names.write(text + "\n")
csv_file.close()