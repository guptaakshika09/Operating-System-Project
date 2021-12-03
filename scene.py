from manim import *
size_sq=0.6
def square_text_box(number, square_color, text_color,size_s=size_sq):
            square = Square(side_length=size_s)
            square.set_stroke(color=square_color)
           
            text =Text((number), color=text_color)
            if(size_s!=size_sq):
                text.scale(0.45)
            else :
                text.scale(0.6)
            squ_text = VGroup()
            squ_text.add(square, text)
            return squ_text


def square_swap(color_name):
            square_fill2 = Square(side_length=size_sq)
            square_fill2.set_stroke(color=color_name, width=0)
            square_fill2.set_fill(color=color_name, opacity=0.5)

            return square_fill2


class fcfs(Scene):
    def construct(self):
        n=int(input("Enter the number of Processes: "))
        arr=[]
        for i in range(n):
            a,b=map(int,input("Enter space separated Arrival time and Execution time for P"+str(i)+": ").split())
            arr.append([a,b,i])
        arr.sort()
        time=0

        text_start = Text("In FCFS processes are queued in the order they arrive in the ready queue." )
        text_start2 = Text("The process that comes first will be executed first, and ")
        text_start3 = Text("the next process will begin only once the previous has completed its execution.")
        text_start.scale(0.5)
        text_start.shift(UP*size_sq*2)
        text_start2.scale(0.5)
        text_start3.scale(0.5)
        text_start3.shift(DOWN*size_sq*2)
        
        text_h=Text("First Come First Serve Algorithm", font="Courier", color=YELLOW)
        text_h.scale(0.8)
        text_h.to_edge(UP)
        self.play(Write(text_h))
        self.wait(1)
        self.play(Write(text_start))
        self.play(Write(text_start2))
        self.play(Write(text_start3))
        self.wait(10)
        self.remove(text_start)
        self.remove(text_start2)
        self.remove(text_start3)
        text_a=Text("Time = "+str(time))
        text_a.shift(2*UP)
        self.add(text_a)
        bub=square_text_box("Start - ", BLUE, WHITE,1.2)
        self.play(GrowFromCenter(bub))
        #bub.shift(6*LEFT)
        bub.to_edge(LEFT)
        last=bub
        i=0
        l=[bub]
        while i<n:
            if(time<arr[i][0]):
                
                time+=1
                self.remove(text_a)
                text_a=Text("Time = "+str(time))
                text_a.shift(2*UP)
                text_h=Text("IDLE", font="Courier", color=RED)
                text_h.scale(1.4)
                text_h.shift(2*DOWN)
                self.play(Write(text_h))
                self.add(text_a)
                self.wait(0.5)
                self.remove(text_h)
                
                
            else:
                for j in range(arr[i][1]):
                    ind_x=arr[i][2]
                    side_color=GREEN_B
                    if(ind_x%2==0):
                        side_color=RED_B
                    bub1=square_text_box("P"+str(ind_x), BLUE_D,side_color)
                    bub1.next_to(l[-1],buff=0)
                    text_h=Text("P"+str(ind_x)+" is executing", font="Courier", color=YELLOW)
                    text_h.scale(1.2)
                    text_h.shift(2*DOWN)
                    self.play(Write(text_h))
                    self.wait(0.5)

                    l.append(bub1)
                    self.play(FadeIn(bub1))
                    time+=1
                    self.remove(text_a)
                    text_a=Text("Time = "+str(time))
                    text_a.shift(2*UP)
                    self.add(text_a)
                    self.wait(0.5)
                    self.remove(text_h)
                    if(len(l)%19==0):
                        for k in range(len(l)):
                            l[k].shift(17*size_sq*LEFT)
                        l=l[17:]
                
                text_h=Text("P"+str(arr[i][2])+"'s execution is finished.", font="Courier", color=GREEN)
                text_h.scale(1.2)
                text_h.shift(2*DOWN)
                self.play(Write(text_h))
                self.wait(0.5)
                self.remove(text_h)
                i+=1
        
