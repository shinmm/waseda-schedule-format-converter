#Function that will remove and reformat elements
def replace(element):
    return str(element).replace("\u3000"," ").replace("月",'Mon.').replace('火','Tues.').replace('水','Wed.').replace('木','Thur.').replace('金','Fri.').replace('土','Sat.')
