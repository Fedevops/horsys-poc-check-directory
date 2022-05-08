## Import libraries
import os, glob, datetime, shutil
from datetime import datetime, date

# Definition of directory
root = r'C:/Users/ferna/Desktop/horsys/horsys-poc-check-directory/subdirectory'
os.chdir(root)
print(f'Analising directory....:{root}')
print('='*60)


# Definition of execution date
today = datetime.now()

# Capture only date in string format
today = str(today)[:10] 

# Conference Routine:
# Use of date for create custom directories
conferred = 'conf_' +today # A new directory for each day

# Analising of content of original directory
types = '*.txt'
files = glob.glob(types) # Search file in current directory

print("="*60)
print('Content of directory:')
for file in files:
    print(f'arquivo:{file}')

print("="*60)

# Create a new directory (daily) for conference
# Verify if directory already exists
if os.path.exists(conferred):
    print('Directory of conference already exists!')
else:
    print('Directory not found, creating...')
    os.mkdir(conferred) # Create a new directory

print("="*60)

"""
# Copy files
For each file in directory:
    - Copy the file with a new name;
    - Insert a new line, for conference confirmated

"""
for k in range(0, len(files)):
    # New name => Original name + conf + current date
    newName = files[k][:-4]+'_conf_'+today+'.txt'
    shutil.copy(files[k], f'{conferred}\{newName}')

    # Adding a new line in file content
    with open(f'{conferred}\{newName}', 'a') as file:
        file.write(f'\nConferency in: {today}')

print("Analising sucessfully!")
print("="*60)

