# AWS-LB-Search
Small tool I wrote to go through a folder of gzipped AWS Load Balancer logs and search for a status code or a string.

Required: Python 3, tkinter (optional but makes your life a lot easier), all the rest (gzip, zlib and os) should come with your python installation.

The workflow is commented in unzip.py, but the gist of it is:
1. Run py unzip.py
2. select the folder where the files are
3. Input either "status" or "string" and then a corresponding status code or string you're looking for

It will output your result to a txt file and tell you what the file name is.

if you need to tweak the output, read the comments in the file, it is fairly straightforward to understand.
