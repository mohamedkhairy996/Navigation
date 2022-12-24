# importing Library for Searching Algorithm
import Astar
import DFS
import BFS
import UCS
import DATA
# importing Library for GUI
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import cv2

#######################################################################################################################

initCity = " "
goalCity = " "
searchAlgo = " "
points = DATA.points

def find_button():      # function to get values after press "Find" button
    global initCity
    global goalCity
    global searchAlgo
    global points
    initCity = combo1.get()
    goalCity = combo2.get()
    searchAlgo = combo3.get()
    # check data if user ignore to enter any data
    if (initCity == "Pick a city") and (goalCity == "Pick a city") and (searchAlgo == "Pick an algorithm"):
        messagebox.showerror('ERROR !', "Please chose the two cities and searching algorithm")
    elif (initCity != "Pick a city") and (goalCity == "Pick a city") and (searchAlgo == "Pick an algorithm"):
        messagebox.showerror('ERROR !', "Please chose the goal city and searching algorithm")
    elif (initCity == "Pick a city") and (goalCity != "Pick a city") and (searchAlgo == "Pick an algorithm"):
        messagebox.showerror('ERROR !', "Please chose the init city and searching algorithm")
    elif (initCity != "Pick a city") and (goalCity != "Pick a city") and (searchAlgo == "Pick an algorithm"):
        messagebox.showerror('ERROR !', "Please chose the searching algorithm")
    elif (initCity == "Pick a city") and (goalCity == "Pick a city") and (searchAlgo != "Pick an algorithm"):
        messagebox.showerror('ERROR !', "Please chose the searching algorithm")
    elif (initCity != "Pick a city") and (goalCity == "Pick a city") and (searchAlgo != "Pick an algorithm"):
        messagebox.showerror('ERROR !', "Please chose the goal city")
    elif (initCity == "Pick a city") and (goalCity != "Pick a city") and (searchAlgo != "Pick an algorithm"):
        messagebox.showerror('ERROR !', "Please chose the init city")
    elif initCity == goalCity:
        messagebox.showerror('ERROR !', "Please chose different cities")
    else:
        title = "Route from " + initCity + " to " + goalCity + " using " + searchAlgo
        list = []
        if searchAlgo == "BFS":
            list = BFS.bfs(initCity, goalCity)
        else:
            if searchAlgo == "DFS":
                DFS.visited = set()
                DFS.dfsPath = []
                list = DFS.dfs(initCity, goalCity)
            elif searchAlgo == "A*":
                path = Astar.A_star(initCity, goalCity)
                path_cost = Astar.path_f_cost(path)[-1]
                title += ", and the cost is " + str(path_cost) + " km"
                for it in path:
                    list.append(it[0])
            else:
                path = UCS.ucs(initCity, goalCity)
                path_cost = UCS.path_cost(path)[0]
                title += ", and the cost is " + str(path_cost) + " km"
                for it in path:
                    list.append(it[0])

            img2 = cv2.imread(r'map.png', 1)
            for i in range(0, len(list), 1):
                if i != len(list) - 1:
                     cv2.arrowedLine(img2, points[list[i]], points[list[i + 1]], (0, 0, 0), 2)
                if i == 0:
                    cv2.circle(img2, points[list[i]], 7, (0, 0, 255), -1)      # init city
                elif i == len(list) - 1:
                    cv2.circle(img2, points[list[i]], 7, (255, 255, 0), -1)     # goal city
                else:
                    cv2.circle(img2, points[list[i]], 7, (128, 128, 128), -1)
                cv2.imshow(title, img2)
                cv2.waitKey(1000)


            cv2.waitKey(0)
            cv2.destroyAllWindows()
    """
    img2 = cv2.imread(r'map.png', 1)
    for i in list:                      # loop for drawing circles for cities
         cv2.circle(img2, points[i], 7, (0, 0, 0), -1)

    for i in range(0, len(list)-1, 1):    # loop for drawing lines for cities
        cv2.line(img2, points[list[i]], points[list[i+1]], (0, 0, 255), 5)
    cv2.imshow(title, img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    list=[]
    """
def clear_button():      # function to get values after press "Clear" button
    combo1.set("Pick a city")
    combo2.set("Pick a city")
    combo3.set("Pick an algorithm")
#######################################################################################################################

# cities names list
cityList = ["shebin", "minuf", "tala", "birket as sab", "el bagour", "ashmun", "quwaysna", "el sadat city", "el shohada",
            "Kafr El Zayat", "basioun", "tanta", "qutur", "El Mahalla El Kubra", "As Santah", "Samannoud", "zefta", "banha",
            "qalyub", "Al Qanatir Al Khayriyyah", "Shubra Al Khaymah", "el khankah", "kafr shokr", "shibin el qanatir", "toukh"]
