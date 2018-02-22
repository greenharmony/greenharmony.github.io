#!/bin/python

import os
import sys

#Removing all work html files
#keeping CNAME, index_template.html, work_template.html as it is.
important = ['CNAME', 'index_template.html', 'work_template.html']
working_dir = os.path.abspath('../')

for content in os.listdir(working_dir):
	file_name = os.path.join(working_dir, content)
	if os.path.isfile(file_name) and content not in important:
		os.remove(file_name)


work_img_path = '../images/works'
marker = "<!--LastLineMarker-->\n"


work_html = open('../work_template.html', 'r')
lineListWork = work_html.readlines()

index_of_marker = lineListWork.index(marker)
flag = index_of_marker + 1

img_file_1 = lineListWork[:flag]
img_file_3 = lineListWork[flag:]
work_html.close()


index_html = open('../index_template.html', 'r')
lineListIndex = index_html.readlines()

index_of_marker = lineListIndex.index(marker)
flag = index_of_marker + 1

indx_file_1 = lineListIndex[:flag]
indx_file_3 = lineListIndex[flag:]
index_html.close()


img_code = '''
                                        <div class="col-md-12">
                                                <figure><img src="images/works/{}" alt="Green Harmony" class="img-responsive"></figure>
                                        </div>'''

indx_code = '''
				<a class="gallery-item" href="{}">
					<img src="images/works/{}" alt="Green Harmony">
					<span class="overlay">
						<span>{} Photos</span>
					</span>
				</a>'''

index_html = open('../index.html', 'w')
index_html.writelines(indx_file_1)

for fold in sorted(os.listdir(work_img_path)):
	fl_fold_html = open('../'+fold+'.html', 'w')
	fl_fold_html.writelines(img_file_1)	
	for img in sorted(os.listdir(work_img_path+'/'+fold)):
		fl_fold_html.write(img_code.format(fold+'/'+img))

	fl_fold_html.writelines(img_file_3)
	fl_fold_html.close()
	index_html.write(indx_code.format(fold+'.html', fold+'/'+img, len(os.listdir(work_img_path+'/'+fold))))

index_html.writelines(indx_file_3)
index_html.close()