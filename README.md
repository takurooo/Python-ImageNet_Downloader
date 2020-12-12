![logo](https://user-images.githubusercontent.com/35373553/72666208-63d7b900-3a53-11ea-8b5b-c4acffe078cc.png)

----
Download image data from ImageNet with python.

# Usage
### How to use example
```
usage: example.py [-h] [-root ROOT] [-limit LIMIT] [-r] [-v] wnid

Download images from ImageNet.

positional arguments:
  wnid             download wnid

optional arguments:
  -h, --help       show this help message and exit
  -root ROOT       root dir
  -limit LIMIT     max save num
  -r, --recursive  save recursive
  -v, --verbose    show process message
```

```
python example.py <WordnetID> -v -limit 5
```
Start download 5 images.

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
