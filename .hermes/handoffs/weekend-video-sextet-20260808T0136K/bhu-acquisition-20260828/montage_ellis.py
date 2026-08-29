from PIL import Image

def create_montage(start, end, filename):
    images = [Image.open(f"ellis_page_{i}.png") for i in range(start, end+1)]
    widths, heights = zip(*(i.size for i in images))
    total_width = sum(widths)
    max_height = max(heights)
    new_im = Image.new('RGB', (total_width, max_height))
    x_offset = 0
    for im in images:
      new_im.paste(im, (x_offset,0))
      x_offset += im.size[0]
    new_im.save(filename)

create_montage(1, 4, "ellis_1_4.png")
create_montage(5, 8, "ellis_5_8.png")
create_montage(9, 12, "ellis_9_12.png")
create_montage(13, 16, "ellis_13_16.png")
