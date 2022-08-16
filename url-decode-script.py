
import os
import urllib.parse

todo = os.getcwd() + "/todo"
done = os.getcwd() + "/done"

for filename in os.listdir(todo):
    current_path = todo + "/" + filename
    decoded_filename = urllib.parse.unquote(filename)
    print("Current file name: ", filename)
    print("Decoded file name: ", decoded_filename)
    os.rename(current_path, os.path.join(done, decoded_filename))
