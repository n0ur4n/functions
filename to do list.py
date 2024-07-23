tasks=[]
print("Welcome To The To Do List")
task=input("Enter a task: ")

def add (tasks):
    print("your tasks are:", task )
    tasks.append(task)

finish=input("Mark your task (completed/not completed) ")
def mark(tasks):
    
    
    if finish=="completed":
        print("task" , task ,"is completed")
    elif finish=="not completed":
        print("task",task,"is not completed")

def view(tasks):
    global finish
    viewing=input("Click to view tasks--->")
    if viewing=="":
        print(tasks)
        print (finish) 

def delete(tasks):
    deleted=input("Enter the task you want to delete: ")
    if task in tasks:
        tasks.remove(task)
        print("task has been removed")
        print(tasks)
    else:
        print("task not found")
    
add(tasks)
mark(tasks)
view(tasks) 
delete(tasks)

    