import subprocess
import tkinter as tk
import customtkinter as ctk
from tkinter import *
from customtkinter import *
import subprocess
import os
from PIL import Image, ImageTk
import pyglet
import token_checker as token_checker
import proxy_checker as proxy_checker
import icon as icon
import threading

pyglet.font.add_file(os.path.join(
    os.getcwd(), "design", "font", "Roboto-Regular.ttf"))

def get_hwid():
    try:
        if os.name == 'posix':
            cmd = 'cat /etc/machine-id'
            uuid = subprocess.check_output(cmd,shell=True)
            uuid = uuid[:-1].decode('utf-8')
            return uuid
        if os.name == 'nt':
            try:
                cmd = 'powershell -Command (Get-WmiObject -Class Win32_ComputerSystemProduct).UUID'
                uuid = subprocess.run(cmd, capture_output=True, text=True, shell=True)
                uuid = uuid.stdout.strip()
                return uuid
            except:
                cmd = 'wmic csproduct get uuid'
                uuid = str(subprocess.check_output(cmd))
                pos1 = uuid.find("\\n")+2
                uuid = uuid[pos1:-15]
                return uuid
    except:
      return "failed get hwid"
  
class gui_class():
    def __init__(self, tk):
        global background_image
        print("Welcome Sussyraider 3.0 Rewrite")
        self.theme = "#293350"
        self.theme2 = "#3A476A"
        self.linetheme = "#222e3f"
        self.stringtheme = "white"
        self.buttontheme = "#21262D"
        self.entrytheme = "#60677F"
        self.font = "Roboto"
        self.title = "Sussyraider 3.0 Rewrite"
        self.version = "3.0"
        self.status = "SUCCESS?"
        self.size = "1260x792"
        self.hwid = get_hwid()
        self.tk = tk
        self.tk.minsize(width=1260, height=792)
        self.tk.maxsize(width=1260, height=792)
        self.tk.configure(bg="black")
        self.tk.title(self.title)
        self.tk.geometry(self.size)
        Label(self.tk, image=background_image).pack()
        
        self.proxytype = "http"
        self.tokens = []
        self.proxies = []
        self.validtoken = 0
        self.invalidtoken = 0
        self.usetoken = 0
        self.vaildproxies = 0
        self.invaildproxies = 0
        self.useproxies = 0
        self.old_button = 0

        # proxies
        self.http_value = BooleanVar()
        self.http_value.set("False")
        self.socks4_value = BooleanVar()
        self.socks4_value.set("True")
        self.socks5_value = BooleanVar()
        self.socks5_value.set("True")
        self.proxysetting = BooleanVar()
        self.proxysetting.set("True")
        # global setting
        self.delay = IntVar()
        self.delay.set(0)

        self.apikey = StringVar()
        self.apikey.set("")

        self.token_checkmode = BooleanVar()
        self.token_checkmode.set("True")
        
        # joiner
        self.memberscreensetting = BooleanVar()
        self.memberscreensetting.set("False")
        self.hcaptchasetting = BooleanVar()
        self.hcaptchasetting.set("False")
        self.joinmessagesetting = BooleanVar()
        self.joinmessagesetting.set("False")

        self.joinresult_success = 0
        self.joinresult_failed = 0
        self.joinresult_memberscreen = 0
        self.joinresult_success_label = StringVar()
        self.joinresult_success_label.set("Success: 000")
        self.joinresult_failed_label = StringVar()
        self.joinresult_failed_label.set("Failed: 000")
        self.joinresult_memberscreen_label = StringVar()
        self.joinresult_memberscreen_label.set("MemberScreen: 000")

        # leaver
        self.leaveresult_success = 0
        self.leaveresult_failed = 0
        self.leaveresult_success_label = StringVar()
        self.leaveresult_success_label.set("Success: 000")
        self.leaveresult_failed_label = StringVar()
        self.leaveresult_failed_label.set("Failed: 000")

        Label(self.tk, text="Hardware ID: " + get_hwid(),
              bg=self.theme, fg=self.stringtheme, font=(self.font, 24, "")).place(x=410, y=27)

        self.setup_frame()
        self.setup_modulelist(1, 0)
        self.setup_modulesetting(1, 0)
        self.setup_tokens()
        self.setup_proxies()
        self.setup_modulesetting(1, 1)
        
        
    def clear_frame(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()
        
    def setup_frame(self):
        self.modulelist_frame = tk.Frame(self.tk, width=265, height=650)
        self.modulelist_frame.place(x=54, y=90)
        self.modulelist_frame.configure(bg=self.theme2)

        self.modulesetting_frame = tk.Frame(self.tk, width=850, height=310)
        self.modulesetting_frame.place(x=355, y=90)
        self.modulesetting_frame.configure(bg=self.theme2)

        self.tokens_frame = tk.Frame(self.tk, width=405, height=310)
        self.tokens_frame.place(x=355, y=432)
        self.tokens_frame.configure(bg=self.theme2)

        self.proxies_frame = tk.Frame(self.tk, width=405, height=310)
        self.proxies_frame.place(x=799, y=432)
        self.proxies_frame.configure(bg=self.theme2)

    def setup_modulelist(self, num, num2):
        global button_image_join_leave, button_image_nick_avator, button_image_reaction, button_image_report, button_image_spammer, button_image_vcspammer, button_image_friend_dm, button_image_btnpusher
        global button_image_sel_join_leave, button_image_sel_nick_avator, button_image_sel_reaction, button_image_sel_report, button_image_sel_spammer, button_image_sel_vcspammer, button_image_sel_friend_dm, button_image_sel_btnpusher
        frame = self.modulelist_frame

        if num == 1:
            self.clear_frame(frame)
            tk.Label(frame, text="ModuleList",
                bg=self.theme2, fg=self.stringtheme, font=(self.font, 24, "")).place(x=50, y=7)

            self.button_1 = tk.Button(frame, image=button_image_join_leave, relief="flat", bg=self.theme2,
                   activebackground=self.theme2, borderwidth=0, command=lambda: self.setup_modulesetting(1, 1))
            self.button_1.place(x=20, y=60)

            #self.button_2 = tk.Button(frame, image=button_image_nick_avator, relief="flat", bg=self.theme2,
            #       activebackground=self.theme2, borderwidth=0, command=lambda: self.setup_modulesetting(1, 2 ))
            #self.button_2.place(x=20, y=120)
#
            #self.button_3 = tk.Button(frame, image=button_image_friend_dm, relief="flat", bg=self.theme2,
            #       activebackground=self.theme2, borderwidth=0, command=lambda: self.setup_modulesetting(1, 3))
            #self.button_3.place(x=20, y=180)
#
            #self.button_4 = tk.Button(frame, image=button_image_spammer, relief="flat", bg=self.theme2,
            #       activebackground=self.theme2, borderwidth=0, command=lambda: self.setup_modulesetting(1, 4))
            #self.button_4.place(x=20, y=240)
#
            #self.button_5 = tk.Button(frame, image=button_image_vcspammer, relief="flat", bg=self.theme2,
            #       activebackground=self.theme2, borderwidth=0, command=lambda: self.setup_modulesetting(1, 5))
            #self.button_5.place(x=20, y=300)
#
            #self.button_6 = tk.Button(frame, image=button_image_reaction, relief="flat", bg=self.theme2,
            #       activebackground=self.theme2, borderwidth=0, command=lambda: self.setup_modulesetting(1, 6))
            #self.button_6.place(x=20, y=360)
#
            #self.button_7 = tk.Button(frame, image=button_image_btnpusher, relief="flat", bg=self.theme2,
            #       activebackground=self.theme2, borderwidth=0, command=lambda: self.setup_modulesetting(1, 7))
            #self.button_7.place(x=20, y=420)
#
            #self.button_8 = tk.Button(frame, image=button_image_report, relief="flat", bg=self.theme2,
            #       activebackground=self.theme2, borderwidth=0, command=lambda: self.setup_modulesetting(1, 8))
            #self.button_8.place(x=20, y=480)

            tk.Button(frame, image=button_image_white_l, relief="flat", bg=self.theme2,
                   activebackground=self.theme2, borderwidth=0).place(x=50, y=550)
            tk.Button(frame, image=button_image_blue_r, relief="flat", bg=self.theme2,
                   activebackground=self.theme2, borderwidth=0, command=lambda: self.setup_modulelist(2, 1)).place(x=140, y=550)

        if num == 2:
            self.clear_frame(frame)
            tk.Label(frame, text="ModuleList",
                bg=self.theme2, fg=self.stringtheme, font=(self.font, 24, "")).place(x=50, y=7)

            #self.button_9 = tk.Button(frame, image=button_image_join_leave, relief="flat", bg=self.theme2,
            #       activebackground=self.theme2, borderwidth=0, command=lambda: self.setup_modulesetting(1, 9))
            #self.button_9.place(x=20, y=60)

            tk.Button(frame, image=button_image_blue_l, relief="flat", bg=self.theme2,
                   activebackground=self.theme2, borderwidth=0, command=lambda: self.setup_modulelist(1, 0)).place(x=50, y=550)
            tk.Button(frame, image=button_image_white_r, relief="flat", bg=self.theme2,
                   activebackground=self.theme2, borderwidth=0).place(x=140, y=550)

        if num == 3:
            if self.old_button == 1:
                self.button_1.destroy()
                self.button_1 = tk.Button(frame, image=button_image_join_leave, relief="flat", bg=self.theme2,
                    activebackground=self.theme2, borderwidth=0, command=lambda: self.setup_modulesetting(1, 1))
                self.button_1.place(x=20, y=60)
            if self.old_button == 2:
                self.button_2.destroy()
                self.button_2 = tk.Button(frame, image=button_image_nick_avator, relief="flat", bg=self.theme2,
                    activebackground=self.theme2, borderwidth=0, command=lambda: self.setup_modulesetting(1, 2 ))
                self.button_2.place(x=20, y=120)
            if self.old_button == 3:
                self.button_3.destroy()
                self.button_3 = tk.Button(frame, image=button_image_friend_dm, relief="flat", bg=self.theme2,
                    activebackground=self.theme2, borderwidth=0, command=lambda: self.setup_modulesetting(1, 3))
                self.button_3.place(x=20, y=180)
            if self.old_button == 4:
                self.button_4.destroy()
                self.button_4 = tk.Button(frame, image=button_image_spammer, relief="flat", bg=self.theme2,
                    activebackground=self.theme2, borderwidth=0, command=lambda: self.setup_modulesetting(1, 4))
                self.button_4.place(x=20, y=240)
            if self.old_button == 5:
                self.button_5.destroy()
                self.button_5 = tk.Button(frame, image=button_image_vcspammer, relief="flat", bg=self.theme2,
                    activebackground=self.theme2, borderwidth=0, command=lambda: self.setup_modulesetting(1, 5))
                self.button_5.place(x=20, y=300)
            if self.old_button == 6:
                self.button_6.destroy()
                self.button_6 = tk.Button(frame, image=button_image_reaction, relief="flat", bg=self.theme2,
                    activebackground=self.theme2, borderwidth=0, command=lambda: self.setup_modulesetting(1, 6))
                self.button_6.place(x=20, y=360)
            if self.old_button == 7:
                self.button_7.destroy()
                self.button_7 = tk.Button(frame, image=button_image_btnpusher, relief="flat", bg=self.theme2,
                    activebackground=self.theme2, borderwidth=0, command=lambda: self.setup_modulesetting(1, 7))
                self.button_7.place(x=20, y=420)
            if self.old_button == 8:
                self.button_8.destroy()
                self.button_8 = tk.Button(frame, image=button_image_report, relief="flat", bg=self.theme2,
                    activebackground=self.theme2, borderwidth=0, command=lambda: self.setup_modulesetting(1, 8))
                self.button_8.place(x=20, y=480)
            if self.old_button == 9:
                self.button_9.destroy()
                self.button_9 = tk.Button(frame, image=button_image_report, relief="flat", bg=self.theme2,
                    activebackground=self.theme2, borderwidth=0, command=lambda: self.setup_modulesetting(1, 9))
                self.button_9.place(x=20, y=60)
        if num == 4:
            if num2 == 1:
                self.button_1 = tk.Button(frame, image=button_image_sel_join_leave, relief="flat", bg=self.theme2,
                    activebackground=self.theme2, borderwidth=0, command=lambda: self.setup_modulesetting(1, 1))
                self.button_1.place(x=20, y=60)
            if num2 == 2:
                self.button_2 = tk.Button(frame, image=button_image_sel_nick_avator, relief="flat", bg=self.theme2,
                    activebackground=self.theme2, borderwidth=0, command=lambda: self.setup_modulesetting(1, 2 ))
                self.button_2.place(x=20, y=120)
            if num2 == 3:
                self.button_3.destroy()
                self.button_3 = tk.Button(frame, image=button_image_sel_friend_dm, relief="flat", bg=self.theme2,
                    activebackground=self.theme2, borderwidth=0, command=lambda: self.setup_modulesetting(1, 3))
                self.button_3.place(x=20, y=180)
            if num2 == 4:
                self.button_4.destroy()
                self.button_4 = tk.Button(frame, image=button_image_sel_spammer, relief="flat", bg=self.theme2,
                    activebackground=self.theme2, borderwidth=0, command=lambda: self.setup_modulesetting(1, 4))
                self.button_4.place(x=20, y=240)
            if num2 == 5:
                self.button_5.destroy()
                self.button_5 = tk.Button(frame, image=button_image_sel_vcspammer, relief="flat", bg=self.theme2,
                    activebackground=self.theme2, borderwidth=0, command=lambda: self.setup_modulesetting(1, 5))
                self.button_5.place(x=20, y=300)
            if num2 == 6:
                self.button_6.destroy()
                self.button_6 = tk.Button(frame, image=button_image_sel_reaction, relief="flat", bg=self.theme2,
                    activebackground=self.theme2, borderwidth=0, command=lambda: self.setup_modulesetting(1, 6))
                self.button_6.place(x=20, y=360)
            if num2 == 7:
                self.button_7.destroy()
                self.button_7 = tk.Button(frame, image=button_image_sel_btnpusher, relief="flat", bg=self.theme2,
                    activebackground=self.theme2, borderwidth=0, command=lambda: self.setup_modulesetting(1, 7))
                self.button_7.place(x=20, y=420)
            if num2 == 8:
                self.button_8.destroy()
                self.button_8 = tk.Button(frame, image=button_image_sel_report, relief="flat", bg=self.theme2,
                    activebackground=self.theme2, borderwidth=0, command=lambda: self.setup_modulesetting(1, 8))
                self.button_8.place(x=20, y=480)
            if num2 == 9:
                self.button_9.destroy()
                self.button_9 = tk.Button(frame, image=button_image_sel_join_leave, relief="flat", bg=self.theme2,
                    activebackground=self.theme2, borderwidth=0, command=lambda: self.setup_modulesetting(1, 9))
                self.button_9.place(x=20, y=60)

    def setup_modulesetting(self, num1, num2):
        global button_image_setting, entry_image_1, entry_image_2, button_image_start, button_image_stop, button_image_join, button_image_leave
        global button_image_toggle_true, button_image_toggle_false
        frame = self.modulesetting_frame
        self.clear_frame(frame)
        tk.Label(frame, text="ModuleSetting",
              bg=self.theme2, fg=self.stringtheme, font=(self.font, 25, "")).place(x=15, y=8)
        tk.Button(frame, image=button_image_setting, relief="flat", bg=self.theme2,
               activebackground=self.theme2, borderwidth=0).place(x=880, y=13)
        if self.old_button != 0:
            self.setup_modulelist(3, 0)
        self.setup_modulelist(4, num2)
        self.old_button = num2
        if num2 == 1:
        #    tk.Label(frame, text="Coming soon :L",
        #        bg=self.theme2, fg=self.stringtheme, font=(self.font, 21, "")).place(x=30, y=65)
            #EntryBox
            Label(frame, text="InviteLink",
                bg=self.theme2, fg=self.stringtheme, font=(self.font, 21, "")).place(x=30, y=65)
            Label(frame, image=entry_image_1,
                bg=self.theme2, fg=self.stringtheme, font=(self.font, 21, "")).place(x=25, y=105)
            #self.invitelinkentry = tk.Entry(frame, font=(self.font, 15, ""), bg=self.entrytheme, fg=self.stringtheme, relief="flat" , insertbackground="white", width=25)
            self.invitelinkentry = ctk.CTkEntry(frame, font=(self.font, 15, "normal"), bg_color=self.entrytheme, fg_color=self.entrytheme, width=250, height=15, border_color=self.entrytheme, text_color="white")
            self.invitelinkentry.place(x=38, y=111)
            Label(frame, text="ServerID",
                bg=self.theme2, fg=self.stringtheme, font=(self.font, 21, "")).place(x=30, y=155)
            Label(frame, image=entry_image_1,
                bg=self.theme2, fg=self.stringtheme, font=(self.font, 21, "")).place(x=25, y=195)
            #self.serveridentry = tk.Entry(frame, font=(self.font, 15, ""), bg=self.entrytheme, fg=self.stringtheme, relief="flat" , insertbackground="white", width=25)
            #self.serveridentry.place(x=38, y=201)
            self.serveridentry = ctk.CTkEntry(frame, font=(self.font, 15, "normal"), bg_color=self.entrytheme, fg_color=self.entrytheme, width=250, height=15, border_color=self.entrytheme, text_color="white")
            self.serveridentry.place(x=36, y=201)

            #Join/Leave button
            Button(frame, image=button_image_join, relief="flat", bg=self.theme2,
                activebackground=self.theme2, borderwidth=0, command=lambda: self.module(1)).place(x=35, y=265)
            Button(frame, image=button_image_leave, relief="flat", bg=self.theme2,
                activebackground=self.theme2, borderwidth=0, command=lambda: self.module(2)).place(x=180, y=265)
            #CheckButton
            Label(frame, text="MemberScreen",
                bg=self.theme2, fg=self.stringtheme, font=(self.font, 21, "")).place(x=380, y=65)
            Checkbutton(frame, image=button_image_proxy_false, selectimage=button_image_proxy_true, fg=self.theme2, bg=self.theme2, activebackground=self.theme2, selectcolor=self.theme2, indicatoron=False, 
                borderwidth=0, relief="flat", overrelief="flat", variable=self.memberscreensetting).place(x=340, y=68)
            Label(frame, text="hCaptcha",
                bg=self.theme2, fg=self.stringtheme, font=(self.font, 21, "")).place(x=380, y=105)
            Checkbutton(frame, image=button_image_proxy_false, selectimage=button_image_proxy_true, fg=self.theme2, bg=self.theme2, activebackground=self.theme2, selectcolor=self.theme2, indicatoron=False, 
                borderwidth=0, relief="flat", overrelief="flat", variable=self.hcaptchasetting).place(x=340, y=108)
            Label(frame, text="JoinMessage",
                bg=self.theme2, fg=self.stringtheme, font=(self.font, 21, "")).place(x=640, y=65)
            Checkbutton(frame, image=button_image_proxy_false, selectimage=button_image_proxy_true, fg=self.theme2, bg=self.theme2, activebackground=self.theme2, selectcolor=self.theme2, indicatoron=False, 
                borderwidth=0, relief="flat", overrelief="flat", variable=self.joinmessagesetting).place(x=600, y=68)
            #result Label
            Label(frame, text="Join",
                bg=self.theme2, fg=self.stringtheme, font=(self.font, 25, "")).place(x=340, y=145)
            Label(frame, textvariable=self.joinresult_success_label,
                bg=self.theme2, fg=self.stringtheme, font=(self.font, 21, "")).place(x=340, y=190)
            Label(frame, textvariable=self.joinresult_failed_label,
                bg=self.theme2, fg=self.stringtheme, font=(self.font, 21, "")).place(x=340, y=225)
            Label(frame, textvariable=self.joinresult_memberscreen_label,
                bg=self.theme2, fg=self.stringtheme, font=(self.font, 21, "")).place(x=340, y=260)
        
            Label(frame, text="Leave",
                bg=self.theme2, fg=self.stringtheme, font=(self.font, 25, "")).place(x=610, y=145)
            Label(frame, textvariable=self.leaveresult_success_label,
                bg=self.theme2, fg=self.stringtheme, font=(self.font, 21, "")).place(x=610, y=190)
            Label(frame, textvariable=self.leaveresult_failed_label,
                bg=self.theme2, fg=self.stringtheme, font=(self.font, 21, "")).place(x=610, y=225)
        if num2 == 9:
            tk.Label(frame, text="Coming soon :L",
                bg=self.theme2, fg=self.stringtheme, font=(self.font, 21, "")).place(x=30, y=65)

    def setup_tokens(self):
        global button_image_upload, button_image_line, button_image_plus, button_image_minus, button_image_proxy_false, button_image_proxy_true
        frame = self.tokens_frame
        self.clear_frame(frame)
        tk.Label(frame, text="Tokens",
              bg=self.theme2, fg=self.stringtheme, font=(self.font, 25, "")).place(x=15, y=8)
        self.totalTokenLabel = StringVar()
        self.totalTokenLabel.set("Total: 000")
        self.validTokenlabel = StringVar()
        self.validTokenlabel.set("Valid: 000")
        self.invalidTokenlabel = StringVar()
        self.invalidTokenlabel.set("Invalid: 000")
        self.useTokenLabel = StringVar()
        self.useTokenLabel.set("000")

        tk.Label(frame, textvariable=self.totalTokenLabel,
              bg=self.theme2, fg=self.stringtheme, font=("", 22, "")).place(x=25, y=75)
        tk.Label(frame, textvariable=self.validTokenlabel,
              bg=self.theme2, fg=self.stringtheme, font=("", 22, "")).place(x=25, y=110)
        tk.Label(frame, textvariable=self.invalidTokenlabel,
              bg=self.theme2, fg=self.stringtheme, font=("", 22, "")).place(x=25, y=145)
        tk.Label(frame, image=button_image_line,
              bg=self.theme2, fg=self.stringtheme).place(x=210, y=70)
        tk.Label(frame, text="Use Tokens",
              bg=self.theme2, fg=self.stringtheme, font=("", 20, "")).place(x=240, y=75)

        tk.Button(frame, image=button_image_minus, relief="flat", bg=self.theme2,
               activebackground=self.theme2, borderwidth=0, command=lambda: self.use_token(False), repeatdelay=100, repeatinterval=10).place(x=240, y=125)
        tk.Button(frame, image=button_image_plus, relief="flat", bg=self.theme2,
               activebackground=self.theme2, borderwidth=0, command=lambda: self.use_token(True), repeatdelay=100, repeatinterval=10).place(x=275, y=125)

        tk.Label(frame, textvariable=self.useTokenLabel,
              bg=self.theme2, fg=self.stringtheme, font=("", 30, "")).place(x=310, y=110)

        tk.Button(frame, image=button_image_upload, relief="flat", bg=self.theme2,
               activebackground=self.theme2, borderwidth=0, command=lambda: self.token_load()).place(x=135, y=12)

        tk.Checkbutton(frame, image=button_image_proxy_false, selectimage=button_image_proxy_true, fg=self.theme2, bg=self.theme2, activebackground=self.theme2, selectcolor=self.theme2, indicatoron=False, 
            borderwidth=0, relief="flat", overrelief="flat", variable=self.token_checkmode).place(x=200, y=15)

        tk.Label(frame, text="Fast Check",
              bg=self.theme2, fg=self.stringtheme, font=("", 22, "")).place(x=230, y=12)

    def setup_proxies(self):
        global button_image_upload, button_image_setting, button_image_proxy_true, button_image_proxy_false, button_image_toggle_true, button_image_toggle_false
        frame = self.proxies_frame
        self.clear_frame(frame)
        tk.Label(frame, text="Proxies",
              bg=self.theme2, fg=self.stringtheme, font=(self.font, 25, "")).place(x=15, y=7)
        self.totalProxiesLabel = StringVar()
        self.totalProxiesLabel.set("Total: 000")
        self.validProxiesLabel = StringVar()
        self.validProxiesLabel.set("Valid: 000")
        self.invalidProxiesLabel = StringVar()
        self.invalidProxiesLabel.set("Invalid: 000")
        self.useProxiesLabel = StringVar()
        self.useProxiesLabel.set("000")

        tk.Label(frame, textvariable=self.totalProxiesLabel,
              bg=self.theme2, fg=self.stringtheme, font=("", 22, "")).place(x=25, y=160)
        tk.Label(frame, textvariable=self.validProxiesLabel,
              bg=self.theme2, fg=self.stringtheme, font=("", 22, "")).place(x=25, y=190)
        tk.Label(frame, textvariable=self.invalidProxiesLabel,
              bg=self.theme2, fg=self.stringtheme, font=("", 22, "")).place(x=25, y=220)
        tk.Label(frame, image=button_image_line,
              bg=self.theme2, fg=self.stringtheme).place(x=210, y=70)
        tk.Label(frame, text="Use Proxies",
              bg=self.theme2, fg=self.stringtheme, font=("", 20, "")).place(x=25, y=65)

        tk.Button(frame, image=button_image_minus, relief="flat", bg=self.theme2,
               activebackground=self.theme2, borderwidth=0, command=lambda: self.use_proxy(False), repeatdelay=100, repeatinterval=10).place(x=25, y=115)
        tk.Button(frame, image=button_image_plus, relief="flat", bg=self.theme2,
               activebackground=self.theme2, borderwidth=0, command=lambda: self.use_proxy(True), repeatdelay=100, repeatinterval=10).place(x=60, y=115)

        tk.Label(frame, textvariable=self.useProxiesLabel, bg=self.theme2,
              fg=self.stringtheme, font=("", 30, "")).place(x=90, y=100)

        tk.Button(frame, image=button_image_upload, relief="flat", bg=self.theme2,
               activebackground=self.theme2, borderwidth=0, command=lambda: self.proxy_load()).place(x=135, y=12)

        tk.Checkbutton(frame, image=button_image_toggle_false, selectimage=button_image_toggle_true, fg=self.theme2, bg=self.theme2, activebackground=self.theme2, selectcolor=self.theme2, indicatoron=False, 
            borderwidth=0, relief="flat", overrelief="flat", variable=self.proxysetting).place(x=330, y=12)
        tk.Label(frame, text="ProxyType",
              bg=self.theme2, fg=self.stringtheme, font=("", 20, "")).place(x=240, y=65)
        tk.Label(frame, text="Http(s)",
              bg=self.theme2, fg=self.stringtheme, font=("", 20, "")).place(x=240, y=110)
        tk.Label(frame, text="Socks4",
              bg=self.theme2, fg=self.stringtheme, font=("", 20, "")).place(x=240, y=145)
        tk.Label(frame, text="Socks5",
              bg=self.theme2, fg=self.stringtheme, font=("", 20, "")).place(x=240, y=180)

        tk.Checkbutton(frame, image=button_image_proxy_true, selectimage=button_image_proxy_false, fg=self.theme2, bg=self.theme2, activebackground=self.theme2, selectcolor=self.theme2, indicatoron=False, 
            borderwidth=0, relief="flat", overrelief="flat", variable=self.http_value, command=lambda: self.select_proxy("http")).place(x=340, y=110)
        tk.Checkbutton(frame, image=button_image_proxy_true, selectimage=button_image_proxy_false, fg=self.theme2, bg=self.theme2, activebackground=self.theme2, selectcolor=self.theme2, indicatoron=False, 
            borderwidth=0, relief="flat", overrelief="flat", variable=self.http_value, command=lambda: self.select_proxy("http")).place(x=340, y=110)
        tk.Checkbutton(frame, image=button_image_proxy_true, selectimage=button_image_proxy_false, fg=self.theme2, bg=self.theme2, activebackground=self.theme2, selectcolor=self.theme2, indicatoron=False, 
            borderwidth=0, relief="flat", overrelief="flat", variable=self.socks4_value, command=lambda: self.select_proxy("socks4")).place(x=340, y=145)
        tk.Checkbutton(frame, image=button_image_proxy_true, selectimage=button_image_proxy_false, fg=self.theme2, bg=self.theme2, activebackground=self.theme2, selectcolor=self.theme2, indicatoron=False, 
            borderwidth=0, relief="flat", overrelief="flat", variable=self.socks5_value, command=lambda: self.select_proxy("socks5")).place(x=340, y=180)
    
    # token option
    def token_load(self):
        fTyp = [("", "*.txt")]
        iFile = os.path.abspath(os.path.dirname(__file__))
        filepath = filedialog.askopenfilename(
            filetype=fTyp, initialdir=iFile, title="Select Tokens")
        if filepath == "":
            return
        tokens = open(filepath, 'r').read().splitlines()
        if tokens == []:
            return
        self.tokens = []
        self.validtoken = 0
        self.invalidtoken = 0
        self.usetoken = 0
        self.totalTokenLabel.set("Total: "+str(len(tokens)).zfill(3))
        mode = self.token_checkmode.get()
        token_checker.check(self, mode, self.proxysetting.get(), self.proxies, self.proxytype, tokens)

    def update_token(self, status, token):
        if status == True:
            self.tokens.append(token)
            self.validtoken += 1
            self.validTokenlabel.set("Valid: "+str(self.validtoken).zfill(3))
        if status == False:
            self.invalidtoken += 1
            self.invalidTokenlabel.set("Invalid: "+str(self.invalidtoken).zfill(3))
        self.usetoken = self.validtoken
        self.useTokenLabel.set(str(self.usetoken).zfill(3))

    def use_token(self, status):
        if status == True:
            if self.validtoken <= self.usetoken:
                return
            self.usetoken += 1
        if status == False:
            if self.usetoken <= 1:
                return
            self.usetoken -= 1
        self.useTokenLabel.set(str(self.usetoken).zfill(3))

    # proxy option
    def proxy_load(self):
        fTyp = [("", "*.txt")]
        iFile = os.path.abspath(os.path.dirname(__file__))
        filepath = filedialog.askopenfilename(
            filetype=fTyp, initialdir=iFile, title="Select Proxies")
        if filepath == "":
            return
        proxies = open(filepath, 'r').read().splitlines()
        if proxies == []:
            return
        self.proxies = []
        self.vaildproxies = 0
        self.invaildproxies = 0
        self.useproxies = 0
        self.totalProxiesLabel.set("Total: "+str(len(proxies)).zfill(3))
        proxy_checker.check(self, proxies, self.proxytype)

    def update_proxy(self, status, proxy):
        if status == True:
            self.proxies.append(proxy)
            self.vaildproxies += 1
            self.validProxiesLabel.set("Valid: "+str(self.vaildproxies).zfill(3))
        if status == False:
            self.invaildproxies += 1
            self.invalidProxiesLabel.set("Invalid: "+str(self.invaildproxies).zfill(3))
        self.useproxies = self.vaildproxies
        self.useProxiesLabel.set(str(self.useproxies).zfill(3))

    def use_proxy(self, status):
        if status == True:
            if self.vaildproxies <= self.useproxies:
                return
            self.useproxies += 1
        if status == False:
            if self.useproxies <= 1:
                return
            self.useproxies -= 1
        self.useProxiesLabel.set(str(self.useproxies).zfill(3))

    def select_proxy(self, type):
        self.http_value.set("True")
        self.socks4_value.set("True")
        self.socks5_value.set("True")
        self.proxytype = type
        if type == "http":
            self.http_value.set("False")
        if type == "socks4":
            self.socks4_value.set("False")
        if type == "socks5":
            self.socks5_value.set("False")
        print(self.proxytype)

    # Modules options

    def update_module(self, module, result):
        if module == 1: # Joiner
            if result == 1: # Success
                self.joinresult_success += 1
                self.joinresult_success_label.set("Success: "+str(self.joinresult_success).zfill(3))
            if result == 2: # Failed
                self.joinresult_failed += 1
                self.joinresult_failed_label.set("Failed: "+str(self.joinresult_failed).zfill(3))
            if result == 3: # Memberscreen
                self.joinresult_memberscreen += 1
                self.joinresult_memberscreen_label.set("MemberScreen: "+str(self.joinresult_memberscreen).zfill(3))
        if module == 2: # Leaver
            if result == 1: # Success
                self.leaveresult_success += 1
                self.leaveresult_success_label.set("Success: "+str(self.leaveresult_success).zfill(3))
            if result == 2: # Failed
                self.leaveresult_failed += 1
                self.leaveresult_failed_label.set("Failed: "+str(self.leaveresult_failed).zfill(3))
        if module == 3: # Nick
            pass
        if module == 4: # Avator
            pass
    
    def thread_module(self, module):
        threading.Thread(target=self.module, args=(module)).start()

    def module(self, module):
        tokens = self.tokens
        proxies = self.proxies
        proxytype = self.proxytype
        apikey = self.apikey.get()
        delay = self.delay.get()
        if tokens == []:
            print("[-] Token is not loaded")
            return
        if proxies == []:
            print("[-] Proxies is not loaded")
            return
        if module == 1: # Joiner
            serverid = self.serveridentry.get()
            invitelink = self.invitelinkentry.get()
            memberscreen = self.memberscreensetting.get()
            hcaptcha = self.hcaptchasetting.get()
            joinmessage = self.joinmessagesetting.get()
            if invitelink == "":
                print("[-] InviteLink is not set")
                return
            if invitelink.__contains__('discord.gg/'):
                invitelink = invitelink.replace('discord.gg/', '').replace('https://', '').replace('http://', '')
            elif invitelink.__contains__('discord.com/invite/'):
                invitelink = invitelink.replace('discord.com/invite/', '').replace('https://', '').replace('http://', '')
            try:
                invitelink = invitelink.split(".gg/")[1]
            except:
                pass
            if memberscreen == True:
                if serverid == "":
                    print("[-] ServerID is not set")
                    return
                else:
                    print("[-] このオプションを使うと100%アカウントがあの世へ行きます。")
            if hcaptcha == True:
                if apikey == "":
                    print("[-] Apikey is not set")
                    return
            if joinmessage == True:
                if serverid == "":
                    print("[-] ServerID is not set")
                    return
            threading.Thread().start()

        if module == 2: #Leave
            print(tokens)
            
# instance tk
window = Tk()
# main class

# 画像変数の作成

# background
image = Image.open(os.path.join(os.getcwd(), "design", "background.png")).resize(
    (1260, 792), Image.LANCZOS)
background_image = ImageTk.PhotoImage(image)
# setting
image = Image.open(os.path.join(os.getcwd(), "design", "setting.png")).resize(
    (30, 30), Image.LANCZOS)
button_image_setting = ImageTk.PhotoImage(image)
# upload
image = Image.open(os.path.join(os.getcwd(), "design", "upload.png")).resize(
    (30, 30), Image.LANCZOS)
button_image_upload = ImageTk.PhotoImage(image)
# blue right
image = Image.open(os.path.join(os.getcwd(), "design",
                   "blue_right.png")).resize((60, 60), Image.LANCZOS)
button_image_blue_r = ImageTk.PhotoImage(image)
# blue left
image = Image.open(os.path.join(os.getcwd(), "design", "blue_left.png")).resize(
    (60, 60), Image.LANCZOS)
button_image_blue_l = ImageTk.PhotoImage(image)
# white right
image = Image.open(os.path.join(os.getcwd(), "design",
                   "white_right.png")).resize((60, 60), Image.LANCZOS)
button_image_white_r = ImageTk.PhotoImage(image)
# white left
image = Image.open(os.path.join(os.getcwd(), "design",
                   "white_left.png")).resize((60, 60), Image.LANCZOS)
button_image_white_l = ImageTk.PhotoImage(image)
# plus
image = Image.open(os.path.join(os.getcwd(), "design", "plus.png")).resize(
    (18, 18), Image.LANCZOS)
button_image_plus = ImageTk.PhotoImage(image)
# minus
image = Image.open(os.path.join(os.getcwd(), "design", "minus.png")).resize(
    (18, 18), Image.LANCZOS)
button_image_minus = ImageTk.PhotoImage(image)
# line
image = Image.open(os.path.join(os.getcwd(), "design", "line.png")).resize(
    (2, 225), Image.LANCZOS)
button_image_line = ImageTk.PhotoImage(image)

# join_leave
image = Image.open(os.path.join(os.getcwd(), "design",
                   "join_leave.png")).resize((225, 45), Image.LANCZOS)
button_image_join_leave = ImageTk.PhotoImage(image)
image = Image.open(os.path.join(os.getcwd(), "design",
                   "sel_join_leave.png")).resize((225, 45), Image.LANCZOS)
button_image_sel_join_leave = ImageTk.PhotoImage(image)
# nick_avator
image = Image.open(os.path.join(os.getcwd(), "design",
                   "nick_avator.png")).resize((225, 45), Image.LANCZOS)
button_image_nick_avator = ImageTk.PhotoImage(image)
image = Image.open(os.path.join(os.getcwd(), "design",
                   "sel_nick_avator.png")).resize((225, 45), Image.LANCZOS)
button_image_sel_nick_avator = ImageTk.PhotoImage(image)
# friend_dm
image = Image.open(os.path.join(os.getcwd(), "design", "friend_dm.png")).resize(
    (225, 45), Image.LANCZOS)
button_image_friend_dm = ImageTk.PhotoImage(image)
image = Image.open(os.path.join(os.getcwd(), "design",
                   "sel_friend_dm.png")).resize((225, 45), Image.LANCZOS)
button_image_sel_friend_dm = ImageTk.PhotoImage(image)
# spammer
image = Image.open(os.path.join(os.getcwd(), "design", "spammer.png")).resize(
    (225, 45), Image.LANCZOS)
button_image_spammer = ImageTk.PhotoImage(image)
image = Image.open(os.path.join(os.getcwd(), "design",
                   "sel_spammer.png")).resize((225, 45), Image.LANCZOS)
button_image_sel_spammer = ImageTk.PhotoImage(image)
# reaction
image = Image.open(os.path.join(os.getcwd(), "design", "reaction.png")).resize(
    (225, 45), Image.LANCZOS)
button_image_reaction = ImageTk.PhotoImage(image)
image = Image.open(os.path.join(os.getcwd(), "design",
                   "sel_reaction.png")).resize((225, 45), Image.LANCZOS)
button_image_sel_reaction = ImageTk.PhotoImage(image)
# vcspammer
image = Image.open(os.path.join(os.getcwd(), "design", "vcspammer.png")).resize(
    (225, 45), Image.LANCZOS)
button_image_vcspammer = ImageTk.PhotoImage(image)
image = Image.open(os.path.join(os.getcwd(), "design",
                   "sel_vcspammer.png")).resize((225, 45), Image.LANCZOS)
button_image_sel_vcspammer = ImageTk.PhotoImage(image)
# btnpusher
image = Image.open(os.path.join(os.getcwd(), "design", "btnpusher.png")).resize(
    (225, 45), Image.LANCZOS)
button_image_btnpusher = ImageTk.PhotoImage(image)
image = Image.open(os.path.join(os.getcwd(), "design",
                   "sel_btnpusher.png")).resize((225, 45), Image.LANCZOS)
button_image_sel_btnpusher = ImageTk.PhotoImage(image)
# report
image = Image.open(os.path.join(os.getcwd(), "design", "report.png")).resize(
    (225, 45), Image.LANCZOS)
button_image_report = ImageTk.PhotoImage(image)
image = Image.open(os.path.join(os.getcwd(), "design",
        "sel_report.png")).resize((225, 45), Image.LANCZOS)
button_image_sel_report = ImageTk.PhotoImage(image)

#proxy checkbutton
image = Image.open(os.path.join(os.getcwd(), "design", "proxy_true.png")).resize((25, 25), Image.LANCZOS)
button_image_proxy_true = ImageTk.PhotoImage(image)
image = Image.open(os.path.join(os.getcwd(), "design","proxy_false.png")).resize((25, 25), Image.LANCZOS)
button_image_proxy_false = ImageTk.PhotoImage(image)
#toggle checkbutton
image = Image.open(os.path.join(os.getcwd(), "design", "toggle_true.png")).resize((50, 25), Image.LANCZOS)
button_image_toggle_true = ImageTk.PhotoImage(image)
image = Image.open(os.path.join(os.getcwd(), "design", "toggle_false.png")).resize((50, 25), Image.LANCZOS)
button_image_toggle_false = ImageTk.PhotoImage(image)
#entry image
image = Image.open(os.path.join(os.getcwd(), "design", "entry_image_1.png")).resize((270, 30), Image.LANCZOS)
entry_image_1 = ImageTk.PhotoImage(image)
image = Image.open(os.path.join(os.getcwd(), "design", "entry_image_2.png")).resize((270, 30), Image.LANCZOS)
entry_image_2 = ImageTk.PhotoImage(image)
#button start stop
image = Image.open(os.path.join(os.getcwd(), "design", "start.png")).resize((115, 30), Image.LANCZOS)
button_image_start = ImageTk.PhotoImage(image)
image = Image.open(os.path.join(os.getcwd(), "design", "stop.png")).resize((115, 30), Image.LANCZOS)
button_image_stop = ImageTk.PhotoImage(image)

#button join leave
image = Image.open(os.path.join(os.getcwd(), "design", "join.png")).resize((115, 30), Image.LANCZOS)
button_image_join = ImageTk.PhotoImage(image)
image = Image.open(os.path.join(os.getcwd(), "design", "leave.png")).resize((115, 30), Image.LANCZOS)
button_image_leave = ImageTk.PhotoImage(image)


data = icon.geticon()
window.tk.call('wm', 'iconphoto', window._w, tk.PhotoImage(data=data))

launcher = gui_class(window)
# run event loop
window.mainloop()