# IMDB Custom Search.py
# version 1.0
# Max Laurie 02/09/2021

# Takes input from user and constructs an imdb search web address which opens automatically in browser


import webbrowser
import tkinter


def get_genres():
    return ["- Select -",
            "Action",
            "Adventure",
            "Animation",
            "Biography",
            "Comedy",
            "Crime",
            "Documentary",
            "Drama",
            "Family",
            "Fantasy",
            "Film-Noir",
            "Game-Show",
            "History",
            "Horror",
            "Music",
            "Musical",
            "Mystery",
            "News",
            "Reality-TV",
            "Romance",
            "Sci-Fi",
            "Sport",
            "Talk-Show",
            "Thriller",
            "War",
            "Western"]


def reset_click():
    reset_colours()
    min_vote_box.delete(0, 'end')
    genre_selected.set(get_genres()[0])
    english_only_tickbox.select()
    features_only_tickbox.select()
    date_from_box.delete(0, 'end')
    date_to_box.delete(0, 'end')
    max_runtime_box.delete(0, 'end')
    keyword_box.delete(0, 'end')


def reset_colours():
    min_vote_label.config(fg="black")
    date_from_label.config(fg="black")
    date_to_label.config(fg="black")
    max_runtime_label.config(fg="black")


def search_click():
    min_votes_value = min_vote_box.get()
    genre_value = genre_selected.get()
    english_only_value = english_only_selection.get()
    features_only_value = features_only_selection.get()
    date_from_value = date_from_box.get()
    date_to_value = date_to_box.get()
    max_runtime_value = max_runtime_box.get()
    keyword_value = keyword_box.get()

    error_log = []

    if min_votes_value != "":
        try:
            int(min_votes_value)
        except ValueError:
            error_log.append("min_vote")
        else:
            min_votes = f"?num_votes={min_votes_value},"
    else:
        min_votes = "?num_votes=0,"

    if genre_value != "- Select -":
        genre = f"&genres={genre_value}"
    else:
        genre = ""

    if english_only_value != 0:
        language = "&languages=en"
    else:
        language = ""

    if features_only_value != 0:
        feature = "&title_type=feature"
    else:
        feature = ""

    if date_from_value != "" and date_to_value != "":
        try:
            int(date_from_value)
        except ValueError:
            error_log.append("date_from")
        else:
            if len(date_from_value) != 4:
                error_log.append("date_from")
        try:
            int(date_to_value)
        except ValueError:
            error_log.append("date_to")
        else:
            if len(date_to_value) != 4:
                error_log.append("date_to")
        if "date_from" in error_log or "date_to" in error_log:
            pass
        else:
            date_range = f"&year={date_from_value}-01-01,{date_to_value}-12-31"

    if date_from_value != "" and date_to_value == "":
        try:
            int(date_from_value)
        except ValueError:
            error_log.append("date_from")
        else:
            if len(date_from_value) != 4:
                error_log.append("date_from")
            else:
                date_range = f"&year={date_from_value}-01-01,"
    if date_from_value == "" and date_to_value != "":
        try:
            int(date_to_value)
        except ValueError:
            error_log.append("date_to")
        else:
            if len(date_to_value) != 4:
                error_log.append("date_to")
            else:
                date_range = f"&year=,{date_to_value}-01-01"
    if date_from_value == "" and date_to_value == "":
        date_range = ""

    if max_runtime_value != "":
        try:
            int(max_runtime_value)
        except ValueError:
            error_log.append("max_runtime")
        else:
            runtime = f"&runtime=0,{max_runtime_value}"
    else:
        runtime = ""

    if keyword_value != "":
        keyword = f"&keywords={keyword_value}"
    else:
        keyword = ""

    reset_colours()

    if len(error_log) != 0:
        if "min_vote" in error_log:
            min_vote_label.config(fg="red")
        if "date_from" in error_log:
            date_from_label.config(fg="red")
        if "date_to" in error_log:
            date_to_label.config(fg="red")
        if "max_runtime" in error_log:
            max_runtime_label.config(fg="red")
        return
    else:
        address = (f"https://www.imdb.com/search/title/{min_votes}{genre}{language}"
                   f"{feature}{runtime}{keyword}{date_range}&sort=user_rating,desc")

        webbrowser.open(address, new=2)


