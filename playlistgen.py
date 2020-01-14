import os
import sys

'''
format
<media src="C:Songs\abc.mp4"/>
'''


#folder_name = os.path.basename(sys.argv[2])
if len(sys.argv)>3:
    total_count = str(sys.argv[3])
else:
    total_count = -1
pre_media_str = '\t\t\t' + '<media src=\"' + os.path.abspath(sys.argv[2]) + '\\' #'<media src=\"..\..\..\..\\' + folder_name + '\\'
post_media_str = '"/>\n'
pre_title_str = '\t\t' + '<title>'
post_title_str = '</title>\n'

with open(sys.argv[1]+'.wpl','w',encoding='utf-8') as outfile, open(os.path.join(os.path.dirname(__file__),'template.wplt'),'r') as infile:
    for lines in infile:
        if '<title>' in lines:
            outfile.write( pre_title_str + sys.argv[1] + post_title_str )
        else:
            outfile.write(lines)
            
        if r'<seq>' in lines:
            count = 0
            for filename in os.scandir(sys.argv[2]):
                count += 1
                if True or filename.is_file():
                    try:
                        print(filename.name)
                        outfile.write( pre_media_str + filename.name.replace('&','&amp;') + post_media_str )
                    except:
                        pass
                if(str(count)==-1):
                    continue
                if(str(count)==total_count):
                    break

def count_files(dir):
    return len([1 for x in list(os.scandir(dir)) if x.is_file()])
