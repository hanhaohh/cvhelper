import os 
def save(data, filename, dir=None):
    try:
        with open(filename, 'a') as f:
            for i in data:
                f.write(i+"\n")
    except FileNotFoundError as e:
        dir = os.path.dirname(filename)
        os.makedirs(dir)
        with open(filename, 'wb') as f:
            f.write(data)
    f.close()
    return filename