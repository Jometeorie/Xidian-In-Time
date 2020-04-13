'''
生成对应图片的json数据，用于给前端导入进AI
'''
from collections import OrderedDict
import json
import os
from PIL import Image

if __name__ == '__main__':
	if not os.path.exists('生成素材/university'):
		os.mkdir('生成素材/university')
	if not os.path.exists('生成素材/e'):
		os.mkdir('生成素材/e')
	if not os.path.exists('生成素材/country'):
		os.mkdir('生成素材/country')

	for png_file in os.listdir('生成素材'):
		if '.png' in png_file and '.0' not in png_file:
			png_id = str(int(png_file.split('ID')[1].split('_')[0]))
			png_year = str(int(png_file.split('Year')[1].split('.')[0]))
			png_type = str(int(png_file.split('Type')[1].split('_')[0]))
			if png_type in [str(i) for i in range(1, 6)]:
				# university
				if not os.path.exists('生成素材/university/' + png_year):
					os.mkdir('生成素材/university/' + png_year)
				png_image = Image.open('生成素材/' + png_file)
				f = '生成素材/university/' + png_year + '/' + png_id + '_' + png_type + '_' + png_year + '.png'
				print('Proceesing ' + f)
				png_image.save(f)
			elif png_type in [str(i) for i in range(6, 9)]:
				# e
				if not os.path.exists('生成素材/e/' + png_year):
					os.mkdir('生成素材/e/' + png_year)
				png_image = Image.open('生成素材/' + png_file)
				f = '生成素材/e/' + png_year + '/' + png_id + '_' + png_type + '_' + png_year + '.png'
				print('Proceesing ' + f)
				png_image.save(f)
			elif png_type in [str(i) for i in range(9, 11)]:
				# country
				if not os.path.exists('生成素材/country/' + png_year):
					os.mkdir('生成素材/country/' + png_year)
				png_image = Image.open('生成素材/' + png_file)
				f = '生成素材/country/' + png_year + '/' + png_id + '_' + png_type + '_' + png_year + '.png'
				print('Proceesing ' + f)
				png_image.save(f)