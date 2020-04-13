'''
用于生成一张时间段小图片
'''
from PIL import Image, ImageDraw, ImageFont

def add_text(image, ttf_path, text, font_size, height, position = 'mid', color = 'black'):
	'''
	在时间段中添加文字
	image: 需要处理的图像
	ttf_path: 字体路径
	text: 需要添加的文字
	font_size: 字体大小
	height: 高度
	position: 字体位置，在'mid', 'left'和'right'中选择
	color: 字体颜色
	PS: 时间片的生成目前还不能够批量生成，需要进一步进行修改
	'''
	ttf = ImageFont.truetype(ttf_path, font_size)
	text_width = ttf.getsize(text)
	if position == 'mid':
		text_coordinate = (int((image.size[0] - text_width[0]) / 2), 
			int((height - text_width[1]) / 2))
	elif position == 'left':
		text_coordinate = (int((image.size[0] - text_width[0]) / 4), 
			int((height - text_width[1]) / 2))
	elif position == 'right':
		text_coordinate = (int((image.size[0] - text_width[0]) / 4 * 3), 
			int((height - text_width[1]) / 2))
	else:
		raise('postion参数有问题')
	img_draw = ImageDraw.Draw(image)
	img_draw.text(text_coordinate, text, font = ttf, fill = color)

if __name__ == '__main__':
	# for year in range(1931, 2021):
	image = Image.new('RGB', (150, 200), (255, 255, 255))
	ttf_path = "fonts/kai.ttf"

		# mid_text = str(year % 1000)
		# while len(mid_text) != 3:
		# 	mid_text = '0' + mid_text
		# if int(year / 1000) == 1:
		# 	mid_text = '  ' + mid_text
		# else:
		# 	mid_text = '   ' + mid_text

		# add_text(image, ttf_path, str(int(year / 1000)) + '  ', 80, 155, 'left', 'red')

		# add_text(image, ttf_path, mid_text, 60, 170, 'mid', 'black')

	add_text(image, ttf_path, '1   ', 80, 45, 'left', 'red')
	add_text(image, ttf_path, '  880', 60, 60, 'mid', 'black')
	add_text(image, ttf_path, '-', 60, 155, 'mid', 'black')
	add_text(image, ttf_path, '1890', 60, 255, 'mid', 'black')
	image.save('时间片/1880_1890.png')

		# image.save('时间片/' + str(year) + '.png')