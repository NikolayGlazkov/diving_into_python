"""('C:/Users/User/Documents/', 'example', '.txt')"""
def get_file_info(file_path):
    ferst = f'{"/".join(file_path.split("/")[:-1],)}/'
    two = (file_path.split("/")[-1]).split(".")[0]
    free = f'.{(file_path.split("/")[-1]).split(".")[1]}'
    my_typle = (ferst,two,free)
    return my_typle

file_path = "C:/Users/User/Documents/example.txt"
print(get_file_info(file_path))