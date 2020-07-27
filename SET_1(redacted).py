def saver(event):
    global quests
    global sets_names

    old_path=os.getcwd()
    

    p="\ "
    p=p[0:1]
    g=os.listdir(path=".")

    e=0
    for i in g:
        if i=='LastSave':
            e=1
    if e==1:
        num_of_dirs=1
        for i in g:
            if i[:13]=="SetGenerator_":
                if int(i[13])>=num_of_dirs:
                    num_of_dirs=int(i[13])+1

        f='SetGenerator_'+str(num_of_dirs)
        try:
            os.makedirs(f)
        except OSError:
            pass
        path=os.getcwd()+'\SetGenerator_'+str(num_of_dirs)
        os.chdir(path)
        try:
            os.makedirs('Cards')
        except OSError:
            pass
        try:
            os.makedirs('Sets')
        except OSError:
            pass
        os.chdir(old_path)
        
        
        path=old_path+"\LastSave\Cards"
        os.chdir(path)
        g=os.listdir(path=".")
        for i in g:
            shutil.copyfile(r''+old_path+"\LastSave\Cards"+p+i, r''+old_path+p+f+'\Cards'+p+i)

        path=old_path+"\LastSave\Sets"
        os.chdir(path)
        g=os.listdir(path=".")
        for i in g:
            shutil.copyfile(r''+old_path+"\LastSave\Sets"+p+i, r''+old_path+p+f+'\Sets'+p+i)
        os.chdir(old_path)

        
    try:
        os.makedirs('LastSave')
        path=old_path+'\LastSave'
        os.chdir(path)
        os.makedirs('Cards')
        os.makedirs('Sets')
    except OSError:
        pass
    path=old_path+"\LastSave"
    os.chdir(path)

    
    folder = path +'\Cards'
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        if os.path.isfile(file_path):
            os.unlink(file_path)

    folder = path+'\Sets'
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        if os.path.isfile(file_path):
            os.unlink(file_path)


    try:
        os.makedirs('Cards')
    except OSError:
        pass
    try:
        os.makedirs('Sets')
    except OSError:
        pass

    new_path=path+'\Cards'
    os.chdir(new_path)
    m=int(go_to_page_entry.get())-1
    for i in range(12):
        s=quests[m][i]
        shutil.copyfile(r''+old_path+'\Cards'+p+s+'.png', r''+new_path+p+s+'.png')

    new_path=path+'\Sets'
    os.chdir(new_path)
    cnt1=1
    cnt2=1
    for i in range(len(sets_names)):
            s=sets_names[i]
            shutil.copyfile(r''+old_path+'\Cards'+p+s+'.png', r''+old_path+'\LastSave\Sets'+p+s+'.png')
            shutil.move(s+'.png', 'Set'+str(cnt1)+'_'+str(cnt2)+'.png')
            cnt2+=1
            if cnt2==4:
                cnt2=1
                cnt1+=1
    os.chdir(old_path)
    
def set_finder():
    global quests
    global panel_2
    global sets
    m=int(go_to_page_entry.get())-1
    set_label=Label(panel_2,text="SETы:", height=2, width=20)
    set_label.place(x=745, y=5)
    p=5
    l=900
    if len(sets)!=0:
        for i in range(len(sets)):
            for j in range(3):
                sets[i][j].destroy()
    sets=[]
    global sets_names
    sets_names=[]
    
    for i in range(12):
        for j in range(i+1,12):
            for k in range(j+1,12):
                cnt=0
                for z in range(4):
                    if (quests[m][i][z]==quests[m][j][z]==quests[m][k][z]) or (quests[m][i][z]!=quests[m][j][z] and quests[m][i][z]!=quests[m][k][z] and quests[m][j][z]!=quests[m][k][z]):
                        cnt+=1
                    else:
                        break
                if cnt==4:
                    q=[i,j,k]
                    w=[[0] for y in range(3)]
                    sets.append(w)
                    for f in range(3):
                        sets_names.append(quests[int(go_to_page_entry.get())-1][q[f]])
                        im = PIL.Image.open(quests[int(go_to_page_entry.get())-1][q[f]]+".png")
                        sizer=im.size
                        z=sizer[0]/sizer[1]
                        if z>1:
                            size=(int(125*z),125)
                        else:
                            size=(int(125*z),125)
                        imnew=im.resize(size)
                        photo = PIL.ImageTk.PhotoImage(imnew)
                        sets[-1][f]=Label(panel_2, image=photo)
                        sets[-1][f].image=photo
                        sets[-1][f].place(x=l,y=p)
                        l+=100
                    l=900
                    p+=140