class sjn(Scene):
    def construct(self):
        n=int(input("Enter the number of Processes: "))
        arr=[]
        for i in range(n):
            a,b=map(int,input("Enter space separated Arrival time and Execution time for P"+str(i)+": ").split())
            arr.append([a,b,i])
        arr.sort()
        x=[]
        time=0
        text_h=Text("Shortest Job Next Algorithm", font="Courier", color=YELLOW)
        text_h.scale(0.8)
        text_h.to_edge(UP)
        self.play(Write(text_h))
        self.wait(1)

        text_start = Text("Shortest Job Next is a scheduling algorithm that selects " )
        text_start2 = Text("the waiting process with the smallest execution time to execute next ")
        #text_start3 = Text("the next process will begin only once the previous has completed its execution.")
        text_start.scale(0.5)
        text_start.shift(UP*size_sq*2)
        text_start2.scale(0.5)
        #text_start3.scale(0.5)
        #text_start3.shift(DOWN*size_sq*2)

        self.play(Write(text_start))
        self.play(Write(text_start2))
        #self.play(Write(text_start3))
        self.wait(10)
        self.remove(text_start)
        self.remove(text_start2)
        #self.remove(text_start3)


        text_a=Text("Time = "+str(time))
        text_a.shift(2*UP)
        self.add(text_a)
        bub=square_text_box("Start - ", BLUE, WHITE,1.2)
        self.play(GrowFromCenter(bub))
        bub.shift(6.5*LEFT)
        last=bub
        i=0
        t=0
        

        l=[bub]
        while i<n+1:
            if(i<n and time<arr[i][0]):
                if len(x)==0:
                    time+=1
                    self.remove(text_a)
                    text_a=Text("Time = "+str(time))
                    text_a.shift(2*UP)
                    self.add(text_a)
                    text_h=Text("IDLE", font="Courier", color=RED)
                    text_h.scale(1.4)
                    text_h.scale(1.2)
                    text_h.shift(2*DOWN)
                    self.play(Write(text_h))
                    self.wait(0.5)
                    self.remove(text_h)
                    self.wait(0.5)
            else :
                while(i<n and time>=arr[i][0]):
                    x.append([arr[i][1],arr[i][2]])
                    text_h=Text("P"+str(arr[i][2])+" is now Available and arrived at "+str(arr[i][0]), font="Courier", color=PINK)
                    text_h.scale(0.7)
                    text_h.shift(2*DOWN)
                    self.play(Write(text_h))
                    self.wait(0.5)
                    self.remove(text_h)


                    i+=1
                
                
            if len(x)>0:
                x.sort()
                y=x.pop(0)
                
                for j in range(y[0]):
                    ind_x=y[1]
                    side_color=GREEN_B
                    if(t%2==0):
                        side_color=RED_B
                    bub1=square_text_box("P"+str(ind_x), BLUE_D,side_color)
                    bub1.next_to(l[-1],buff=0)
                    text_h=Text("P"+str(ind_x)+" is executing", font="Courier", color=YELLOW)
                    text_h.scale(0.8)
                    text_h.shift(2*DOWN)
                    self.play(Write(text_h))
                    self.wait(0.5)
                    self.remove(text_h)
                    l.append(bub1)
                    self.play(FadeIn(bub1))
                    time+=1
                    self.remove(text_a)
                    text_a=Text("Time = "+str(time))
                    text_a.shift(2*UP)
                    self.add(text_a)
                    self.wait(0.5)
                    if(len(l)%19==0):
                        for k in range(len(l)):
                            l[k].shift(17*size_sq*LEFT)
                        l=l[17:]
                text_h=Text("P"+str(y[1])+"'s execution is finished.", font="Courier", color=GREEN)
                text_h.scale(1.2)
                text_h.shift(2*DOWN)
                self.play(Write(text_h))
                self.wait(0.5)
                self.remove(text_h)
                t+=1
            if(i==n and len(x)==0):
                break
        

class prioritySch(Scene):
    def construct(self):
        n=int(input("Enter the number of Processes: "))
        arr=[]
        for i in range(n):
            a,b,c=map(int,input("Enter space separated Arrival time, Execution time and Priority for P"+str(i)+": ").split())
            arr.append([a,b,c,i])
        arr.sort()
        time=0
        text_h=Text("Priority Scheduling Algorithm", font="Courier", color=YELLOW)
        text_h.scale(0.8)
        text_h.to_edge(UP)
        self.play(Write(text_h))
        self.wait(1)

        text_start = Text("Each process is assigned a priority." )
        text_start2 = Text("The CPU is allocated to the process with the highest priority (smallest integer is highest priority) ")
        #text_start3 = Text("the next process will begin only once the previous has completed its execution.")
        text_start.scale(0.5)
        text_start.shift(UP*size_sq*2)
        text_start2.scale(0.5)
        #text_start3.scale(0.5)
        #text_start3.shift(DOWN*size_sq*2)

        self.play(Write(text_start))
        self.play(Write(text_start2))
        #self.play(Write(text_start3))
        self.wait(10)
        self.remove(text_start)
        self.remove(text_start2)
        #self.remove(text_start3)

        text_a=Text("Time = "+str(time))
        text_a.shift(2*UP)
        self.add(text_a)
        bub=square_text_box("Start - ", BLUE, WHITE,1.2)
        self.play(GrowFromCenter(bub))
        bub.shift(6.5*LEFT)
        
        i=0
        t=0
        x=[]
        l=[bub]
        while i<n+1:
            
            if(i<n and time<arr[i][0]):
                if len(x)==0:
                    time+=1
                    self.remove(text_a)
                    text_a=Text("Time = "+str(time))
                    text_a.shift(2*UP)
                    self.add(text_a)
                    text_h=Text("IDLE", font="Courier", color=RED)
                    text_h.scale(1.4)
                    text_h.scale(1.2)
                    text_h.shift(2*DOWN)
                    self.play(Write(text_h))
                    self.wait(0.5)
                    self.remove(text_h)
                    self.wait(0.5)
            else :
                while(i<n and time>=arr[i][0]):
                    x.append([arr[i][2],arr[i][1],arr[i][3]])
                    text_h=Text("P"+str(arr[i][2])+" is now Available and arrived at time = "+str(arr[i][0]), font="Courier", color=PINK)
                    text_h.scale(0.7)
                    text_h.shift(2*DOWN)
                    self.play(Write(text_h))
                    self.wait(0.5)
                    self.remove(text_h)
                    i+=1
                
                
            if len(x)>0:
                x.sort()
                y=x.pop(0)
                
                for j in range(y[1]):
                    ind_x=y[2]
                    side_color=GREEN_B
                    if(t%2==0):
                        side_color=RED_B
                    bub1=square_text_box("P"+str(ind_x), BLUE_D,side_color)
                    bub1.next_to(l[-1],buff=0)
                    text_h=Text("P"+str(ind_x)+" is executing", font="Courier", color=YELLOW)
                    text_h.scale(0.8)
                    text_h.shift(2*DOWN)
                    self.play(Write(text_h))
                    self.wait(0.5)
                    self.remove(text_h)
                    
                    l.append(bub1)
                    self.play(FadeIn(bub1))
                    time+=1
                    self.remove(text_a)
                    text_a=Text("Time = "+str(time))
                    text_a.shift(2*UP)
                    self.add(text_a)
                    self.wait(0.5)
                    if(len(l)%19==0):
                        for k in range(len(l)):
                            l[k].shift(17*size_sq*LEFT)
                        l=l[17:]
                        #l=l[16:]
                text_h=Text("P"+str(y[2])+"'s execution is finished.", font="Courier", color=GREEN)
                text_h.scale(1.2)
                text_h.shift(2*DOWN)
                self.play(Write(text_h))
                self.wait(0.5)
                self.remove(text_h)
                        
                t+=1
            if(i==n and len(x)==0):
                break


