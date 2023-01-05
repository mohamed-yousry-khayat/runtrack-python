def change_place():
    list = ["moi", "toi", "lui"]
    mot1 = "moi"
    mot2 = "lui"
    list.remove("moi")
    list.insert(2,mot1)
    list.remove("lui")
    list.insert(0,mot2)
    print(list)

change_place()
