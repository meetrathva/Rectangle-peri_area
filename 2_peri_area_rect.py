length = int(input("Enter length: "))
width = int(input("Enter width: "))
area = length * width
perimeter = 2 * (length + width)
fh = open("2_peri_area_rect.txt","w")
fh.write("Area of rectangle: ")
fh.write(str(area))
fh.write("\nPerimeter of rectangle: ")
fh.write(str(perimeter))
fh.close()