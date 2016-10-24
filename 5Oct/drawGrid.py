# yanfangguo@vub.ac.be
# scripting language courses 2nd WPO 14:28 5OCT2016


def create_corners():
    return "#----" * 2 + "#\n"


def create_central():
    return "|    " * 2 + "|\n"


def create_grid():
    return create_corners() + create_central() * 3 + create_corners() + create_central() * 3 + create_corners()


def create_corners1(width):
    return "#" + (width - 1) * '-'+'#'+(width - 1) * '-' + "#\n"


def create_central1(width):
   return "|"+(width-1)*' '+'|'+(width-1)*' '+"|\n"


def create_grid1(width):
    return create_corners1(width) + create_central1(width) * width + create_corners1(width) + create_central1(width) * width + create_corners1(width)


def create_grid2(width,length):
    return create_corners1(width) + create_central1(width) * length + create_corners1(width) + create_central1(width) * length + create_corners1(width)


print(create_grid2(5,6))
print ('haha')