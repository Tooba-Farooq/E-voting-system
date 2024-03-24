import customtkinter
import tkinter
import pyodbc
from tkinter import *
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import datetime, timedelta
import os

user_pass = None
ccodelabel = None
provincelabel = None
idlabel = None
cnamelabel = None

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the Access database file
db_file = os.path.join(current_dir, 'PD.accdb')

# Establish connection
con = pyodbc.connect((r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                      rf'DBQ={db_file};'))

# Create a tkinter window
root2 = customtkinter.CTk()
root2.title("User Login")
customtkinter.set_default_color_theme("green")

# Load images for party logos
lion_original = PhotoImage(file="images\\5b4ee57146316.png")
bat_original = PhotoImage(file="images\\PTI_Symbol_Elections.png")
arrow_original = PhotoImage(file="images\\ppp arrow.png")
balance_original = PhotoImage(file="images\\5b4ee75074c57.png")
lion_resized = lion_original.subsample(8, 8)
bat_resized = bat_original.subsample(8, 8)
arrow_resized = arrow_original.subsample(8, 8)
balance_resized = balance_original.subsample(8, 8)
party_logos = [lion_resized, balance_resized, arrow_resized, bat_resized]

# Define functions


# Main window function
def mainwindow():
    # Frame for the left side of the window
    left_frame1 = customtkinter.CTkFrame(master=root2, width=300, fg_color="#014112", height=500, corner_radius=0)
    left_frame1.pack(side="left", fill="both")
    # Frame for the right side of the window
    right_frame1 = customtkinter.CTkFrame(master=root2, width=1800, fg_color="white", height=500, corner_radius=0)
    right_frame1.pack(side="right", fill="both")
    # Banner image for the Election Commission
    ecp_banner = PhotoImage(file="images\\Untitled2.png")
    ecp_banner_label = Label(master=right_frame1, image=ecp_banner, background="white", height=250)
    ecp_banner_label.pack(fill="y")
    # Welcome message
    text_label = Label(master=right_frame1, text="Welcome!\n Please access the panel on the left for further "
                                                 "information.", foreground="#1c1c1c", font=("corbel", 30, "bold"),
                       background="white")
    text_label.pack()

    # Function to translate the content
    def translate():
        cursor3 = con.cursor()
        cursor3.execute(f"FROM Citizens WHERE Password = '{user_pass}' SELECT Name ")
        user_data = cursor3.fetchall()
        namelabel2 = user_data[0][0]
        dashboard = customtkinter.CTkFrame(master=right_frame1, width=1800, fg_color="white", height=500,
                                           corner_radius=0)
        dashboard.pack(side="right", fill="both")
        ecp_banner_label1 = Label(master=dashboard, image=ecp_banner, background="white", height=250)
        ecp_banner_label1.pack(fill="y")
        welcome_label = customtkinter.CTkLabel(master=dashboard, text=f" Welcome {namelabel2}",
                                               font=("Times New Roman", 40, "bold"), text_color="black")
        welcome_label.pack(anchor="w")
        welcome_text = customtkinter.CTkLabel(master=dashboard,
                                              text="  پاکستان الیکشن کمیشن کا مقصد ان انتخابات کو مکمل شفافیت "
                                                   "اور انصاف\n کے ساتھ منعقد کرنا ہے.آپ نے عام انتخابات 2024 کے لیے"
                                                   " کامیابی سے رجسٹریشن کرائی ہے. متوقع انتخابات کی تاریخ [تاریخ] ہے.",
                                              fg_color="white", text_color="black", font=("Times New Roman", 25))
        welcome_text.pack(anchor="w")

    def dashboard_frame():
        cursor4 = con.cursor()
        cursor4.execute(f"SELECT Name FROM Citizens WHERE Password = '{user_pass}'")
        user_data = cursor4.fetchall()
        namelabel2 = user_data[0][0]

        dashboard = customtkinter.CTkFrame(master=right_frame1, width=1800, fg_color="white", height=500,
                                           corner_radius=0)
        dashboard.pack(side="right", fill="both")
        ecp_banner_label1 = Label(master=dashboard, image=ecp_banner, background="white", height=250)
        ecp_banner_label1.pack(fill="y")
        welcome_label = customtkinter.CTkLabel(master=dashboard, text=f" Welcome {namelabel2}",
                                               font=("Times New Roman", 40, "bold"), text_color="black")
        welcome_label.pack(anchor="w")
        welcome_text = customtkinter.CTkLabel(master=dashboard,
                                              text="  You have successfully registered for the General Elections 2024."
                                                   " The expected election date is [date].",
                                              fg_color="white", text_color="black", font=("Times New Roman", 22))
        welcome_text.pack(anchor="w")
        welcome_text = customtkinter.CTkLabel(master=dashboard,
                                              text=" The Pakistan Election Commission aims to hold these elections"
                                                   " with absolute transparency and fairness.           \n"
                                                   "\n  As citizens of the Islamic Republic of Pakistan, we must be "
                                                   "held to the highest standard of honesty and integrity."
                                                   "\n Our founding leader, Quaid-e-Azam Muhammad Ali Jinnah said: "
                                                   "'Work honestly and sincerely and be faithful   \nand loyal"
                                                   " to the Pakistani Government, and I can assure you there will be "
                                                   "nothing greater in the world than your"
                                                   "\nown conscience. When your appear before God, you can say that "
                                                   "you performed your duty with the highest      "
                                                   "\nsense of integrity, honesty, and with loyalty and faithfulness'.",
                                              fg_color="white", text_color="black", font=("Times New Roman", 22))
        welcome_text.pack(anchor="w")
        welcome_text = customtkinter.CTkLabel(master=dashboard,
                                              text="\n\n Hence, we must all strive to vote for these elections with "
                                                   "honesty, and should report and                       "
                                                   "\n  instances of fraudulent behavior. For further details, please"
                                                   " access the panel on the left.                         ",
                                              fg_color="white", text_color="black", font=("Times New Roman", 22))
        welcome_text.pack(anchor="w")
        translate_button = customtkinter.CTkButton(master=dashboard, text="Translate to urdu", bg_color="white",
                                                   fg_color="#014112", font=("arial", 17, "bold"),
                                                   hover_color="#568203", text_color="white",
                                                   corner_radius=10, width=10,
                                                   command=lambda: when_clicked2(translate))
        translate_button.place(relx=0.9, rely=0.9, anchor=tkinter.CENTER)

    def user_frame():
        global ccodelabel
        global provincelabel
        global idlabel

        # Create a frame for displaying user information
        userframe = customtkinter.CTkFrame(master=right_frame1, width=1800, fg_color="white", height=500,
                                           corner_radius=0)
        userframe.pack(side="right", fill="both")

        # Display Election Commission banner
        ecp_banner_label1 = Label(master=userframe, image=ecp_banner, background="white", height=250)
        ecp_banner_label1.pack(fill="y")
        user_text = customtkinter.CTkLabel(master=userframe,
                                           text="  You have successfully registered for the General Elections 2024.",
                                           fg_color="white", text_color="black", font=("Times New Roman", 18))
        user_text.place(relx=0.0092, rely=0.31)
        user_text = customtkinter.CTkLabel(master=userframe,
                                           text="  If there are any discrepancies in the following data, please contact"
                                                " the relevant authorities immediately.",
                                           fg_color="white", text_color="black", font=("Times New Roman", 18))
        user_text.place(relx=0.0092, rely=0.35)

        # Labels for displaying user data
        label_text = ["Name", "Father's Name", "CNIC Number", "Date Of Birth", "Address", "City", "Province", "Contact",
                      "Constituency Code", "Constituency Name"]
        for i in range(0, 10):
            labels = customtkinter.CTkButton(master=userframe, fg_color="#378805", text_color="white", corner_radius=5,
                                             font=("aharoni", 19, "bold"), text=label_text[i], state=DISABLED,
                                             text_color_disabled="white", width=189)
            labels.place(relx=0.035, rely=0.4+(0.055*i))

        # Fetch user data from the database
        cursor2 = con.cursor()
        cursor2.execute(f"SELECT Name, [Father's name], ID, Date, Address, City, Province, Contact, "
                        f"[Constituency code], [Constituency name] FROM Citizens WHERE Password = '{user_pass}'")
        user_data = cursor2.fetchall()
        provincelabel = user_data[0][6]
        ccodelabel = user_data[0][8]

        # Display user data fetched from the database
        for i in range(0, 10):
            if i == 3:
                # Format date of birth to dd/mm/yyyy format
                date_string = user_data[0][i]
                formatted_date = date_string.strftime('%d/%m/%Y')
                label_values = customtkinter.CTkLabel(master=userframe, fg_color="#014112", text_color="white",
                                                      font=("aharoni", 19, "bold"), text=formatted_date, width=585,
                                                      corner_radius=5)
                label_values.place(relx=0.35, rely=0.4 + (0.055 * i))
            else:
                # Display other user data
                label_values = customtkinter.CTkLabel(master=userframe, fg_color="#014112", text_color="white",
                                                      font=("aharoni", 19, "bold"), text=user_data[0][i], width=585,
                                                      corner_radius=5)
                label_values.place(relx=0.35, rely=0.4+(0.055*i))

    def vote_frame():
        global ccodelabel
        global idlabel
        cursor1 = con.cursor()
        # Fetching user's constituency code and ID from the database using the provided password
        cursor1.execute(f"SELECT [Constituency code], ID FROM Citizens WHERE Password = '{user_pass}'")
        user_data = cursor1.fetchall()
        if user_data:
            ccodelabel = user_data[0][0]
            idlabel = user_data[0][1]
        parties = ["PMLN", "JI", "PPP", "PTI"]

        # Function to confirm vote
        def confirm():
            # Get the selected party and candidate
            selected_party = parties[x.get()]
            selected_candidate = candidates[x.get()][0]
            confirmation_message = messagebox.askyesnocancel(title="Confirmation Message",
                                                             message=f"Are you sure you want to vote "
                                                                     f"for {selected_candidate}?")
            # Display confirmation message
            if confirmation_message:
                messagebox.showinfo("Vote Casted", f"You have successfully voted for {selected_candidate}!")
                # Disable the vote button to prevent multiple votes
                votebutton.config(state=DISABLED)
                """cursor1.execute("UPDATE [PM Candidates] SET Votes = Votes+1 WHERE Party = ?",
                                selected_party)"""
                cursor1.execute(f"UPDATE [MNA Candidates] SET Votes = Votes+1 WHERE (Party = '{selected_party}' AND "
                                f"[Constituency code] = '{ccodelabel}')")
                """cursor1.execute("UPDATE CM_Candidate SET Votes = Votes+1 WHERE (Party = ? AND Province = ?)",
                                (selected_party, provincelabel))"""
                # Update the 'Voted' status for the user in the database
                cursor1.execute(f"UPDATE Citizens SET Voted = 'Yes' WHERE ID = '{idlabel}'")
                con.commit()
            else:
                print("Vote canceled")

        voteframe = customtkinter.CTkFrame(master=right_frame1, width=1800, fg_color="white", height=500,
                                           corner_radius=0)
        voteframe.pack(side="right", fill="both")
        ecp_banner_label1 = Label(master=voteframe, image=ecp_banner, background="white", height=250)
        ecp_banner_label1.pack(fill="y")
        cursor1.execute(f"SELECT [Candidate Name] FROM [MNA Candidates] WHERE [Constituency Code] = '{ccodelabel}'")
        candidates = cursor1.fetchall()
        # Variable to store the selected candidate
        x = IntVar()
        for i in range(len(parties)):
            radiobutton1 = Radiobutton(voteframe, variable=x, value=i,
                                       image=party_logos[i],
                                       compound="top")
            candidate_name = Label(master=voteframe, text=f"{candidates[i][0]}",
                                   font=("Times New Roman", 13), fg="black", bg="white")
            if i == 0:
                radiobutton1.place(relx=0.3, rely=0.3)
                candidate_name.place(relx=0.3, rely=0.47)
            elif i == 1:
                radiobutton1.place(relx=0.58, rely=0.3)
                candidate_name.place(relx=0.58, rely=0.47)
            elif i == 2:
                radiobutton1.place(relx=0.3, rely=0.55)
                candidate_name.place(relx=0.3, rely=0.72)
            else:
                radiobutton1.place(relx=0.58, rely=0.55)
                candidate_name.place(relx=0.58, rely=0.72)
        # Button for casting vote
        votebutton = Button(voteframe, text="Vote", font=("Comic Sans", 30), fg="white", bg="#0e4f13",
                            activeforeground="white", activebackground="#0e4f13", command=confirm)
        votebutton.place(relx=0.445, rely=0.85)
        # Check if the user has already voted
        cursor1.execute(f"SELECT Voted FROM Citizens WHERE ID = '{idlabel}'")
        voted = (cursor1.fetchone())[0]
        # If user has already voted, disable the vote button and inform the user
        if voted == "Yes":
            votebutton.config(state=DISABLED)
            inform = Label(master=voteframe, text="You have already voted!",
                           font=("Times New Roman", 12), fg="black", bg="white")
            inform.place(relx=0.43, rely=0.79)

    """def pm_frame():
        cursor2 = con.cursor()
        pmframe = customtkinter.CTkFrame(master=right_frame1, width=1800, fg_color="white", height=500,
                                         corner_radius=0)
        pmframe.pack(side="right", fill="both")
        ecp_banner_label1 = Label(master=pmframe, image=ecp_banner, background="white", height=250)
        ecp_banner_label1.pack(fill=Y)
        key = Label(master=pmframe, text="Key", font=("Times New Roman", 18, "italic"), fg="black", bg="white",
                    height=2)
        key.place(relx=0.69, rely=0.47)
        c = ["#32a852", "#01796f", "#5f7a67", "#052b10"]
        for i in range(0, 4):
            colour1 = Label(master=pmframe, text=" ", bg=c[i], width=12, height=2)
            colour1.place(relx=0.53, rely=0.56 + (0.09 * i))
        cursor2.execute("SELECT Party, [Candidate Name] FROM [PM Candidates]")
        candidate = cursor2.fetchall()
        for j in range(0, 4):
            candidate_name = Label(master=pmframe, text=f"{candidate[j][1]} ({candidate[j][0]})",
                                   font=("Times New Roman", 16), fg="black", bg="white", height=2)
            candidate_name.place(relx=0.63, rely=0.55 + (0.09 * j))
        cursor2.execute("SELECT Party, Votes FROM [PM Candidates]")
        pmdata = cursor2.fetchall()
        pmparties, pmvotes = zip(*pmdata)
        fig, ax = plt.subplots()
        bars = ax.bar(pmparties, pmvotes, color=c, width=0.4)
        cursor2.execute("SELECT COUNT (*) FROM Citizens WHERE Voted <> 'Yes'")
        result = cursor2.fetchone()
        if result[0] == 0:
            winner_index = pmvotes.index(max(pmvotes))
            winner_party = pmparties[winner_index]
            cursor2.execute("SELECT [Candidate Name] FROM [PM Candidates] WHERE Party = ?", (winner_party,))
            winner_candidate = cursor2.fetchone()
            runner_up_index = (winner_index + 1) % len(pmparties)
            vote_difference = pmvotes[winner_index] - pmvotes[runner_up_index]
            ax.set_xlabel(f"{winner_candidate[0]} ({winner_party}) has won by {vote_difference} votes")
        for bar, vote_count in zip(bars, pmvotes):
            ax.annotate(str(vote_count), xy=(bar.get_x() + bar.get_width() / 2, bar.get_height()),
                        xytext=(0, 3), textcoords="offset points",
                        ha='center', va='bottom')
        ax.set_ylim(0, max(pmvotes) * 1.1)
        ax.set_title("Votes for PM", fontsize=10)
        canvas = FigureCanvasTkAgg(fig, master=pmframe)
        canvas.draw()
        canvas.get_tk_widget().place(relx=0.28, rely=0.28, anchor="n")
        plt.close(fig)

    def cm_frame():
        global provincelabel
        cursor1 = con.cursor()
        cursor1.execute(f"SELECT Province FROM Citizens WHERE Password = '{user_pass}'")
        user_data = cursor1.fetchall()
        if user_data:
            provincelabel = user_data[0][0]
        cmframe = customtkinter.CTkFrame(master=right_frame1, width=1800, fg_color="white", height=500,
                                         corner_radius=0)
        cmframe.pack(side="right", fill="both")
        ecp_banner_label1 = Label(master=cmframe, image=ecp_banner, background="white", height=250)
        ecp_banner_label1.pack(fill=Y)
        key = Label(master=cmframe, text="Key", font=("Times New Roman", 18, "italic"), fg="black", bg="white",
                    height=2)
        key.place(relx=0.69, rely=0.47)
        c = ["#32a852", "#01796f", "#5f7a67", "#052b10"]
        for i in range(0, 4):
            colour1 = Label(master=cmframe, text=" ", bg=c[i], width=12, height=2)
            colour1.place(relx=0.53, rely=0.56 + (0.09 * i))
        cursor1.execute("SELECT Party, Candidate_Name FROM CM_Candidate WHERE Province=?",
                        (provincelabel,))
        candidate = cursor1.fetchall()
        for j in range(0, 4):
            candidate_name = Label(master=cmframe, text=f"{candidate[j][1]} ({candidate[j][0]})",
                                   font=("Times New Roman", 16), fg="black", bg="white", height=2)
            candidate_name.place(relx=0.63, rely=0.55 + (0.09 * j))
        cursor1.execute("SELECT Party, Votes FROM CM_Candidate WHERE Province=?", (provincelabel,))
        cmdata = cursor1.fetchall()
        cmparties, cmvotes = zip(*cmdata)
        fig1, ax1 = plt.subplots()
        bars = ax1.bar(cmparties, cmvotes, color=c, width=0.4)
        cursor1.execute("SELECT COUNT (*) FROM Citizens WHERE Voted <> 'Yes'")
        result = cursor1.fetchone()
        if result[0] == 0:
            winner_index1 = cmvotes.index(max(cmvotes))
            winner_party1 = cmparties[winner_index1]
            cursor1.execute("SELECT Candidate_Name FROM CM_Candidate WHERE (Province = ? AND"
                            " Party = ?)", (provincelabel, winner_party1))
            winner_candidate = cursor1.fetchone()
            runner_up_index1 = (winner_index1 + 1) % len(cmparties)
            vote_difference1 = cmvotes[winner_index1] - cmvotes[runner_up_index1]
            ax1.set_xlabel(f"{winner_candidate[0]} ({winner_party1}) has won by {vote_difference1} votes")
        ax1.set_title(f"Votes for CM ({provincelabel})", fontsize=10)
        for bar, vote_count in zip(bars, cmvotes):
            ax1.annotate(str(vote_count), xy=(bar.get_x() + bar.get_width() / 2, bar.get_height()),
                         xytext=(0, 3), textcoords="offset points",
                         ha='center', va='bottom')
        ax1.set_ylim(0, max(cmvotes) * 1.1)
        canvas1 = FigureCanvasTkAgg(fig1, master=cmframe)
        canvas1.draw()
        canvas1.get_tk_widget().place(relx=0.28, rely=0.28, anchor="n")
        plt.close(fig1)"""

    def display_election_results(constituency_code, frame):
        cursor = con.cursor()
        # Fetch the constituency name based on the provided constituency code
        cursor.execute("SELECT [Constituency Name] FROM [MNA Candidates] WHERE [Constituency Code] = ?",
                       (constituency_code,))
        constituency_name = cursor.fetchone()
        if constituency_name:
            # Create a key for color codes
            key = Label(master=frame, text="Key", font=("Times New Roman", 18, "italic"), fg="black", bg="white",
                        height=2)
            key.place(relx=0.69, rely=0.47)
            c = ["#32a852", "#01796f", "#5f7a67", "#052b10"]
            for i in range(0, 4):
                colour1 = Label(master=frame, text=" ", bg=c[i], width=12, height=2)
                colour1.place(relx=0.55, rely=0.56 + (0.09 * i))

            # Fetch candidate names and parties from the database
            cursor.execute("SELECT Party, [Candidate Name] FROM [MNA Candidates] WHERE [Constituency Code] = ?",
                           (constituency_code,))
            candidates = cursor.fetchall()
            for j in range(0, min(len(candidates), 4)):
                candidate_name = Label(master=frame, text=f"{candidates[j][1]} ({candidates[j][0]})",
                                       font=("Times New Roman", 16), fg="black", bg="white", height=2)
                candidate_name.place(relx=0.65, rely=0.55 + (0.09 * j))

            # Fetch vote counts for each party
            cursor.execute("SELECT Party, Votes FROM [MNA Candidates] WHERE [Constituency Code] = ?",
                           (constituency_code,))
            mnadata = cursor.fetchall()
            mnaparties, mnavotes = zip(*mnadata)

            # Plotting the election results
            fig, ax = plt.subplots()
            bars = ax.bar(mnaparties, mnavotes, color=c, width=0.4)
            cursor.execute("SELECT COUNT (*) FROM Citizens WHERE Voted <> 'Yes'")
            result = cursor.fetchone()
            if result[0] == 0:
                # Calculate winner and display winner information
                winner_index2 = mnavotes.index(max(mnavotes))
                winner_party2 = mnaparties[winner_index2]
                cursor.execute("SELECT [Candidate Name] FROM [MNA Candidates] WHERE "
                               "([Constituency code] = ? AND Party = ?)", (constituency_code, winner_party2))
                winner_candidate = cursor.fetchone()
                runner_up_index2 = (winner_index2 + 1) % len(mnaparties)
                vote_difference2 = mnavotes[winner_index2] - mnavotes[runner_up_index2]
                ax.set_xlabel(f"{winner_candidate[0]} ({winner_party2}) has won by {vote_difference2} votes")
            ax.set_title(f"{ccodelabel} {cnamelabel}", fontsize=10)

            ax.set_title(f"{constituency_code} {constituency_name[0]}", fontsize=10)

            # Annotating each bar with its vote count
            for bar, vote_count in zip(bars, mnavotes):
                ax.annotate(str(vote_count), xy=(bar.get_x() + bar.get_width() / 2, bar.get_height()),
                            xytext=(0, 3), textcoords="offset points",
                            ha='center', va='bottom')
            ax.set_ylim(0, max(mnavotes) * 1.1)

            # Embed the plot in the tkinter frame
            canvas = FigureCanvasTkAgg(fig, master=frame)
            canvas.draw()
            canvas.get_tk_widget().place(relx=0.3, rely=0.28, anchor="n")
            # Close the matplotlib figure to prevent multiple windows
            plt.close(fig)

    def mna_frame():
        global ccodelabel
        global cnamelabel
        cursor1 = con.cursor()

        # Fetch the constituency code and name of the logged-in user
        cursor1.execute(f"SELECT [Constituency code], [Constituency name] FROM Citizens WHERE Password = '{user_pass}'")
        user_data = cursor1.fetchall()
        if user_data:
            ccodelabel = user_data[0][0]
            cnamelabel = user_data[0][1]
            # Create the MNA frame and display election results for the constituency
            mnaframe = customtkinter.CTkFrame(master=right_frame1, width=1800, fg_color="white", height=500,
                                              corner_radius=0)
            mnaframe.pack(side="right", fill="both")
            ecp_banner_label1 = Label(master=mnaframe, image=ecp_banner, background="white", height=250)
            ecp_banner_label1.pack(fill=Y)
            display_election_results(ccodelabel, mnaframe)

    def search_frame():
        # Create the search frame
        searchframe = customtkinter.CTkFrame(master=right_frame1, width=1800, fg_color="white", height=500,
                                             corner_radius=0)
        searchframe.pack(side="right", fill="both")
        ecp_banner_label1 = Label(master=searchframe, image=ecp_banner, background="white", height=250)
        ecp_banner_label1.pack(fill="y")
        # Define valid constituency codes
        valid_ccodes = [f"NA-{i}" for i in range(1, 267)]

        def search_result():
            global cnamelabel

            # Retrieve the constituency code from the search bar
            ccode = search_bar.get().upper()
            # Remove previous search elements from the frame
            search_text.destroy()
            search_bar.destroy()
            search.destroy()

            # Check if the entered constituency code is valid
            if ccode in valid_ccodes:
                # Display a message if data is not available for a specific constituency
                if ccode == "NA-8":
                    nonavailability = customtkinter.CTkLabel(master=searchframe, text="Data not available.",
                                                             fg_color="white", text_color="black",
                                                             font=("Times New Roman", 22))
                    nonavailability.place(relx=0.01, rely=0.3)
                else:
                    # Display election results for the searched constituency
                    display_election_results(ccode, searchframe)
            else:
                # Display a message for an invalid constituency code
                invalid_ccode = customtkinter.CTkLabel(master=searchframe, text="Invalid constituency code",
                                                       fg_color="white", text_color="black",
                                                       font=("Times New Roman", 22))
                invalid_ccode.place(relx=0.01, rely=0.3)
        search_text = customtkinter.CTkLabel(master=searchframe, text="To search result of any other constituency, type"
                                                                      " constituency code in the search bar in this "
                                                                      "format: NA-1",
                                             fg_color="white", text_color="black", font=("Times New Roman", 20),
                                             corner_radius=5)
        search_text.place(relx=0.01, rely=0.45)
        # Add search bar for entering constituency code
        search_bar = customtkinter.CTkEntry(master=searchframe, bg_color="white", border_width=2, border_color="gray",
                                            width=450, placeholder_text="Search", height=50)
        search_bar.place(relx=0.2, rely=0.5)
        # Add search button
        search = customtkinter.CTkButton(master=searchframe, text="Search", bg_color="#b1b3b1", border_width=2,
                                         border_color="gray", height=50, corner_radius=5, command=search_result)
        search.place(relx=0.6, rely=0.5)

    def help_frame():
        # Create the help frame
        helpframe = customtkinter.CTkFrame(master=right_frame1, width=1800, fg_color="white", height=500,
                                           corner_radius=0)
        helpframe.pack(side="right", fill="both")
        ecp_banner_label1 = Label(master=helpframe, image=ecp_banner, background="white", height=250)
        ecp_banner_label1.pack(fill="y")
        bottom_left_text = Label(master=helpframe, text="FAQ", font=("Times New Roman", 30), fg="black")
        bottom_left_text.place(x=450, y=205)
        bottom_left_text = Label(master=helpframe, text="1.How do i cast my vote?", font=("Times New Roman", 22),
                                 fg="black", bg="white")
        bottom_left_text.place(x=20, y=240)
        bottom_left_text = Label(master=helpframe,
                                 text="Ans:First you need to login if you have already registered ,if not then get "
                                      "registered first and then in dashboard on \n left side go to the option voting "
                                      ", there you can vote your desired party.",
                                 font=("Times New Roman", 22), fg="black", bg="white")
        bottom_left_text.place(x=20, y=275)
        bottom_left_text = Label(master=helpframe, text="2.How do i change my password?", font=("Times New Roman", 22),
                                 fg="black", bg="white")
        bottom_left_text.place(x=20, y=350)
        bottom_left_text = Label(master=helpframe,
                                 text="Ans:In order to change your password you need to get registered again.",
                                 font=("Times New Roman", 22), fg="black", bg="white")
        bottom_left_text.place(x=20, y=385)
        bottom_left_text = Label(master=helpframe, text="3.Which features are present in the dashboard?",
                                 font=("Times New Roman", 22), fg="black", bg="white")
        bottom_left_text.place(x=20, y=425)
        bottom_left_text = Label(master=helpframe,
                                 text="Ans:First option in dashboard is home page, second is user details where you "
                                      "can find your details, third option is ",
                                 font=("Times New Roman", 22), fg="black", bg="white")
        bottom_left_text.place(x=20, y=460)
        bottom_left_text = Label(master=helpframe,
                                 text="voting panel where you can cast your vote,fourth one is results where you can "
                                      "find results as soon a elections are \n over and lastly help where you get "
                                      "answers to your queries",
                                 font=("Times New Roman", 22), fg="black", bg="white")
        bottom_left_text.place(x=20, y=492)
        bottom_left_text = Label(master=helpframe, text="4.I have found some errors in my data,how do i fix it?",
                                 font=("Times New Roman", 22), fg="black", bg="white")
        bottom_left_text.place(x=20, y=582)
        bottom_left_text = Label(master=helpframe,
                                 text="Ans:We have taken data from nadra so if you have found any errors reach to the"
                                      " concerned authorities.",
                                 font=("Times New Roman", 22), fg="black", bg="white")
        bottom_left_text.place(x=20, y=622)
        bottom_left_text = Label(master=helpframe, text="5.When and how will be the results displayed?",
                                 font=("Times New Roman", 22), fg="black", bg="white")
        bottom_left_text.place(x=20, y=662)
        bottom_left_text = Label(master=helpframe,
                                 text="Ans.Results will be shown in the result section presented on dashboard as"
                                      " soon as election is over.",
                                 font=("Times New Roman", 22), fg="black", bg="white")
        bottom_left_text.place(x=20, y=702)

    def sign_out():
        # Ask for confirmation before signing out
        confirm_message = messagebox.askyesnocancel(title="Confirmation Message",
                                                    message="Are you sure want to sign out?")
        if confirm_message:
            # If confirmed, return to the login page
            when_clicked(login_page)
        else:
            # If canceled, stay on the main window
            mainwindow()

    def destroy_previous_frames():
        # Destroy all widgets in the right_frame1
        for i in right_frame1.winfo_children():
            i.destroy()

    def erase_indicate():
        # Reset the background color of all indicators
        dashboard_indicate.config(background="#014112")
        user_button_indicate.config(background="#014112")
        votepanel_indicate.config(background="#014112")
        """pm_indicate.config(background="#014112")
        cm_indicate.config(background="#014112")"""
        mna_indicate.config(background="#014112")
        search_indicate.config(background="#014112")
        help_indicate.config(background="#014112")

    def when_clickedd(indicator, frame_x):
        erase_indicate()
        indicator.config(background="white")
        destroy_previous_frames()
        frame_x()

    def when_clicked2(frame_y):
        destroy_previous_frames()
        frame_y()

    # buttons
    dashboard_button = customtkinter.CTkButton(master=left_frame1, hover_color="#568203", fg_color="#014112",
                                               text="Home", font=("sans serif", 33, "bold"), width=250,
                                               command=lambda: when_clickedd(dashboard_indicate, dashboard_frame))
    dashboard_button.place(x=5, y=240)
    dashboard_indicate = tkinter.Label(master=left_frame1, text=" ", background="#014112", width=1, height=2)
    dashboard_indicate.place(x=2, y=243)

    user_button = customtkinter.CTkButton(master=left_frame1, hover_color="#568203", fg_color="#014112",
                                          text="User Details", font=("sans serif", 33, "bold"), width=250,
                                          command=lambda: when_clickedd(user_button_indicate, user_frame))
    user_button.place(x=5, y=300)
    user_button_indicate = Label(master=left_frame1, text=" ", background="#014112", width=1, height=2)
    user_button_indicate.place(x=2, y=303)

    votepanel_button = customtkinter.CTkButton(master=left_frame1, hover_color="#568203", fg_color="#014112",
                                               text="Voting Panel", font=("sans serif", 33, "bold"), width=250,
                                               command=lambda: when_clickedd(votepanel_indicate, vote_frame))
    votepanel_button.place(x=5, y=360)
    votepanel_indicate = Label(master=left_frame1, text=" ", background="#014112", width=1, height=2)
    votepanel_indicate.place(x=2, y=363)

    """pm_button = customtkinter.CTkButton(master=left_frame1, hover_color="#568203", fg_color="#014112",
                                        text="Result for PM", font=("sans serif", 33, "bold"), width=250,
                                        command=lambda: when_clickedd(pm_indicate, pm_frame))
    pm_button.place(x=5, y=420)
    pm_indicate = Label(master=left_frame1, text=" ", background="#014112", width=1, height=2)
    pm_indicate.place(x=2, y=423)
    cm_button = customtkinter.CTkButton(master=left_frame1, hover_color="#568203", fg_color="#014112",
                                        text="Result for CM", font=("sans serif", 33, "bold"), width=250,
                                        command=lambda: when_clickedd(cm_indicate, cm_frame))
    cm_button.place(x=5, y=480)
    cm_indicate = Label(master=left_frame1, text=" ", background="#014112", width=1, height=2)
    cm_indicate.place(x=2, y=483)"""
    mna_button = customtkinter.CTkButton(master=left_frame1, hover_color="#568203", fg_color="#014112",
                                         text="Result", font=("sans serif", 33, "bold"), width=250,
                                         command=lambda: when_clickedd(mna_indicate, mna_frame))
    mna_button.place(x=5, y=420)
    mna_indicate = Label(master=left_frame1, text=" ", background="#014112", width=1, height=2)
    mna_indicate.place(x=2, y=423)
    search_button = customtkinter.CTkButton(master=left_frame1, hover_color="#568203", fg_color="#014112",
                                            text="Search", font=("sans serif", 33, "bold"), width=250,
                                            command=lambda: when_clickedd(search_indicate, search_frame))
    search_button.place(x=5, y=480)
    search_indicate = Label(master=left_frame1, text=" ", background="#014112", width=1, height=2)
    search_indicate.place(x=2, y=483)
    help_button = customtkinter.CTkButton(master=left_frame1, hover_color="#568203", fg_color="#014112", text="Help",
                                          font=("sans serif", 33, "bold"), width=250,
                                          command=lambda: when_clickedd(help_indicate, help_frame))
    help_button.place(x=5, y=540)
    help_indicate = Label(master=left_frame1, text=" ", background="#014112", width=1, height=2)
    help_indicate.place(x=2, y=543)
    sign_out_button = customtkinter.CTkButton(master=left_frame1, hover_color="#568203", fg_color="#014112",
                                              text="Sign Out", font=("sans serif", 33, "bold"), width=250,
                                              command=sign_out)
    sign_out_button.place(x=5, y=600)


