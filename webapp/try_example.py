try:
    with open('myfile.txt') as fh:
        print(file_data)
except FileNotFoundErrod:
    print('The data file is missing.')
except PermissionError:
    print('This is not allowed.')
except Exception as err:
    print('Some other error occured:', str(err))