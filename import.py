import gui

def importer(first_name, last_name, phone, address):
    path ='file_name.json' 
    data = open(path, 'a')
    data.write(f'{first_name}, {last_name}, {phone}, {address}')
    data.close()

def inpor(en):
    first_name = gui.input_con('first_name')  
    last_name = gui.input_con('last_name')
    phone = gui.input_con('phone')
    address = gui.input_con('address')

inpor()