tasks = []
def add_task(task_name):
    """Thêm một công việc mới vào danh sách."""
    tasks.append(task_name)
    print(f"Đã thêm công việc: '{task_name}'")

def list_task(tasks):
    for i in tasks:
        if i["completed"] == "True":
            print(f'[x] {i["name"]}')
        else:
            print(f'[ ] {i["name"]}')

def complete_task(task_index):
    for i in range(len(tasks)):
        print(f'{i+1}. {tasks[i]}')
        if (task_index - 1 == i):
            tasks[i][1] = "True"

# --- Điểm bắt đầu của chương trình ---
if __name__ == "__main__":
    print("Chào mừng đến với ứng dụng To-Do List!")
    add_task("Học bài GitHub")
    add_task("Học bài Git")
    for i in range(2):
        name = input('Nhập tên công việc: ')
        completed_input = input("Nhập trạng thái hoàn thành (True/False): ").strip().lower()
        completed = "True" 
        if completed_input == "true" else "False"

        dic = {"name" : name, "completed" : completed}
        add_task(dic)
    
    complete_task(1)
    list_task(tasks)