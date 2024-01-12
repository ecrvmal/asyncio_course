


class Text:
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return f'{self.text}'


class Image:
    def __init__(self, image):
        self.image = image

    def __str__(self):
        return f'{self.image}'


class Comment:
    def __init__(self, author, text):
        self.author = author
        self.text = text

    def __str__(self):
        return f'comment: {self.author} {self.text}'



class Page:
    # def __init__(self):
    #     self.obj_on_page = []
    def __init__(self, *args):
        self.obj_on_page = [*args]

    def add_obj(self, obj):
        self.obj_on_page.append(obj)

    def insert_obj(self, index,  obj):
        self.obj_on_page.insert(index, obj)

    def pop_obj(self, index):
        self.obj_on_page.pop(index)

    def update_obj(self, index, new_obj):
        self.obj_on_page[index]= new_obj



    def __str__(self):
        # return f"{' '.join(self.obj_on_page)}"
        # return f'{self.obj_on_page}'
        # return f"{' '.join(self.obj_on_page.__str__())}"
        # return f"{' '.join(*[el.__str__() for el in self.obj_on_page])}"
        text =''
        for el in self.obj_on_page:
            text += el.__str__()
            text +='\n'
        return text

if __name__ == '__main__':
    comment = Comment('Ivan', 'Test text')
    text1 = Text ('text 1')
    image = Image('image 1')
    text2 = Text ('text 2')

    page = Page(text1, image, text2, comment)
    # page.add_obj(text1)
    # page.add_obj(text2)
    # page.add_obj(image)
    # page.add_obj(comment)

    print(page)
    page.update_obj(0, text2)
    page.update_obj(2, text1)
    print(page)

