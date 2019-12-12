import numpy as np
arr = np.arange(10)
print(arr)

np.save('saved_array', arr) # first line is the created sheet, second is the data you want to save into it.
# new file has been created  - saved_array.npy

new_array = np.load('saved_array.npy')
print(new_array)

# Save Multiple array
array_1 = np.arange(25)
array_2 = np.arange(30)

np.savez('saved_archive.npz', x=array_1, y=array_2)

load_archive = np.load('saved_archive.npz')

print('load_archive[x] is')
print(load_archive['x'])

print('load_archive[y] is')
print(load_archive['y'])

# save as a txt file
np.savetxt('notepadfile.txt', array_1, delimiter=',')

# load the text file
load_txt_file = np.loadtxt('notepadfile.txt', delimiter=',')
print('load_txt_file is')
print(load_txt_file)   # note-file converts integer to float number 0. 1.


