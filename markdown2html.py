import os, markdown2, fnmatch           # dependant on python-markdown2
tmp = open("template.html","r").read()  # HTML document with {{content}} tag

def locate(pattern, root=os.curdir):
  '''Locate all files matching supplied filename pattern in and below
  supplied root directory.'''
  for path, dirs, files in os.walk(os.path.abspath(root)):
    for filename in fnmatch.filter(files, pattern):
      yield os.path.join(path, filename)

for files in locate("*.markdown"):
  print files
  try:
    markdownoutput = markdown2.markdown(open(files).read())
    output = tmp.replace("{{content}}", markdownoutput.encode('utf-8'))
    f = open(files.replace(".markdown",".html"),"w")
    f.write(output)
  except (SyntaxError):
    print files, "\tBADLY FORMED!"
