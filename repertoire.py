import tkinter as tk
import os

##-----------INITIALIZE APP-----------
RepertoireApp = tk.Tk()
RepertoireApp.title("Repertoire Manager")
RepertoireApp.geometry("1030x600")
RepertoireApp.resizable(False, False)
##------------------------------------


##----------CREATES "files" AND "artists" LISTS, WHICH ARE LISTS  -----------------
##         WITH TITLES AND ARTISTS NAMES GOTTEN FROM .txt FILES
os.chdir("songs/") ##CHANGE DIRECTORY TO "songs" FOLDER

files = os.listdir(".")

titles = []
artists = []



for x in range(len(files)):
	with open(files[x]) as f:
		content = f.readlines()

	name = content[0].strip('\n')

	artist = ''
	title = ''

	index = 1000

	for x in range(0,len(name)):
		if x < len(name)- 1:
			if name[x + 1] == "-":
				index = x
			if x < index:
				artist += name[x]
			if x > index + 2:
				title += name[x]
	title += name[-1:]

	titles.append(title)
	artists.append(artist)

##--------------CREATES LISTS FOR TITLE SORTING-------------
titles_sorted_TITLES = sorted(titles)

titles_index = []

for x in range(len(titles_sorted_TITLES)):
	for y in range(len(titles)):
		if titles_sorted_TITLES[x] == titles[y]:
			titles_index.append(y)
			break

artists_sorted_TITLES = []
files_TITLES = []

for x in range(len(titles_index)):
	for y in range(len(artists)):
		if y == titles_index[x]:
			artists_sorted_TITLES.append(artists[y])
			files_TITLES.append(files[y])


##--------------CREATES LISTS FOR ARTISTS SORTING-------------


artists_sorted_ARTISTS = sorted(artists)

artist_unique = []

for x in artists_sorted_ARTISTS:
	if artist_unique.count(x) == 0:
		artist_unique.append(x)


titles_sorted_ARTISTS = []
files_ARTISTS = []

for x in range(len(artist_unique)):
	for y in range(len(artists)):
		if artist_unique[x] == artists[y]:
			titles_sorted_ARTISTS.append(titles[y])
			files_ARTISTS.append(files[y])


#----------------------------------------
####UNTIL NOW:
# artists_sorted_TITLES: ARTISTS SORTED, ACCORDING TO TITLES SORTED IN APLHABETICAL
# titles_sorted_TITLES: TITLES SORTED TO ALPHABETICAL
# artists : ARTISTS IN THE FOLDER ORDER
# titles: TITLES IN THE FOLDER ORDER
# PS: artists and titles are in the SAME ORDER
# artists_sorted: ARTISTS SORTED IN ALPHABETICAL ORDER
# artists_unique: ARTISTS IN ALL SONGSS(NOT REPEATED)
# titles_sorted_ARTISTS: TITLES SORTED ACCORDING TO ARTISTS IN ALPHABETICAL


##---------------CREATES STRINGS FOR TITLES SORTING-----------------
space = " "
TITLES_SORT = []
ARTIST_SORT = []
FILES_SORT = []

for x in range(len(titles_sorted_TITLES)):
	spacing = 64-len(titles_sorted_TITLES[x])
	TITLES_SORT.append(titles_sorted_TITLES[x]+ spacing*space +artists_sorted_TITLES[x])

##---------------CREATES STRINGS FOR ARTISTS SORTING-----------------

for x in range(len(titles_sorted_ARTISTS)):
	spacing = 64-len(titles_sorted_ARTISTS[x])
	ARTIST_SORT.append(titles_sorted_ARTISTS[x]+ spacing*space + artists_sorted_ARTISTS[x])


##############################################################

def ArtistSort():
	n = 0
	sorting_boolean[0] = 1
	while n < len(TITLES_SORT):
		n+= 1
		Lb.delete(0)
	for item in ARTIST_SORT:
		Lb.insert(tk.END, item)



def TitleSort():
	n = 0
	sorting_boolean[0] = 0
	while n < len(TITLES_SORT):
		n+= 1
		Lb.delete(0)
	for item in TITLES_SORT:
		Lb.insert(tk.END, item)

def ListToSong(self):
	if sorting_boolean[0] == 0:
		FILES_SORT = files_TITLES
	elif sorting_boolean[0] == 1:
		FILES_SORT = files_ARTISTS
	SongPage.tkraise()
	a = Lb.curselection()
	song_txt.config(state= tk.NORMAL)
	song_txt.delete('1.0', tk.END)
	with open(FILES_SORT[a[0]]) as f:
		content = f.readlines()
	for x in content:  #ACTUALLY PRINT
		song_txt.insert(tk.END, x)
	song_txt.config(state= tk.DISABLED)

def SongToList():
	ListPage.tkraise()



sorting_boolean = [1]

SongPage = tk.Frame(RepertoireApp, width=600, height=600)
SongPage.grid(row = 0, column = 0, sticky = "nsew")

button1 = tk.Button(SongPage, text = "Return to List", width = 120, height = 1, command = SongToList)
button1.grid(row=0, column = 0, sticky = tk.W, )

song_txt = tk.Text(SongPage, borderwidth=3, relief="sunken", width = 100, height = 29)
song_txt.config(font=("consolas", 12), undo=True, wrap='word')
song_txt.grid(row=1, column=0, sticky="nsew")
song_txt.config(state= tk.DISABLED)
scrollb_song = tk.Scrollbar(SongPage, command=song_txt.yview )
scrollb_song.grid(row=1, column=1, sticky='nsew')
song_txt['yscrollcommand'] = scrollb_song.set


###########################################################################
ListPage = tk.Frame(RepertoireApp, width = 600, height = 600)
ListPage.grid(row = 0, column = 0, sticky = "nsew")

label = tk.Label(ListPage, text = "Start Page")
label.grid(row = 0, column = 0, pady = 10, padx = 10, sticky = tk.W)

title_button = tk.Button(ListPage, text = "TITLE", width = 60, height = 1, command = TitleSort)
title_button.grid(row=1, column = 0, sticky = tk.W)

artist_button = tk.Button(ListPage, text = "ARTIST", width = 60, height = 1, command = ArtistSort)
artist_button.grid(row=1, column = 1, sticky = tk.W)

Lb = tk.Listbox(ListPage, width = 125, height= 33, selectmode = tk.EXTENDED, font = ("Courier 10"))
Lb.grid(row = 2, column = 0, columnspan=2)
for item in ARTIST_SORT:
	Lb.insert(tk.END, item)

scrollb_list = tk.Scrollbar(ListPage, command=Lb.yview )
scrollb_list.grid(row=2, column=2, sticky='nsew')
Lb['yscrollcommand'] = scrollb_list.set

Lb.bind("<Double-Button-1>", ListToSong)

RepertoireApp.mainloop()