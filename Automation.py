import cv2
import dropbox
import time
import random
start_time=time.time()
def snap():
    number=random.randint(0,100)
    capture=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=capture.read()
        imgname="img"+str(number)+".png"
        cv2.imwrite(imgname,frame)
        result=False
    return imgname
    print("Snapshot taken")
    capture.release()
    cv2.destroyAllWindows()

def uploadFile(imgname):
    access_token="sl.AwCPQwyLnCXNrrFwJJHRw3r2HCY2KLvUudZ521Kfb2ruuZ9DvAEJPvvtWYo-31w7B13vumGhDpIVuaEKlbjO99XSqOYS6isUjFVPk7GXxg8gMrI5QLOJdNNJlm8qzcw2-j6P3Gc"
    file=image_counter
    file_from=file
    file_to="/newfolder1/"+(imgname)
    dbx=dropbox.Dropbox(access_token)

    with open(file_from, "rb") as f:
        dbx.files_upload(f.read(),file_to, mode=dropbox.files.WriteMode.overwrite)
        print("File uploaded")

def main():
    while(True):
        if((time.time()-start_time)>=20):
            name=snap()
            uploadFile(name)

main()