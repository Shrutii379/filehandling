# import os
# import tkinter as tk
# from tkinter import ttk
# from pathlib import Path
# from datetime import datetime

# # ---------------------------------------------------------------------------
# # Palette — deep slate workspace with a single warm amber accent.
# # ---------------------------------------------------------------------------
# BG        = "#1c2129"   # app background
# PANEL     = "#242a35"   # sidebar / cards
# PANEL_ALT = "#2b3240"   # input field background
# BORDER    = "#3a4250"
# TEXT      = "#e7eaf0"
# SUBTEXT   = "#8b93a3"
# ACCENT    = "#e0a458"   # amber — the one accent, used sparingly
# ACCENT_DK = "#c98d42"
# OK_CLR    = "#6fbf8b"
# ERR_CLR   = "#d97a7a"
# MONO      = ("Consolas", 10)
# SANS      = ("Segoe UI", 10)
# SANS_B    = ("Segoe UI Semibold", 11)


# ACTIONS = {
#     "create_file":   {"label": "Create File",   "fields": ["Filename", "Content"]},
#     "read_file":     {"label": "Read File",      "fields": ["Filename"]},
#     "update_file":   {"label": "Append to File", "fields": ["Filename", "Content to add"]},
#     "delete_file":   {"label": "Delete File",    "fields": ["Filename"]},
#     "create_folder": {"label": "Create Folder",  "fields": ["Folder name"]},
#     "delete_folder": {"label": "Delete Folder",  "fields": ["Folder name"]},
#     "rename_file":   {"label": "Rename File",    "fields": ["Current filename", "New filename"]},
# }


# class FileManagerApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Filekeep")
#         self.root.geometry("860x560")
#         self.root.minsize(760, 480)
#         self.root.configure(bg=BG)

#         self.active_action = None
#         self.field_vars = {}

#         self._build_style()
#         self._build_layout()
#         self._select_action("create_file")

#     # ------------------------------------------------------------------ style
#     def _build_style(self):
#         style = ttk.Style(self.root)
#         style.theme_use("clam")

#         style.configure("Side.TFrame", background=PANEL)
#         style.configure("Main.TFrame", background=BG)

#         style.configure(
#             "Nav.TButton",
#             background=PANEL, foreground=SUBTEXT,
#             font=SANS, borderwidth=0, anchor="w",
#             padding=(14, 10),
#         )
#         style.map(
#             "Nav.TButton",
#             background=[("active", PANEL_ALT)],
#             foreground=[("active", TEXT)],
#         )

#         style.configure(
#             "NavActive.TButton",
#             background=PANEL_ALT, foreground=ACCENT,
#             font=("Segoe UI Semibold", 10), borderwidth=0, anchor="w",
#             padding=(14, 10),
#         )
#         style.map("NavActive.TButton", background=[("active", PANEL_ALT)])

#         style.configure(
#             "Run.TButton",
#             background=ACCENT, foreground="#231a0f",
#             font=("Segoe UI Semibold", 10), borderwidth=0, padding=(16, 8),
#         )
#         style.map("Run.TButton", background=[("active", ACCENT_DK)])

#     # ----------------------------------------------------------------- layout
#     def _build_layout(self):
#         # ---- sidebar --------------------------------------------------
#         sidebar = ttk.Frame(self.root, style="Side.TFrame", width=200)
#         sidebar.pack(side="left", fill="y")
#         sidebar.pack_propagate(False)

#         brand = tk.Frame(sidebar, bg=PANEL)
#         brand.pack(fill="x", pady=(22, 18), padx=16)
#         tk.Label(brand, text="FILEKEEP", bg=PANEL, fg=TEXT,
#                   font=("Segoe UI Semibold", 14)).pack(anchor="w")
#         tk.Label(brand, text="local file & folder tools", bg=PANEL, fg=SUBTEXT,
#                   font=("Segoe UI", 8)).pack(anchor="w")

#         tk.Frame(sidebar, bg=BORDER, height=1).pack(fill="x", padx=16, pady=(0, 8))

#         self.nav_buttons = {}
#         for key, meta in ACTIONS.items():
#             btn = ttk.Button(
#                 sidebar, text=meta["label"], style="Nav.TButton",
#                 command=lambda k=key: self._select_action(k),
#             )
#             btn.pack(fill="x", padx=8, pady=1)
#             self.nav_buttons[key] = btn

#         # ---- main area --------------------------------------------------
#         main = ttk.Frame(self.root, style="Main.TFrame")
#         main.pack(side="left", fill="both", expand=True)

