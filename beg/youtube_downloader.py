# importing the module  
from pytube import YouTube  
  
# where to save  
SAVE_PATH = "/home/pavan/Videos/" #to_do  
  
# link of the video to be downloaded  
link=str(input("Enter Link here"))
  
try:  
    # object creation using YouTube 
    # which was imported in the beginning  
    yt = YouTube(link)  
    yt.streams.get_highest_resolution().download(SAVE_PATH)
except:  
    print("Error") #to handle exception  
print('Task Completed!')  