import turtle as t

#make a function called virus_shape(size, colors_list) that draws the virus shape with size and the colors contained in colors_list


def virus_shape(size, list_of_colors):

    t.speed(70)
    t.bgcolor('black')


    #represents the index of colors strings in colors_list
    i=0

    while size>0:
        t.left(size)
        t.color(list_of_colors[i])
        t.forward(size*3)
        size=size-0.4
        
        i = i+1
        
        if i== len(list_of_colors):
            i=0

input_size = int(input("please type a size: "))

colors_li=[]

while True:
    color = input("choose a color: ")
    colors_li.append(color)
    question = input("do you want to add a new color?(y/n): ")
    if question == 'n' :
        break
    

virus_shape(input_size,colors_li)