# Main

main_window = tkinter.Tk()

main_window.title("IMDB Custom Search")
main_window.geometry("600x500")
main_window.configure(bg="#f0f0f0")

main_window.iconphoto(False, tkinter.PhotoImage(file="gfx\\Icon.png"))

main_window_bg = tkinter.PhotoImage(file="gfx\\Bg.png")
bg_label = tkinter.Label(main_window, image=main_window_bg)
bg_label.place(x=-2, y=-2)

min_vote_label = tkinter.Label(main_window, text="Min no. votes")
min_vote_label.grid(row=1, column=1, sticky='w', ipadx=10)
min_vote_box = tkinter.Entry(main_window, width=7)
min_vote_box.grid(row=1, column=2, sticky='w')

genre_label = tkinter.Label(main_window, text="Genre")
genre_label.grid(row=2, column=1, sticky='w', ipadx=5)
genre_selected = tkinter.StringVar()
genre_selected.set(get_genres()[0])
genre_dropdown = tkinter.OptionMenu(main_window, genre_selected, *get_genres())
genre_dropdown.grid(row=2, column=2, sticky='w')

english_only_label = tkinter.Label(main_window, text="English only")
english_only_label.grid(row=3, column=1, sticky='w', ipadx=5)
english_only_selection = tkinter.IntVar()
english_only_tickbox = tkinter.Checkbutton(main_window, variable=english_only_selection, onvalue=1, offvalue=0)
english_only_tickbox.select()
english_only_tickbox.grid(row=3, column=2, sticky='w')

features_only_label = tkinter.Label(main_window, text="Features only")
features_only_label.grid(row=4, column=1, sticky='w', ipadx=10)
features_only_selection = tkinter.IntVar()
features_only_tickbox = tkinter.Checkbutton(main_window, variable=features_only_selection, onvalue=1, offvalue=0)
features_only_tickbox.select()
features_only_tickbox.grid(row=4, column=2, sticky='w')

date_from_label = tkinter.Label(main_window, text="Year from")
date_from_label.grid(row=1, column=4, sticky='w')
date_from_box = tkinter.Entry(main_window, width=8)
date_from_box.grid(row=1, column=5, sticky='w')

date_to_label = tkinter.Label(main_window, text="Year to")
date_to_label.grid(row=2, column=4, sticky='w')
date_to_box = tkinter.Entry(main_window, width=8)
date_to_box.grid(row=2, column=5, sticky='w')

max_runtime_label = tkinter.Label(main_window, text="Max. runtime")
max_runtime_label.grid(row=3, column=4, sticky='w')
max_runtime_box = tkinter.Entry(main_window, width=8)
max_runtime_box.grid(row=3, column=5, sticky='w')

keyword_label = tkinter.Label(main_window, text="Keyword")
keyword_label.grid(row=4, column=4, sticky='w')
keyword_box = tkinter.Entry(main_window, width=10)
keyword_box.grid(row=4, column=5, sticky='w')

reset_button = tkinter.Button(main_window, text="Reset", width=15, command=reset_click)
reset_button.grid(row=5, column=2, sticky='w')

search_button = tkinter.Button(main_window, text="Search", width=15, command=search_click)
search_button.grid(row=5, column=4, sticky='e')

name_label = tkinter.Label(main_window, text="© MLaurie '21", fg="#cdcdcd")
name_label.grid(row=6, column=3)

main_window.columnconfigure(0, weight=1)
main_window.columnconfigure(1, weight=1)
main_window.columnconfigure(2, weight=1)
main_window.columnconfigure(3, weight=1)
main_window.columnconfigure(4, weight=1)
main_window.columnconfigure(5, weight=1)
main_window.columnconfigure(6, weight=1)
main_window.rowconfigure(0, weight=1)
main_window.rowconfigure(1, weight=1)
main_window.rowconfigure(2, weight=1)
main_window.rowconfigure(3, weight=1)
main_window.rowconfigure(4, weight=1)
main_window.rowconfigure(5, weight=1)
main_window.rowconfigure(6, weight=0)

main_window.mainloop()
