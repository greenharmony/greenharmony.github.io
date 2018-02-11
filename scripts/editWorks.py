#!/bin/python

import os
import sys

work_img_path = '../images/works'
template_html = open('../work_template.html', 'r')
index_html = open('../index_template.html', 'r')

fl = template_html.readlines()
template_html.close()

img_file_1 = fl[:88]
img_file_3 = fl[88:]

indx = index_html.readlines()
index_html.close()

indx_file_1 = indx[:101]
indx_file_3 = indx[101:]

img_code = '''
                                        <div class="col-md-12">
                                                <figure><img src="../images/{}" alt="Green Harmony" class="img-responsive"></figure>
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
	index_html.write(indx_code.format(fold+'.html', img, len(os.listdir(work_img_path+'/'+fold))))

index_html.writelines(indx_file_3)
index_html.close()