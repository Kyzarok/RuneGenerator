import os
import glob

main_path = 'kmnist/kkanji2'
for filename in os.listdir(main_path):
    filepath = main_path + '/' + filename
    for this_filepath in glob.glob(os.path.join(filepath, '*.png')):
        print(this_filepath)
        this_name = this_filepath[-20:]
        new_path = "big_data/" + this_name
        os.rename(this_filepath, new_path)
