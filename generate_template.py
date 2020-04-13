'''
用于生成一张素材图片的接口
'''
from PIL import Image, ImageDraw, ImageFont
from generate_circle import crop_max_square, crop_center, mask_circle_transparent

def add_text(image, ttf_path, text, font_size, height):
	'''
	在图片中添加文字介绍
	image: 需要处理的图像
	ttf_path: 字体路径
	text: 需要添加的文字
	font_size: 字体大小
	height: 高度
	'''
	ttf = ImageFont.truetype(ttf_path, font_size)
	# text_width = ttf.getsize(text)
	# print(text_width)
	# text_coordinate = (int((image.size[0] - text_width[0]) / 2), 
	# 	int((height - text_width[1]) / 2))
	# img_draw = ImageDraw.Draw(image)
	# img_draw.text(text_coordinate, text, font = ttf, fill = (0, 0, 0))

	one_line_text = ''
	rest_text = text
	# print(text)
	for s in text:
		one_line_text += s
		rest_text = rest_text[1:]
		if ttf.getsize(one_line_text)[0] > 450 or rest_text == '':
			text_width = ttf.getsize(one_line_text)
			text_coordinate = (int((image.size[0] - text_width[0]) / 2), 
				int((height - text_width[1]) / 2))
			img_draw = ImageDraw.Draw(image)
			img_draw.text(text_coordinate, one_line_text, font = ttf, fill = (128, 0, 255))
			one_line_text = ''
			height += (font_size * 2.1)

	return height

def add_pic(image, image_path, save_path, circle_color = 'steelblue'):
	'''
	在图片中插入图片
	image: 需要处理的图像
	image_path: 图片路径
	circle_color: 小圆圈图片，默认为steelblue(steelblue, indianred, springgreen)
	'''
	markImg = Image.open(image_path)
	# 图片大小
	thumb_width = 320
	# 线条偏置
	line_offset = 0
	# 线条宽度
	line_width = 3

	im_square = crop_max_square(markImg).resize((thumb_width, thumb_width), Image.LANCZOS)
	im_thumb = mask_circle_transparent(im_square, 0)

	draw = ImageDraw.Draw(image)

	image.paste(im_thumb, (int((image.size[0] - thumb_width) / 2), 240))
	if '.jpg' in save_path:
		jpg_pic = Image.new('RGB', image.size, (255, 255, 255))
		jpg_pic.paste(image, image)
	else:
		jpg_pic = image

	draw = ImageDraw.Draw(jpg_pic)
	draw.ellipse(((image.size[0] - thumb_width) / 2 - line_offset - line_offset, 
		240 - line_offset - line_offset, 
		(image.size[0] + thumb_width) / 2 + line_offset + line_offset, 
		240 + thumb_width + line_offset + line_offset), 
		None, circle_color, line_width)

	return jpg_pic

if __name__ == '__main__':
	img_path = "green_background.png"
	ttf_path = "fonts/小米兰亭.ttf"

	image = Image.open(img_path)
	add_text(image, ttf_path, '啦啦啦', 100, 190)
	add_text(image, ttf_path, 'Hello world', 80, 350)
	image = add_pic(image, 'origin/mogic.png', 'my_picture/test.jpg', 'yellowgreen')

	image.save('my_picture/test.png')