# Search algorithms names list
algorithmsList = ["BFS", "DFS", "A*", "UCS"]

#######################################################################################################################

video = cv2.VideoCapture('intro0.mp4')
fps = int(video.get(cv2.CAP_PROP_FPS))                      # calculate fps
while video.isOpened():
    graped, fr = video.read()                               # read video
    key = cv2.waitKey(1)                                    # wait if user enter anything
    if key == ord('q') or not graped:                       # if 'q' is pressed then exit
        break
    if key == ord('0'):                                     # if '0' is pressed then run video again
        video.set(cv2.CAP_PROP_POS_FRAMES,0)
    cv2.imshow("About us", fr)
    cv2.waitKey(fps)                                        # some delay to make video run on it is normal speed

cv2.destroyAllWindows()                                     # when video ended , close the window

#######################################################################################################################


window = Tk()                               # create object from tk
window.title("Navigation")                  # window name
window.iconbitmap('logo.ico')               # window icon
window.minsize(width=500, height=500)       # minium size of window
window.maxsize(width=1107, height=900)      # maximum size of window
window.geometry("1107x790")                 # Size of Window
window.configure(bg='White')                # window background color
img = PhotoImage(file='background.png')     # window background photo
canvas = Canvas(window)                     # Create Canavs
canvas.create_image(0, 0, image=img, anchor=NW)
canvas.pack(fill=BOTH, expand=1)
frame = LabelFrame(canvas, text='Data Entry', labelanchor='n')                       # create a frame

#######################################################################################################################

l1 = Label(frame, text='Initial City', foreground='black', font=("Arial", 10))  # label1
l1.grid(row=0, column=0, columnspan=2, sticky=NSEW)
l2 = Label(frame, text='Goal City ', foreground='black', font=("Arial", 10))    # label2
l2.grid(row=2, column=0, columnspan=2, sticky=NSEW)
l3 = Label(frame, text='Search algorithms', foreground='black', font=("Arial", 10))    # label3
l3.grid(row=4, column=0, columnspan=2, sticky=NSEW)


#######################################################################################################################

combo1 = ttk.Combobox(frame, values=cityList, height=20, width=20, font=("Arial", 10))       # combobox1 for start city
combo1.set("Pick a city")
combo1.grid(row=0, column=3)
combo2 = ttk.Combobox(frame, values=cityList, height=20, width=20, font=("Arial", 10))       # combobox2 for goal city
combo2.set("Pick a city")
combo2.grid(row=2, column=3)
combo3 = ttk.Combobox(frame, values=algorithmsList, height=20, width=20, font=("Arial", 10))
combo3.set("Pick an algorithm")                                                       # combobox3 for Search algorithms
combo3.grid(row=4, column=3)

#######################################################################################################################

btn1 = Button(frame, text='Find', background='orange', foreground='white', font=("Arial", 10), command=find_button)
btn1.grid(row=5, column=2, padx=5)                                             # button 1 "find"
btn2 = Button(frame, text='Clear', background='orange', foreground='white', font=("Arial", 10), command=clear_button)
btn2.grid(row=5, column=3, padx=5)                                             # button 2 "clear"
btn3 = Button(frame, text='Exit', background='orange', foreground='white', font=("Arial", 10), command=frame.quit)
btn3.grid(row=5, column=4, padx=5)                                              # button 3 "exit"

#######################################################################################################################

frame.grid(padx=400, pady=300)
#frame.place(relx=0.2,rely=0.85,anchor=S)
window.mainloop()



"""
start = input("enter start :") #'shebin'
destination = input("enter destination :") #'Shubra Al Khaymah' #
algorithm = int(input("choose Algorithm : \n1)Astar\n2)UCS\n3)DFS\n4)BFS\n : "))
if algorithm==1:
    path=Astar.A_star(start,destination)
    list = []
    path_cost = Astar.path_f_cost(path)[-1]
    for it in path:
        list.append(it[0])
    print("The A* path is : ", list[0:])
    print("The cost of this path is = ", path_cost, "KM")
elif algorithm==2:
    path=UCS.ucs(start,destination)
    list = []
    path_cost = UCS.path_cost(path)[0]
    for it in path:
        list.append(it[0])
    print("The Uniform Cost Search path is : ", list[0:])
    print("The cost of this path is = ", path_cost, "KM")
elif algorithm==3:
    path=DFS.dfs(start,destination)
    print("The Depth-First Search Path is :" ,path)
elif algorithm==4:
    path=BFS.bfs(start,destination)
    print("The Breadth-First Search Path is :" ,path)
else:
    print("chosse from 1 : 4")
"""