def login_page():
    global enter_cnic
    global enter_password
    global user_pass
    left_frame1 = customtkinter.CTkFrame(master=root2, fg_color="#f0f0f0", width=400)
    left_frame1.pack(side="left", fill="both")
    right_frame1 = customtkinter.CTkFrame(master=root2, fg_color="#014112", width=1960)
    right_frame1.pack(side="right", fill="both")
    pec_welcomelabel1 = tkinter.Label(right_frame1, text="PAKISTAN \nELECTION \nCOMMISSION", font=("arial black", 55),
                                      background="#014112", foreground="white")
    pec_welcomelabel1.pack(padx=35, pady=100, anchor="s")
    pec_welcometext1 = tkinter.Label(right_frame1,
                                     text="Welcome to the official portal of the Pakistan Election Commission.     "
                                          "\n This is where your vote will be cast for the upcoming General Elections."
                                          "\n Please Login to proceed.", font=("arial", 23, "bold"), width=1000,
                                     background="#014112", foreground="white")
    pec_welcometext1.pack(padx=35, pady=10)

    login_label1 = customtkinter.CTkButton(master=left_frame1, text="LOGIN", bg_color="white", fg_color="#014112",
                                           font=("sans serif", 48, "bold"), width=100, text_color="white",
                                           state=DISABLED, text_color_disabled="white")
    login_label1.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)
    enter_cnic = customtkinter.CTkEntry(master=left_frame1, bg_color="white", border_width=2, border_color="gray",
                                        width=200, placeholder_text="Enter CNIC number", height=40)
    enter_cnic.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)
    enter_password = customtkinter.CTkEntry(master=left_frame1, bg_color="white", border_width=2, border_color="gray",
                                            width=200, placeholder_text="Enter Password", show="•", height=40)
    enter_password.place(relx=0.5, rely=0.46, anchor=tkinter.CENTER)
    login_button1 = customtkinter.CTkButton(master=left_frame1, width=200, bg_color="light blue", fg_color="#014112",
                                            text="Login", text_color="WHITE", height=40,
                                            font=("sans serif", 20, "bold"), command=login_)
    login_button1.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)
    new_user1 = customtkinter.CTkLabel(master=left_frame1, text="New User?", fg_color="#f0f0f0", bg_color="white",
                                       height=35, font=("calibri", 15, "bold"), text_color="black")
    new_user1.place(relx=0.5, rely=0.65, anchor=tkinter.CENTER)
    register_button1 = customtkinter.CTkButton(master=left_frame1, width=160, bg_color="light green",
                                               fg_color="#014112", text="Register Here", text_color="WHITE", height=40,
                                               font=("sans serif", 20, "bold"), command=lambda: when_clicked(reg_page))
    register_button1.place(anchor=tkinter.CENTER, relx=0.5, rely=0.7)


