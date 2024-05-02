import tkinter as tk
from tkinter import messagebox
import pickle

class Employee: #Define employee class
    def __init__(self, name, employee_ID, department, job,
                 salary, age, dob, passport):
        #Initialize class objects and attributes
        self.name = name
        self.employee_ID = employee_ID
        self.department = department
        self.job = job
        self.salary = salary
        self.age = age
        self.dob = dob
        self.passport = passport

class Event: #Define event class
    def __init__(self, event_ID, type, theme, date, time, duration,
                 venue,client, guest_list, catering_company,
                 entertainment_company, suppliers, invoice):
        # Initialize class objects and attributes
        self.event_ID = event_ID
        self.type = type
        self.theme = theme
        self.date = date
        self.time = time
        self.duration = duration
        self.venue = venue
        self.client = client
        self.guest_list = guest_list
        self.catering_company = catering_company
        self.entertainment_company = entertainment_company
        self.suppliers = suppliers
        self.invoice = invoice

class Client: #Define client class
    def __init__(self, client_ID, name, address, contact_details, budget):
        # Initialize class objects and attributes
        self.client_ID = client_ID
        self.name = name
        self.address = address
        self.contact_details = contact_details
        self.budget = budget

class Guest: #Define guest class
    def __init__(self, guest_ID, name, address, contact_details):
        # Initialize class objects and attributes
        self.guest_ID = guest_ID
        self.name = name
        self.address = address
        self.contact_details = contact_details

class Venue: #Define venue class
    def __init__(self, venue_ID, name, address, contact, min_guests, max_guests
                 ):
        # Initialize class objects and attributes
        self.venue_ID = venue_ID
        self.name = name
        self.address = address
        self.contact = contact
        self.min_guests = min_guests
        self.max_guests = max_guests

class Caterers: #Define caterers class
    def __init__(self, caterers_ID, name, address, contact_details,
                 menu, min_guests, max_guests):
        # Initialize class objects and attributes
        self.caterers_ID = caterers_ID
        self.name = name
        self.address = address
        self.contact_details = contact_details
        self.menu = menu
        self.min_guests = min_guests
        self.max_guests = max_guests

