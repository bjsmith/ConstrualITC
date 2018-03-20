import re
script_to_fix_filepath='/Users/benjaminsmith/GDrive/neural-construal-level/code/SmithAdaptConstrualITCmTurk/html/index.html'
find_replace_location='/Users/benjaminsmith/GDrive/neural-construal-level/code/SmithAdaptConstrualITC/replacer/'
script_text=open(script_to_fix_filepath).read()

find_replace_list=[['find'+str.zfill(str(i),2)+'.txt','replace'+str.zfill(str(i),2)+'.txt'] for i in range(1,14+1) ]

print 'got '+ str(find_replace_list.__len__()) + ' pairs to replace'
for frpair in find_replace_list:
    find_text=open(find_replace_location + frpair[0]).read()
    find_text_re=re.escape(" ".join(find_text.split())).replace('\\ ','\s+')
    replace_text=open(find_replace_location + frpair[1]).read()
    textLocation=re.search(find_text_re,script_text)
    print '----'+frpair[0]+'\n'+find_text + "\nat " + str(textLocation) + "->\n"+replace_text +'\n----\n'

    script_text=re.sub(find_text_re,replace_text,script_text)

f = open(script_to_fix_filepath,'w')
f.write(script_text)
f.close()

