'''program to get extension of a file '''

import os

extension=os.path.splitext('name.txt')
print(f"The name of the file is : {extension[0]}")
print(f"The extension of the file is : {extension[1]}")