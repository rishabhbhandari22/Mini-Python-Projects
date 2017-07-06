import dropbox
import os
import webbrowser

app_key = "<Your Key>"
app_secret = "<Your Key>"
access_token="<Your Key>"


client = dropbox.client.DropboxClient(access_token)
print 'linked account: ', client.account_info()
file_list = os.listdir(".")
count = 0
for file in file_list:
    fileName, fileExtension = os.path.splitext(file)
    if fileExtension!='.py':
        count+=1
        f = open(file, 'rb')
        response = client.put_file('/Uploaded-Files/'+ fileName + fileExtension, f)
        print "Uploaded File "+ str(count)