class srt(Scene):
    def construct(self):
        n=int(input("Enter the number of Processes: "))
        arr=[]
        for i in range(n): 
            a,b=map(int,input("Enter space separated Arrival time and Execution time for P"+str(i)+": ").split())
            arr.append([a,b,i])
        arr.sort()
        time=0
        text_h=Text("Shortest Remaining Time Algorithm", font="Courier", color=YELLOW)
        text_h.scale(0.8)
        text_h.to_edge(UP)
        self.play(Write(text_h))
        self.wait(1)

        text_start = Text("The processor is allocated to the job closest to completion but " )
        text_start2 = Text("it can be preempted by a newer ready job with shorter time to completion ")
        #text_start3 = Text("the next process will begin only once the previous has completed its execution.")
        text_start.scale(0.5)
        text_start.shift(UP*size_sq*2)
        text_start2.scale(0.5)
        #text_start3.scale(0.5)
        #text_start3.shift(DOWN*size_sq*2)

        self.play(Write(text_start))
        self.play(Write(text_start2))
        #self.play(Write(text_start3))
        self.wait(10)
        self.remove(text_start)
        self.remove(text_start2)
        #self.remove(text_start3)


        text_a=Text("Time = "+str(time))
        text_a.shift(2*UP)
        self.add(text_a)
        bub=square_text_box("Start - ", BLUE, WHITE,1.2)
        self.play(GrowFromCenter(bub))
        bub.shift(6.5*LEFT)
        i=0
        t=0
        x=[]
        l=[bub]
        while i<n+1:
            if i<n and time<arr[i][0]:
                if len(x)==0:
                    time+=1
                    self.remove(text_a)
                    text_a=Text("Time = "+str(time))
                    text_a.shift(2*UP)
                    self.add(text_a)
                    text_h=Text("IDLE", font="Courier", color=RED)
                    text_h.scale(1.4)
                    text_h.scale(1.2)
                    text_h.shift(2*DOWN)
                    self.play(Write(text_h))
                    self.wait(0.5)
                    self.remove(text_h)
                    self.wait(0.5)
            else :
                while i<n and time>=arr[i][0]:
                    x.append([arr[i][1],arr[i][2]])
                    text_h=Text("P"+str(arr[i][2])+" is now Available and arrived at time = "+str(arr[i][0]), font="Courier", color=PINK)
                    text_h.scale(0.7)
                    text_h.shift(2*DOWN)
                    self.play(Write(text_h))
                    self.wait(0.5)
                    self.remove(text_h)
                    i+=1
            if(len(x)>0):
                x.sort()
                x[0][0]-=1
                
                text_h=Text("P"+str(x[0][1])+" is executing", font="Courier", color=YELLOW)
                text_h.scale(0.8)
                text_h.shift(2*DOWN)
                self.play(Write(text_h))
                self.wait(0.5)
                self.remove(text_h)
                    
                bub1=square_text_box("P"+str(x[0][1]), BLUE_D,GREEN_B)
                bub1.next_to(l[-1],buff=0)
                l.append(bub1)
                self.play(FadeIn(bub1))
                time+=1
                self.remove(text_a)
                text_a=Text("Time = "+str(time))
                text_a.shift(2*UP)
                self.add(text_a)
                self.wait(0.5)
                if(x[0][0]==0):
                    text_h=Text("P"+str(x[0][1])+"'s execution is finished.", font="Courier", color=GREEN)
                    text_h.scale(1.2)
                    text_h.shift(2*DOWN)
                    self.play(Write(text_h))
                    self.wait(0.5)
                    self.remove(text_h)
                    x.pop(0)

                if(len(l)%19==0):
                    for k in range(len(l)):
                        l[k].shift(17*size_sq*LEFT)
                    l=l[17:]
            if(i==n and len(x)==0):
                break

                
            
