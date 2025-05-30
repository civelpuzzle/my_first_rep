import tkinter as tk
from tkinter import filedialog, messagebox

def add_code_block(text_input):

	try:
		selected_text = text_input.get(tk.SEL_FIRST, tk.SEL_LAST)
		text_input.insert(tk.SEL_FIRST, "```\n")
		text_input.insert(tk.SEL_LAST, "\n```")
	except tk.TclError:
		cursop_pos = text_input.index(tk.INSERT)
		text_input.insert(cursop_pos, "\n```\n\n```\n")

def save_as_markdown(text_input):

	text = text_input.get("1.0", tk.END)
	if not text.strip():
		messagebox.showwarning("Пустое содержимое")
		return

	file_path = filedialog.asksaveasfilename(
		defaultextension=".md",
		filetypes = [("Markdown Files", "*.md"), ("All Files", "*.*")],
		title = "Сохранить как Markdown"
	)

	if file_path:
		try:
			with open(file_path, 'w', encoding = 'utf-8') as file:
				file.write(text)
			messagebox.showinfo("Успех", f"Файл успешно сохранён: \n{file_path}")
		except Exception as e:
			messagebox.showerror("Ошибка", f"Не удалось сохранить файл:\n{str(e)}")

def preview_markdown(text_input):
    """Показывает предпросмотр markdown"""
    text = text_input.get("1.0", tk.END)
    if not text.strip():
        messagebox.showwarning("Пустое содержимое", "Нечего показывать в предпросмотре.")
        return
    
    preview_window = tk.Toplevel()
    preview_window.title("Предпросмотр Markdown")
    preview_window.geometry("600x400")
    
    preview_text = tk.Text(
        preview_window, 
        font=('Helvetica', 12), 
        wrap=tk.WORD, 
        padx=10, 
        pady=10
    )
    preview_text.insert(tk.END, text)
    preview_text.config(state=tk.DISABLED)
    
    scrollbar = tk.Scrollbar(preview_window, command=preview_text.yview)
    preview_text.configure(yscrollcommand=scrollbar.set)
    
    preview_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

def clear_text(text_input):
    """Очищает поле ввода"""
    if messagebox.askyesno("Подтверждение", "Вы уверены, что хотите очистить текст?"):
        text_input.delete("1.0", tk.END)

def create_gui():
    """Создаёт графический интерфейс"""
    root = tk.Tk()
    root.title("Генератор Markdown для GitHub")
    root.geometry("800x600")
    root.configure(bg='#f0f0f0')
    
    # Заголовок
    title_label = tk.Label(
        root, 
        text="Генератор Markdown для GitHub", 
        font=('Helvetica', 16, 'bold'), 
        bg='#f0f0f0'
    )
    title_label.pack(pady=10)
    
    # Описание
    desc_label = tk.Label(
        root, 
        text="Введите текст ниже, и он будет преобразован в Markdown формат", 
        font=('Helvetica', 12), 
        bg='#f0f0f0'
    )
    desc_label.pack(pady=5)
    
    # Поле для ввода текста
    text_frame = tk.Frame(root, bg='#f0f0f0')
    text_frame.pack(pady=10, fill=tk.BOTH, expand=True)
    
    text_input = tk.Text(
        text_frame, 
        font=('Helvetica', 12), 
        wrap=tk.WORD, 
        padx=10, 
        pady=10,
        height=15
    )
    scrollbar = tk.Scrollbar(text_frame, command=text_input.yview)
    text_input.configure(yscrollcommand=scrollbar.set)
    
    text_input.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    # Кнопки
    buttons_frame = tk.Frame(root, bg='#f0f0f0')
    buttons_frame.pack(pady=10)
    
    # Кнопка добавления блока кода
    code_btn = tk.Button(
        buttons_frame, 
        text="Добавить блок кода", 
        command=lambda: add_code_block(text_input),
        font=('Helvetica', 12),
        bg='#4CAF50',
        fg='white'
    )
    code_btn.pack(side=tk.LEFT, padx=5)
    
    # Кнопка сохранения
    save_btn = tk.Button(
        buttons_frame, 
        text="Сохранить как Markdown", 
        command=lambda: save_as_markdown(text_input),
        font=('Helvetica', 12),
        bg='#2196F3',
        fg='white'
    )
    save_btn.pack(side=tk.LEFT, padx=5)
    
    # Кнопка предпросмотра
    preview_btn = tk.Button(
        buttons_frame, 
        text="Предпросмотр", 
        command=lambda: preview_markdown(text_input),
        font=('Helvetica', 12),
        bg='#FF9800',
        fg='white'
    )
    preview_btn.pack(side=tk.LEFT, padx=5)
    
    # Кнопка очистки
    clear_btn = tk.Button(
        buttons_frame, 
        text="Очистить", 
        command=lambda: clear_text(text_input),
        font=('Helvetica', 12),
        bg='#f44336',
        fg='white'
    )
    clear_btn.pack(side=tk.LEFT, padx=5)
    
    root.mainloop()

if __name__ == "__main__":
    create_gui()