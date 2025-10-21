tasks = []
def delete_task(task_index):
    """Xóa một công việc khỏi danh sách dựa trên chỉ số (tính từ 1)."""
    if 1 <= task_index <= len(tasks):
        removed_task = tasks.pop(task_index - 1)
        print(f"Đã xóa công việc: '{removed_task['name']}'")
    else:
        print("Lỗi: Chỉ số không hợp lệ. Không có công việc nào bị xóa.")
tasks = [
    {"name": "Học Git", "completed": "False"},
    {"name": "Làm bài tập", "completed": "True"},
    {"name": "Dọn phòng", "completed": "False"}
]
try:
    index = int(input("🔸 Nhập số thứ tự công việc bạn muốn xóa: "))
    delete_task(index)
except ValueError:
    print("❗ Vui lòng nhập một số hợp lệ.")