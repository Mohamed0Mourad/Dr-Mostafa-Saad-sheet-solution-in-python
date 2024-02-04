input_string = input()
sequence_list = input_string[1:-1].replace(" ", "").split(",")
if len(input_string) == 2:
    print(0)
else:
    out = len(set(sequence_list))
    print(out)
