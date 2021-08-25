import os

def renamer():
    i = 0 # initiate/iterate over files or lists
    path = "C:\\Users\\HOME\\OneDrive\\Documents\\My Web Sites"
    for filename in os.listdir(path):
        names = f"website {i}.html"
        src = path + filename
        dest = path + names
        
        os.rename(src,dest)
        i = i + 1
    
if __name__ == "__main__":
    renamer()

# rename 300 files/images/songs/videos/docs using goodRenamer