def reg_page():
    def check_cnic_and_set_password():
        cnic_value = enter_cnic1.get()
        password_value = enter_password1.get()
        cursor = con.cursor()
        cursor.execute(f"SELECT * FROM Citizens WHERE ID = '{cnic_value}'")
        result = cursor.fetchone()
        if result:
            if not password_value:
                messagebox.showinfo(message="Password cannot be empty.", title="Error")
                return
            user_id, dob = result.ID, result.Date
            # Check age for voting eligibility
            eighteen_years_ago = datetime.now() - timedelta(days=365 * 18)

            if dob <= eighteen_years_ago:
                # User is 18 or older, allow voting
                cursor.execute(f"UPDATE Citizens SET Password = '{password_value}' WHERE ID = '{user_id}'")
                con.commit()
                messagebox.showinfo(message="Registration Successful!\nPlease proceed to Login.",
                                    title="Confirmation Message")
                when_clicked(login_page)

            else:
                # User is younger than 18, not eligible to vote
                messagebox.showinfo(message="Unable to register.\nYou are under 18.", title="Confirmation Message")
        else:
            messagebox.showinfo(message="Unable to register.\nCNIC not found.", title="Confirmation Message")

    left_frame1 = customtkinter.CTkFrame(master=root2, fg_color="#f0f0f0", width=400)
    left_frame1.pack(side="left", fill="both")
    right_frame1 = customtkinter.CTkFrame(master=root2, fg_color="#014112", width=1960)
    right_frame1.pack(side="right", fill="both")
    pec_welcomelabel1 = tkinter.Label(right_frame1, text="PAKISTAN \nELECTION \nCOMMISSION", font=("arial black", 55),
                                      background="#014112", foreground="white")
    pec_welcomelabel1.pack(padx=35, pady=100, anchor="s")
    pec_welcometext1 = tkinter.Label(right_frame1,
                                     text="Welcome to the official portal of the Pakistan Election Commission.     "
                                          "\n This is where your vote will be cast for the upcoming General Elections."
                                          "\n Please Register to proceed.", font=("arial", 25, "bold"), width=1000,
                                     background="#014112", foreground="white")
    pec_welcometext1.pack(padx=35, pady=10)
    back_button = customtkinter.CTkButton(master=left_frame1, text="go back", bg_color="white", fg_color="#014112",
                                          font=("arial", 15, "bold"), hover_color="#568203", text_color="white",
                                          command=lambda: when_clicked(login_page), corner_radius=2, width=10)
    back_button.place(relx=0.1, rely=0.1, anchor=tkinter.CENTER)
    register_label = customtkinter.CTkButton(master=left_frame1, text="Register", bg_color="white", fg_color="#014112",
                                             font=("sans serif", 48, "bold"), width=100, text_color="white",
                                             state=DISABLED, text_color_disabled="white")
    register_label.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)
    enter_cnic1 = customtkinter.CTkEntry(master=left_frame1, bg_color="white", border_width=2, border_color="gray",
                                         width=200, placeholder_text="Enter valid CNIC number", height=40)
    enter_cnic1.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)
    enter_password1 = customtkinter.CTkEntry(master=left_frame1, bg_color="white", border_width=2, border_color="gray",
                                             width=200, placeholder_text="Set Password", show="•", height=40)
    enter_password1.place(relx=0.5, rely=0.36, anchor=tkinter.CENTER)
    place_holder_text = ["Enter Father's Name", "Enter City Of Residence", "Enter Date Of Birth", "Enter Gender"]
    for i in range(0, 4):
        rest_of_entry_label = customtkinter.CTkEntry(master=left_frame1, bg_color="white", border_width=2,
                                                     border_color="gray", width=200,
                                                     placeholder_text=place_holder_text[i], height=40)
        rest_of_entry_label.place(relx=0.5, rely=0.42+(0.06*i), anchor=tkinter.CENTER)

    register_button1 = customtkinter.CTkButton(master=left_frame1, width=200, bg_color="light blue", fg_color="#014112",
                                               text="Confirm Registration", text_color="WHITE", height=40,
                                               font=("sans serif", 20, "bold"), command=check_cnic_and_set_password)
    register_button1.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)


