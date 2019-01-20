#This script is a CSV File, and contains a method that will convert the CSV data to EXCEL(.xlsx)
import csv
import xlsxwriter
from help import replace

class CSV:

    def __init__(self, csv_filename):
        self.csv_filename = csv_filename
        #csv_file = open(csv_filename, "r",encoding="utf-8-sig")

    def getCSVfilename(self):
        return self.csv_filename


    def toExcel(self):
        pass
        csv_file = open(self.csv_filename, "r",encoding="utf-8-sig")
        workbook = xlsxwriter.Workbook('Excel'+str(self.csv_filename).replace(".csv","")+".xlsx")
        worksheet = workbook.add_worksheet()
        cellformat = workbook.add_format()
        cellformat.set_text_wrap()
        #fixed cells in the excel document
        worksheet.write('A1','PERIOD(時限)')
        worksheet.write('A2','1')
        worksheet.write('A3','2')
        worksheet.write('A4','3')
        worksheet.write('A5','4')
        worksheet.write('A6','5')
        worksheet.write('A7','6')
        worksheet.write('A8','7')
        worksheet.write('B1','MONDAY(月)')
        worksheet.write('C1','TUESDAY(火)')
        worksheet.write('D1','WEDNESDAY(水)')
        worksheet.write('E1','THURSDAY(木)')
        worksheet.write('F1','FRIDAY(金)')
        worksheet.write('G1','SATURDAY(土)')
        worksheet.write('H1','SUNDAY(日)')
        # Add auto text wrapping for proper spacing
        worksheet.set_column('A1:H1', 17, cellformat)



        #read file
        csv_fileIterable = csv.reader(csv_file)

        field_list = []
        day_to_excel = {'Mon.':'B' , 'Tues.': 'C', 'Wed.':'D', 'Thur.':'E','Fri.':'F','Sat.' : 'G'}
        not_first =False

        for row in csv_fileIterable:
            count = 0
            for ele in row:
                field_list.append(replace(ele))
                count+=1
                if(count ==12):
                    #list is full with one clss 1 is day 2 is period
                    if not_first==True:
                        print(field_list)
                        if "###" in str(field_list[1]):
                            print("double?")
                            #Class is a double day period and room
                            # if it contains ### as delimiter split into two and also
                            day = list(filter(None,str(field_list[1]).split("###")))
                            period= list(filter(None,str(field_list[2]).split("###")))
                            instructor= list(filter(None,str(field_list[6]).split("###")))
                            campus = list(filter(None,str(field_list[7]).split("###")))
                            room = list(filter(None,str(field_list[8]).split("###")))


                            #loop as many days there are. Some classes have 2 periods back to back or 2 periods a week etc
                            for i in range(len(day)):
                                #first d is D
                                double_period = day_to_excel[str(day[i])] + str(period[i])
                                if "-" in double_period:
                                    #double_period is a double period class
                                    pcor = period[i].split('-')
                                    print(pcor)
                                    for j in range(len(pcor)):
                                        p = day_to_excel[str(day[i])]+ str(int(pcor[j])+1)
                                        worksheet.write(p,field_list[5])
                                else:
                                    #one period but twice a week
                                    dd = day_to_excel[str(day[i])] + str(int(period[i])+1)
                                    worksheet.write(dd, field_list[5])

                            print(day)
                            print(period)
                            print(instructor)
                            print(campus)
                            print(room)
                            print(dd)
                            print(double_period)

                        else: #class is single period a week
                            period = str(day_to_excel.get(field_list[1])) + str((int(field_list[2]) + 1))
                            print(period)
                            worksheet.write(period,field_list[5])
                    #reset
                    count = 0
                    not_first=True
                    print(field_list)
                    del field_list[:]




        workbook.close()

        csv_file.close()