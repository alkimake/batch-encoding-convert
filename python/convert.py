import fnmatch
import os, sys
import codecs
import re
import shutil
import fastchardet


class Convert:
    includes = ['*.java', '*.xml'] # for files only


    def __init__(self):
        self.includes = r'|'.join([fnmatch.translate(x) for x in self.includes])
        pass

    def convert_to_utf8(self, filename):
        # try to open the file and exit if some IOError occurs
        """

        :param filename:
        """
        try:
            f = open(filename, 'r').read()
            print fastchardet.detect(f)
        except Exception:
            sys.exit(1)


        try:
            if fastchardet.detect(f)['encoding']:
                data = f.decode(fastchardet.detect(f)['encoding'])
                # now get the absolute path of our filename and append .bak
                # to the end of it (for our backup file)
                fpath = os.path.abspath(filename)
                newfilename = fpath + '.bak'
                # and make our backup file with shutil
                shutil.copy(filename, newfilename)

                # and at last convert it to utf-8
                f = open(filename, 'w')
                try:
                    f.write(data.encode('utf-8'))
                except Exception, e:
                    print e
                finally:
                    f.close()
            else:
                print "Skipping"
        except Exception, e:
            print e


    def begin(self,dir):
        for (path, dirs, files) in os.walk(os.path.abspath(dir)):
            files = [os.path.join(path, f) for f in files]
            files = [f for f in files if re.match(self.includes, f)]

            for file in files:
                print file
                self.convert_to_utf8(file)
            for dir in dirs:
                self.begin(os.path.abspath(dir))

        print "Processing Done..."


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