# other functions
def destroy():
    for i in root2.winfo_children():
        i.destroy()


def when_clicked(page):
    destroy()
    page()


# login page first page when clicked
def validate_login(cnic, password):
    cursor1 = con.cursor()
    cursor1.execute("SELECT * FROM Citizens WHERE ID=? AND Password=?", (cnic, password))
    user = cursor1.fetchone()
    if user:
        return True
    else:
        return False


def login_():
    cnic = enter_cnic.get()
    global user_pass
    password = enter_password.get()
    if validate_login(cnic, password):
        user_pass = enter_password.get()
        when_clicked(mainwindow)
    else:
        messagebox.showinfo(message="Unable to Login.\nPlease provide valid credentials.")


left_frame = customtkinter.CTkFrame(master=root2, fg_color="#f0f0f0", width=400)
left_frame.pack(side="left", fill="both")
right_frame = customtkinter.CTkFrame(master=root2, fg_color="#014112", width=1960)
right_frame.pack(side="right", fill="both")
PEC_welcomelabel = tkinter.Label(right_frame, text="PAKISTAN \nELECTION \nCOMMISSION", font=("arial black", 55),
                                 background="#014112", foreground="white")
PEC_welcomelabel.pack(padx=35, pady=100, anchor="s")
PEC_logo = PhotoImage(file="images\\logo.png")
PEC_logo_label = Label(master=left_frame, image=PEC_logo, height=480)
PEC_logo_label.pack()
PEC_welcometext = tkinter.Label(right_frame, text="Welcome to the official portal of the Pakistan Election Commission. "
                                                  "\n This is where your vote will be cast for the upcoming General "
                                                  "Elections.\n Please Login to proceed.", font=("arial", 26, "bold"),
                                width=1000, background="#014112", foreground="white")
