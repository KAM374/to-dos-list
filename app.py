app = Flask(__name__)

@app.route('/')
def todo_list():
    return "To-Do List"
 while True:
     tasks = []
      i=0
      i=i+1
      action = input("Type 'add', 'delete', 'quit': ")
    
      if action == "add":
        task = input("enter a task: ")
        tasks.append(task)
        
      elif action == "delete":
        num = int(input("enter the task number to delete: "))
        tasks.pop(num-1)
        print("Your To-Do List \n",  tasks)
        
      elif  action == "quit":
        print("Your To-Do List \n",  tasks)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)
