# -*- coding: utf-8 -*-
from tkinter import ttk
import tkinter as tk
from tkinter import scrolledtext
import openai

api_key = "key22222222222"
openai.api_key = api_key

def askChatGPT(messages):
    MODEL = "gpt-3.5-turbo"
    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=messages,
        temperature=0.1
    )
    return response['choices'][0]['message']['content']

def display_message(role, content):
    display_text.insert(tk.END, role + ": " + content + "\n")

def choose_girlfriend():
    global selected_girlfriend
    selected_girlfriend = girlfriend_combobox.get()
    root.destroy()

    if selected_girlfriend == "キャラクター1/角色1":
        messages.append({
            "role": "system",
            "content": "キャラクター設定1/角色1"
        })
        display_message("システム/系统", '你面前的是ｘｘｘｘｘ，ｘｘｘｘｘｘｘ。ｘｘｘｘｘｘ，你可以自由地与她对话，但是请不要强迫她。当你输入 quit 时，将终止程序')

    elif selected_girlfriend == "キャラクター2/角色2":
        messages.append({
            "role": "system",
            "content": "キャラクター設定2/角色2"
        })
        display_message("システム/系统", '你面前的是ｘｘｘｘｘ，ｘｘｘｘｘｘｘ。ｘｘｘｘｘｘ，你可以自由地与她对话，但是请不要强迫她。当你输入 quit 时，将终止程序')

    elif selected_girlfriend == "キャラクター3/角色3":
        messages.append({
            "role": "system",
            "content": "キャラクター設定3/角色3"
        })
        display_message("システム/系统", '你面前的是ｘｘｘｘｘ，ｘｘｘｘｘｘｘ。ｘｘｘｘｘｘ，你可以自由地与她对话，但是请不要强迫她。当你输入 quit 时，将终止程序')



def send_message():
    user_input = input_text.get("1.0", tk.END).strip()
    input_text.delete("1.0", tk.END)

    if user_input == 'quit':
        window.destroy()
        return

    message = {"role": "user", "content": user_input}
    messages.append(message)

    response = askChatGPT(messages)
    message = {"role": "assistant", "content": response}
    messages.append(message)
    display_message("you", user_input)
    if selected_girlfriend == "キャラクター1/角色1":
        display_message("キャラクター1の名前/角色1的名字", response)
    elif selected_girlfriend == "キャラクター2/角色2":
        display_message("キャラクター2の名前/角色2的名字", response)
    elif selected_girlfriend == "キャラクター3/角色3":
        display_message("キャラクター3の名前/角色3的名字", response)

messages = []


root = tk.Tk()
root.title("キャラクター選択/选择角色")
root.geometry("500x150")


label = tk.Label(root, text="好きなキャラクターのタイプを選んでください/请选择你喜欢的角色类型：", font=('Arial', 11))
label.pack(pady=10)

girlfriend_types = ["キャラクター1/角色1", "キャラクター2/角色2", "キャラクター3/角色3"]
girlfriend_combobox = ttk.Combobox(root, values=girlfriend_types, font=('Arial', 10), width=40)
girlfriend_combobox.pack(pady=10)

confirm_button = tk.Button(root, text="确定", command=choose_girlfriend, width=20, height=1)
confirm_button.pack(pady=10)

window = tk.Tk()
window.title("Chat Girl")
window.geometry("500x400")

input_label = tk.Label(window, text="入力ください/请输入：")
input_label.pack(pady=5)

input_text = scrolledtext.ScrolledText(window, width=50, height=4)
input_text.pack(pady=5)

send_button = tk.Button(window, text="送信/发送", command=send_message)
send_button.pack(pady=5)

display_label = tk.Label(window, text="メッセージ/对话内容：")
display_label.pack(pady=5)

display_text = scrolledtext.ScrolledText(window, width=50, height=15)
display_text.pack()


root.mainloop()


