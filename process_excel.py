'''
用于批量处理Excel文件，从而批量生成素材图片
'''
import pandas as pd
from generate_template import *
import os
from PIL import Image

if __name__ == '__main__':
	# data = pd.read_excel('template.xlsx')
	data = pd.read_excel('原始素材/temp.xlsx')
	pic_idx = 0
	for info in data.values:
		# first_text_content, first_text_font, first_text_type, \
		# second_text_content, second_text_font, second_text_type, \
		# circle_pic_path, output_path, \
		# third_text_content, fourth_text_content, \
		# fifth_text_content, sixth_text_content, \
		# seventh_text_content, eighth_text_content, year = info

		# first_text_content = str(data['Name'][pic_idx])
		first_text_content = str(data['内容'][pic_idx])
		first_text_type, second_text_type = 'nan', 'nan'
		# second_text_content = str(data['birth'][pic_idx]) + ' - ' + str(data['die'][pic_idx])
		second_text_content = 'nan'
		# circle_pic_path = str(data['小圆圈路径'][pic_idx])
		circle_pic_path = 'nan'
		output_path = '生成素材/ID' + str(data['id'][pic_idx]) + '_Type' + str(data['type'][pic_idx]) + '_Year' + str(data['year'][pic_idx]) + '.png'
		third_text_content, fourth_text_content, fifth_text_content, \
		sixth_text_content, seventh_text_content, eighth_text_content = \
		'nan', 'nan', 'nan', 'nan', 'nan', 'nan'

		img_path = "blue_background.png"

		# 第一行字体
		ttf_path = "fonts/youyuan.TTF"
		first_text_font = 32 # 70

		image = Image.open(img_path)

		# if len(first_text_content) >= 7:
		# 	first_text_font = 50
		last_height = add_text(image, ttf_path, str(first_text_content), 
			first_text_font, 300) # 200

		# 第二行字体
		ttf_path = "fonts/小米兰亭.ttf"
		second_text_font = 50
		if str(second_text_content) != 'nan':
			last_height = add_text(image, ttf_path, second_text_content, 
				second_text_font, max(360, last_height + 10))
		
		# 有小图片就生成小图片
		print(output_path)
		if str(circle_pic_path) != 'nan':
			# temp = os.listdir('原始素材/' + (circle_pic_path))[0]
			# circle_pic_path = circle_pic_path + '/' + temp
			circle_pic_path = '原始素材/' + circle_pic_path
			image = add_pic(image, circle_pic_path, output_path, 'steelblue')
		
		# 有三四五六七八行内容就生成对应行的内容
		if str(third_text_content) != 'nan':
			last_height = add_text(image, ttf_path, str(third_text_content), 
				second_text_font, max(480, last_height + 10))
		if str(fourth_text_content) != 'nan':
			last_height = add_text(image, ttf_path, str(fourth_text_content), 
				second_text_font, max(600, last_height + 10))
		if str(fifth_text_content) != 'nan':
			last_height = add_text(image, ttf_path, str(fifth_text_content), 
				second_text_font,  max(720, last_height + 10))
		if str(sixth_text_content) != 'nan':
			last_height = add_text(image, ttf_path, str(sixth_text_content), 
				second_text_font, max(840, last_height + 10))
		if str(seventh_text_content) != 'nan':
			last_height = add_text(image, ttf_path, str(seventh_text_content), 
				second_text_font, max(960, last_height + 10))
		if str(eighth_text_content) != 'nan':
			last_height = add_text(image, ttf_path, str(eighth_text_content), 
				second_text_font, max(1080, last_height + 10))
		# if str(nine) != 'nan':
		# 	last_height = add_text(image, ttf_path, str(nine), 
		# 		second_text_font, max(1180, last_height + 10))
		# if str(ten) != 'nan':
		# 	last_height = add_text(image, ttf_path, str(ten), 
		# 		second_text_font, max(1280, last_height + 10))

		image.save(output_path)

		pic_idx += 1