#Chess
from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
import network
import pickle
from _thread import *

net = network.Network()

current_player = None
class chess():
    def __init__(self):
        self.root = Tk()
        self.root.title("Chess Game")
        self.grid()
        self.image()
        self.winner()
        self.menu()
        #self.block()
        self.time_grid()
        self.game_mode_rapid()
        start_new_thread(self.receive,())
        self.root.mainloop()
    
    def grid(self):
        self.initial_color = 'lime green'
        self.response = True
        self.castle_white_short = False
        self.castle_white_long = False
        self.castle_black_short = False
        self.castle_black_long = False
        self.n = 0

        letter_list = ["a","b","c","d","e","f","g","h"]
        num_list = [8,7,6,5,4,3,2,1]

        self.coords = []                          #The MAIN LIST where all the buttons along their coordinates are stored
        self.coords_dic = {}

        #For Placing 64 buttons
        for r in range(8):
            for c in range(8):
                but = Button(self.root,text='',height=4,width=9,command= lambda x=r,y=c: self.select(x,y))
                but.grid(row=r,column=c+1,sticky='nsew')
                self.coords.append((but,r,c))

        #For showing the number of rows on left
        for i in range(8):
            lab = Label(self.root,text=num_list[i])
            lab.grid(row=i,column=0)

        #For showing the letter of column at bottom
        for j in range(8):
            lab1 = Label(self.root,text=letter_list[j])
            lab1.grid(row=8,column=j+1)

        #For making a alternate colored grids like a chessboard
        for i in range(64):
            if (int(self.coords[i][1]) + int(self.coords[i][2])) % 2 !=0 :
                self.coords[i][0].configure(bg = self.initial_color,activebackground = self.initial_color)


        #Game should be disabled at beginning
        for i in range(64):
                self.coords[i][0].configure(state=DISABLED)

        self.piece = []                 # Stores all the details of the current selected piece


    def image(self):                               # The image of the piece
        self.image_code = [("white","pawn","pyimage1"),("black","pawn","pyimage2"),("white","horse","pyimage3"),("black","horse","pyimage4"),("white","bishop","pyimage5"),("black","bishop","pyimage6"),("white","rook","pyimage7"),("black","rook","pyimage8"),("white","queen","pyimage9"),("black","queen","pyimage10"),("white","king","pyimage11"),("black","king","pyimage12")]
        wpawn = Image.open('./Images/white_pawn.png')
        self.wpawn = ImageTk.PhotoImage(wpawn)
        for i in range(64):
            if self.coords[i][1]==6:
                self.coords[i][0].configure(image=self.wpawn,height=70,width=70)           # Creating the initial case for board

        bpawn = Image.open('./Images/black_pawn.png')
        self.bpawn = ImageTk.PhotoImage(bpawn)
        for i in range(64):
            if self.coords[i][1]==1:
                self.coords[i][0].configure(image=self.bpawn,height=70,width=70)
                print(self.coords[i][0]['image'])

        whorse = Image.open('./Images/white_knight.png')
        #whorse1 = whorse.resize((70,90))
        self.whorse=ImageTk.PhotoImage(whorse)
        for i in range(64):
            if self.coords[i][1]==7 and self.coords[i][2]==1 or self.coords[i][1]==7 and self.coords[i][2]==6:
                self.coords[i][0].configure(image=self.whorse,height=70,width=70)

        bhorse = Image.open('./Images/black_knight.png')
        self.bhorse = ImageTk.PhotoImage(bhorse)
        for i in range(64):
            if self.coords[i][1]==0 and self.coords[i][2]==1 or self.coords[i][1]==0 and self.coords[i][2]==6:
                self.coords[i][0].configure(image=self.bhorse,height=70,width=70)

        wbishop = Image.open('./Images/white_bishop.png')
        self.wbishop = ImageTk.PhotoImage(wbishop)
        for i in range(64):
            if self.coords[i][1]==7 and self.coords[i][2]==2 or self.coords[i][1]==7 and self.coords[i][2]==5:
                self.coords[i][0].configure(image=self.wbishop,height=70,width=70)

        bbishop = Image.open('./Images/black_bishop.png')
        #bbishop1 = bbishop.resize((70,90))
        self.bbishop = ImageTk.PhotoImage(bbishop)
        for i in range(64):
            if self.coords[i][1]==0 and self.coords[i][2]==2 or self.coords[i][1]==0 and self.coords[i][2]==5:
                self.coords[i][0].configure(image=self.bbishop,height=70,width=70)

        wrook = Image.open('./Images/white_rook.png')
        self.wrook = ImageTk.PhotoImage(wrook)
        for i in range(64):
            if self.coords[i][1]==7 and self.coords[i][2]==0 or self.coords[i][1]==7 and self.coords[i][2]==7:
                self.coords[i][0].configure(image=self.wrook,height=70,width=70)

        brook = Image.open('./Images/black_rook.png')
        self.brook = ImageTk.PhotoImage(brook)
        for i in range(64):
            if self.coords[i][1]==0 and self.coords[i][2]==0 or self.coords[i][1]==0 and self.coords[i][2]==7:
                self.coords[i][0].configure(image=self.brook,height=70,width=70)

        wqueen = Image.open('./Images/white_queen.png')
        self.wqueen = ImageTk.PhotoImage(wqueen)
        for i in range(64):
            if self.coords[i][1]==7 and self.coords[i][2]==3:
                self.coords[i][0].configure(image=self.wqueen,height=70,width=70)
        
        bqueen = Image.open('./Images/black_queen.png')
        self.bqueen = ImageTk.PhotoImage(bqueen)
        for i in range(64):
            if self.coords[i][1]==0 and self.coords[i][2]==3:
                self.coords[i][0].configure(image=self.bqueen,height=70,width=70)

        wking = Image.open('./Images/white_king.png')
        self.wking = ImageTk.PhotoImage(wking)
        for i in range(64):
            if self.coords[i][1]==7 and self.coords[i][2]==4:
                self.coords[i][0].configure(image=self.wking,height=70,width=70)

        bking = Image.open('./Images/black_king.png')
        self.bking = ImageTk.PhotoImage(bking)
        for i in range(64):
            if self.coords[i][1]==0 and self.coords[i][2]==4:
                self.coords[i][0].configure(image=self.bking,height=70,width=70)

        
        for i in range(64):
            self.coords_dic[i]=self.coords[i][0]['image']
        print(self.coords_dic)

    def select(self,r,c):
        for i in range(64):                                                 # This loop is basically for checking if a square with "O" or red bg has been selected or not
            if self.coords[i][1]==r and self.coords[i][2]==c:
                print(self.coords[i][0]['image'])
                print(self.coords[i][0]['text'])
                if self.coords[i][0]["text"]=="O" or self.coords[i][0]['bg']=='red':             # This condition is a condition in which the piece can be captured or moved accordingly
                    self.clear_marks()
                    self.move(r,c)
                    start_new_thread(self.receive,())

                    
                    
        '''for i in range(64):    
            if self.coords[i][0]["text"]=="O" or self.coords[i][0]['bg']=='red':             #Removes all the previous "O" and red buttons which were made by previous selections
                self.coords[i][0].configure(text='',bg='#f0f0f0') '''
        self.clear_marks()
        
        for i in range(64):                                                                      #This loop is basically for showing all the possible ways a selected piece can move(or capture) on the chess board
                if self.coords[i][1]==r and self.coords[i][2]==c:                                #Checking following conditions for a particular selected button / pice
                    if self.coords[i][0]['image']=='pyimage1' and self.n%2==0 and current_player==0:              #WHITE PAWN
                        self.piece.clear()
                        self.piece.append(self.coords[i])
                        print(self.piece)                                                        # Storing a piece info to use it later

                        for j in range(64):
                            if self.coords[j][1]==r-1 and self.coords[j][2]==c and self.coords[j][0]['image']=='':      # Giving specific conditions to a piece(a pawn here) to create "O" and red buttons (possible moves)
                                self.coords[j][0].configure(text="O")
                                
                            if self.coords[j][1]==r-2 and r-2==4 and self.coords[j][2]==c and self.coords[j][0]['image']=='':
                                self.coords[j][0].configure(text="O")


                            for k in range(len(self.image_code)):
                                if self.image_code[k][0]=="black":
                                    if self.coords[j][1]==r-1 and self.coords[j][2]==c+1 and self.coords[j][0]['image']==self.image_code[k][2]:
                                        self.coords[j][0].configure(bg='red',activebackground='red')
                                    if self.coords[j][1]==r-1 and self.coords[j][2]==c-1 and self.coords[j][0]['image']==self.image_code[k][2]:
                                        self.coords[j][0].configure(bg='red',activebackground='red')

                    if self.coords[i][0]['image']=='pyimage2' and self.n%2!=0 and current_player==1:               #BLACK PAWN             
                        self.piece.clear()
                        self.piece.append(self.coords[i])
                        print(self.piece)

                        for j in range(64):
                            if self.coords[j][1]==r+1 and self.coords[j][2]==c and self.coords[j][0]['image']=='':      # Giving specific conditions to a piece(a pawn here) to create "O" and red buttons (possible moves)
                                print(r+1,c)
                                print(self.coords[j][0]['text'])
                                self.coords[j][0]['text']="O"
                                print(self.coords[j][0]['text'])
                                print("ho raha hai bhai")

                            if self.coords[j][1]==r+2 and r+2==3 and self.coords[j][2]==c and self.coords[j][0]['image']=='':
                                self.coords[j][0].configure(text="O")

                                
                            for k in range(len(self.image_code)):
                                if self.image_code[k][0]=="white":
                                    if self.coords[j][1]==r+1 and self.coords[j][2]==c+1 and self.coords[j][0]['image']==self.image_code[k][2]:
                                        self.coords[j][0].configure(bg='red',activebackground='red')
                                    if self.coords[j][1]==r+1 and self.coords[j][2]==c-1 and self.coords[j][0]['image']==self.image_code[k][2]:
                                        self.coords[j][0].configure(bg='red',activebackground='red')


                        #for i in range(64):
                         #   if self.coords[i][1]==r+1 and self.coords[i][2]==c and self.coords[i][0]['image']==''

                    if self.coords[i][0]['image']=='pyimage3' and self.n%2==0 and current_player==0 or self.coords[i][0]['image']=='pyimage4' and self.n%2!=0 and current_player==1:       #KNIGHT
                        self.piece.clear()
                        self.piece.append(self.coords[i])
                        print(self.piece)

                        for j in range(64):
                            if self.coords[j][0]['image']=='':
                                if self.coords[j][1]==r-2 and self.coords[j][2]==c-1:
                                    self.coords[j][0].configure(text="O")
                                if self.coords[j][1]==r-2 and self.coords[j][2]==c+1:
                                    self.coords[j][0].configure(text="O")
                                if self.coords[j][1]==r+2 and self.coords[j][2]==c-1:
                                    self.coords[j][0].configure(text="O")
                                if self.coords[j][1]==r+2 and self.coords[j][2]==c+1:
                                    self.coords[j][0].configure(text="O")
                                if self.coords[j][1]==r-1 and self.coords[j][2]==c+2:
                                    self.coords[j][0].configure(text="O")
                                if self.coords[j][1]==r-1 and self.coords[j][2]==c-2:
                                    self.coords[j][0].configure(text="O")
                                if self.coords[j][1]==r+1 and self.coords[j][2]==c+2:
                                    self.coords[j][0].configure(text="O")
                                if self.coords[j][1]==r+1 and self.coords[j][2]==c-2:
                                    self.coords[j][0].configure(text="O")

                            for k in range(len(self.image_code)):
                                if self.image_code[k][0]=='black' and self.coords[i][0]['image']=='pyimage3' or self.image_code[k][0]=='white' and self.coords[i][0]['image']=='pyimage4':
                                    if self.coords[j][1]==r-2 and self.coords[j][2]==c-1 and self.coords[j][0]['image']==self.image_code[k][2]:
                                        self.coords[j][0].configure(bg='red',activebackground='red')
                                    if self.coords[j][1]==r-2 and self.coords[j][2]==c+1 and self.coords[j][0]['image']==self.image_code[k][2]:
                                        self.coords[j][0].configure(bg='red',activebackground='red')
                                    if self.coords[j][1]==r+2 and self.coords[j][2]==c-1 and self.coords[j][0]['image']==self.image_code[k][2]:
                                        self.coords[j][0].configure(bg='red',activebackground='red')
                                    if self.coords[j][1]==r+2 and self.coords[j][2]==c+1 and self.coords[j][0]['image']==self.image_code[k][2]:
                                        self.coords[j][0].configure(bg='red',activebackground='red')
                                    if self.coords[j][1]==r-1 and self.coords[j][2]==c+2 and self.coords[j][0]['image']==self.image_code[k][2]:
                                        self.coords[j][0].configure(bg='red',activebackground='red')
                                    if self.coords[j][1]==r-1 and self.coords[j][2]==c-2 and self.coords[j][0]['image']==self.image_code[k][2]:
                                        self.coords[j][0].configure(bg='red',activebackground='red')
                                    if self.coords[j][1]==r+1 and self.coords[j][2]==c+2 and self.coords[j][0]['image']==self.image_code[k][2]:
                                        self.coords[j][0].configure(bg='red',activebackground='red')
                                    if self.coords[j][1]==r+1 and self.coords[j][2]==c-2 and self.coords[j][0]['image']==self.image_code[k][2]:
                                        self.coords[j][0].configure(bg='red',activebackground='red')

                    if self.coords[i][0]['image']=='pyimage5' and self.n%2==0 and current_player==0 or self.coords[i][0]['image']=='pyimage6' and self.n%2!=0 and current_player==1:              #BISHOP
                        self.piece.clear()
                        self.piece.append(self.coords[i])
                        print(self.piece)

                        # 4 LISTS WHICH WILL HAVE COORDINATES ALONG EACH DIAGONAL FROM THE CURRENT POSITION OF THE BISHOP
                        ur_pg = []
                        br_pg = []
                        ul_pg = []
                        bl_pg = []

                        for j in range(63,-1,-1):                                 #ULTA LOOP FOR UPPER DIAGONALS
                            #if self.coords[j][0]['image']=='':
                                for k in range(1,9):
                                    if self.coords[j][1]==r-k and self.coords[j][2]==c+k:                    
                                        #self.coords[j][0].configure(text="O")                                   #### OK SO FIRST ITERATE AS GIVEN ON LEFT AND GET ALL POSSIBLE CORRDS WHERE BISHOP CAN MOVE
                                        ur_pg.append((self.coords[j][0],r-k,c+k))                      #### THEN GO THROUGH SIMILAR ITERATION AS SHOWN IN LEFT AGAIN BUT ADD ONE EXTRA CONDITION OF CHECKING AT WHAT POSITION THERE IS AN IMAGE
                                                                                                       #### IF AN IMAGE IS DETECTED, THEN ABOUT THAT COORDINATE, SLICE THE LIST AND PREVIOUS AND IMAGE KA COORD WHICH WILL HAVE "O" MARKS.
                                                                                                       #### MAKE 4 LISTS ONE FOR EACH DIRECTION
                                    if self.coords[j][1]==r-k and self.coords[j][2]==c-k:
                                        #self.coords[j][0].configure(text="O")
                                        ul_pg.append((self.coords[j][0],r-k,c-k))
                        for j in range(64):
                            for k in range(1,9):
                                if self.coords[j][1]==r+k and self.coords[j][2]==c+k:   
                                    #self.coords[j][0].configure(text="O") 
                                    br_pg.append((self.coords[j][0],r+k,c+k))   

                                if self.coords[j][1]==r+k and self.coords[j][2]==c-k:
                                    #self.coords[j][0].configure(text="O")
                                    bl_pg.append((self.coords[j][0],r+k,c-k))                
                        
                        # NOW THESE DIFFERENT 4 LISTS ARE THE FINAL LISTS WHICH WILL STORE THE FINAL POSSIBLE VALUES OF COORDINATES
                        l1=[]
                        l2=[]
                        l3=[]
                        l4=[]

                        for k in range(len(ur_pg)):            #THESE LOOPS WILL CHECK WHERE THERE IS IMAGE ALONG DIAGONAL, IF THERE IS THEN THE LOOP WILL APPEND ALL VALUES OF THE INITIAL LIST INTO THE FINAL LIST UNTILL THE COORDINATE OF THE IMAGE
                            if ur_pg[k][0]['image']=='':
                                l1.append(ur_pg[k])
                            else:
                                break
                        print(l1)

                        for k in range(len(br_pg)):
                            if br_pg[k][0]['image']=='':
                                l2.append(br_pg[k])
                            else:
                                break
                        print(l2)

                        for k in range(len(ul_pg)):
                            if ul_pg[k][0]['image']=='':
                                l3.append(ul_pg[k])
                            else:
                                break
                        print(l3)

                        for k in range(len(bl_pg)):
                            if bl_pg[k][0]['image']=='':
                                l4.append(bl_pg[k])
                            else:
                                break
                        print(l4)

                        for k in range(len(l1)):                         
                            l1[k][0].configure(text="O")
                        for k in range(len(l2)):
                            l2[k][0].configure(text="O")
                        for k in range(len(l3)):
                            l3[k][0].configure(text="O")
                        for k in range(len(l4)):
                            l4[k][0].configure(text="O")

                        for l in range(64):                        #ITERATING THROUGH FINAL LISTS
                            for k in range(len(self.image_code)):
                                if self.image_code[k][0]=='black' and self.coords[i][0]['image']=='pyimage5':
                                    if len(l1)!=0:
                                        if self.coords[l][1]==l1[len(l1)-1][1] - 1 and self.coords[l][2]==l1[len(l1)-1][2] + 1 and self.coords[l][0]['image']==self.image_code[k][2]:    ## Inn dono mai iske saath ek if condition do which states that if list l1,l2,l3,l4 are empty then current image ke index se diagnolly wale ko check karke kaat do
                                            self.coords[l][0].configure(bg='red',activebackground='red')
                                    if len(l2)!=0:
                                        if self.coords[l][1]==l2[len(l2)-1][1] + 1 and self.coords[l][2]==l2[len(l2)-1][2] + 1 and self.coords[l][0]['image']==self.image_code[k][2]:
                                            self.coords[l][0].configure(bg='red',activebackground='red')
                                    if len(l3)!=0:
                                        if self.coords[l][1]==l3[len(l3)-1][1] - 1 and self.coords[l][2]==l3[len(l3)-1][2] - 1 and self.coords[l][0]['image']==self.image_code[k][2]:
                                            self.coords[l][0].configure(bg='red',activebackground='red')
                                    if len(l4)!=0:
                                        if self.coords[l][1]==l4[len(l4)-1][1] + 1 and self.coords[l][2]==l4[len(l4)-1][2] - 1 and self.coords[l][0]['image']==self.image_code[k][2]:
                                           self.coords[l][0].configure(bg='red',activebackground='red')

                                    if len(l1)==0:
                                        if self.coords[l][1]==r-1 and self.coords[l][2]==c+1 and self.coords[l][0]['image']==self.image_code[k][2]:
                                            self.coords[l][0].configure(bg='red',activebackground='red')
                                    if len(l2)==0:
                                        if self.coords[l][1]==r+1 and self.coords[l][2]==c+1 and self.coords[l][0]['image']==self.image_code[k][2]:
                                            self.coords[l][0].configure(bg='red',activebackground='red')
                                    if len(l3)==0:
                                        if self.coords[l][1]==r-1 and self.coords[l][2]==c-1 and self.coords[l][0]['image']==self.image_code[k][2]:
                                            self.coords[l][0].configure(bg='red',activebackground='red')
                                    if len(l4)==0:
                                        if self.coords[l][1]==r+1 and self.coords[l][2]==c-1 and self.coords[l][0]['image']==self.image_code[k][2]:
                                            self.coords[l][0].configure(bg='red',activebackground='red')

                                if self.image_code[k][0]=='white' and self.coords[i][0]['image']=='pyimage6':
                                    if len(l1)!=0:
                                        if self.coords[l][1]==l1[len(l1)-1][1] - 1 and self.coords[l][2]==l1[len(l1)-1][2] + 1 and self.coords[l][0]['image']==self.image_code[k][2]:    ## Inn dono mai iske saath ek if condition do which states that if list l1,l2,l3,l4 are empty then current image ke index se diagnolly wale ko check karke kaat do
                                            self.coords[l][0].configure(bg='red',activebackground='red')
                                    if len(l2)!=0:
                                        if self.coords[l][1]==l2[len(l2)-1][1] + 1 and self.coords[l][2]==l2[len(l2)-1][2] + 1 and self.coords[l][0]['image']==self.image_code[k][2]:
                                            self.coords[l][0].configure(bg='red',activebackground='red')
                                    if len(l3)!=0:
                                        if self.coords[l][1]==l3[len(l3)-1][1] - 1 and self.coords[l][2]==l3[len(l3)-1][2] - 1 and self.coords[l][0]['image']==self.image_code[k][2]:
                                            self.coords[l][0].configure(bg='red',activebackground='red')
                                    if len(l4)!=0:
                                        if self.coords[l][1]==l4[len(l4)-1][1] + 1 and self.coords[l][2]==l4[len(l4)-1][2] - 1 and self.coords[l][0]['image']==self.image_code[k][2]:
                                           self.coords[l][0].configure(bg='red',activebackground='red')

                                    if len(l1)==0:
                                        if self.coords[l][1]==r-1 and self.coords[l][2]==c+1 and self.coords[l][0]['image']==self.image_code[k][2]:
                                            self.coords[l][0].configure(bg='red',activebackground='red')
                                    if len(l2)==0:
                                        if self.coords[l][1]==r+1 and self.coords[l][2]==c+1 and self.coords[l][0]['image']==self.image_code[k][2]:
                                            self.coords[l][0].configure(bg='red',activebackground='red')
                                    if len(l3)==0:
                                        if self.coords[l][1]==r-1 and self.coords[l][2]==c-1 and self.coords[l][0]['image']==self.image_code[k][2]:
                                            self.coords[l][0].configure(bg='red',activebackground='red')
                                    if len(l4)==0:
                                        if self.coords[l][1]==r+1 and self.coords[l][2]==c-1 and self.coords[l][0]['image']==self.image_code[k][2]:
                                            self.coords[l][0].configure(bg='red',activebackground='red')


                    if self.coords[i][0]['image']=='pyimage7' and self.n%2==0 and current_player==0 or self.coords[i][0]['image']=='pyimage8' and self.n%2!=0 and current_player==1:           #ROOK (HAVE DONE SIMILAR PROCEDURE AS BISHOP)
                        self.piece.clear()
                        self.piece.append(self.coords[i])
                        print(self.piece)

                        # 4 LISTS WHICH WILL HAVE COORDINATES ALONG EACH LINE FROM THE CURRENT POSITION OF THE ROOK
                        up_pg = []
                        down_pg = []
                        left_pg=[]
                        right_pg=[]

                        for j in range(63,-1,-1):                             #ULTA LOOP FOR PIECES WHICH HAVE TO BE CHECKED FROM BOTTOM
                            for k in range(1,9):
                                if self.coords[j][1]==r-k and self.coords[j][2]==c:
                                    up_pg.append((self.coords[j][0],r-k,c))
                                if self.coords[j][1]==r and self.coords[j][2]==c-k:
                                    left_pg.append((self.coords[j][0],r,c-k))

                        for j in range(64):
                            for k in range(1,9):
                                if self.coords[j][1]==r+k and self.coords[j][2]==c:
                                    down_pg.append((self.coords[j][0],r+k,c))
                                if self.coords[j][1]==r and self.coords[j][2]==c+k:
                                    right_pg.append((self.coords[j][0],r,c+k))

                        # NOW THESE DIFFERENT 4 LISTS ARE THE FINAL LISTS WHICH WILL STORE THE FINAL POSSIBLE VALUES OF COORDINATES
                        up1 = []
                        down1 = []
                        left1 = []
                        right1 = []

                        for k in range(len(up_pg)):                          #THESE LOOPS WILL CHECK WHERE THERE IS IMAGE ALONG DIAGONAL, IF THERE IS THEN THE LOOP WILL APPEND ALL VALUES OF THE INITIAL LIST INTO THE FINAL LIST UNTILL THE COORDINATE OF THE IMAGE
                            if up_pg[k][0]['image']=='':
                                up1.append(up_pg[k])
                            else:
                                break
                        print(up1)

                        for k in range(len(down_pg)):
                            if down_pg[k][0]['image']=='':
                                down1.append(down_pg[k])
                            else:
                                break
                        print(down1)

                        for k in range(len(left_pg)):
                            if left_pg[k][0]['image']=='':
                                left1.append(left_pg[k])
                            else:
                                break
                        print(left1)

                        for k in range(len(right_pg)):
                            if right_pg[k][0]['image']=='':
                                right1.append(right_pg[k])
                            else:
                                break
                        print(right1)

                        for k in range(len(up1)):
                            up1[k][0].configure(text="O")
                        for k in range(len(down1)):
                            down1[k][0].configure(text="O")
                        for k in range(len(left1)):
                            left1[k][0].configure(text="O")
                        for k in range(len(right1)):
                            right1[k][0].configure(text="O")

                        for j in range(64):
                            for k in range(len(self.image_code)):
                                if self.image_code[k][0]=='black' and self.coords[i][0]['image']=='pyimage7':
                                    if len(up1)!=0:
                                        if self.coords[j][1]==up1[len(up1)-1][1] - 1 and self.coords[j][2]==up1[len(up1)-1][2] and self.coords[j][0]['image']==self.image_code[k][2]:
                                            self.coords[j][0].configure(bg='red',activebackground='red')
                                    if len(down1)!=0:
                                        if self.coords[j][1]==down1[len(down1)-1][1] + 1 and self.coords[j][2]==down1[len(down1)-1][2] and self.coords[j][0]['image']==self.image_code[k][2]:
                                            self.coords[j][0].configure(bg='red',activebackground='red')
                                    if len(left1)!=0:
                                        if self.coords[j][1]==left1[len(left1)-1][1]  and self.coords[j][2]==left1[len(left1)-1][2]-1 and self.coords[j][0]['image']==self.image_code[k][2]:
                                            self.coords[j][0].configure(bg='red',activebackground='red')
                                    if len(right1)!=0:
                                        if self.coords[j][1]==right1[len(right1)-1][1]  and self.coords[j][2]==right1[len(right1)-1][2]+1 and self.coords[j][0]['image']==self.image_code[k][2]:
                                            self.coords[j][0].configure(bg='red',activebackground='red')
                                    
                                    if len(up1)==0:
                                        if self.coords[j][1]==r-1 and self.coords[j][2]==c and self.coords[j][0]['image']==self.image_code[k][2]:
                                            self.coords[j][0].configure(bg='red',activebackground='red')
                                    if len(down1)==0:
                                        if self.coords[j][1]==r+1 and self.coords[j][2]==c and self.coords[j][0]['image']==self.image_code[k][2]:
                                            self.coords[j][0].configure(bg='red',activebackground='red')
                                    if len(left1)==0:
                                        if self.coords[j][1]==r and self.coords[j][2]==c-1 and self.coords[j][0]['image']==self.image_code[k][2]:
                                            self.coords[j][0].configure(bg='red',activebackground='red')
                                    if len(right1)==0:
                                        if self.coords[j][1]==r and self.coords[j][2]==c+1 and self.coords[j][0]['image']==self.image_code[k][2]:
                                            self.coords[j][0].configure(bg='red',activebackground='red')
                                
                                if self.image_code[k][0]=='white' and self.coords[i][0]['image']=='pyimage8':
                                    if len(up1)!=0:
                                        if self.coords[j][1]==up1[len(up1)-1][1] - 1 and self.coords[j][2]==up1[len(up1)-1][2] and self.coords[j][0]['image']==self.image_code[k][2]:
                                            self.coords[j][0].configure(bg='red',activebackground='red')
                                    if len(down1)!=0:
                                        if self.coords[j][1]==down1[len(down1)-1][1] + 1 and self.coords[j][2]==down1[len(down1)-1][2] and self.coords[j][0]['image']==self.image_code[k][2]:
                                            self.coords[j][0].configure(bg='red',activebackground='red')
                                    if len(left1)!=0:
                                        if self.coords[j][1]==left1[len(left1)-1][1]  and self.coords[j][2]==left1[len(left1)-1][2] - 1 and self.coords[j][0]['image']==self.image_code[k][2]:
                                            self.coords[j][0].configure(bg='red',activebackground='red')
                                    if len(right1)!=0:
                                        if self.coords[j][1]==right1[len(right1)-1][1]  and self.coords[j][2]==right1[len(right1)-1][2] + 1 and self.coords[j][0]['image']==self.image_code[k][2]:
                                            self.coords[j][0].configure(bg='red',activebackground='red')
                                    
                                    if len(up1)==0:
                                        if self.coords[j][1]==r-1 and self.coords[j][2]==c and self.coords[j][0]['image']==self.image_code[k][2]:
                                            self.coords[j][0].configure(bg='red',activebackground='red')
                                    if len(down1)==0:
                                        if self.coords[j][1]==r+1 and self.coords[j][2]==c and self.coords[j][0]['image']==self.image_code[k][2]:
                                            self.coords[j][0].configure(bg='red',activebackground='red')
                                    if len(left1)==0:
                                        if self.coords[j][1]==r and self.coords[j][2]==c-1 and self.coords[j][0]['image']==self.image_code[k][2]:
                                            self.coords[j][0].configure(bg='red',activebackground='red')
                                    if len(right1)==0:
                                        if self.coords[j][1]==r and self.coords[j][2]==c+1 and self.coords[j][0]['image']==self.image_code[k][2]:
                                            self.coords[j][0].configure(bg='red',activebackground='red')
                    if self.coords[i][0]['image']=='pyimage9' and self.n%2==0 and current_player==0 or self.coords[i][0]['image']=='pyimage10' and self.n%2!=0 and current_player==1:             #QUEEN (HAVE DONE SIMILAR PROCEDURE AS BISHOP AND ROOK)
                        self.piece.clear()
                        self.piece.append(self.coords[i])
                        print(self.piece)

                        #ALL POSSIBLE DIRECTIONS
                        up_q = []
                        down_q = []
                        left_q = []
                        right_q = []
                        up_right = []
                        down_right = []
                        up_left = []
                        down_left = []

                        for j in range(63,-1,-1):
                                for k in range(1,9):
                                    if self.coords[j][1]==r-k and self.coords[j][2]==c:
                                        up_q.append((self.coords[j][0],r-k,c))
                                    if self.coords[j][1]==r and self.coords[j][2]==c-k:
                                        left_q.append((self.coords[j][0],r,c-k))
                                    if self.coords[j][1]==r-k and self.coords[j][2]==c+k:
                                        up_right.append((self.coords[j][0],r-k,c+k))
                                    if self.coords[j][1]==r-k and self.coords[j][2]==c-k:
                                        up_left.append((self.coords[j][0],r-k,c-k))

                        for j in range(64):
                            for k in range(1,9):
                                    if self.coords[j][1]==r+k and self.coords[j][2]==c:
                                        down_q.append((self.coords[j][0],r+k,c))
                                    if self.coords[j][1]==r and self.coords[j][2]==c+k:
                                        right_q.append((self.coords[j][0],r,c+k))
                                    if self.coords[j][1]==r+k and self.coords[j][2]==c+k:   
                                        down_right.append((self.coords[j][0],r+k,c+k))   
                                    if self.coords[j][1]==r+k and self.coords[j][2]==c-k:
                                        down_left.append((self.coords[j][0],r+k,c-k))  

                        up_q1 = []
                        down_q1 = []
                        left_q1 = []
                        right_q1 = []
                        up_right1 = []
                        down_right1 = []
                        up_left1 = []
                        down_left1 = []

                        for k in range(len(up_q)):
                            if up_q[k][0]['image']=='':
                                up_q1.append(up_q[k])
                            else:
                                break
                        print(up_q1)

                        for k in range(len(down_q)):
                            if down_q[k][0]['image']=='':
                                down_q1.append(down_q[k])
                            else:
                                break
                        print(down_q1)

                        for k in range(len(left_q)):
                            if left_q[k][0]['image']=='':
                                left_q1.append(left_q[k])
                            else:
                                break
                        print(left_q1)

                        for k in range(len(right_q)):
                            if right_q[k][0]['image']=='':
                                right_q1.append(right_q[k])
                            else:
                                break
                        print(right_q1)

                        for k in range(len(up_right)):
                            if up_right[k][0]['image']=='':
                                up_right1.append(up_right[k])
                            else:
                                break
                        print(up_right1)

                        for k in range(len(down_right)):
                            if down_right[k][0]['image']=='':
                                down_right1.append(down_right[k])
                            else:
                                break
                        print(down_right1)

                        for k in range(len(up_left)):
                            if up_left[k][0]['image']=='':
                                up_left1.append(up_left[k])
                            else:
                                break
                        print(up_left1)

                        for k in range(len(down_left)):
                            if down_left[k][0]['image']=='':
                                down_left1.append(down_left[k])
                            else:
                                break
                        print(down_left1)

                        for k in range(len(up_q1)):
                            up_q1[k][0].configure(text="O")
                        for k in range(len(down_q1)):
                            down_q1[k][0].configure(text="O")
                        for k in range(len(left_q1)):
                            left_q1[k][0].configure(text="O")
                        for k in range(len(right_q1)):
                            right_q1[k][0].configure(text="O")
                        for k in range(len(up_right1)):
                            up_right1[k][0].configure(text="O")
                        for k in range(len(up_left1)):
                            up_left1[k][0].configure(text="O")
                        for k in range(len(down_right1)):
                            down_right1[k][0].configure(text="O")
                        for k in range(len(down_left1)):
                            down_left1[k][0].configure(text="O")

                        for j in range(64):
                            for k in range(len(self.image_code)):
                                if self.image_code[k][0]=='black' and self.coords[i][0]['image']=='pyimage9':
                                    if len(up_q1)!=0:
                                        if self.coords[j][1]==up_q1[len(up_q1)-1][1] - 1 and self.coords[j][2]==up_q1[len(up_q1)-1][2] and self.coords[j][0]['image']==self.image_code[k][2]:
                                            self.coords[j][0].configure(bg='red',activebackground='red')
                                    if len(down_q1)!=0:
                                        if self.coords[j][1]==down_q1[len(down_q1)-1][1] + 1 and self.coords[j][2]==down_q1[len(down_q1)-1][2] and self.coords[j][0]['image']==self.image_code[k][2]:
                                            self.coords[j][0].configure(bg='red',activebackground='red')
                                    if len(left_q1)!=0:
                                        if self.coords[j][1]==left_q1[len(left_q1)-1][1]  and self.coords[j][2]==left_q1[len(left_q1)-1][2]-1 and self.coords[j][0]['image']==self.image_code[k][2]:
                                            self.coords[j][0].configure(bg='red',activebackground='red')
                                    if len(right_q1)!=0:
                                        if self.coords[j][1]==right_q1[len(right_q1)-1][1]  and self.coords[j][2]==right_q1[len(right_q1)-1][2]+1 and self.coords[j][0]['image']==self.image_code[k][2]:
                                            self.coords[j][0].configure(bg='red',activebackground='red')
                                    if len(up_right1)!=0:
                                        if self.coords[j][1]==up_right1[len(up_right1)-1][1] - 1 and self.coords[j][2]==up_right1[len(up_right1)-1][2] + 1 and self.coords[j][0]['image']==self.image_code[k][2]:    ## Inn dono mai iske saath ek if condition do which states that if list l1,l2,l3,l4 are empty then current image ke index se diagnolly wale ko check karke kaat do
                                            self.coords[j][0].configure(bg='red',activebackground='red')
                                    if len(down_right1)!=0:
                                        if self.coords[j][1]==down_right1[len(down_right1)-1][1] + 1 and self.coords[j][2]==down_right1[len(down_right1)-1][2] + 1 and self.coords[j][0]['image']==self.image_code[k][2]:
                                            self.coords[j][0].configure(bg='red',activebackground='red')
                                    if len(up_left1)!=0:
                                        if self.coords[j][1]==up_left1[len(up_left1)-1][1] - 1 and self.coords[j][2]==up_left1[len(up_left1)-1][2] - 1 and self.coords[j][0]['image']==self.image_code[k][2]:
                                            self.coords[j][0].configure(bg='red',activebackground='red')
                                    if len(down_left1)!=0:
                                        if self.coords[j][1]==down_left1[len(down_left1)-1][1] + 1 and self.coords[j][2]==down_left1[len(down_left1)-1][2] - 1 and self.coords[j][0]['image']==self.image_code[k][2]:
                                           self.coords[j][0].configure(bg='red',activebackground='red')

                                    
                                    if len(up_q1)==0:
                                        if self.coords[j][1]==r-1 and self.coords[j][2]==c and self.coords[j][0]['image']==self.image_code[k][2]:
                                            self.coords[j][0].configure(bg='red',activebackground='red')
                                    if len(down_q1)==0:
                                        if self.coords[j][1]==r+1 and self.coords[j][2]==c and self.coords[j][0]['image']==self.image_code[k][2]:
                                            self.coords[j][0].configure(bg='red',activebackground='red')
                                    if len(left_q1)==0:
                                        if self.coords[j][1]==r and self.coords[j][2]==c-1 and self.coords[j][0]['image']==self.image_code[k][2]:
                                            self.coords[j][0].configure(bg='red',activebackground='red')
                                    if len(right_q1)==0:
                                        if self.coords[j][1]==r and self.coords[j][2]==c+1 and self.coords[j][0]['image']==self.image_code[k][2]:
                                            self.coords[j][0].configure(bg='red',activebackground='red')
                                    if len(up_right1)==0:
                                        if self.coords[j][1]==r-1 and self.coords[j][2]==c+1 and self.coords[j][0]['image']==self.image_code[k][2]:
                                            self.coords[j][0].configure(bg='red',activebackground='red')
                                    if len(down_right1)==0:
                                        if self.coords[j][1]==r+1 and self.coords[j][2]==c+1 and self.coords[j][0]['image']==self.image_code[k][2]:
                                            self.coords[j][0].configure(bg='red',activebackground='red')
                                    if len(up_left1)==0:
                                        if self.coords[j][1]==r-1 and self.coords[j][2]==c-1 and self.coords[j][0]['image']==self.image_code[k][2]:
                                            self.coords[j][0].configure(bg='red',activebackground='red')
                                    if len(down_left1)==0:
                                        if self.coords[j][1]==r+1 and self.coords[j][2]==c-1 and self.coords[j][0]['image']==self.image_code[k][2]:
                                            self.coords[j][0].configure(bg='red',activebackground='red')

                                            
                                if self.image_code[k][0]=='white' and self.coords[i][0]['image']=='pyimage10':
                                    if len(up_q1)!=0:
                                        if self.coords[j][1]==up_q1[len(up_q1)-1][1] - 1 and self.coords[j][2]==up_q1[len(up_q1)-1][2] and self.coords[j][0]['image']==self.image_code[k][2]:
                                            self.coords[j][0].configure(bg='red',activebackground='red')
                                    if len(down_q1)!=0:
                                        if self.coords[j][1]==down_q1[len(down_q1)-1][1] + 1 and self.coords[j][2]==down_q1[len(down_q1)-1][2] and self.coords[j][0]['image']==self.image_code[k][2]:
                                            self.coords[j][0].configure(bg='red',activebackground='red')
                                    if len(left_q1)!=0:
                                        if self.coords[j][1]==left_q1[len(left_q1)-1][1]  and self.coords[j][2]==left_q1[len(left_q1)-1][2]-1 and self.coords[j][0]['image']==self.image_code[k][2]:
                                            self.coords[j][0].configure(bg='red',activebackground='red')
                                    if len(right_q1)!=0:
                                        if self.coords[j][1]==right_q1[len(right_q1)-1][1]  and self.coords[j][2]==right_q1[len(right_q1)-1][2]+1 and self.coords[j][0]['image']==self.image_code[k][2]:
                                            self.coords[j][0].configure(bg='red',activebackground='red')
                                    if len(up_right1)!=0:
                                        if self.coords[j][1]==up_right1[len(up_right1)-1][1] - 1 and self.coords[j][2]==up_right1[len(up_right1)-1][2] + 1 and self.coords[j][0]['image']==self.image_code[k][2]:    ## Inn dono mai iske saath ek if condition do which states that if list l1,l2,l3,l4 are empty then current image ke index se diagnolly wale ko check karke kaat do
                                            self.coords[j][0].configure(bg='red',activebackground='red')
                                    if len(down_right1)!=0:
                                        if self.coords[j][1]==down_right1[len(down_right1)-1][1] + 1 and self.coords[j][2]==down_right1[len(down_right1)-1][2] + 1 and self.coords[j][0]['image']==self.image_code[k][2]:
                                            self.coords[j][0].configure(bg='red',activebackground='red')
                                    if len(up_left1)!=0:
                                        if self.coords[j][1]==up_left1[len(up_left1)-1][1] - 1 and self.coords[j][2]==up_left1[len(up_left1)-1][2] - 1 and self.coords[j][0]['image']==self.image_code[k][2]:
                                            self.coords[j][0].configure(bg='red',activebackground='red')
                                    if len(down_left1)!=0:
                                        if self.coords[j][1]==down_left1[len(down_left1)-1][1] + 1 and self.coords[j][2]==down_left1[len(down_left1)-1][2] - 1 and self.coords[j][0]['image']==self.image_code[k][2]:
                                           self.coords[j][0].configure(bg='red',activebackground='red')

                                    
                                    if len(up_q1)==0:
                                        if self.coords[j][1]==r-1 and self.coords[j][2]==c and self.coords[j][0]['image']==self.image_code[k][2]:
                                            self.coords[j][0].configure(bg='red',activebackground='red')
                                    if len(down_q1)==0:
                                        if self.coords[j][1]==r+1 and self.coords[j][2]==c and self.coords[j][0]['image']==self.image_code[k][2]:
                                            self.coords[j][0].configure(bg='red',activebackground='red')
                                    if len(left_q1)==0:
                                        if self.coords[j][1]==r and self.coords[j][2]==c-1 and self.coords[j][0]['image']==self.image_code[k][2]:
                                            self.coords[j][0].configure(bg='red',activebackground='red')
                                    if len(right_q1)==0:
                                        if self.coords[j][1]==r and self.coords[j][2]==c+1 and self.coords[j][0]['image']==self.image_code[k][2]:
                                            self.coords[j][0].configure(bg='red',activebackground='red')
                                    if len(up_right1)==0:
                                        if self.coords[j][1]==r-1 and self.coords[j][2]==c+1 and self.coords[j][0]['image']==self.image_code[k][2]:
                                            self.coords[j][0].configure(bg='red',activebackground='red')
                                    if len(down_right1)==0:
                                        if self.coords[j][1]==r+1 and self.coords[j][2]==c+1 and self.coords[j][0]['image']==self.image_code[k][2]:
                                            self.coords[j][0].configure(bg='red',activebackground='red')
                                    if len(up_left1)==0:
                                        if self.coords[j][1]==r-1 and self.coords[j][2]==c-1 and self.coords[j][0]['image']==self.image_code[k][2]:
                                            self.coords[j][0].configure(bg='red',activebackground='red')
                                    if len(down_left1)==0:
                                        if self.coords[j][1]==r+1 and self.coords[j][2]==c-1 and self.coords[j][0]['image']==self.image_code[k][2]:
                                            self.coords[j][0].configure(bg='red',activebackground='red')

                    if self.coords[i][0]['image']=='pyimage11' and self.n%2==0 and current_player==0 or self.coords[i][0]['image']=='pyimage12' and self.n%2!=0 and current_player==1:           #KINGS
                        self.piece.clear()
                        self.piece.append(self.coords[i])
                        print(self.piece)

                        for j in range(64):
                            if self.coords[j][1]==r-1 and self.coords[j][2]==c and self.coords[j][0]['image']=='':
                                self.coords[j][0].configure(text="O")
                            if self.coords[j][1]==r-1 and self.coords[j][2]==c-1 and self.coords[j][0]['image']=='':
                                self.coords[j][0].configure(text="O")
                            if self.coords[j][1]==r-1 and self.coords[j][2]==c+1 and self.coords[j][0]['image']=='':
                                self.coords[j][0].configure(text="O")
                            if self.coords[j][1]==r and self.coords[j][2]==c-1 and self.coords[j][0]['image']=='':
                                self.coords[j][0].configure(text="O")
                            if self.coords[j][1]==r and self.coords[j][2]==c+1 and self.coords[j][0]['image']=='':
                                self.coords[j][0].configure(text="O")
                            if self.coords[j][1]==r+1 and self.coords[j][2]==c-1 and self.coords[j][0]['image']=='':
                                self.coords[j][0].configure(text="O")
                            if self.coords[j][1]==r+1 and self.coords[j][2]==c and self.coords[j][0]['image']=='':
                                self.coords[j][0].configure(text="O")
                            if self.coords[j][1]==r+1 and self.coords[j][2]==c+1 and self.coords[j][0]['image']=='':
                                self.coords[j][0].configure(text="O")

                            #Castle
                            if self.coords[i][1]==7 and self.coords[i][2]==4 and self.coords[i][0]['image']=='pyimage11':
                                if self.coords[63][0]['image']=='pyimage7' and self.castle_white_short!=-1:
                                    if self.coords[j][1]==r and self.coords[j][2]==c+2 and self.coords[j][0]['image']=='' and self.coords[j-1][0]['image']=='':
                                        self.coords[j][0].configure(text="O")
                                        self.castle_white_short = True

                                if self.coords[56][0]['image']=='pyimage7' and self.castle_white_long!=-1:
                                    if self.coords[j][1]==r and self.coords[j][2]==c-2 and self.coords[j][0]['image']=='' and self.coords[j+1][0]['image']=='' and self.coords[j-1][0]['image']=='':
                                        self.coords[j][0].configure(text="O")
                                        self.castle_white_long = True

                            if self.coords[i][1]==0 and self.coords[i][2]==4 and self.coords[i][0]['image']=='pyimage12':
                                if self.coords[7][0]['image']=='pyimage8' and self.castle_black_short!=-1:
                                    if self.coords[j][1]==r and self.coords[j][2]==c+2 and self.coords[j][0]['image']=='' and self.coords[j-1][0]['image']=='':
                                        self.coords[j][0].configure(text="O")
                                        self.castle_black_short = True

                                if self.coords[0][0]['image']=='pyimage8' and self.castle_black_long!=-1:
                                    if self.coords[j][1]==r and self.coords[j][2]==c-2 and self.coords[j][0]['image']=='' and self.coords[j+1][0]['image']=='' and self.coords[j-1][0]['image']=='':
                                        self.coords[j][0].configure(text="O")
                                        self.castle_black_long = True


                            
                            for k in range(len(self.image_code)):
                                if self.image_code[k][0]=='black' and self.coords[i][0]['image']=='pyimage11':
                                    if self.coords[j][1]==r-1 and self.coords[j][2]==c and self.coords[j][0]['image']==self.image_code[k][2]:
                                        self.coords[j][0].configure(bg='red',activebackground='red')
                                    if self.coords[j][1]==r-1 and self.coords[j][2]==c-1 and self.coords[j][0]['image']==self.image_code[k][2]:
                                        self.coords[j][0].configure(bg='red',activebackground='red')
                                    if self.coords[j][1]==r-1 and self.coords[j][2]==c+1 and self.coords[j][0]['image']==self.image_code[k][2]:
                                        self.coords[j][0].configure(bg='red',activebackground='red')
                                    if self.coords[j][1]==r and self.coords[j][2]==c-1 and self.coords[j][0]['image']==self.image_code[k][2]:
                                        self.coords[j][0].configure(bg='red',activebackground='red')
                                    if self.coords[j][1]==r and self.coords[j][2]==c+1 and self.coords[j][0]['image']==self.image_code[k][2]:
                                        self.coords[j][0].configure(bg='red',activebackground='red')
                                    if self.coords[j][1]==r+1 and self.coords[j][2]==c and self.coords[j][0]['image']==self.image_code[k][2]:
                                        self.coords[j][0].configure(bg='red',activebackground='red')
                                    if self.coords[j][1]==r+1 and self.coords[j][2]==c-1 and self.coords[j][0]['image']==self.image_code[k][2]:
                                        self.coords[j][0].configure(bg='red',activebackground='red')
                                    if self.coords[j][1]==r+1 and self.coords[j][2]==c+1 and self.coords[j][0]['image']==self.image_code[k][2]:
                                        self.coords[j][0].configure(bg='red',activebackground='red')
                                if self.image_code[k][0]=='white' and self.coords[i][0]['image']=='pyimage12':
                                    if self.coords[j][1]==r-1 and self.coords[j][2]==c and self.coords[j][0]['image']==self.image_code[k][2]:
                                        self.coords[j][0].configure(bg='red',activebackground='red')
                                    if self.coords[j][1]==r-1 and self.coords[j][2]==c-1 and self.coords[j][0]['image']==self.image_code[k][2]:
                                        self.coords[j][0].configure(bg='red',activebackground='red')
                                    if self.coords[j][1]==r-1 and self.coords[j][2]==c+1 and self.coords[j][0]['image']==self.image_code[k][2]:
                                        self.coords[j][0].configure(bg='red',activebackground='red')
                                    if self.coords[j][1]==r and self.coords[j][2]==c-1 and self.coords[j][0]['image']==self.image_code[k][2]:
                                        self.coords[j][0].configure(bg='red',activebackground='red')
                                    if self.coords[j][1]==r and self.coords[j][2]==c+1 and self.coords[j][0]['image']==self.image_code[k][2]:
                                        self.coords[j][0].configure(bg='red',activebackground='red')
                                    if self.coords[j][1]==r+1 and self.coords[j][2]==c and self.coords[j][0]['image']==self.image_code[k][2]:
                                        self.coords[j][0].configure(bg='red',activebackground='red')
                                    if self.coords[j][1]==r+1 and self.coords[j][2]==c-1 and self.coords[j][0]['image']==self.image_code[k][2]:
                                        self.coords[j][0].configure(bg='red',activebackground='red')
                                    if self.coords[j][1]==r+1 and self.coords[j][2]==c+1 and self.coords[j][0]['image']==self.image_code[k][2]:
                                        self.coords[j][0].configure(bg='red',activebackground='red')

                    
                            



    def move(self,r,c):           #This function basically moves the paricular piece 
        self.n = self.n + 1       #This will help maintain alternate chances of white and black piece player
        print(self.piece)
        for i in range(64):
            #self.coords[i][0].configure(state=ACTIVE)
            if self.coords[i][1]==r and self.coords[i][2]==c:                    #Placing the piece on the selected "O" or capture
                if (int(self.coords[i][1]) + int(self.coords[i][2])) % 2 !=0 :    
                    self.coords[i][0].configure(text='',image=self.piece[0][0]['image'],height=70,width=70,bg=self.initial_color,activebackground = self.initial_color)        #Moving the previous image on the new coordinates
                else:
                    self.coords[i][0].configure(text='',image=self.piece[0][0]['image'],height=70,width=70,bg='#f0f0f0')
        self.piece[0][0].configure(image='',height=4,width=9)          #Deleting the image on previous coordinates
        
        
        if self.castle_white_short == True and self.coords[62][0]['image']=='pyimage11':
            self.coords[61][0].configure(image='pyimage7',height=70,width=70)
            self.coords[63][0].configure(image='',height=4,width=9)
            self.castle_white_short = -1
            self.castle_white_long = -1

        if self.castle_white_long == True and self.coords[58][0]['image']=='pyimage11':
            self.coords[59][0].configure(image='pyimage7',height=70,width=70)
            self.coords[56][0].configure(image='',height=4,width=9)
            self.castle_white_long = -1
            self.castle_white_short = -1

        if self.castle_black_short==True and self.coords[6][0]['image']=='pyimage12':
            self.coords[5][0].configure(image='pyimage8',height=70,width=70)
            self.coords[7][0].configure(image='',height=4,width=9)
            self.castle_black_short = -1
            self.castle_black_long = -1

        if self.castle_black_long==True and self.coords[2][0]['image']=='pyimage12':
            self.coords[3][0].configure(image='pyimage8',height=70,width=70)
            self.coords[0][0].configure(image='',height=4,width=9)
            self.castle_black_short = -1
            self.castle_black_long = -1

        if self.coords[60][0]['image']=='':
            self.castle_white_short = -1
            self.castle_white_long = -1

        if self.coords[4][0]['image']=='':
            self.castle_black_short = -1
            self.castle_black_long = -1
        #Called these functions here cz they have to be checked after every move
        #net.send(self.coords)
        #data_to_be_sent = pickle.dumps(self.coords)
        #net.send(data_to_be_sent)
        self.pawn_promotion()
        self.winner()

        for i in range(64):
            self.coords_dic[i] = self.coords[i][0]['image']
        
        data = pickle.dumps(self.coords_dic)
        net.send(data)

    def receive(self):
        print(net.recv_data)
        net.receive()
        if type(net.recv_data)==dict:
            self.coords_dic = net.recv_data
            for i in range(64):
                if self.coords_dic[i]=='':
                    self.coords[i][0].configure(height=4,width=9,image='')
                else:
                    self.coords[i][0].configure(height=70,width=70,image=self.coords_dic[i])
        self.n = self.n + 1
        start_new_thread(self.receive,())
        
                    
    def pawn_promotion(self):
        for i in range(64):
            if self.coords[i][0]['image']=='pyimage1' and self.coords[i][1]==0 or self.coords[i][0]['image']=='pyimage2' and self.coords[i][1]==7:
                self.top = Toplevel(self.root)
                but1 = Button(self.top,text="Queen",command=lambda: self.pawn_promote('queen'))
                but1.grid(row=0,column=0)
                but2 = Button(self.top,text="Bishop",command= lambda: self.pawn_promote('bishop'))
                but2.grid(row=0,column=1)
                but3 = Button(self.top,text="Rook",command= lambda: self.pawn_promote('rook'))
                but3.grid(row=1,column=0)
                but4 = Button(self.top,text="Knight",command= lambda: self.pawn_promote('knight'))
                but4.grid(row=1,column=1)


    def pawn_promote(self,piece):
        for i in range(64):
            if self.coords[i][0]['image']=='pyimage1' and self.coords[i][1]==0:
                if piece=='queen':        #If you select a button of particular piece name , the pawn promotes to that piece
                    self.coords[i][0]['image']=''
                    self.coords[i][0]['image']='pyimage9'
                if piece=='bishop':
                    self.coords[i][0]['image']=''
                    self.coords[i][0]['image']='pyimage5'
                if piece=='rook':
                    self.coords[i][0]['image']=''
                    self.coords[i][0]['image']='pyimage7'
                if piece=='knight':
                    self.coords[i][0]['image']=''
                    self.coords[i][0]['image']='pyimage3'

            if self.coords[i][0]['image']=='pyimage2' and self.coords[i][1]==7:
                if piece=='queen':
                    self.coords[i][0]['image']=''
                    self.coords[i][0]['image']='pyimage10'
                if piece=='bishop':
                    self.coords[i][0]['image']=''
                    self.coords[i][0]['image']='pyimage6'
                if piece=='rook':
                    self.coords[i][0]['image']=''
                    self.coords[i][0]['image']='pyimage8'
                if piece=='knight':
                    self.coords[i][0]['image']=''
                    self.coords[i][0]['image']='pyimage4'

        self.top.destroy()



    def clear_marks(self):         #Function for clearing all previous "O" and red
        for i in range(64):
            if self.coords[i][0]['text']=="O" or self.coords[i][0]['bg']=='red':
                if (int(self.coords[i][1]) + int(self.coords[i][2])) % 2 !=0 :
                    self.coords[i][0].configure(text='',bg=self.initial_color,activebackground=self.initial_color)
                else:
                    self.coords[i][0].configure(text='',bg='#f0f0f0',activebackground='#f0f0f0')

    def time_grid(self):           #Function for maintaining the timer
        self.time_hourw = 10
        self.time_minw = 00
        self.time_minb = 00
        self.time_hourb = 10
        self.lab_white1 = Label(self.root,text=self.time_hourw)
        self.lab_white1.grid(row=8,column=9)
        self.lab_white2 = Label(self.root,text=":")
        self.lab_white2.grid(row=8,column=10)
        self.lab_white3 = Label(self.root,text=self.time_minw)
        self.lab_white3.grid(row=8,column=11)

        self.lab_black1 = Label(self.root,text=self.time_hourb)
        self.lab_black1.grid(row=0,column=9)
        self.lab_black2 = Label(self.root,text=":")
        self.lab_black2.grid(row=0,column=10)
        self.lab_black3 = Label(self.root,text=self.time_minb)
        self.lab_black3.grid(row=0,column=11)


        self.timer()


    def timer(self):           
        if self.n%2==0:
            if self.time_minw==0:
                self.time_hourw = self.time_hourw - 1
                self.time_minw = 59
            else:
                self.time_minw = self.time_minw - 1
            
            self.lab_white1['text'] = self.time_hourw
            self.lab_white3['text'] = self.time_minw


        else:
            if self.time_minb==0:
                self.time_hourb = self.time_hourb - 1
                self.time_minb = 59
            else:
                self.time_minb = self.time_minb - 1
            
            self.lab_black1['text'] = self.time_hourb
            self.lab_black3['text'] = self.time_minb

        if self.time_minw==0 and self.time_hourw==0:
            self.response= True
            self.block()
            messagebox.showinfo("Chess Game","Black has won the game on time")

        if self.time_minb==0 and self.time_hourb==0:
            self.response= True
            self.block()
            messagebox.showinfo("Chess Game","White has won the game on time")

        if self.response==False or self.coords[0][0]['state']==ACTIVE:
            self.root.after(1000,self.timer)



    def winner(self):
        images=[]
        for i in range(64):
            if self.coords[i][0]['image']!='' and self.coords[i][0]['image'] not in images:
                images.append(self.coords[i][0]['image'])
        if 'pyimage12' not in images:
            messagebox.showinfo("Chess Game","White has checkmated Black and won")
            self.response = True
            self.block()
        if 'pyimage11' not in images:
            messagebox.showinfo("Chess Game","Black has checkmated White and won")
            self.response = True
            self.block()

    def block(self):
            for i in range(64):
                self.coords[i][0].configure(state=DISABLED)

    def active(self):
        for i in range(64):
            self.coords[i][0].configure(state=ACTIVE)

    def menu(self):
        my_menu = Menu(self.root)
        self.root.configure(menu=my_menu)
        game_menu = Menu(my_menu)
        game_mode_menu = Menu(game_menu)
        my_menu.add_cascade(label = "Game",menu=game_menu)


        game_menu.add_cascade(label="Game Mode",menu=game_mode_menu)
        game_mode_menu.add_command(label="Rapid (10 Min)",command=self.game_mode_rapid)
        game_mode_menu.add_command(label="Bullet (1 Min)",command=self.game_mode_bullet)
        game_mode_menu.add_command(label="30 Mins",command=self.game_mode_30)
        #game_menu.add_command(label="Game Mode")
        game_menu.add_command(label = "Change Board Color",command=self.color)
        game_menu.add_command(label="Exit",command=self.root.destroy)

    def game_mode_rapid(self):
        self.time_hourw = 10
        self.time_minw = 00
        self.time_minb = 00
        self.time_hourb = 10
        self.active()
        self.response = False
        self.timer()

    def game_mode_bullet(self):
        self.time_hourw = 1
        self.time_minw = 00
        self.time_minb = 00
        self.time_hourb = 1
        self.active()
        self.response = False
        self.timer()

    def game_mode_30(self):
        self.time_hourw = 30
        self.time_minw = 00
        self.time_minb = 00
        self.time_hourb = 30
        self.active()
        self.response = False
        self.timer()

    def color(self):
        top = Toplevel()
        lab1 = Label(top,text="Enter Grid Color Code you want: ")
        lab1.grid(row=0,column=0)

        e1 = Entry(top,width=10)
        e1.grid(row=0,column=1)

        def save():
            if e1.get()!='':
                self.new_color = e1.get()
                self.initial_color = self.new_color
                but1.configure(state=DISABLED)
                top.destroy()

            for i in range(64):
                if (int(self.coords[i][1]) + int(self.coords[i][2])) % 2 !=0 :
                    try:
                        self.coords[i][0].configure(bg=self.new_color,activebackground=self.new_color)
                    except:
                        print("gadbad")
                        messagebox.showerror("Chess Game","Enter Valid Color Code")
                        break

        but1 = Button(top,text="Save Change",command=save)
        but1.grid(row=1,column=0)

                

wait = Tk()
lab = Label(wait,text="Waiting for connection with second game")
lab.pack()
while True:
    net.receive()
    if net.recv_data[0]=="Connected to the server":
        current_player = net.recv_data[1]
        print(current_player)
    if net.recv_data[0]=="Start Game" or str(net.recv_data)=="Start Game":
            if net.recv_data[0]=="Start Game":
                current_player = net.recv_data[1]
                print(current_player)

            print("Destroying")
            wait.destroy()
            break
chess()
wait.mainloop()