class EventManagentSystemGUI: #Define GUI class
    def __init__(self, master):
        # Initialize GUI with master
        self.master = master
        self.master.title("Event Management System") #Set title for GUI window
        self.create_widgets() #Create GUI widgets
        #Initialize empty lists to store records
        self.employee = []
        self.event = []
        self.client = []
        self.guest = []
        self.venue = []
        self.caterers = []
        self.load_data() #Load existing data from file

    def create_widgets(self):
        # Create the main frame for GUI
        self.main_frame = tk.Frame(self.master)
        self.main_frame.pack(padx=20, pady=20)

        # Create add buttons
        self.add_button = tk.Button(self.main_frame, text="Add", command=self.add_record)
        self.add_button.grid(row=0, column=0, padx=5, pady=5)

        #Create delete bottons
        self.delete_button = tk.Button(self.main_frame, text="Delete", command=self.delete_record)
        self.delete_button.grid(row=0, column=1, padx=5, pady=5)

        #Create modify bottons
        self.modify_button = tk.Button(self.main_frame, text="Modify", command=self.modify_record)
        self.modify_button.grid(row=0, column=2, padx=5, pady=5)

        #Create display bottons
        self.display_button = tk.Button(self.main_frame, text="Display", command=self.display_record)
        self.display_button.grid(row=0, column=3, padx=5, pady=5)

        # Add labels for record types
        tk.Label(self.main_frame, text="Record Type:").grid(row=1, column=0, padx=5, pady=5) #Create label

        self.record_type = tk.StringVar() #Create stringVar to hold selected record type
        self.record_type.set("Employee") #Set default value for record type
        self.record_type_menu = tk.OptionMenu(self.main_frame, self.record_type, "Employee", "Event", "Client","Guest",
                                              "Venue", "Caterers") #Create dropdown menu
        self.record_type_menu.grid(row=1, column=1, columnspan=3, padx=5, pady=5) #Place dropdown menu in grid layout

    def add_record(self):
        record_type = self.record_type.get() #Get the selected record type
        #Check the selected record type and call the corresponding add function
        if record_type == "Employee":
            self.add_employee()
        elif record_type == "Event":
            self.add_event()
        elif record_type == "Client":
            self.add_client()
        elif record_type == "Guest":
            self.add_guest()
        elif record_type == "Venue":
            self.add_venue()
        elif record_type == "Caterers":
            self.add_caterers()

    def delete_record(self):
        record_type = self.record_type.get() #Check the selected record type
        index = self.listbox.curselection() #Get the index of the selected item
        
        #Check if an item is selected
        if index:
            index = int(index[0]) #Convert index to integer

            #Check the selected record type and delete the corresponding record
            if record_type == "Employee":
                del self.employee[index]
            elif record_type == "Event":
                del self.event[index]
            elif record_type == "Client":
                del self.client[index]
            elif record_type == "Guest":
                del self.guest[index]
            elif record_type == "Venue":
                del self.venue[index]
            elif record_type == "Caterers":
                del self.caterers[index]
            messagebox.showinfo("Success", "Record deleted successfully.") #Show success message after deleting the record
            self.display_record() #Refresh the display to reflect changes
        else:
            messagebox.showerror("Error", "Please select a record to delete.") #Show wrror message if no item is selected

    def modify_record(self):
        record_type = self.record_type.get() #Get the selected record type
        index = self.listbox.curselection() #Get the index of the selected item

        #Check if an item is selected
        if index:
            index = int(index[0]) #Convert index to integer

            #Check the selected record type and call modify_record_details method
            if record_type == "Employee":
                self.modify_record_details(index, self.employee, "Employee")
            elif record_type == "Event":
                self.modify_record_details(index, self.event, "Event")
            elif record_type == "Client":
                self.modify_record_details(index, self.client, "Client")
            elif record_type == "Guest":
                self.modify_record_details(index, self.guest, "Guest")
            elif record_type == "Venue":
                self.modify_record_details(index, self.venue, "Venue")
            elif record_type == "Caterers":
                self.modify_record_details(index, self.caterers, "Caterers")
        else:
            messagebox.showerror("Error", "Please select a record to modify.") #Show error message if no item is selected

    def modify_record_details(self, index, record_list, record_type):
        #Open a new top-level window for modifying record details
        top = tk.Toplevel(self.master)
        top.title(f"Modify {record_type}") #Set title of the top-level window

        #Get the record to be motified and its attributes
        record = record_list[index]
        attributes = self.get_record_attributes(record_type) #Get attributes for the specified record type

        entry_list = [] #Initialize a list to store Entry widgets

        #Iterate over attributes and create labels and entry fields for each attribute
        for i, attribute in enumerate(attributes):
            #Create label for the attribute
            tk.Label(top, text=f"{attribute.capitalize()}:").grid(row=i, column=0, padx=5, pady=5)
            #Create entry field and insert current atttribute value
            entry = tk.Entry(top)
            entry.insert(0, getattr(record, attribute)) #Get attribute value using getattr() function
            entry.grid(row=i, column=1, padx=5, pady=5)
            entry_list.append(entry) #Add entry field to entry_list for future reference

        def save_record():
            #Iterate over attributes and update record with entry values
            for i, attribute in enumerate(attributes):
                setattr(record, attribute, entry_list[i].get()) #Get attribute value 
            messagebox.showinfo("Success", f"{record_type} modified successfully.") #Show success message
            top.destroy() #Close
            self.display_record() #Refresh the displayed records
            
        #Create a save botton 
        save_button = tk.Button(top, text="Save", command=save_record)
        save_button.grid(row=len(attributes), columnspan=2, padx=5, pady=5)

    def get_record_attributes(self, record_type):
        #Define attributes based on the record type
        if record_type == "Employee":
            return ["name", "employee_ID", "department", "job", "salary", "age", "dob", "passport"]
        elif record_type == "Event":
            return ["event_ID", "type", "theme", "date", "time", "duration", "venue", "client", "guest_list",
                    "catering_company", "entertainment_company", "suppliers", "invoice"]
        elif record_type == "Client":
            return ["client_ID", "name", "address", "contact_details", "budget"]
        elif record_type == "Guest":
            return ["guest_ID", "name", "address", "contact_details"]
        elif record_type == "Venue":
            return ["venue_ID", "name", "address", "contact", "min_guests", "max_guests"]
        elif record_type == "Caterers":
            return ["caterers_ID", "name", "address", "contact_details", "menu", "min_guests", "max_guests"]

    def display_record(self):
        #Destroy exisiting listbox frame
        try:
            self.listbox_frame.destroy()
        except AttributeError:
            pass

        #Create a new listbox frame
        self.listbox_frame = tk.Frame(self.main_frame)
        self.listbox_frame.grid(row=2, column=0, columnspan=4, padx=5, pady=5)

        #Determine the record type and corresponding labels
        record_type = self.record_type.get()
        if record_type == "Employee":
            records = self.employee
            labels = ["Name", "Employee ID", "Department", "Job", "Salary", "Age", "Date of Birth", "Passport"]
        elif record_type == "Event":
            records = self.event
            labels = ["Event ID", "Type", "Theme", "Date", "Time", "Duration", "Venue", "Client", "Guest List",
                      "Catering Company", "Entertainment Company", "Suppliers", "Invoice"]
        elif record_type == "Client":
            records = self.client
            labels = ["Client ID", "Name", "Address", "Contact Details", "Budget"]
        elif record_type == "Guest":
            records = self.guest
            labels = ["Guest ID", "Name", "Address", "Contact Details"]
        elif record_type == "Venue":
            records = self.venue
            labels = ["Venue ID", "Name", "Address", "Contact", "Min Guests", "Max Guests"]
        elif record_type == "Caterers":
            records = self.caterers
            labels = ["Caterers ID", "Name", "Address", "Contact Details", "Menu", "Min Guests", "Max Guests"]

        #Create a listbox to display records
        self.listbox = tk.Listbox(self.listbox_frame, width=100)
        self.listbox.grid(row=0, column=0, padx=5, pady=5)

        #Populate the listbox with record details
        for record in records:
            record_details = ""
            for label, attribute in zip (labels, record.__dict__.values()):
                record_details += f"{label}: {attribute}  -  " #Combine label and attribute
            self.listbox.insert(tk.END, record_details)

        #Add a scrollbar 
        scrollbar = tk.Scrollbar(self.listbox_frame, orient=tk.VERTICAL)
        scrollbar.config(command=self.listbox.yview)
        ##The sticky parameter ensures that the scrollbar remains aligend vertically and spans from top to bottom
        scrollbar.grid(row=0, column=1, sticky=tk.N + tk.S)  

        self.listbox.config(yscrollcommand=scrollbar.set) #Connectlistbox and scrollbar

    def add_employee(self):
        top = tk.Toplevel(self.master)
        top.title("Add Employee")

        tk.Label(top, text="Name:").grid(row=0, column=0, padx=5, pady=5)
        tk.Label(top, text="Employee ID:").grid(row=1, column=0, padx=5, pady=5)
        tk.Label(top, text="Department:").grid(row=2, column=0, padx=5, pady=5)
        tk.Label(top, text="Job:").grid(row=3, column=0, padx=5, pady=5)
        tk.Label(top, text="Salary:").grid(row=4, column=0, padx=5, pady=5)
        tk.Label(top, text="Age:").grid(row=5, column=0, padx=5, pady=5)
        tk.Label(top, text="Date of Birth:").grid(row=6, column=0, padx=5, pady=5)
        tk.Label(top, text="Passport:").grid(row=7, column=0, padx=5, pady=5)

        name_entry = tk.Entry(top)
        employee_id_entry = tk.Entry(top)
        department_entry = tk.Entry(top)
        job_entry = tk.Entry(top)
        salary_entry = tk.Entry(top)
        age_entry = tk.Entry(top)
        dob_entry = tk.Entry(top)
        passport_entry = tk.Entry(top)

        name_entry.grid(row=0, column=1, padx=5, pady=5)
        employee_id_entry.grid(row=1, column=1, padx=5, pady=5)
        department_entry.grid(row=2, column=1, padx=5, pady=5)
        job_entry.grid(row=3, column=1, padx=5, pady=5)
        salary_entry.grid(row=4, column=1, padx=5, pady=5)
        age_entry.grid(row=5, column=1, padx=5, pady=5)
        dob_entry.grid(row=6, column=1, padx=5, pady=5)
        passport_entry.grid(row=7, column=1, padx=5, pady=5)

        def save_employee():
            name = name_entry.get()
            employee_ID = employee_id_entry.get()
            department = department_entry.get()
            job = job_entry.get()
            salary = salary_entry.get()
            age = age_entry.get()
            dob = dob_entry.get()
            passport = passport_entry.get()

            new_employee = Employee(name, employee_ID, department, job, salary, age, dob, passport)
            self.employee.append(new_employee)
            messagebox.showinfo("Success", "Employee added successfully.")
            top.destroy()
            self.display_record()

        save_button = tk.Button(top, text="Save", command=save_employee)
        save_button.grid(row=8, columnspan=2, padx=5, pady=5)

    def add_event(self):
        top = tk.Toplevel(self.master)
        top.title("Add Event")

        tk.Label(top, text="Event ID:").grid(row=0, column=0, padx=5, pady=5)
        tk.Label(top, text="Type:").grid(row=1, column=0, padx=5, pady=5)
        tk.Label(top, text="Theme:").grid(row=2, column=0, padx=5, pady=5)
        tk.Label(top, text="Date:").grid(row=3, column=0, padx=5, pady=5)
        tk.Label(top, text="Time:").grid(row=4, column=0, padx=5, pady=5)
        tk.Label(top, text="Duration:").grid(row=5, column=0, padx=5, pady=5)
        tk.Label(top, text="Venue:").grid(row=6, column=0, padx=5, pady=5)
        tk.Label(top, text="Client:").grid(row=7, column=0, padx=5, pady=5)
        tk.Label(top, text="Guest List:").grid(row=8, column=0, padx=5, pady=5)
        tk.Label(top, text="Catering Company:").grid(row=9, column=0, padx=5, pady=5)
        tk.Label(top, text="Entertainment Company:").grid(row=10, column=0, padx=5, pady=5)
        tk.Label(top, text="Suppliers:").grid(row=11, column=0, padx=5, pady=5)
        tk.Label(top, text="Invoice:").grid(row=12, column=0, padx=5, pady=5)

        event_id_entry = tk.Entry(top)
        type_entry = tk.Entry(top)
        theme_entry = tk.Entry(top)
        date_entry = tk.Entry(top)
        time_entry = tk.Entry(top)
        duration_entry = tk.Entry(top)
        venue_entry = tk.Entry(top)
        client_entry = tk.Entry(top)
        guest_list_entry = tk.Entry(top)
        catering_company_entry = tk.Entry(top)
        entertainment_company_entry = tk.Entry(top)
        suppliers_entry = tk.Entry(top)
        invoice_entry = tk.Entry(top)

        event_id_entry.grid(row=0, column=1, padx=5, pady=5)
        type_entry.grid(row=1, column=1, padx=5, pady=5)
        theme_entry.grid(row=2, column=1, padx=5, pady=5)
        date_entry.grid(row=3, column=1, padx=5, pady=5)
        time_entry.grid(row=4, column=1, padx=5, pady=5)
        duration_entry.grid(row=5, column=1, padx=5, pady=5)
        venue_entry.grid(row=6, column=1, padx=5, pady=5)
        client_entry.grid(row=7, column=1, padx=5, pady=5)
        guest_list_entry.grid(row=8, column=1, padx=5, pady=5)
        catering_company_entry.grid(row=9, column=1, padx=5, pady=5)
        entertainment_company_entry.grid(row=10, column=1, padx=5, pady=5)
        suppliers_entry.grid(row=11, column=1, padx=5, pady=5)
        invoice_entry.grid(row=12, column=1, padx=5, pady=5)

        def save_event():
            event_ID = event_id_entry.get()
            type = type_entry.get()
            theme = theme_entry.get()
            date = date_entry.get()
            time = time_entry.get()
            duration = duration_entry.get()
            venue = venue_entry.get()
            client = client_entry.get()
            guest_list = guest_list_entry.get()
            catering_company = catering_company_entry.get()
            entertainment_company = entertainment_company_entry.get()
            suppliers = suppliers_entry.get()
            invoice = invoice_entry.get()

            new_event = Event(event_ID, type, theme, date, time, duration, venue, client, guest_list,
                              catering_company, entertainment_company, suppliers, invoice)
            self.event.append(new_event)
            messagebox.showinfo("Success", "Event added successfully.")
            top.destroy()
            self.display_record()

        save_button = tk.Button(top, text="Save", command=save_event)
        save_button.grid(row=13, columnspan=2, padx=5, pady=5)

    def add_client(self):
        top = tk.Toplevel(self.master)
        top.title("Add Client")

        tk.Label(top, text="Client ID:").grid(row=0, column=0, padx=5, pady=5)
        tk.Label(top, text="Name:").grid(row=1, column=0, padx=5, pady=5)
        tk.Label(top, text="Address:").grid(row=2, column=0, padx=5, pady=5)
        tk.Label(top, text="Contact Details:").grid(row=3, column=0, padx=5, pady=5)
        tk.Label(top, text="Budget:").grid(row=4, column=0, padx=5, pady=5)

        client_id_entry = tk.Entry(top)
        name_entry = tk.Entry(top)
        address_entry = tk.Entry(top)
        contact_details_entry = tk.Entry(top)
        budget_entry = tk.Entry(top)

        client_id_entry.grid(row=0, column=1, padx=5, pady=5)
        name_entry.grid(row=1, column=1, padx=5, pady=5)
        address_entry.grid(row=2, column=1, padx=5, pady=5)
        contact_details_entry.grid(row=3, column=1, padx=5, pady=5)
        budget_entry.grid(row=4, column=1, padx=5, pady=5)

        def save_client():
            client_ID = client_id_entry.get()
            name = name_entry.get()
            address = address_entry.get()
            contact_details = contact_details_entry.get()
            budget = budget_entry.get()

            new_client = Client(client_ID, name, address, contact_details, budget)
            self.client.append(new_client)
            messagebox.showinfo("Success", "Client added successfully.")
            top.destroy()
            self.display_record()

        save_button = tk.Button(top, text="Save", command=save_client)
        save_button.grid(row=5, columnspan=2, padx=5, pady=5)

    def add_guest(self):
        top = tk.Toplevel(self.master)
        top.title("Add Guest")

        tk.Label(top, text="Guest ID:").grid(row=0, column=0, padx=5, pady=5)
        tk.Label(top, text="Name:").grid(row=1, column=0, padx=5, pady=5)
        tk.Label(top, text="Address:").grid(row=2, column=0, padx=5, pady=5)
        tk.Label(top, text="Contact Details:").grid(row=3, column=0, padx=5, pady=5)

        guest_id_entry = tk.Entry(top)
        name_entry = tk.Entry(top)
        address_entry = tk.Entry(top)
        contact_details_entry = tk.Entry(top)

        guest_id_entry.grid(row=0, column=1, padx=5, pady=5)
        name_entry.grid(row=1, column=1, padx=5, pady=5)
        address_entry.grid(row=2, column=1, padx=5, pady=5)
        contact_details_entry.grid(row=3, column=1, padx=5, pady=5)

        def save_guest():
            guest_ID = guest_id_entry.get()
            name = name_entry.get()
            address = address_entry.get()
            contact_details = contact_details_entry.get()

            new_guest = Guest(guest_ID, name, address, contact_details)
            self.guest.append(new_guest)
            messagebox.showinfo("Success", "Guest added successfully.")
            top.destroy()
            self.display_record()

        save_button = tk.Button(top, text="Save", command=save_guest)
        save_button.grid(row=4, columnspan=2, padx=5, pady=5)

    def add_venue(self):
        top = tk.Toplevel(self.master)
        top.title("Add Venue")

        tk.Label(top, text="Venue ID:").grid(row=0, column=0, padx=5, pady=5)
        tk.Label(top, text="Name:").grid(row=1, column=0, padx=5, pady=5)
        tk.Label(top, text="Address:").grid(row=2, column=0, padx=5, pady=5)
        tk.Label(top, text="Contact:").grid(row=3, column=0, padx=5, pady=5)
        tk.Label(top, text="Min Guests:").grid(row=4, column=0, padx=5, pady=5)
        tk.Label(top, text="Max Guests:").grid(row=5, column=0, padx=5, pady=5)

        venue_id_entry = tk.Entry(top)
        name_entry = tk.Entry(top)
        address_entry = tk.Entry(top)
        contact_entry = tk.Entry(top)
        min_guests_entry = tk.Entry(top)
        max_guests_entry = tk.Entry(top)

        venue_id_entry.grid(row=0, column=1, padx=5, pady=5)
        name_entry.grid(row=1, column=1, padx=5, pady=5)
        address_entry.grid(row=2, column=1, padx=5, pady=5)
        contact_entry.grid(row=3, column=1, padx=5, pady=5)
        min_guests_entry.grid(row=4, column=1, padx=5, pady=5)
        max_guests_entry.grid(row=5, column=1, padx=5, pady=5)

        def save_venue():
            venue_ID = venue_id_entry.get()
            name = name_entry.get()
            address = address_entry.get()
            contact = contact_entry.get()
            min_guests = min_guests_entry.get()
            max_guests = max_guests_entry.get()

            new_venue = Venue(venue_ID, name, address, contact, min_guests, max_guests)
            self.venue.append(new_venue)
            messagebox.showinfo("Success", "Venue added successfully.")
            top.destroy()
            self.display_record()

        save_button = tk.Button(top, text="Save", command=save_venue)
        save_button.grid(row=6, columnspan=2, padx=5, pady=5)

    def add_caterers(self):
        top = tk.Toplevel(self.master)
        top.title("Add Caterers")

        tk.Label(top, text="Caterers ID:").grid(row=0, column=0, padx=5, pady=5)
        tk.Label(top, text="Name:").grid(row=1, column=0, padx=5, pady=5)
        tk.Label(top, text="Address:").grid(row=2, column=0, padx=5, pady=5)
        tk.Label(top, text="Contact:").grid(row=3, column=0, padx=5, pady=5)
        tk.Label(top, text="Menu:").grid(row=4, column=0, padx=5, pady=5)
        tk.Label(top, text="Min Guests:").grid(row=5, column=0, padx=5, pady=5)
        tk.Label(top, text="Max Guests:").grid(row=6, column=0, padx=5, pady=5)

        caterers_id_entry = tk.Entry(top)
        name_entry = tk.Entry(top)
        address_entry = tk.Entry(top)
        contact_entry = tk.Entry(top)
        menu_entry = tk.Entry(top)
        min_guests_entry = tk.Entry(top)
        max_guests_entry = tk.Entry(top)

        caterers_id_entry.grid(row=0, column=1, padx=5, pady=5)
        name_entry.grid(row=1, column=1, padx=5, pady=5)
        address_entry.grid(row=2, column=1, padx=5, pady=5)
        contact_entry.grid(row=3, column=1, padx=5, pady=5)
        menu_entry.grid(row=4, column=1, padx=5, pady=5)
        min_guests_entry.grid(row=5, column=1, padx=5, pady=5)
        max_guests_entry.grid(row=6, column=1, padx=5, pady=5)

        def save_caterers():
            caterers_ID = caterers_id_entry.get()
            name = name_entry.get()
            address = address_entry.get()
            contact = contact_entry.get()
            menu = menu_entry.get()
            min_guests = min_guests_entry.get()
            max_guests = max_guests_entry.get()

            new_caterers = Caterers(caterers_ID, name, address, contact, menu, min_guests, max_guests)
            self.caterers.append(new_caterers)
            messagebox.showinfo("Success", "Caterers added successfully.")
            top.destroy()
            self.display_record()

        save_button = tk.Button(top, text="Save", command=save_caterers)
        save_button.grid(row=7, columnspan=2, padx=5, pady=5)

    def load_data(self):
        try:
            with open("data.pickle", "rb") as f: #Open data.pickle file in read mode as binary
                #Load data from pickle file and assign to respective lists
                data = pickle.load(f) #Load data from file
                self.employee = data.get('employee', [])
                self.event = data.get('event', [])
                self.client = data.get('client', [])
                self.guest = data.get('guest', [])
                self.venue = data.get('venue', [])
                self.caterers = data.get('caterers', [])
        except FileNotFoundError: #Handle file not found error
            pass #Do nothing if file not found

#Create root window and intialize the GUI
root = tk.Tk()
app = EventManagentSystemGUI(root)
root.mainloop()
