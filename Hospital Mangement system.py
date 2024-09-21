#Modules
from email.mime import application
from tkinter import *
from tkinter import ttk
import random
import datetime
import tkinter.messagebox

class Hospital:
    def __init__(self,root):
        self.root = root
        self.root.title("Hosipital Management System")
        self.root.geometry("1350x750+0+0")
        self.root.configure(background="powder blue")

        cmbNameTablets = StringVar()
        Ref = StringVar()
        Dose = StringVar()
        NumberTablets = StringVar()
        Lot = StringVar()
        IssuedDate = StringVar()
        ExpDate = StringVar()
        DailyDose = StringVar()
        PossibleSideEffects = StringVar()
        FurtherInformation = StringVar()
        StorageAdvice = StringVar()
        DrivingUsingMachine = StringVar()
        HowtoUseMedication = StringVar()
        PatientID = StringVar()
        PatientNHSNO = StringVar()
        PatientName = StringVar()
        DateofBirth = StringVar()
        PatientAddress = StringVar()
        Prescription = StringVar()

        #=========================Funtion======================================================================

        def iPrescription():

            self.txtPrescription.insert(END,'Name of Tablets: \t\t' + cmbNameTablets.get() + "\n")
            self.txtPrescription.insert(END,'Reference No.: \t\t' + Ref.get() + "\n")
            self.txtPrescription.insert(END,'Dose: \t\t' + Dose.get() + "\n")
            self.txtPrescription.insert(END,'Number of Tablets: \t\t' + NumberTablets.get() + "\n")
            self.txtPrescription.insert(END,'Lot: \t\t' + Lot.get() + "\n")
            self.txtPrescription.insert(END,'Issued Date: \t\t' + IssuedDate.get() + "\n")
            self.txtPrescription.insert(END,'Exp. Date: \t\t' + ExpDate.get() + "\n")
            self.txtPrescription.insert(END,'Daily Dose: \t\t' + DailyDose.get() + "\n")
            self.txtPrescription.insert(END,'Possible Side Effects: \t\t' + PossibleSideEffects.get() + "\n")
            self.txtPrescription.insert(END,'Further Information: \t\t' + FurtherInformation.get() + "\n")
            self.txtPrescription.insert(END,'Storage Advice: \t\t' + StorageAdvice.get() + "\n")
            self.txtPrescription.insert(END,'Driving or Using Machines: \t\t' + DrivingUsingMachine.get() + "\n")
            self.txtPrescription.insert(END,'How to Use Medication: \t\t' + HowtoUseMedication.get() + "\n")
            self.txtPrescription.insert(END,'Patient ID: \t\t' + PatientID.get() + "\n")
            self.txtPrescription.insert(END,'NHS Number: \t\t' + PatientNHSNO.get() + "\n")
            self.txtPrescription.insert(END,'Patient Name: \t\t' +PatientName.get() + "\n")
            self.txtPrescription.insert(END,'Date of Birth: \t\t' + DateofBirth.get() + "\n")
            self.txtPrescription.insert(END,'Patient Address: \t\t' + PatientAddress.get() + "\n")
            return
        
        def iPrescriptionData():
            
            self.txtFrameDetail.insert(END,"\t"+cmbNameTablets.get() + "\t\t"+Ref.get() + "\t"+Dose.get() + 
                                       "\t\t"+NumberTablets.get() + "\t"+Lot.get() +"\t"+IssuedDate.get() + 
                                       "\t\t"+ExpDate.get() + "\t"+DailyDose.get() +"\t\t"+StorageAdvice.get() + 
                                       "\t"+PatientNHSNO.get() + "\t\t"+PatientName.get() + "\t"+DateofBirth.get() +
                                       "\t"+PatientAddress.get() + "\n")    
            return
        
        def iDelete():

            cmbNameTablets.set("")
            self.cboNameTablet.current(0)
            Ref.set("")
            Dose.set("")
            NumberTablets.set("")
            Lot.set("")
            IssuedDate.set("")
            ExpDate.set("")
            DailyDose.set("")
            PossibleSideEffects.set("")
            FurtherInformation.set("")
            StorageAdvice.set("")
            DrivingUsingMachine.set("")
            HowtoUseMedication.set("")
            PatientID.set("")
            PatientNHSNO.set("")
            PatientName.set("")
            DateofBirth.set("")
            PatientAddress.set("")
            self.txtPrescription.delete("1.0",END)
            self.txtFrameDetail.delete("1.0",END)
            return
        
        def iReset():
        
            cmbNameTablets.set("")
            self.cboNameTablet.current(0)
            Ref.set("")
            Dose.set("")
            NumberTablets.set("")
            Lot.set("")
            IssuedDate.set("")
            ExpDate.set("")
            DailyDose.set("")
            PossibleSideEffects.set("")
            FurtherInformation.set("")
            StorageAdvice.set("")
            DrivingUsingMachine.set("")
            HowtoUseMedication.set("")
            PatientID.set("")
            PatientNHSNO.set("")
            PatientName.set("")
            DateofBirth.set("")
            PatientAddress.set("")
            self.txtPrescription.delete("1.0",END)
            #self.txtFrameDetail.delete("1.0",END)
            return

        def iExit():
            iExit=tkinter.messagebox.askyesno("Hosipital Management System","Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return

        #=========================Frame======================================================================
        MainFrame = Frame(self.root, bg="#060270")
        MainFrame.grid()

        TitleFrame = Frame(MainFrame, bd=2, width=1350, padx=20, relief=RIDGE, bg="#FACB0C")
        TitleFrame.pack(side=TOP)

        self.IblTitle = Label(TitleFrame, font=("Helvetica", 40, 'bold'), text="\tHosipital Management System\t", padx=2, bg="#63E131")
        self.IblTitle.grid()

        FrameDetail = Frame(MainFrame, bd=20, width=1350, height=300, padx=20, relief=RIDGE, bg="#01BBFF")
        FrameDetail.pack(side=BOTTOM)

        ButtonFrame = Frame(MainFrame, bd=20, width=1350, height=50, padx=20, relief=RIDGE, bg="#FF01D4")
        ButtonFrame.pack(side=BOTTOM)

        DataFrame = Frame(MainFrame, bd=20, width=1350, height=400, padx=20, relief=RIDGE, bg="#C00D51")
        DataFrame.pack(side=BOTTOM)

        DataFrameLEFT = LabelFrame(DataFrame, bd=10, width=800, height=300, padx=20, relief=RIDGE
                              , font=("arial", 12, 'bold'), text="Patient Information",
                               bg="#35DBE7")
        DataFrameLEFT.pack(side=LEFT)
        
        DataFrameRIGHT = LabelFrame(DataFrame, bd=10, width=450, height=300, padx=20, relief=RIDGE
                                    , font=("arial", 12, 'bold'), text="Prescription", bg="#35DBE7")
        DataFrameRIGHT.pack(side=RIGHT)

        #=========================DataFrameLEFT========================================================================
        self.IblNameTablets = Label(DataFrameLEFT, font=("arial", 12, 'bold'), text="Name of Tablets:", padx=2, pady=2,bg="#79E719")
        self.IblNameTablets.grid(row=0, column=0, sticky=W)

        self.cboNameTablet = ttk.Combobox(DataFrameLEFT, textvariable=cmbNameTablets, state='readonly',
                                          font=('arial', 12, 'bold'), width=20, background="#79E719")
        self.cboNameTablet['value'] = ('','Ibuprofein','co-codamol','Paracetamol','Aniodipine')
        self.cboNameTablet.current(0)
        self.cboNameTablet.grid(row=0, column=1)

        self.IblFurtherInfo = Label(DataFrameLEFT, font=("arial", 12, 'bold'), text="Further Information:", padx=2, pady=2,bg="#79E719")
        self.IblFurtherInfo.grid(row=0, column=2, sticky=W)
        self.txtFurtherInfo = Entry(DataFrameLEFT, font=("arial", 12, 'bold'), textvariable=FurtherInformation, width=25)
        self.txtFurtherInfo.grid(row=0, column=3)

        self.IblRef = Label(DataFrameLEFT, font=("arial", 12, 'bold'), text="Reference No:", padx=2, pady=2,bg="#79E719")
        self.IblRef.grid(row=1, column=0, sticky=W)
        self.txtRef = Entry(DataFrameLEFT, font=("arial", 12, 'bold'), textvariable=Ref, width=25)
        self.txtRef.grid(row=1, column=1)

        self.IblStorage = Label(DataFrameLEFT, font=("arial", 12, 'bold'), text="Storage Advice:", padx=2, pady=2,bg="#79E719")
        self.IblStorage.grid(row=1, column=2, sticky=W)
        self.txtStorage = Entry(DataFrameLEFT, font=("arial", 12, 'bold'), textvariable=StorageAdvice, width=25)
        self.txtStorage.grid(row=1, column=3)

        self.IblDose = Label(DataFrameLEFT, font=("arial", 12, 'bold'), text="Dose:", padx=2, pady=2,bg="#79E719")
        self.IblDose.grid(row=2, column=0, sticky=W)
        self.txtDose = Entry(DataFrameLEFT, font=("arial", 12, 'bold'), textvariable=Dose, width=25)
        self.txtDose.grid(row=2, column=1)

        self.IblDUseMachine = Label(DataFrameLEFT, font=("arial", 12, 'bold'), text="Driving Machines:", padx=2, pady=2,bg="#79E719")
        self.IblDUseMachine.grid(row=2, column=2, sticky=W)
        self.txtDUseMachine = Entry(DataFrameLEFT, font=("arial", 12, 'bold'), textvariable=DrivingUsingMachine, width=25)
        self.txtDUseMachine.grid(row=2, column=3)

        self.IblNoofTablets = Label(DataFrameLEFT, font=("arial", 12, 'bold'), text="No. of Tablets:", padx=2, pady=2,bg="#79E719")
        self.IblNoofTablets.grid(row=3, column=0, sticky=W)
        self.txtNoofTablets = Entry(DataFrameLEFT, font=("arial", 12, 'bold'), textvariable=NumberTablets, width=25)
        self.txtNoofTablets.grid(row=3, column=1)

        self.IblUseMedication = Label(DataFrameLEFT, font=("arial", 12, 'bold'), text="Medication:", padx=2, pady=2,bg="#79E719")
        self.IblUseMedication.grid(row=3, column=2, sticky=W)
        self.txtUseMedication = Entry(DataFrameLEFT, font=("arial", 12, 'bold'), textvariable=HowtoUseMedication, width=25)
        self.txtUseMedication.grid(row=3, column=3)

        self.IblLot = Label(DataFrameLEFT, font=("arial", 12, 'bold'), text="Lot:", padx=2, pady=2,bg="#79E719")
        self.IblLot.grid(row=4, column=0, sticky=W)
        self.txtLot = Entry(DataFrameLEFT, font=("arial", 12, 'bold'), textvariable=Lot, width=25)
        self.txtLot.grid(row=4, column=1)

        self.IblPatientID = Label(DataFrameLEFT, font=("arial", 12, 'bold'), text="Patient ID:", padx=2, pady=2,bg="#79E719")
        self.IblPatientID.grid(row=4, column=2, sticky=W)
        self.txtPatientID = Entry(DataFrameLEFT, font=("arial", 12, 'bold'), textvariable=PatientID, width=25)
        self.txtPatientID.grid(row=4, column=3)

        self.IblIssuedDate = Label(DataFrameLEFT, font=("arial", 12, 'bold'), text="Issued Date:", padx=2, pady=2,bg="#79E719")
        self.IblIssuedDate.grid(row=5, column=0, sticky=W)
        self.txtIssuedDate = Entry(DataFrameLEFT, font=("arial", 12, 'bold'), textvariable=IssuedDate, width=25)
        self.txtIssuedDate.grid(row=5, column=1)

        self.IblNHSNumber = Label(DataFrameLEFT, font=("arial", 12, 'bold'), text="NHS Number:", padx=2, pady=2,bg="#79E719")
        self.IblNHSNumber.grid(row=5, column=2, sticky=W)
        self.txtNHSNumber = Entry(DataFrameLEFT, font=("arial", 12, 'bold'), textvariable=PatientNHSNO, width=25)
        self.txtNHSNumber.grid(row=5, column=3)

        self.IblExpdate = Label(DataFrameLEFT, font=("arial", 12, 'bold'), text="Exp Date:", padx=2, pady=2,bg="#79E719")
        self.IblExpdate.grid(row=6, column=0, sticky=W)
        self.txtExpdate = Entry(DataFrameLEFT, font=("arial", 12, 'bold'), textvariable=ExpDate, width=25)
        self.txtExpdate.grid(row=6, column=1)

        self.IblPatientName = Label(DataFrameLEFT, font=("arial", 12, 'bold'), text="Patient Name:", padx=2, pady=2,bg="#79E719")
        self.IblPatientName.grid(row=6, column=2, sticky=W)
        self.txtPatientName = Entry(DataFrameLEFT, font=("arial", 12, 'bold'), textvariable=PatientName, width=25)
        self.txtPatientName.grid(row=6, column=3)

        self.IblDailyDose = Label(DataFrameLEFT, font=("arial", 12, 'bold'), text="Daily Dose:", padx=2, pady=2,bg="#79E719")
        self.IblDailyDose.grid(row=7, column=0, sticky=W)
        self.txtDailyDose = Entry(DataFrameLEFT, font=("arial", 12, 'bold'), textvariable=DailyDose, width=25)
        self.txtDailyDose.grid(row=7, column=1)

        self.IblDateofBirth = Label(DataFrameLEFT, font=("arial", 12, 'bold'), text="Date of Birth:", padx=2, pady=2,bg="#79E719")
        self.IblDateofBirth.grid(row=7, column=2, sticky=W)
        self.txtDateofBirth = Entry(DataFrameLEFT, font=("arial", 12, 'bold'), textvariable=DateofBirth, width=25)
        self.txtDateofBirth.grid(row=7, column=3)

        self.IblSideEffects = Label(DataFrameLEFT, font=("arial", 12, 'bold'), text="Side Effects:", padx=2, pady=2,bg="#79E719")
        self.IblSideEffects.grid(row=8, column=0, sticky=W)
        self.txtSideEffects = Entry(DataFrameLEFT, font=("arial", 12, 'bold'), textvariable=PossibleSideEffects, width=25)
        self.txtSideEffects.grid(row=8, column=1)

        self.IblPatientAddress = Label(DataFrameLEFT, font=("arial", 12, 'bold'), text="Patient Address:", padx=2, pady=2,bg="#79E719")
        self.IblPatientAddress.grid(row=8, column=2, sticky=W)
        self.txtPatientAddress = Entry(DataFrameLEFT, font=("arial", 12, 'bold'), textvariable=PatientAddress, width=25)
        self.txtPatientAddress.grid(row=8, column=3)

        #=========================DataFrameRight======================================================================
        
        self.txtPrescription = Text(DataFrameRIGHT, font=("arial", 12, 'bold'), width=43, height=14,padx=2, pady=6)
        self.txtPrescription.grid(row=0, column=0)

        #=========================ButtonFrame======================================================================

        self.btnPrescription = Button(ButtonFrame, text="Prescription", font=('arial', 12, 'bold'), width=24, bd=4, command=iPrescription)
        self.btnPrescription.grid(row=0, column=0)
        self.btnReceipt = Button(ButtonFrame, text="Prescription Data", font=('arial', 12, 'bold'), width=24, bd=4, command=iPrescriptionData)
        self.btnReceipt.grid(row=0, column=1)
        self.btnDelete = Button(ButtonFrame, text="Delete", font=('arial', 12, 'bold'), width=24, bd=4, command=iDelete)
        self.btnDelete.grid(row=0, column=2)
        self.btnReset = Button(ButtonFrame, text="Reset", font=('arial', 12, 'bold'), width=24, bd=4, command=iReset)
        self.btnReset.grid(row=0, column=3)
        self.btnExit = Button(ButtonFrame, text="Exit", font=('arial', 12, 'bold'), width=24, bd=4, command=iExit)
        self.btnExit.grid(row=0, column=4)

        #=========================FrameDetail======================================================================
        
        self.Ibllabel = Label(FrameDetail, font=("arial", 10, 'bold'), text="Name of Tablets\t Reference No.\tDoseage\t No. of Tablets\t Lot\t Issued Date\t Exp. Date\t Daily Dose\t Storage Adv.\tNHS Number\t Patient Name\t DOB\t Address", pady=8, bg="#A4FFFF")
        self.Ibllabel.grid(row=0, column=0)

        self.txtFrameDetail = Text(FrameDetail, font=("arial", 12, 'bold'), width=141, height=4,padx=2, pady=4, bg="#FFECA1")
        self.txtFrameDetail.grid(row=1, column=0)


if __name__=='__main__':
    root=Tk()
    application = Hospital(root)
    root.mainloop()