PEC_welcometext.pack(padx=35, pady=10)


login_label = customtkinter.CTkButton(master=left_frame, text="LOGIN", bg_color="white", fg_color="#014112",
                                      font=("sans serif", 48, "bold"), width=100, text_color="white", state=DISABLED,
                                      text_color_disabled="white").place(relx=0.5, rely=0.65, anchor=tkinter.CENTER)
enter_cnic = customtkinter.CTkEntry(master=left_frame, bg_color="white", border_width=2, border_color="gray", width=200,
                                    placeholder_text="Enter CNIC number", height=40)
enter_cnic.place(relx=0.5, rely=0.72, anchor=tkinter.CENTER)
enter_password = customtkinter.CTkEntry(master=left_frame, bg_color="white", border_width=2, border_color="gray",
                                        width=200, placeholder_text="Enter Password", show="•", height=40)
enter_password.place(relx=0.5, rely=0.78, anchor=tkinter.CENTER)
login_button = customtkinter.CTkButton(master=left_frame, width=200, bg_color="light blue", fg_color="#014112",
                                       text="Login", text_color="WHITE", height=40, font=("sans serif", 20, "bold"),
                                       command=login_)
login_button.place(relx=0.5, rely=0.84, anchor=tkinter.CENTER)
new_user = customtkinter.CTkLabel(master=left_frame, text="New User?", fg_color="#f0f0f0", bg_color="white", height=35,
                                  font=("calibri", 15, "bold"), text_color="black")
new_user.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)
register_button = customtkinter.CTkButton(master=left_frame, width=160, bg_color="light green", fg_color="#014112",
                                          text="Register Here", text_color="WHITE", height=40,
                                          font=("sans serif", 20, "bold"), command=lambda: when_clicked(reg_page))
register_button.place(anchor=tkinter.CENTER, relx=0.5, rely=0.94)


root2.mainloop()