#         self.title_lbl = tk.Label(main, text="", bg=BG, fg=TEXT, font=("Segoe UI Semibold", 15))
#         self.title_lbl.pack(anchor="w", padx=24, pady=(22, 2))

#         self.subtitle_lbl = tk.Label(main, text="", bg=BG, fg=SUBTEXT, font=SANS)
#         self.subtitle_lbl.pack(anchor="w", padx=24, pady=(0, 14))

#         self.form_frame = tk.Frame(main, bg=BG)
#         self.form_frame.pack(fill="x", padx=24)

#         run_row = tk.Frame(main, bg=BG)
#         run_row.pack(fill="x", padx=24, pady=(6, 14))
#         self.run_btn = ttk.Button(run_row, text="Run", style="Run.TButton", command=self._run_action)
#         self.run_btn.pack(side="left")

#         tk.Frame(main, bg=BORDER, height=1).pack(fill="x", padx=24, pady=(0, 10))

#         tk.Label(main, text="ACTIVITY LOG", bg=BG, fg=SUBTEXT,
#                  font=("Segoe UI Semibold", 8)).pack(anchor="w", padx=24)

#         console_wrap = tk.Frame(main, bg=PANEL, highlightthickness=1, highlightbackground=BORDER)
#         console_wrap.pack(fill="both", expand=True, padx=24, pady=(6, 20))

#         self.console = tk.Text(
#             console_wrap, bg=PANEL, fg=TEXT, insertbackground=TEXT,
#             font=MONO, relief="flat", padx=12, pady=10, wrap="word", state="disabled",
#         )
#         self.console.pack(fill="both", expand=True)
#         self.console.tag_configure("ok", foreground=OK_CLR)
#         self.console.tag_configure("err", foreground=ERR_CLR)
#         self.console.tag_configure("dim", foreground=SUBTEXT)

#     # ------------------------------------------------------------- selection
#     def _select_action(self, key):
#         self.active_action = key
#         meta = ACTIONS[key]

#         for k, btn in self.nav_buttons.items():
#             btn.configure(style="NavActive.TButton" if k == key else "Nav.TButton")

#         self.title_lbl.configure(text=meta["label"])
#         self.subtitle_lbl.configure(text=self._subtitle_for(key))

#         for child in self.form_frame.winfo_children():
#             child.destroy()
#         self.field_vars = {}

#         for field in meta["fields"]:
#             row = tk.Frame(self.form_frame, bg=BG)
#             row.pack(fill="x", pady=5)
#             tk.Label(row, text=field, bg=BG, fg=SUBTEXT, font=SANS, width=16, anchor="w").pack(side="left")

#             multiline = "Content" in field
#             if multiline:
#                 entry = tk.Text(row, height=3, bg=PANEL_ALT, fg=TEXT, insertbackground=TEXT,
#                                  relief="flat", font=SANS, highlightthickness=1,
#                                  highlightbackground=BORDER, highlightcolor=ACCENT)
#                 entry.pack(side="left", fill="x", expand=True, ipady=4)
#             else:
#                 var = tk.StringVar()
#                 entry = tk.Entry(row, textvariable=var, bg=PANEL_ALT, fg=TEXT, insertbackground=TEXT,
#                                   relief="flat", font=SANS, highlightthickness=1,
#                                   highlightbackground=BORDER, highlightcolor=ACCENT)
#                 entry.pack(side="left", fill="x", expand=True, ipady=5)

#             self.field_vars[field] = entry

#     @staticmethod
#     def _subtitle_for(key):
#         return {
#             "create_file": "Make a new file and write its starting content.",
#             "read_file": "Display the contents of an existing file.",
#             "update_file": "Append text to the end of an existing file.",
#             "delete_file": "Permanently remove a file.",
#             "create_folder": "Make a new, empty folder.",
#             "delete_folder": "Remove an empty folder.",
#             "rename_file": "Rename an existing file in place.",
#         }[key]

#     # ---------------------------------------------------------------- helpers
#     def _field(self, name):
#         widget = self.field_vars[name]
#         if isinstance(widget, tk.Text):
#             return widget.get("1.0", "end").rstrip("\n")
#         return widget.get().strip()

#     def _log(self, msg, kind="dim"):
#         self.console.configure(state="normal")
#         stamp = datetime.now().strftime("%H:%M:%S")
#         prefix = {"ok": "  OK   ", "err": "  ERR  "}.get(kind, "  ...  ")
#         self.console.insert("end", f"{stamp}{prefix}", ("dim",))
#         self.console.insert("end", f"{msg}\n", (kind,))
#         self.console.see("end")
#         self.console.configure(state="disabled")

