'''
将矩形图片整合成圆形
'''
from PIL import Image, ImageDraw, ImageFilter

def crop_max_square(pil_img):
	return crop_center(pil_img, min(pil_img.size), min(pil_img.size))

def crop_center(pil_img, crop_width, crop_height):
	img_width, img_height = pil_img.size
	return pil_img.crop(((img_width - crop_width) // 2, 
		(img_height - crop_height) // 2, 
		(img_width + crop_width) // 2, 
		(img_height + crop_height) // 2))

def mask_circle_transparent(pil_img, blur_radius, offset = 0):
	offset = blur_radius * 2 + offset
	mask = Image.new("L", pil_img.size, 0)
	draw = ImageDraw.Draw(mask)
	draw.ellipse((offset, offset, pil_img.size[0] - offset, pil_img.size[1] - offset), fill = 255)
	mask = mask.filter(ImageFilter.GaussianBlur(blur_radius))

	result = pil_img.copy().convert('RGBA')
	result.putalpha(mask)

	# background = Image.new('RGB', pil_img.size, 'steelblue')

	jpg_pic = Image.new('RGB', result.size, (255, 255, 255))
	jpg_pic.paste(result, result)
	# jpg_pic.paste(background, result)

	return jpg_pic

if __name__ == '__main__':
	markImg = Image.open('origin/mogic.png')
	thumb_width = 300

	im_square = crop_max_square(markImg).resize((thumb_width, thumb_width), Image.LANCZOS)
	im_thumb = mask_circle_transparent(im_square, 0)
	im_thumb.save('my_picture/111.png')