import tkinter as tk
import sys
from tkinter import messagebox as msg
from PIL import Image, ImageTk

class AppPage(tk.Frame):

    def __init__(self, parent, App):
        self.app = App
        self.settings = App.settings
        self.current_contact = self.settings.contacts[0]
        self.last_current_contact_index = 0
        self.update_mode = False
        self.contacts_index = []

        super().__init__(parent) #parent = window.container
        self.grid(row=0, column=0, sticky="nsew")

        parent.grid_rowconfigure(0, weight=1)
        parent.grid_columnconfigure(0, weight=1)

        self.create_left_frame()
        self.create_right_frame()
        self.config_left_and_right_frame()      

    def create_left_frame(self):
        self.left_frame = tk.Frame(self, bg="pink")
        self.left_frame.grid(row=0, column=0, sticky="nsew")

        #self.create_left_header()
        self.create_left_content()

    def create_right_frame(self):
        self.right_frame = tk.Frame(self, bg="ivory", width=2*self.settings.width//3)
        self.right_frame.grid(row=0, column=1, sticky="nsew")

        self.create_right_header()
        self.create_right_content()
        self.create_right_footer()

    def config_left_and_right_frame(self):
        self.grid_columnconfigure(0, weight=1) # 1/3
        self.grid_columnconfigure(1, weight=2) # 2/3
        self.grid_rowconfigure(0, weight=1)

    def create_left_header(self):
        frame_w = self.settings.width//5
        frame_h = self.settings.height//5
        self.left_header = tk.Frame(self.left_frame, width=frame_w, height=frame_h)
        self.left_header.pack()

        image = Image.open(self.settings.logo)
        i_w, i_h = image.size
        ratio = i_w/frame_w
        new_size = (int(i_w/ratio), int(i_h/ratio)) # (x,y)
        image = image.resize(new_size)

        self.label_logo = tk.Label(self.left_header, image=self.logo)
        self.label_logo.pack()

    def show_list_contacts_in_listbox(self):
        contacts = self.settings.contacts
        # for contact in contacts:
        #   for phone, info in contact.items():
        #       capital = f"{info['stock']} {info['capital']}"
        #       self.contacts_list_box.insert("end", capital)
        for index in self.contacts_index:
            contact = contacts[index]
            for stock, info in contact.items():
                product_name = f"{info['product']}"
                self.contacts_list_box.insert("end", product_name)

    def create_left_content(self):
        frame_w = self.settings.width//3
        frame_h = 4*self.settings.height//5
        self.left_content = tk.Frame(self.left_frame, width=frame_w, height=frame_h, bg="papayawhip")
        self.left_content.pack(fill="x")

        self.contacts_list_box = tk.Listbox(self.left_content, bg="papayawhip", fg="black", font=("Arial", 12), height=frame_h)
        self.contacts_list_box.pack(side="left", fill="both", expand=True)

        self.contacts_scroll = tk.Scrollbar(self.left_content)
        self.contacts_scroll.pack(side="right", fill="y")

        contacts = self.settings.contacts
        self.contacts_index = []
        counter = 0
        for contact in contacts:
            self.contacts_index.append(counter)
            counter += 1
        self.show_list_contacts_in_listbox()

        self.contacts_list_box.configure(yscrollcommand=self.contacts_scroll.set) # set di Scroll
        self.contacts_scroll.configure(command=self.contacts_list_box.yview) # yview di Listbox

        self.contacts_list_box.bind("<<ListboxSelect>>", self.clicked_item_inListBox)

    def show_all_contact_in_listbox(self):
        self.contacts_list_box.delete(0, 'end')
        contacts = self.settings.contacts
        self.contacts_index = []
        counter = 0
        for contact in contacts:
            self.contacts_index.append(counter)
            counter += 1
        self.show_list_contacts_in_listbox()


    def clicked_item_inListBox(self, event):
        if not self.update_mode:
            selection = event.widget.curselection()
            try :
                clicked_item_index = selection[0]
                self.last_current_contact_index = clicked_item_index
            except IndexError:
                clicked_item_index = self.last_current_contact_index
            
            index = self.contacts_index[clicked_item_index]
            self.current_contact = self.settings.contacts[index]
            print(clicked_item_index,"=>",index)
            for stock, info in self.current_contact.items():
                stock = stock
                product_name = info['product']
                capitals = info['capital']
                selles_price = info['selles_price']
                net_profit = info['net_profit']

            #self.product_name_label.configure(text=product_name)
            self.table_info[0][1].configure(text=stock)
            self.table_info[1][1].configure(text=capitals)
            self.table_info[2][1].configure(text=selles_price)
            self.table_info[3][1].configure(text=net_profit)

    def create_right_header(self):
        frame_w = 2*self.settings.width//3
        frame_h = self.settings.height//5

        self.right_header = tk.Frame(self.right_frame, width=frame_w, height=frame_h, bg="ivory")
        self.right_header.pack()
        self.create_detail_right_header()

    def create_detail_right_header(self):
        frame_w = 2*self.settings.width//3
        frame_h = self.settings.height//5

        self.detail_header = tk.Frame(self.right_header, width=frame_w, height=frame_h, bg="green")
        self.detail_header.grid(row=0, column=0, sticky="nsew")

        data_dictionary = list(self.current_contact.values())[0]
        full_name = f"{data_dictionary['product']}"
        self.virt_img = tk.PhotoImage(width=1, height=1)
        self.full_name_label = tk.Label(self.detail_header, text=full_name, font=("Arial", 30), width=frame_w, height=frame_h, image=self.virt_img, compound='c', bg="ivory")
        self.full_name_label.pack()

        self.right_header.grid_rowconfigure(0, weight=1)
        self.right_header.grid_columnconfigure(0, weight=1)


    def create_right_content(self):
        frame_w = 2*self.settings.width//3
        frame_h = 3*(4*self.settings.height//5)//4

        self.right_content = tk.Frame(self.right_frame, width=frame_w, height=frame_h, bg="ivory")
        self.right_content.pack(expand=True, pady=90)
        self.create_detail_right_content()

    def create_detail_right_content(self):
        frame_w = 2*self.settings.width//3
        frame_h = 3*(4*self.settings.height//5)//4

        self.detail_content = tk.Frame(self.right_content, width=frame_w, height=frame_h, bg="ivory")
        self.detail_content.grid(row=0, column=0, sticky="nsew")

        for stock, info in self.current_contact.items():
            info = [
                ['Stok Produk :', stock],
                ['Modal :', info['capital']],
                ['Harga Jual :', info['selles_price']],
                ['Keuntungan :', info['net_profit']]
            ]
        self.table_info = []
        rows, columns = len(info), len(info[0]) # 3, 2
        for row in range(rows):
            aRow = []
            for column in range(columns):
                label = tk.Label(self.detail_content, text=info[row][column], font=("Arial", 12), bg="ivory")
                aRow.append(label)
                if column == 0:
                    sticky = "e"
                else:
                    sticky = "w"
                label.grid(row=row, column=column, sticky=sticky)
            self.table_info.append(aRow)


        self.right_content.grid_rowconfigure(0, weight=1)
        self.right_content.grid_columnconfigure(0, weight=1)


    def create_right_footer(self):
        frame_w = 2*self.settings.width//3
        frame_h = (4*self.settings.height//5)//4

        self.right_footer = tk.Frame(self.right_frame, width=frame_w, height=frame_h, bg="ivory")
        self.right_footer.pack(expand=True)

        self.create_detail_right_footer()


    def create_detail_right_footer(self):
        frame_w = 2*self.settings.width//3
        frame_h = (4*self.settings.height//5)//4

        self.detail_footer = tk.Frame(self.right_footer, width=frame_w, height=frame_h, bg="ivory")
        self.detail_footer.grid(row=0, column=0, sticky="nsew")

        features = ['Add', 'Delete', 'Edit', '             [ EXIT ]']
        commands = [self.clicked_add_new_btn, self.clicked_delete_btn, self.clicked_update_btn, self.quit]
        self.buttons_features = []
        for feature in features:
            button = tk.Button(self.detail_footer, text=feature, bg="ivory", fg="darkslategray", bd=0, font=("Arial", 12, "bold"), command=commands[features.index(feature)])
            button.grid(row=0, column=features.index(feature), sticky="nsew", padx=20)
            self.buttons_features.append(button)

        self.right_footer.grid_rowconfigure(0, weight=1)
        self.right_footer.grid_columnconfigure(0, weight=1)

    def recreate_right_frame(self):
        #self.clicked_update_btn.destroy()
        self.detail_update_content.destroy()
        self.detail_update_footer.destroy()

        #RECREATE HEADER
        self.create_detail_right_header()

        #RECREATE CONTENT
        self.create_detail_right_content()

        #RECREATE FOOTER
        self.create_detail_right_footer()

    def recreate_right_frame_after_delete(self):

        self.detail_header.destroy()
        self.detail_content.destroy()
        self.detail_footer.destroy()

        #RECREATE HEADER
        self.create_detail_right_header()

        #RECREATE CONTENT
        self.create_detail_right_content()

        #RECREATE FOOTER
        self.create_detail_right_footer()

    def recreate_right_frame_after_add_new(self):
        self.detail_add_new_header.destroy()
        self.detail_add_new_content.destroy()
        self.detail_add_new_footer.destroy()

        #RECREATE HEADER
        self.create_detail_right_header()

        #RECREATE CONTENT
        self.create_detail_right_content()

        #RECREATE FOOTER
        self.create_detail_right_footer()
    def clicked_update_btn(self):
        self.update_mode = True
        frame_w = 2*self.settings.width//3
        frame_h = self.settings.height//5

        self.detail_content.destroy()
        self.detail_footer.destroy()

        self.detail_update_content = tk.Frame(self.right_content, width=frame_w, height=frame_h, bg="ivory")
        self.detail_update_content.grid(row=0, column=0, sticky="nsew")

        for stock, info in self.current_contact.items():
            info = [
                ['Product :', info['product']],
                ['Modal :', info['capital']],
                ['Stok Produk :', stock],
                ['Harga Jual :', info['selles_price']],
                ['Keuntungan :', info['net_profit']]
            ]
        self.table_info = []
        self.entry_update_contact_vars = [tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar()]
        rows, columns = len(info), len(info[0]) # 3, 2
        for row in range(rows):
            aRow = []
            for column in range(columns):
                if column == 0:
                    label = tk.Label(self.detail_update_content, text=info[row][column], font=("Arial", 12), bg="ivory")
                    sticky = "e"
                    aRow.append(label)
                    label.grid(row=row, column=column, sticky=sticky)
                else:
                    entry = tk.Entry(self.detail_update_content, font=("Arial", 12), bg="ivory", textvariable=self.entry_update_contact_vars[row])
                    entry.insert(0, info[row][column])
                    sticky = "w"
                    aRow.append(entry)
                    entry.grid(row=row, column=column, sticky=sticky)
            self.table_info.append(aRow)

        self.right_content.grid_rowconfigure(0, weight=1)
        self.right_content.grid_columnconfigure(0, weight=1)

        frame_w = 2*self.settings.width//3
        frame_h = (4*self.settings.height//5)//4

        self.detail_update_footer = tk.Frame(self.right_footer, width=frame_w, height=frame_h, bg="ivory")
        self.detail_update_footer.grid(row=0, column=0, sticky="nsew")

        features = ['Save', 'Cancel']
        commands = [self.clicked_save_contact_btn, self.clicked_cancel_contact_btn]
        self.buttons_features = []
        for feature in features:
            button = tk.Button(self.detail_update_footer, text=feature, bg="ivory", fg="darkslategray", bd=0, font=("Arial", 12, "bold"), command=commands[features.index(feature)])
            button.grid(row=0, column=features.index(feature), sticky="nsew", padx=20)
            self.buttons_features.append(button)

        self.right_footer.grid_rowconfigure(0, weight=1)
        self.right_footer.grid_columnconfigure(0, weight=1)


    def clicked_delete_btn(self):
        self.update_mode = True
        #print(self.last_current_contact_index)

        confirm = msg.askyesnocancel('Contactapp Delete Confirmation', 'Are you sure to delete this contact ?')
        index  = self.last_current_contact_index
        if confirm:
            self.settings.contacts.pop(index)
            #self.settings.save_data_to_json()
            self.last_current_contact_index = 0
            self.current_contact = self.settings.contacts[self.last_current_contact_index]

            self.recreate_right_frame_after_delete()
            self.show_all_contact_in_listbox()

        self.update_mode = False

    def clicked_add_new_btn(self):
        self.update_mode = True

        self.detail_header.destroy()
        self.detail_content.destroy()
        self.detail_footer.destroy()

        frame_w = 2*self.settings.width//3
        frame_h = self.settings.height//5

        self.detail_add_new_header = tk.Frame(self.right_header, width=frame_w, height=frame_h, bg="ivory")
        self.detail_add_new_header.grid(row=0, column=0, sticky="nsew")

        self.virt_img = tk.PhotoImage(width=1, height=1)
        self.add_new_label = tk.Label(self.detail_add_new_header, text="Add New Product", font=("Arial", 30), width=frame_w, height=frame_h, image=self.virt_img, compound='c', bg="ivory")
        self.add_new_label.pack()

        self.right_header.grid_rowconfigure(0, weight=1)
        self.right_header.grid_columnconfigure(0, weight=1)

        frame_w = 2*self.settings.width//3
        frame_h = 3*(4*self.settings.height//5)//4

        self.detail_add_new_content = tk.Frame(self.right_content, width=frame_w, height=frame_h, bg="ivory")
        self.detail_add_new_content.grid(row=0, column=0, sticky="nsew")

        info = [
            ['Product :', None],
            ['Modal :', None],
            ['Stok Produk :', None],
            ['Harga Jual :', None],
            ['Keuntungan :', None]
        ]
        self.table_info = []
        self.entry_update_contact_vars = [tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar()]
        rows, columns = len(info), len(info[0]) # 3, 2
        for row in range(rows):
            aRow = []
            for column in range(columns):
                if column == 0:
                    label = tk.Label(self.detail_add_new_content, text=info[row][column], font=("Arial", 12), bg="ivory")
                    sticky = "e"
                    aRow.append(label)
                    label.grid(row=row, column=column, sticky=sticky)
                else:
                    entry = tk.Entry(self.detail_add_new_content, font=("Arial", 12), bg="ivory", textvariable=self.entry_update_contact_vars[row])
                    sticky = "w"
                    aRow.append(entry)
                    entry.grid(row=row, column=column, sticky=sticky)
            self.table_info.append(aRow)


        self.right_content.grid_rowconfigure(0, weight=1)
        self.right_content.grid_columnconfigure(0, weight=1)

        frame_w = 2*self.settings.width//3
        frame_h = (4*self.settings.height//5)//4

        self.detail_add_new_footer = tk.Frame(self.right_footer, width=frame_w, height=frame_h, bg="ivory")
        self.detail_add_new_footer.grid(row=0, column=0, sticky="nsew")

        features = ['Save', 'Cancel']
        commands = [self.clicked_save_add_new_contact_btn, self.clicked_cancel_add_new_contact_btn]
        self.buttons_features = []
        for feature in features:
            button = tk.Button(self.detail_add_new_footer, text=feature, bg="ivory", fg="darkslategray", bd=0, font=("Arial", 12, "bold"), command=commands[features.index(feature)])
            button.grid(row=0, column=features.index(feature), sticky="nsew", padx=20)
            self.buttons_features.append(button)

        self.right_footer.grid_rowconfigure(0, weight=1)
        self.right_footer.grid_columnconfigure(0, weight=1)


    def clicked_save_contact_btn(self):
        self.update_mode = False

        confirm = msg.askyesnocancel('Data Save Confirmation', 'Are you sure to update this data ?')
        
        index = self.last_current_contact_index
        if confirm:
            stock = self.entry_update_contact_vars[0].get()
            product_name = self.entry_update_contact_vars[1].get()
            capital = self.entry_update_contact_vars[2].get()
            selles_price = self.entry_update_contact_vars[3].get()
            net_profit = self.entry_update_contact_vars[4].get()
            self.settings.contacts[index] = {
                stock : {
                    "Produk" : product_name,
                    "Modal" : capital,
                    "Harga Jual" : selles_price,
                    "Keuntungan" : net_profit
                }
            }
        self.current_contact = self.settings.contacts[index]

        self.recreate_right_frame()

        self.contacts_list_box.delete(0, 'end')
        self.show_list_contacts_in_listbox()


    def clicked_cancel_contact_btn(self):
        self.update_mode = False

        self.recreate_right_frame()

    def clicked_save_add_new_contact_btn(self):
        self.update_mode = False

        confirm = msg.askyesnocancel('Contactapp Save Confirmation', 'Are you sure to add this contact ?')
        
        if confirm:
            product = self.entry_update_contact_vars[0].get()
            capital = self.entry_update_contact_vars[1].get()
            stock = self.entry_update_contact_vars[2].get()
            selles_price = self.entry_update_contact_vars[3].get()
            net_profit = self.entry_update_contact_vars[4].get()
            new_contact= {
                stock : {
                    "product" : product,
                    "capital" :capital,
                    "selles_price" : selles_price,
                    "net_profit" : net_profit
                }
            }
            self.settings.contacts.append(new_contact)
            #self.settings.save_data_to_json()
        index = len(self.settings.contacts)-1
        self.last_current_contact_index = index
        self.current_contact = self.settings.contacts[self.last_current_contact_index]

        self.recreate_right_frame_after_add_new()

        self.contacts_list_box.delete(0, 'end')
        self.show_all_contact_in_listbox()

    def clicked_cancel_add_new_contact_btn(self):
        pass