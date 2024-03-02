from PIL import Image
import os

filepath = "bev_classification/images/train"
# Train has 0 - 69
width = 200
height = 200
max_width = 0
max_height = 0
tuple_width = ()
tuple_height = ()

width_file = ""
height_file = ""

for i in range(0,69):
    filen = filepath + "_" +str(i)
    directory = os.fsencode(filen)
    print(directory)
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        path = filen + "/" + str(filename)
        if filename.endswith(".csv"):
            continue
        for image in os.listdir(path):
            ima = os.fsdecode(image)    
            if ima.endswith(".jpg"):
    
                file = os.fsdecode(image)
                whole_path = str(path) + "/" +str(file)
                im = Image.open(str(path) + "/" +str(file))
        
            if im.size[0] < width:
                width = im.size[0]
                tuple_width = im.size
                width_file = str(whole_path)
                
            if im.size[1] < height:
                height = im.size[1]
                tuple_height = im.size
                height_file = str(whole_path)


            if im.size[1] > max_height:
                max_height = im.size[1]
            if im.size[0] > max_width:
                max_width = im.size[0]
            
            if im.size[0] < 20 or im.size[1] < 20:
                print(f"removing: {whole_path}")
                os.remove(whole_path)

print(f"Width: {width}")
print(f"Height: {height}")
print(f"width : {tuple_width}, height: {tuple_height}")
print(f"height file: {height_file}")
print(f"width file: {width_file}")
print(f"max width: {max_width}, max heigh: {max_height}")