class rr(Scene):
    def construct(self):
        # quantum =2
        n=int(input("Enter the number of Processes: "))
        arr=[]
        for i in range(n):
            a,b=map(int,input("Enter space separated Arrival time and Execution time for P"+str(i)+": ").split())
            arr.append([a,b,i])
        arr.sort()
        time=0
        text_h=Text("Round Robin Algorithm", font="Courier", color=YELLOW)
        text_h.scale(0.8)
        text_h.to_edge(UP)
        self.play(Write(text_h))
        self.wait(1)

        text_start = Text("Each process is provided a fix time to execute, it is called a quantum." )
        text_start2 = Text("Once a process is executed for a given time period, it is preempted and")
        text_start3 = Text("other process executes for a given time period.")
        text_start.scale(0.5)
        text_start.shift(UP*size_sq*2)
        text_start2.scale(0.5)
        text_start3.scale(0.5)
        text_start3.shift(DOWN*size_sq*2)

        self.play(Write(text_start))
        self.play(Write(text_start2))
        self.play(Write(text_start3))
        self.wait(10)
        self.remove(text_start)
        self.remove(text_start2)
        self.remove(text_start3)

        text_a=Text("Time = "+str(time))
        text_a.shift(2*UP)
        self.add(text_a)
        bub=square_text_box("Start - ", BLUE, WHITE,1.2)
        self.play(GrowFromCenter(bub))
        bub.shift(6.5*LEFT)
        i=0
        t=0
        x=[]
        l=[bub]
        while i<n+1:
            if i<n and time<arr[i][0]:
                if len(x)==0:
                    time+=1
                    self.remove(text_a)
                    text_a=Text("Time = "+str(time))
                    text_a.shift(2*UP)
                    self.add(text_a)
                    text_h=Text("IDLE", font="Courier", color=RED)
                    text_h.scale(1.4)
                    text_h.scale(1.2)
                    text_h.shift(2*DOWN)
                    self.play(Write(text_h))
                    self.wait(0.5)
                    self.remove(text_h)
                    self.wait(0.5)
            else :
                while i<n and time>=arr[i][0]:
                    x=[([arr[i][1],arr[i][2]])]+x
                    text_h=Text("P"+str(arr[i][2])+" is now Available and arrived at time = "+str(arr[i][0]), font="Courier", color=PINK)
                    text_h.scale(0.7)
                    text_h.shift(2*DOWN)
                    self.play(Write(text_h))
                    self.wait(0.5)
                    self.remove(text_h)
                    i+=1
            if(len(x)>0):
                y=x.pop(0)
                
                for j in range(min(y[0],2)):         
                    bub1=square_text_box("P"+str(y[1]), BLUE_D,GREEN_B)
                    bub1.next_to(l[-1],buff=0)
                    l.append(bub1)
                    text_h=Text("P"+str(y[1])+" is executing", font="Courier", color=YELLOW)
                    text_h.scale(0.8)
                    text_h.shift(2*DOWN)
                    self.play(Write(text_h))
                    self.wait(0.5)
                    self.remove(text_h)
                    self.play(FadeIn(bub1))
                    time+=1
                    self.remove(text_a)
                    text_a=Text("Time = "+str(time))
                    text_a.shift(2*UP)
                    self.add(text_a)
                    self.wait(0.5)
                    t+=1
                y[0]-=2
                if(y[0]>0):
                    x.append([y[0],y[1]])
                else:
                    text_h=Text("P"+str(y[1])+"'s execution is finished.", font="Courier", color=GREEN)
                    text_h.scale(1.2)
                    text_h.shift(2*DOWN)
                    self.play(Write(text_h))
                    self.wait(0.5)
                    self.remove(text_h)
                if(len(l)%19==0):
                    for k in range(len(l)):
                        l[k].shift(17*size_sq*LEFT)
                    l=l[17:]
            if(i==n and len(x)==0):
                break


