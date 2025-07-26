#importing required modules
import os,requests,bs4

#url of comic page
url='http://xkcd.com'

#making folder for comic page
os.makedirs('xkcd',exist_ok=True)

while not url.endswith("#"):
    #downloading page usiong request moduke
    print("Dowanloading Page {url}...")
    res=requests.get(url)
    res.raise_for_status()                                              #to check for errors

    #parsing html to clean it up and return a cleaned up format
    soup=bs4.BeautifulSoup(res.text,'html.parser')

    #selecting the image on the page
    comic_item=soup.select("#comic img")

    #if no image exists
    if comic_item==[]:
        print("Could not find image")
    #if image exists
    else:
        comicUrl='https:' + comic_item[0].get('src')


        #downlaoding image
        print("Dowloading image {comicUrl}")
        res=requests.get(comicUrl)
        res.raise_for_status()                                          #to check for errors

        #saving image
        imageFile=open(os.path.join('xkcd',os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        #closing files is a good practice to free up storage systems
        imageFile.close()

    #previous link accessed to get image of eah page
    prevlink=soup.select('a[rel="prev"]')[0]
    url='https://xkcd.com' + prevlink.get('href')

print('Done')