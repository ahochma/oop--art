''' Exercise #7. Python Programming.'''
#########################################
# Question 1 - do not delete this comment
#########################################

class ArtDisplay:

    def __init__(self, name, date, art_type, preserving_date, worth):
        if worth <= 0:
            raise ValueError('Invalid worth value')
        self.name = name
        self.date = date
        self.art_type = art_type
        self.preserving_date = preserving_date
        self.worth = worth

    def __repr__(self):
        return self.name + ' is a ' + self.art_type+ ' that was created in ' + self.date + ' and needs to be preserved in ' + self.preserving_date

    def __gt__(self, other):
        return self.worth > other.worth

    def change_preserving_date(self, new_date):
        self.preserving_date = new_date

#########################################
# Question 2 - do not delete this comment
#########################################

class MuseumSubscriber:

    def __init__(self, name, ticket_type, favorites):
        self.name = name
        self.favorites = favorites
        if ticket_type == '1' or ticket_type == '5':
            self.entries_left = int(ticket_type)
        else:
            self.entries_left = ticket_type

    def __repr__(self):
        if isinstance(self.entries_left, str):
            return self.name + ' has a subscription until the ' + self.entries_left
        else:
            return self.name + ' has ' + str(self.entries_left) + ' entries left'

    def set_entry(self):
        if isinstance(self.entries_left, str):
            print('Welcome subscriber!')
        elif self.entries_left == 0:
            print('Please renew your subscription')
        else:
            self.entries_left -= 1
            print('Welcome!', str(self.entries_left), 'entries left')

    def get_favorites(self):
        return self.favorites

##########################################
# Questions 3 - do not delete this comment
##########################################

class Museum:

    def __init__(self,art_displays):
        self.art_displays = art_displays.copy()
        self.subscribers = []

    def __repr__(self):
        repret = "This museum contains the following displays:" + '\n'
        for art in sorted(self.art_displays, key= lambda x: x.worth):
            repret += repr(art) + '\n'
        return repret

    def get_art_displays(self):
        return self.art_displays

    def get_art_display(self,name):
        for art in self.art_displays:
            if name == art.name:
                return art

    def add_art_display(self,artDisplay):
        lst = self.art_displays
        lst.append(artDisplay)
        self.art_displays = lst

    def add_subscriber(self, subscriber):
        lst = self.subscribers
        lst.append(subscriber)
        self.subscribers = lst

    def change_preserving_date(self, name , new_date):
        for art in self.art_displays:
            if name == art.name:
                art.change_preserving_date(new_date)
                break

    def get_total_worth(self):
        total = 0
        for art in self.art_displays:
            total += art.worth
        return total

    def subscriber_entry(self, name):
        for sub in self.subscribers:
            if sub.name == name:
                sub.set_entry()
                break

    def find_loved_disp(self):
        dict = {self.get_art_displays()[i].name: 0 for i in range(0, len(self.get_art_displays()))}
        for sub in self.subscribers:
            for art in sub.favorites:
                dict[art.name] += 1
        lst = sorted(dict, key=dict.get, reverse=True)
        newlst = [lst[0]]
        i = 0
        while i < len(lst) - 1:
            if dict[lst[i]] == dict[lst[i+1]]:
                newlst.append(lst[i+1])
                i += 1
            else:
                break
        return newlst

#########################################
# Question 4 - do not delete this comment
#########################################

def create_museum(filename):
    f = None
    try:
        f = open(filename, 'r')
        art_list = []
        ret_mus = Museum(art_list)
        for line in f:
            class_name = line.strip().split(',')[0]
            if class_name == 'artDisplay':
                temp_art = ArtDisplay(line.strip().split(',')[1],line.strip().split(',')[2],line.strip().split(',')[3],line.strip().split(',')[4],int(line.strip().split(',')[5]))
                art_list.append(temp_art)
                ret_mus.add_art_display(temp_art)
            if class_name == 'subscriber':
                fav_lst = [art_list[int(line.strip().split(',')[3]) - 1],art_list[int(line.strip().split(',')[4]) - 1],art_list[int(line.strip().split(',')[5]) - 1]]
                temp_sub = MuseumSubscriber(line.strip().split(',')[1],line.strip().split(',')[2],fav_lst)
                ret_mus.add_subscriber(temp_sub)
        print("This museum's worth is", ret_mus.get_total_worth())
        return ret_mus
    except IOError:
        print('Unable to load', filename, 'due to an IO Error')
    finally:
        if f != None:
            f.close()

# use the following code to test your code:
#museum=create_museum('museum.csv')
#print (museum)

