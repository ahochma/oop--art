museum = create_museum('C:/Users/user/Desktop/אוניברסיטת תא/סמסטר א/פייתון/תרגילי בית/ex 7/museum.csv')
print(museum)
print(museum.find_loved_disp())

print("test Q1:")
art1 = ArtDisplay("Goodart", "25.11.1993", "statue", "12.01.21", 200)
print("#1 chek for repr of Art1:")
print(art1)
#art2 = ArtDisplay("artZero0", "01.01.01", "painting", "20.120.22", 0)
#art3 = ArtDisplay("Negart", "02.02.02", "statue", "15.12.15", -80)
#noart = ArtDisplay()
art1.change_preserving_date("12.01.22")
print("#2 chek for change preserving date of art1:")
print(art1)
print("#3 chek that repr return string:")
c1 = repr(art1)
print(c1)
art4 = ArtDisplay("biggerart", "19.12.20", "painting", "15.03.2021", 500)
print("#4 chek gt of ArtDisplay: art1>art4 --- false")
print(art1>art4)
print("#4 chek gt of ArtDisplay: art4>art1 --- true")
print(art4>art1)

print("test Q2:")
subs1 = MuseumSubscriber("One", "1", [art1, art4])
subs2 = MuseumSubscriber("Five","5",[art1])
subs3 = MuseumSubscriber("Date","11.1.2020",[])
print("#1 chek for repr of sub1&2&3:")
print(subs1)
print(subs2)
print(subs3)
print("#2 chek for set_entry of sub1 - 3 times:")
subs1.set_entry()
subs1.set_entry()
subs1.set_entry()
print("#3 chek for set_entry of sub2 - 3 times:")
subs2.set_entry()
subs2.set_entry()
subs2.set_entry()
print("#4 chek for set_entry of sub3 - 2 times:")
subs3.set_entry()
subs3.set_entry()
print("#5 chek for get_fav of sub1:")
print(subs1.get_favorites())
print("#6 chek for get_fav of sub2:")
print(subs2.get_favorites())
print("#7 chek for get_fav of sub3:")
print(subs3.get_favorites())

print("test Q3:")
mus1_empty = Museum([])
mus2_good = Museum([art1,art4])
mus3_another = Museum([art1,art4, ArtDisplay("New","18.12.2020", "statue","29.12.2020", 300)])
print("#1 get_art_displays: mus1&2&3:")
print(mus1_empty.get_art_displays())
print(mus2_good.get_art_displays())
print(mus3_another.get_art_displays())
print("#2 get art - Goodart from mus2:")
print(mus2_good.get_art_display("Goodart"))
print("#3 get art - New from mus3:")
print(mus3_another.get_art_display("New"))
print("#4 try to get no art from mus3:")
print(mus3_another.get_art_display("noart"))
print("#5 add art to mus3 - Addition", " And chek repr for mus3")
mus3_another.add_art_display(ArtDisplay("Addition", "19.12.2022", "painting", "04.04.2021", 400))
print(mus3_another)
print("#6 mus3 subscribers list:")
print(mus3_another.subscribers)
print("#7 add subs1 to mus3:")
mus3_another.add_subscriber(subs1)
print(mus3_another.subscribers)
print("#8 add subs2 & 3 to mus3:")
mus3_another.add_subscriber(subs2)
mus3_another.add_subscriber(subs3)
print(mus3_another.subscribers)
print("#9 change preserving date of New art in mus 3")
mus3_another.change_preserving_date("New", "10.10.2030")
print(mus3_another)
print("#10 total worth of mus1&2&3: 0, 700, 1400")
print(mus1_empty.get_total_worth())
print(mus2_good.get_total_worth())
print(mus3_another.get_total_worth())
print("#11 sub1&2&3 entery to mus3")
mus3_another.subscriber_entry("One")
mus3_another.subscriber_entry("Five")
mus3_another.subscriber_entry(("Date"))
print("#12 find loved in mus1 - no art, mus2 - no sub - Goodart and biggerart, mus3 - Goodart")
#print(mus1_empty.find_loved_disp())
print(mus2_good.find_loved_disp())
print(mus3_another.find_loved_disp())
mus3_another.add_subscriber(MuseumSubscriber("Newsub1", "5", [ArtDisplay("New","18.12.2020", "statue","29.12.2020", 300),ArtDisplay("Addition", "19.12.2022", "painting", "04.04.2021", 400)]))
mus3_another.add_subscriber(MuseumSubscriber("Newsub2", "5", [ArtDisplay("Addition", "19.12.2022", "painting", "04.04.2021", 400)]))
print(mus3_another.find_loved_disp())
mus3_another.add_subscriber(MuseumSubscriber("Newsub3", "1", [ArtDisplay("Addition", "19.12.2022", "painting", "04.04.2021", 400)]))
print(mus3_another.find_loved_disp())