size_sq = 0.7
#-------------------------------------------------------------------------------------------------------------------------------------------------
#FIFO Page Replacement Algorithm    
class fifo(Scene):
    def construct(self):
        from queue import Queue
        print("Enter maximum 20 numbers that will be reference string : ", end=" ")
        pages = list(map(int,input().split()))
        print("Enter the capacity/number of frames : ", end=" ")
        capacity=int(input())
        l=[]
        s=set()
        indexes = Queue()
        page_faults=0
        n=len(pages)
        ref_string=[]

        text_h=Text("FIFO Page Replacement Algorithm", font="Courier", color=YELLOW)
        text_h.scale(0.8)
        text_h.to_edge(UP)
        self.play(Write(text_h))

        text_start = Text("In this process operating system keeps track of all pages in the memory in a queue" )
        text_start2 = Text("oldest page is in the front of the queue.")
        text_start3 = Text("When a page needs to be replaced page in the front of the queue is selected for removal")
        text_start.scale(0.5)
        text_start.shift(UP*size_sq*2)
        text_start2.scale(0.5)
        text_start3.scale(0.5)
        text_start3.shift(DOWN*size_sq*2)

        self.play(Write(text_start))
        self.play(Write(text_start2))
        self.play(Write(text_start3))
        self.wait(10)
        self.remove(text_start)
        self.remove(text_start2)
        self.remove(text_start3)
        
        bubs = square_text_box(str(pages[0]), BLUE_D, GREEN_B)
        bubs.shift((n//2-1) * LEFT)
        ref_string.append(bubs)
        for i in range(1,n):
            bubs = square_text_box(str(pages[i]), BLUE_D, GREEN_B)
            bubs.next_to(ref_string[-1], buff=0)
            ref_string.append(bubs)


        for i in range(n):
            bubs_fill_box1 = square_swap(BLUE_D)
            if(i==0):
                bubs_fill_box1.shift((n//2-1) * LEFT)
            else :
                bubs_fill_box1.next_to(ref_string[i-1], buff=0)
            
            if (len(s)<capacity) :
                if (pages[i] not in s):
                    s.add(pages[i])
                    page_faults+=1
                    indexes.put(pages[i])
                    box = square_text_box(str(pages[i]),BLUE_D, GREEN_B)
                    if(i==0):
                        box.shift((n//2-1) * LEFT)
                    else :
                        box.next_to(l[-1], buff=0)
                    l.append(box)
                    self.play(GrowFromCenter(l[-1]))
                else:
                    text_a=Text("Page " + str(pages[i]) + " is already in memory")
                    text_a.scale(0.5)
                    text_a.shift(UP*size_sq*3)
                    self.add(text_a)
                    self.wait(1)
                    self.remove(text_a)

            else:
                if (pages[i] not in s):
                    value = indexes.queue[0]
                    indexes.get()
                    s.remove(value)
                    self.remove(l[0])
                    l=l[1:]

                    s.add(pages[i])
                    indexes.put(pages[i])
                    page_faults+=1
                    box = square_text_box(str(pages[i]),BLUE_D, GREEN_B)
                    if(i==0):
                        box.shift((n//2-1) * LEFT)
                    else :
                        box.next_to(l[-1], buff=0)
                    l.append(box)
                    self.play(GrowFromCenter(l[-1]))
                else:
                    text_a=Text("Page " + str(pages[i]) + " is already in memory")
                    text_a.scale(0.5)
                    text_a.shift(UP*size_sq*3)
                    self.add(text_a)
                    self.wait(1)
                    self.remove(text_a)

            text_a=Text("Page Faults : "+str(page_faults))
            text_a.scale(0.5)
            text_a.shift(UP*size_sq*3)
            self.add(text_a)
            self.wait(1)
            self.remove(text_a)







                    
#----------------------------------------------------------------------------------------------------------------------------------------------
#LRU Page Replacement Algorithm
class lru(Scene):
    def construct(self):
        print("Enter maximum 20 numbers that will be reference string : ", end=" ")
        pages = list(map(int,input().split()))
        print("Enter the capacity/number of frames : ", end =" ")
        capacity=int(input())
        temp_stack=[]
        l=[]
        f=[]
        page_faults=0
        n=len(pages)
        te=Text("Input : ")
        te.scale(0.5)
        te.shift(UP*size_sq*2)
        te.shift((n//2+1)*LEFT)
        text_h=Text("Least Recently Used Algorithm", font="Courier", color=YELLOW)
        text_h.scale(0.8)
        text_h.to_edge(UP)
        self.play(Write(text_h))
        Frame = Text("Capacity is : " + str(capacity))
        Frame.scale(0.5)
        Frame.shift(DOWN*size_sq*3)

        ref_string=[]
        bubs = square_text_box(str(pages[0]), YELLOW_D, RED_B)
        bubs.shift((n//2-1) * LEFT)
        ref_string.append(bubs)
        for i in range(1,n):
            bubs = square_text_box(str(pages[i]), YELLOW_D, RED_B)
            bubs.shift(UP*size_sq*2)
            bubs.next_to(ref_string[-1], buff=0)
            ref_string.append(bubs)

        text_start = Text("It is a Greedy algorithm where the page to be replaced is least recently used" )
        #text_start2 = Text("oldest page is in the front of the queue.")
        #text_start3 = Text("When a page needs to be replaced page in the front of the queue is selected for removal")
        text_start.scale(0.5)
        text_start.shift(UP*size_sq*2)
        #text_start2.scale(0.5)
        #text_start3.scale(0.5)
        #text_start3.shift(DOWN*size_sq*2)

        self.play(Write(text_start))
        #self.play(Write(text_start2))
        #self.play(Write(text_start3))
        self.wait(10)
        self.remove(text_start)
        #self.remove(text_start2)
        #self.remove(text_start3)


        self.add(Frame)
        self.add(te)
        for j in ref_string:
            j.shift(UP*size_sq*2)
            self.play(GrowFromCenter(j))
        for i in range(n):
            ref_string[i].set_fill(color=YELLOW_C, opacity=0.5)
            if pages[i] not in f:
                if len(f)<capacity:
                    page_faults+=1
                    f.append(pages[i])
                    temp_stack.append(len(f)-1)
                    box = square_text_box(str(pages[i]),BLUE_D, GREEN_B)
                    if(i==0):
                        box.shift((capacity//2-1) * LEFT)
                    else :
                        box.next_to(l[-1], buff=0)
                    l.append(box)
                    self.play(GrowFromCenter(l[-1]))
                else:
                    page_faults+=1
                    temp_ind = temp_stack.pop(0)
                    f[temp_ind]=pages[i]
                    box = square_text_box(str(pages[i]),BLUE_D, GREEN_B)
                    if(temp_ind==0):
                        box.shift((capacity//2-1) * LEFT)
                    else :
                        box.next_to(l[temp_ind-1], buff=0)
                    self.remove(l[temp_ind])
                    l[temp_ind]=box

                    temp_stack.append(temp_ind)
                    self.play(GrowFromCenter(l[temp_ind]))
            else:
                q=temp_stack.index(f.index(pages[i]))
                temp_stack.append(temp_stack.pop(q))
                text_a=Text("Page " + str(pages[i]) + " is already in memory")
                text_a.scale(0.5)
                text_a.shift(DOWN*size_sq*2)
                self.add(text_a)
                self.wait(1)
                self.remove(text_a)
            text_a=Text("Page Faults : "+str(page_faults))
            text_a.scale(0.5)
            text_a.shift(DOWN*size_sq*2)
            self.add(text_a)
            self.wait(1)
            self.remove(text_a)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------
#Optimal Page Replacement Algorithm
class optimal_pr(Scene):
    def construct(self):
        print("Enter maximum 20 numbers that will be reference string : ", end=" ")
        pages = list(map(int,input().split()))
        print("Enter the capacity/number of frames : ", end= " ")
        capacity=int(input())
        l=[]
        f=[]
        page_faults=0
        n=len(pages)

        text_h=Text("Optimal Page Replacement Algorithm", font="Courier", color=YELLOW)
        text_h.scale(0.8)
        text_h.to_edge(UP)
        self.play(Write(text_h))

        text_start = Text("In this algorithm, OS replaces the page that will" )
        text_start2 = Text("not be used for the longest period of time in future")
        #text_start3 = Text("When a page needs to be replaced page in the front of the queue is selected for removal")
        text_start.scale(0.5)
        text_start.shift(UP*size_sq*2)
        text_start2.scale(0.5)
        #text_start3.scale(0.5)
        #text_start3.shift(DOWN*size_sq*2)

        self.play(Write(text_start))
        self.play(Write(text_start2))
        #self.play(Write(text_start3))
        self.wait(10)
        self.remove(text_start)
        self.remove(text_start2)
        #self.remove(text_start3)

        Frame = Text("Capacity is : " + str(capacity))
        Frame.scale(0.5)
        Frame.shift(DOWN*size_sq*3)

        ref_string=[]
        bubs = square_text_box(str(pages[0]), YELLOW_D, RED_B)
        bubs.shift((n//2-1) * LEFT)
        ref_string.append(bubs)
        for i in range(1,n):
            bubs = square_text_box(str(pages[i]), YELLOW_D, RED_B)
            bubs.shift(UP*size_sq*2)
            bubs.next_to(ref_string[-1], buff=0)
            ref_string.append(bubs)

        self.add(Frame)
        
        for j in ref_string:
            j.shift(UP*size_sq*2)
            self.play(GrowFromCenter(j))

        def find_farthest(pages,f,n,i):
            res=-1
            far=i
            for j in range(0,len(f)):
                k=i
                while k<n:
                    if f[j]==pages[k] :
                        if k>far:
                            far=k
                            res=j
                        break
                    k+=1
                if k==n:
                    return j
            if res==-1:
                return 0
            return res

        for i in range(n):
            ref_string[i].set_fill(color=YELLOW_C, opacity=0.5)
            if pages[i] not in f :
                if (len(f)<capacity) :
                    f.append(pages[i])
                    page_faults+=1
                    box = square_text_box(str(pages[i]),BLUE_D, GREEN_B)
                    if(i==0):
                        box.shift((capacity//2-1) * LEFT)
                    else :
                        box.next_to(l[-1], buff=0)
                    l.append(box)
                    self.play(GrowFromCenter(l[-1]))

                else:
                    page_faults+=1
                    ind = find_farthest(pages,f,n,i+1)
                    f[ind]=pages[i]
                    print(ind)
                    box = square_text_box(str(pages[i]),BLUE_D, GREEN_B)
                    if(ind==0):
                        box.shift((capacity//2-1) * LEFT)
                    else :
                        box.next_to(l[ind-1], buff=0)
                    self.remove(l[ind])
                    l[ind]=box

                    self.play(GrowFromCenter(l[ind]))
            else:
                text_a=Text("Page " + str(pages[i]) + " is already in memory")
                text_a.scale(0.5)
                text_a.shift(DOWN*size_sq*2)
                self.add(text_a)
                self.wait(1)
                self.remove(text_a)

            text_a=Text("Page Faults : "+str(page_faults))
            text_a.scale(0.5)
            text_a.shift(DOWN*size_sq*2)
            self.add(text_a)
            self.wait(1)
            self.remove(text_a)


        
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
#SCAN Disk Scheduling Algorithm
class scan(Scene):
    def construct(self):
        from manim.mobject.geometry import ArrowSquareTip
        print("Enter maximum 20 numbers that will be reference string : ", end=" ")
        req = list(map(int,input().split()))
        print("Enter the head position : ", end=" ")
        head=int(input())
        print("Enter direction left/right : ")
        direction = input()
        l=[]
        after_sort=req
        seek_time = 0
        n=len(req)


        text_h=Text("SCAN Disk Scheduling Algorithm", font="Courier", color=YELLOW)
        text_h.scale(0.8)
        text_h.to_edge(UP)
        self.play(Write(text_h))

        text_start = Text("In this algorithm, head starts from one end of the disk and moves towards the other end," )
        text_start2 = Text("servicing requests in between one by one. Then the direction of the head is reversed")
        text_start3 = Text("and the process continues as head continuously scan back and forth to access the disk")
        text_start.scale(0.5)
        text_start.shift(UP*size_sq*2)
        text_start2.scale(0.5)
        text_start3.scale(0.5)
        text_start3.shift(DOWN*size_sq*2)

        self.play(Write(text_start))
        self.play(Write(text_start2))
        self.play(Write(text_start3))
        self.wait(10)
        self.remove(text_start)
        self.remove(text_start2)
        self.remove(text_start3)
        
        eff=Text("Input ")
        eff.scale(0.5)
        eff.shift(UP*size_sq*3)
        self.play(FadeIn(eff))
        self.wait(1)

        ref_string=[]
        bubs = square_text_box(str(req[0]), YELLOW_D, RED_B)
        bubs.shift((n//2-1) * LEFT)
        ref_string.append(bubs)
        for i in range(1,n):
            bubs = square_text_box(str(req[i]), YELLOW_D, RED_B)
            bubs.shift(UP*size_sq*2)
            bubs.next_to(ref_string[-1], buff=0)
            ref_string.append(bubs)

        
        #self.add(Frame)
        
        for j in ref_string:
            j.shift(UP*size_sq*2)
            self.play(FadeIn(j))
        
        self.wait(1)

        for j in ref_string:
            self.play(FadeOut(j))
        

        after_sort.sort()
        eff=Text("After sorting ")
        eff.scale(0.5)
        eff.shift(UP*size_sq*2)
        self.play(FadeIn(eff))
        self.wait(1)
        self.play(FadeOut(eff))
        sort_string = []

        bubs = square_text_box(str(after_sort[0]), YELLOW_D, RED_B)
        bubs.shift((n//2-1) * LEFT)
        sort_string.append(bubs)
        for i in range(1,n):
            bubs = square_text_box(str(after_sort[i]), YELLOW_D, RED_B)
            bubs.shift(UP*size_sq*2)
            bubs.next_to(sort_string[-1], buff=0)
            sort_string.append(bubs)

        for j in range(n):
            sort_string[j].shift(UP*size_sq*2)
            self.play(GrowFromCenter(sort_string[j]))

        size = 8
        disk_size = 200

        left, right, sequence = [], [], []

        if (direction == "left"):
            left.append(0)
        elif (direction == "right"):
            right.append(disk_size - 1)
    
        for i in range(size):
            if (req[i] < head):
                left.append(req[i])
            if (req[i] > head):
                right.append(req[i])

        left.sort()
        right.sort()

        times = 2
        while (times != 0):
            if (direction == "left"):
                for i in range(len(left) - 1, -1, -1):
                    cur_track = left[i]
                    #arrow = Arrow(start=ORIGIN, end=config.top)
                    #arrow.shift(UP*size_sq*3)

                    if left[i]!=0:
                        ind = after_sort.index(left[i])
                        sort_string[ind].set_fill(color=YELLOW_C, opacity=0.5)
                        #arrow.shift(LEFT * (n//2 + ind))
                        #he = Text("Head")
                        #he.scale(0.5)
                        #he.shift(UP*size_sq* 3)
                        #he.shift(LEFT * (n//2 -ind))
                        #self.play(FadeIn(arrow))
                        #self.wait(1)
                        #self.play(FadeOut(arrow))
                    else:
                        ind= after_sort.index(head)
                        #he = Text("Head")
                        #he.scale(0.5)
                        #he.shift(UP*size_sq* 3)
                        #he.shift(LEFT * (n//2 - ind))
                    #self.play(FadeIn(he))
                    #self.wait(1)
                    #self.play(FadeOut(he))
                    sequence.append(cur_track)
                    seek_time += abs(cur_track - head)
                    head = cur_track

                    

                    box = square_text_box(str(cur_track),BLUE_D, GREEN_B)
                    if(len(l)==0):
                        box.shift((n//2-1) * LEFT)
                    else :
                        box.next_to(l[-1], buff=0)
                    l.append(box)
                    self.play(GrowFromCenter(l[-1]))

                    text_a=Text("Seek Time = "+str(seek_time))
                    text_a.scale(0.5)
                    text_a.shift(DOWN*size_sq*2)
                    self.add(text_a)
                    self.wait(1)
                    self.remove(text_a)

                direction = "right"
        
            elif (direction == "right"):
                for i in range(len(right)):
                    cur_track = right[i]

                    ind = after_sort.index(right[i])
                    sort_string[ind].set_fill(color=YELLOW_C, opacity=0.5)

                    sequence.append(cur_track)
                    seek_time += abs(cur_track - head)
                    head = cur_track

                    box = square_text_box(str(cur_track),BLUE_D, GREEN_B)
                    if(len(l)==0):
                        box.shift((n//2-1) * LEFT)
                    else :
                        box.next_to(l[-1], buff=0)
                    l.append(box)
                    self.play(GrowFromCenter(l[-1]))

                    text_a=Text("Seek Time = "+str(seek_time))
                    text_a.scale(0.5)
                    text_a.shift(DOWN*size_sq*2)
                    self.add(text_a)
                    self.wait(1)
                    self.remove(text_a)

                direction = "left"
            times -= 1
        
 

#---------------------------------------------------------------------------------------------------------------------------------------------------
# C - SCAN Disk Scheduling Algorithm
class Cscan(Scene):
    def construct(self):
        print("Enter maximum 20 numbers that will be reference string : ", end =" ")
        req = list(map(int,input().split()))
        print("Enter the head position : ", end =" ")
        head=int(input())
        size = 8    
        disk_size = 200

        l=[]
        after_sort=req
        seek_time = 0
        n=len(req)

        text_h=Text("C-SCAN Disk Scheduling Algorithm", font="Courier", color=YELLOW)
        text_h.scale(0.8)
        text_h.to_edge(UP)
        self.play(Write(text_h))

        text_start = Text("C-SCAN moves the head from one end servicing all the requests to the other end" )
        text_start2 = Text("As soon as the head reaches the other end, it immediately returns to the beginning ")
        text_start3 = Text("of the disk without servicing any requests on the return trip")
        text_start4 = Text("and starts servicing again once reaches the beginning.")
        text_start.scale(0.5)
        text_start.shift(UP*size_sq)
        text_start2.scale(0.5)
        text_start3.scale(0.5)
        text_start4.scale(0.5)
        text_start3.shift(DOWN*size_sq)
        text_start4.shift(DOWN*size_sq*2)

        self.play(Write(text_start))
        self.play(Write(text_start2))
        self.play(Write(text_start3))
        self.play(Write(text_start4))
        self.wait(10)
        self.remove(text_start)
        self.remove(text_start2)
        self.remove(text_start3)
        self.remove(text_start4)
        

        eff=Text("Input ")
        eff.scale(0.5)
        eff.shift(UP*size_sq*3)
        self.play(FadeIn(eff))
        self.wait(1)

        ref_string=[]
        bubs = square_text_box(str(req[0]), YELLOW_D, RED_B)
        bubs.shift((n//2-1) * LEFT)
        ref_string.append(bubs)
        for i in range(1,n):
            bubs = square_text_box(str(req[i]), YELLOW_D, RED_B)
            bubs.shift(UP*size_sq*2)
            bubs.next_to(ref_string[-1], buff=0)
            ref_string.append(bubs)

        for j in ref_string:
            j.shift(UP*size_sq*2)
            self.play(FadeIn(j))
        
        self.wait(1)

        for j in ref_string:
            self.play(FadeOut(j))

        after_sort.sort()
        eff=Text("After sorting ")
        eff.scale(0.5)
        eff.shift(UP*size_sq*2)
        self.play(FadeIn(eff))
        self.wait(1)
        self.play(FadeOut(eff))
        sort_string = []

        bubs = square_text_box(str(after_sort[0]), YELLOW_D, RED_B)
        bubs.shift((n//2-1) * LEFT)
        sort_string.append(bubs)
        for i in range(1,n):
            bubs = square_text_box(str(after_sort[i]), YELLOW_D, RED_B)
            bubs.shift(UP*size_sq*2)
            bubs.next_to(sort_string[-1], buff=0)
            sort_string.append(bubs)

        for j in range(n):
            sort_string[j].shift(UP*size_sq*2)
            self.play(GrowFromCenter(sort_string[j]))

        left, right, sequence = [], [], []

        left.append(0)
        right.append(disk_size - 1)
    
        for i in range(size):
            if (req[i] < head):
                left.append(req[i])
            if (req[i] > head):
                right.append(req[i])

        left.sort()
        right.sort()

        for i in range(len(right)):
            cur_track = right[i]
            if right[i]!=disk_size - 1:
                ind = after_sort.index(right[i])
                sort_string[ind].set_fill(color=YELLOW_C, opacity=0.5)

            sequence.append(cur_track)
            seek_time += abs(cur_track - head)
            head = cur_track

            box = square_text_box(str(cur_track),BLUE_D, GREEN_B)
            if(len(l)==0):
                box.shift((n//2-1) * LEFT)
            else :
                box.next_to(l[-1], buff=0)
            l.append(box)
            self.play(GrowFromCenter(l[-1]))

            text_a=Text("Seek Time = "+str(seek_time))
            text_a.scale(0.5)
            text_a.shift(DOWN*size_sq*2)
            self.add(text_a)
            self.wait(1)
            self.remove(text_a)

        head = 0
 
        seek_time += (disk_size - 1)
        for i in range(len(left)):
            cur_track = left[i]
            if left[i]!=0:
                ind = after_sort.index(left[i])
                sort_string[ind].set_fill(color=YELLOW_C, opacity=0.5)
            sequence.append(cur_track)
            seek_time += abs(cur_track - head)
            head = cur_track

            box = square_text_box(str(cur_track),BLUE_D, GREEN_B)
            if(len(l)==0):
                box.shift((n//2-1) * LEFT)
            else :
                box.next_to(l[-1], buff=0)
            l.append(box)
            self.play(GrowFromCenter(l[-1]))

            text_a=Text("Seek Time = "+str(seek_time))
            text_a.scale(0.5)
            text_a.shift(DOWN*size_sq*2)
            self.add(text_a)
            self.wait(1)
            self.remove(text_a)


        
