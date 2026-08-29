from PIL import Image

def create_montage(start, end, filename):
    images = [Image.open(f"harrison_page_{i}.png") for i in range(start, end+1)]
    widths, heights = zip(*(i.size for i in images))

    total_width = sum(widths)
    max_height = max(heights)

    new_im = Image.new('RGB', (total_width, max_height))

    x_offset = 0
    for im in images:
      new_im.paste(im, (x_offset,0))
      x_offset += im.size[0]

    new_im.save(filename)

create_montage(1, 3, "harrison_1_3.png")
create_montage(4, 6, "harrison_4_6.png")
create_montage(7, 9, "harrison_7_9.png")
