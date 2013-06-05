import fnmatch
import os, sys
import codecs
import re


class Convert:
    sourceEncoding = "ASCII"
    targetEncoding = "utf-8"
    includes = ['*.java', '*.xml'] # for files only


    def __init__(self):
        self.includes = r'|'.join([fnmatch.translate(x) for x in self.includes])
        pass

    def begin(self,dir):
        for (path, dirs, files) in os.walk(os.path.abspath(dir)):
            files = [os.path.join(path, f) for f in files]
            files = [f for f in files if re.match(self.includes, f)]

            for file in files:
                BLOCKSIZE = 1048576 # or some other, desired size in bytes
                with codecs.open(file, "r", self.sourceEncoding) as sourceFile:
                    with codecs.open(file, "w", self.targetEncoding) as targetFile:
                        while True:
                            contents = sourceFile.read(BLOCKSIZE)
                            if not contents:
                                break
                            targetFile.write(contents)
            for dir in dirs:
                self.begin(os.path.abspath(dir))


def Main():
    """
    Parse the commandline and execute the appropriate actions.
    """
    if (len(sys.argv) < 2):
        working_dir = raw_input("Enter location of dir :")
    else:
        working_dir = sys.argv[1]


    a = Convert()
    a.begin(working_dir)



if __name__ == "__main__":
    Main()