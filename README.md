![logo](https://user-images.githubusercontent.com/35373553/72666208-63d7b900-3a53-11ea-8b5b-c4acffe078cc.png)

----
Download image data from ImageNet with python.

# Usage
### How to use example
```
python example.py <WordnetID> -v
```
Start download images.

### How to use downloader module
Sample code.
```py
import downloader
import os
api = downloader.ImageNet(root=os.getcwd())
api.download(wnid, verbose=True)
```

Downloader makes directory.
```
root/  
　├ img/  
　├ list/  
```
If you substitute 'n02112826' for wnid,
Downloader changes directory and save images below.  
```
root/  
　├ img/  
　│　└ n02112826/
　│　      └ n02112826_20084.jpg
　│　      └ n02112826_20105.jpg
　│　      └ ....
　├ list/  
　│　└ n02112826.txt
```


# WordetID
Check WordnetID.   
[ImageNet](http://image-net.org/explore)
