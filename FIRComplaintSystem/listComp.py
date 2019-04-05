from tkinter import *
from tkinter.ttk import *
from db import DBConnect
import sqlite3

class ListComp:
	def __init__(self):
		self._dbconnect = DBConnect()
		self._dbconnect.row_factory = sqlite3.Row
		self._root = Tk()
		self._root.title('List of Complaints')
		tv = Treeview(self._root)
		tv.pack()
		tv.heading('#0', text='ID')
		tv.configure(column=('#PoliceStation', '#Subject', '#ComplaintType', '#Name', '#Gender', '#Address', '#Phone', '#Comment'))
		
		colwidth=150
		
		tv.heading('#PoliceStation',text='Police')
		tv.heading('#Subject',text='Subject')
		tv.heading('#ComplaintType',text='ComplaintType')		
		tv.heading('#Name', text='Name')
		tv.heading('#Gender', text='Gender')
		tv.heading('#Address', text='Address')
		tv.heading('#Phone', text='Phone')				
		tv.heading('#Comment', text='Comment')
		cursor = self._dbconnect.ListRequest()
		
		tv.column("#0", width=100 )
		tv.column("#PoliceStation", width=colwidth )
		tv.column("#Subject", width=colwidth )
		tv.column("#ComplaintType", width=colwidth )
		tv.column("#Name", width=colwidth )
		tv.column("#Gender", width=colwidth )
		tv.column("#Address", width=colwidth )
		tv.column("#Phone", width=colwidth )
		tv.column("#Comment", width=colwidth )
		
		for row in cursor:
			tv.insert('', 'end', '#{}'.format(row['ID']),text=row['ID'])
			tv.set('#{}'.format(row['ID']),'#PoliceStation',row['Police'])
			tv.set('#{}'.format(row['ID']),'#Subject',row['Subject'])
			tv.set('#{}'.format(row['ID']),'#ComplaintType',row['ComplaintType'])			
			tv.set('#{}'.format(row['ID']),'#Name',row['Name'])
			tv.set('#{}'.format(row['ID']),'#Gender',row['Gender'])
			tv.set('#{}'.format(row['ID']),'#Address',row['Address'])
			tv.set('#{}'.format(row['ID']),'#Phone',row['Phone'])			
			tv.set('#{}'.format(row['ID']),'#Comment',row['Comment'])
			