def printer(event):
    global quests
    global cards
    if len(cards)!=0:
        for i in range(12):
            cards[i].destroy()
    cards=[0 for i in range(12)]
    m=5
    n=5
    cnt=0
    w=go_to_page_entry.get()

    old_path=os.getcwd()
    path=old_path+'\Cards'
    os.chdir(path)
    
    if w.isnumeric()==True:
        if int(w)<=int(question_lbl_entry.get()):
            for i in range(12):
                im = PIL.Image.open(quests[int(w)-1][i]+".png")
                sizer=im.size
                z=sizer[0]/sizer[1]
                if z>1:
                    size=(int(250*z),250)
                else:
                    size=(int(250*z),250)
                imnew=im.resize(size)
                photo = PIL.ImageTk.PhotoImage(imnew)
                cards[i]=Label(panel_2, image=photo)
                cards[i].image=photo
                cards[i].place(x=n,y=m)
                n+=185
                cnt+=1
                if cnt==4:
                    m+=280
                    n=5
                    cnt=0
            set_finder()
    os.chdir(old_path)
        
def generator(event):
    global question_lbl_entry
    global panel
    global panel_2
    global out_of_page
    global quests

    m=question_lbl_entry.get()
    if m=='':
        m='0'
    if m.isnumeric()==True:
        out_of_page["text"]="из "+m
        m=int(m)
        quests=[['']*12 for i in range(m)]
        names=[[0]*3 for i in range(4)]
        names[0]=['r','g','b']
        names[1]=['1','2','3']
        names[2]=['r','w','o']
        names[3]=['f','v','n']
        for i in range(m):
            used=[]
            for j in range(12):
                q=0
                while q!=1:
                    now=''
                    for k in range(4):
                        n=random.randint(0,2)
                        now+=names[k][n]
                    if now not in used:
                        used.append(now)
                        quests[i][j]=now
                        q=1






def start(event):  #Создание начального окна
    global panel
    global panel_2
    panel = Frame(root,width=320, bg = '#5daeae',height=250)
    #panel.pack(side = 'left', fill = 'y')
    panel.place(x=0,y=0)

    panel_2 = Frame(root, width =1336, bg = 'white',height=1000)
    panel_2.place(x=320,y=0)
    #panel_2.pack(side = 'right', fill = 'y')

    question_lbl=Label(panel, height=2,text="Кол-во вариантов:", width=20, bg='white',fg='black',bd=4)
    question_lbl.place(x = 5, y = 10)

    global question_lbl_entry
    a=0
    question_lbl_entry=Entry(panel, textvariable=a, width=20, bg='white',fg='black',bd=10)
    question_lbl_entry.place(x=159,y=11)

    generate=Button(panel,text="Генерировать",width=41,height=2)
    generate.bind("<Button-1>",generator)
    generate.place(x = 5, y = 55)


    go_to_page=Label(panel, height=2,text="Перейти к варианту", width=20, bg='white',fg='black',bd=4)
    go_to_page.place(x = 5, y = 99)
    global go_to_page_entry
    b=''
    go_to_page_entry=Entry(panel, textvariable=b, width=11, bg='white',fg='black',bd=10)
    go_to_page_entry.place(x=159,y=99)

    m=question_lbl_entry.get()
    if m=='':
        m='0'
    global out_of_page
    out_of_page=Label(panel, height=2,text="из "+m, width=6, bg='white',fg='black',bd=4)
    out_of_page.place(x = 250, y = 99)

    go=Button(panel,text="Перейти",width=41,height=2)
    go.bind("<Button-1>",printer)
    go.place(x = 5, y = 143)    

    save=Button(panel,text="Сохранить", width=41, height=2)
    save.bind("<Button-1>",saver)
    save.place(x=5,y=187)
    
    

    
from tkinter import *
import random
from tkinter import filedialog
import fileinput
from PIL import ImageTk, Image, ImageGrab
import PIL.Image
import PIL.ImageTk
import os
import shutil



root=Tk()
root.title("SET")
root.state("zoomed")
root["bg"]="white"
#root.resizable(0,0)
quests=[]
sets=[]
cards=[]
start(1)
root.mainloop()
