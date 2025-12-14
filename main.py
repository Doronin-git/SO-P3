from classes import Process, Segment
import os,time
from ui import Visualizer
import tkinter as tk

def getInfo(): #return array of Process
    file_name = "data.txt"
    process_array = []

    if os.path.exists(file_name):
        with open(file_name, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split()
                id,delay,size,time = parts

                p = Process(
                    id = int(id),
                    delay = int(delay),
                    size = int(size),
                    time = int(time),
                    time_left = int(time),
                    state = "waiting"
                )

                process_array.append(p) 
    
    return process_array


def finished(process_array):
    for p in process_array:
        if p.state != "finished":
            return False
    
    return True


def tryToAssign(process_array, tick, segments):
    for p in process_array:
        if p.delay <= tick and p.state == "waiting":
            for i, s in enumerate(segments):
                if s.state == "free" and s.size >= p.size:
                    if s.size == p.size:
                        s.state = "P" + str(p.id)
                        p.state = "in_process"
                    else:
                        new_proc_segment = Segment(s.start, p.size, "P" + str(p.id))
                        new_free_segment = Segment(s.start + p.size, s.size - p.size, "free")

                        segments.pop(i)
                        segments.insert(i, new_free_segment)
                        segments.insert(i, new_proc_segment)

                        p.state = "in_process"

                    break  # segment

            
            if p.state == "in_process":
                break# process_array



def passTime(process_array,segments):
    for p in process_array:
        if p.state== "in_process":
            p.time_left -= 1
            if p.time_left == 0:
                p.state = "finished"

                for s in segments: #find finished process
                    if s.state == "P" + str(p.id):
                        s.state = "free"

            


def blendSegments(segments):
    segments.sort(key=lambda s: s.start)
    i = 0
    while i < len(segments) - 1:
        current = segments[i]
        next = segments[i + 1]
        if current.state == "free" and next.state == "free":
            current.size += next.size
            segments.pop(i + 1)
        else:
            i += 1

    segments.sort(key=lambda s: s.start)  



def printState(tick, process_array, segments):
    print(f"Tick = {tick}")
    print("Processes:")
    for p in process_array:
        print("  ", p)
    print("Segments:")
    # сортируем для вывода
    segments.sort(key=lambda s: s.start)
    for s in segments:
        print("  ", s)
    print("-" * 40)


def main():
    tick = 0
    process_array = getInfo() #array de Process
    segments = [
        Segment(start=0, size=2000, state="free") #create memory segment
    ]
    vis = Visualizer() 

    while not finished(process_array):
        
        passTime(process_array,segments)
        blendSegments(segments)
        tryToAssign(process_array, tick, segments) 
        printState(tick, process_array, segments)

        vis.draw(segments)
        vis.root.update()

        time.sleep(0.5)
        tick = tick + 1
    vis.root.mainloop() # dont close the window
                
main()