#     # ---------------------------------------------------------------- actions
#     def _run_action(self):
#         key = self.active_action
#         try:
#             if key == "create_file":
#                 self._create_file()
#             elif key == "read_file":
#                 self._read_file()
#             elif key == "update_file":
#                 self._update_file()
#             elif key == "delete_file":
#                 self._delete_file()
#             elif key == "create_folder":
#                 self._create_folder()
#             elif key == "delete_folder":
#                 self._delete_folder()
#             elif key == "rename_file":
#                 self._rename_file()
#         except Exception as e:
#             self._log(f"unexpected error — {e}", "err")

#     def _create_file(self):
#         name = self._field("Filename")
#         content = self._field("Content")
#         if not name:
#             self._log("filename is required", "err")
#             return
#         path = Path(name)
#         if path.exists():
#             self._log(f"'{name}' already exists", "err")
#             return
#         with open(name, "w") as f:
#             f.write(content)
#         self._log(f"created '{name}'", "ok")

#     def _read_file(self):
#         name = self._field("Filename")
#         path = Path(name)
#         if not path.exists():
#             self._log(f"'{name}' does not exist", "err")
#             return
#         with open(name, "r") as f:
#             data = f.read()
#         self._log(f"read '{name}' ({len(data)} chars)", "ok")
#         self.console.configure(state="normal")
#         self.console.insert("end", (data if data else "(file is empty)") + "\n", ("dim",))
#         self.console.see("end")
#         self.console.configure(state="disabled")

#     def _update_file(self):
#         name = self._field("Filename")
#         addition = self._field("Content to add")
#         path = Path(name)
#         if not path.exists():
#             self._log(f"'{name}' does not exist", "err")
#             return
#         with open(name, "a") as f:
#             f.write(addition)
#         self._log(f"appended to '{name}'", "ok")

#     def _delete_file(self):
#         name = self._field("Filename")
#         if not os.path.exists(name):
#             self._log(f"'{name}' does not exist", "err")
#             return
#         os.remove(name)
#         self._log(f"deleted '{name}'", "ok")

#     def _create_folder(self):
#         name = self._field("Folder name")
#         path = Path(name)
#         if path.exists():
#             self._log(f"folder '{name}' already exists", "err")
#             return
#         os.mkdir(name)
#         self._log(f"created folder '{name}'", "ok")

#     def _delete_folder(self):
#         name = self._field("Folder name")
#         path = Path(name)
#         if not path.exists():
#             self._log(f"folder '{name}' does not exist", "err")
#             return
#         os.rmdir(name)
#         self._log(f"deleted folder '{name}'", "ok")

#     def _rename_file(self):
#         old = self._field("Current filename")
#         new = self._field("New filename")
#         path = Path(old)
#         if not path.exists():
#             self._log(f"'{old}' does not exist", "err")
#             return
#         os.rename(old, new)
#         self._log(f"renamed '{old}' → '{new}'", "ok")


# if __name__ == "__main__":
#     root = tk.Tk()
#     app = FileManagerApp(root)
#     root.mainloop()


import os
from pathlib import Path
import tkinter as tk
from tkinter import simpledialog

class PastelFileManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Manager")
        self.root.geometry("700x450")
        
        # --- Subtle Pastel Color Palette ---
        self.bg_color = "#F4F1EA"      # Warm subtle off-white/cream
        self.btn_color = "#E8DED1"     # Pastel warm beige
        self.btn_hover = "#C8D5B9"     # Pastel sage green (hover)
        self.text_bg = "#FFFFFF"       # Clean white for output area
        self.text_fg = "#4A443F"       # Soft dark brown/grey for readability
        self.accent = "#8FA596"        # Deeper muted green for accents
        
        self.root.configure(bg=self.bg_color)
        
        # --- UI Layout ---
        # Header
        title_label = tk.Label(
            root, text="File & Folder Manager", 
            font=("Helvetica", 18, "bold"), 
            bg=self.bg_color, fg=self.text_fg
        )
        title_label.pack(pady=(20, 10))

        # Main Layout Frame
        main_frame = tk.Frame(root, bg=self.bg_color)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=25, pady=(0, 25))

        # Left Panel (Buttons)
        btn_frame = tk.Frame(main_frame, bg=self.bg_color)
        btn_frame.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 20))

        # Right Panel (Terminal/Output display)
        output_frame = tk.Frame(main_frame, bg=self.bg_color)
        output_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Output Text Box
        self.output_box = tk.Text(
            output_frame, font=("Courier", 11), bg=self.text_bg, fg=self.text_fg, 
            relief=tk.FLAT, padx=15, pady=15, highlightthickness=1, highlightbackground=self.btn_color
        )
        self.output_box.pack(fill=tk.BOTH, expand=True)
        self.log("Welcome to the File Manager.\nSelect an action from the left panel to begin.")

        # --- Menu Buttons ---
        buttons = [
            ("Create File", self.create_file),
            ("Read File", self.read_file),
            ("Update File", self.update_file),
            ("Delete File", self.del_file),
            ("Create Folder", self.create_folder),
            ("Delete Folder", self.del_folder),
            ("Rename File", self.rename_file)
        ]

        for text, command in buttons:
            btn = tk.Button(
                btn_frame, text=text, command=command,
                font=("Helvetica", 11), bg=self.btn_color, fg=self.text_fg,
                activebackground=self.accent, activeforeground="white",
                relief=tk.FLAT, width=18, pady=8, cursor="hand2"
            )
            btn.pack(pady=6)
            
            # Hover effects
            btn.bind("<Enter>", lambda e, b=btn: b.config(bg=self.btn_hover))
            btn.bind("<Leave>", lambda e, b=btn: b.config(bg=self.btn_color))

    # --- Helper Method ---
    def log(self, message):
        """Displays messages in the UI text box instead of the console."""
        self.output_box.insert(tk.END, "\n" + message)
        self.output_box.see(tk.END) # Auto-scroll to bottom

    # --- File Operations ---
    def create_file(self):
        filename = simpledialog.askstring("Create File", "Enter your filename:")
        if not filename: return
        
        path = Path(filename)
        if path.exists():
            self.log(f"⚠️ File '{filename}' already exists.")
        else:
            content = simpledialog.askstring("Create File", f"Enter content for {filename}:")
            content = content if content else ""
            with open(filename, 'w') as file:
                file.write(content)
            self.log(f"✅ File '{filename}' created successfully.")

    def read_file(self):
        filename = simpledialog.askstring("Read File", "Enter your filename:")
        if not filename: return
        
        path = Path(filename)
        if path.exists():
            with open(filename, 'r') as file:
                content = file.read()
            self.log(f"📄 Contents of '{filename}':\n{content}")
        else:
            self.log(f"❌ File '{filename}' does not exist.")

    def update_file(self):
        filename = simpledialog.askstring("Update File", "Enter name of your file:")
        if not filename: return
        
        path = Path(filename)
        if path.exists():
            content = simpledialog.askstring("Update File", "Enter your file content to append:")
            if content:
                with open(filename, 'a') as file:
                    file.write("\n" + content)
                self.log(f"✅ Content added successfully to '{filename}'.")
        else:
            self.log(f"❌ File '{filename}' does not exist.")

    def del_file(self):
        filename = simpledialog.askstring("Delete File", "Enter your filename:")
        if not filename: return
        
        if os.path.exists(filename):
            os.remove(filename)
            self.log(f"🗑️ File '{filename}' deleted successfully.")
        else:
            self.log(f"❌ File '{filename}' does not exist.")

    def create_folder(self):
        foldername = simpledialog.askstring("Create Folder", "Enter your folder name:")
        if not filename: return
        
        path = Path(foldername)
        if path.exists():
            self.log(f"⚠️ Folder '{foldername}' already exists.")
        else:
            os.mkdir(foldername)
            self.log(f"✅ Folder '{foldername}' created successfully!!")

    def del_folder(self):
        foldername = simpledialog.askstring("Delete Folder", "Enter your folder name:")
        if not filename: return
        
        path = Path(foldername)
        if path.exists():
            try:
                os.rmdir(foldername)
                self.log(f"🗑️ Folder '{foldername}' deleted successfully!!")
            except OSError:
                self.log(f"❌ Folder '{foldername}' is not empty or cannot be deleted.")
        else:
            self.log(f"❌ Folder '{foldername}' does not exist.")

    def rename_file(self):
        old_name = simpledialog.askstring("Rename File", "Enter your current file name:")
        if not old_name: return
        
        path = Path(old_name)
        if path.exists():
            new_name = simpledialog.askstring("Rename File", "Enter the new file name:")
            if new_name:
                os.rename(old_name, new_name)
                self.log(f"✏️ File '{old_name}' renamed to '{new_name}'.")
        else:
            self.log(f"❌ File '{old_name}' does not exist.")

if __name__ == "__main__":
    root = tk.Tk()
    
    # Hide the main window temporarily to prevent flash, center it, then show
    root.withdraw()
    root.update_idletasks()
    x = (root.winfo_screenwidth() - 700) // 2
    y = (root.winfo_screenheight() - 450) // 2
    root.geometry(f"700x450+{x}+{y}")
    root.deiconify()
    
    app = PastelFileManagerApp(root)
    root.mainloop()