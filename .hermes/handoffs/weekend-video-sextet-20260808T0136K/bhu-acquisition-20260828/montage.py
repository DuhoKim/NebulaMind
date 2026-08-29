from PIL import Image

def create_montage(start, end, filename):
    images = [Image.open(f"page_{i}.png") for i in range(start, end+1)]
    widths, heights = zip(*(i.size for i in images))

    total_width = sum(widths)
    max_height = max(heights)

    new_im = Image.new('RGB', (total_width, max_height))

    x_offset = 0
    for im in images:
      new_im.paste(im, (x_offset,0))
      x_offset += im.size[0]

    new_im.save(filename)

create_montage(2, 4, "montage_2_4.png")
create_montage(5, 7, "montage_5_7.png")
create_montage(8, 9, "montage_8_9.png")
