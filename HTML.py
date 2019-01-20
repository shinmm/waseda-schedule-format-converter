from bs4 import BeautifulSoup as soup
import csv
class html:
    page_soup = ''
    clean_soup = ''
    csv_filename = ''
    def __init__(self,html_filename):
        self.html_filename = html_filename
        global page_soup
        global clean_soup
        page_soup = soup(open(self.getFileName()), "html.parser")
        clean_soup = soup(str(page_soup).replace("<br>", "###").replace("</br>","###"),"html.parser")
        #print(clean_soup)
        #print(page_soup)

    def getcleanHTML(self):
        return clean_soup

    def getRawHTML(self):
        return page_soup

    def getFileName(self):
        return self.html_filename

    def getName(self):
        #holds the name of the person
        self.name = str(page_soup.findAll("td", {"class" : "welcome"})[0].text).strip().strip("Welcomeback").strip("さん").strip()
        return self.name


    def toCSV(self):

        # assigns field list that will later be columns or headers in the csv file  will contain 12 elements
        field_names = []
        class_rows = {}
        # contains the fields [term,class title, period, etc]
        for tag in page_soup.findAll("td", {"class": "operationboxt"}):
            field_names.append(tag.text.strip())
        del field_names[0:7]
        #open and write csv file
        global csv_filename
        csv_filename = str(self.getName())+ "_schedule.csv"
        with open(csv_filename, 'w', newline='',encoding='utf-8-sig') as file:
            thewriter = csv.DictWriter(file, fieldnames=field_names)
            thewriter.writeheader()

            #contains all classes
            i = 0
            for tage in clean_soup.findAll("td", {"class": "decisionboxf"}):
                #write each class to csv
                class_rows[field_names[i]] = tage.text.strip()
                i+=1
                if(i == 12):
                    i = 0
                    #write to csv?
                    thewriter.writerow(class_rows)

        file.close()

    def getcsvFilename(self):
        return csv_filename
print("HELLO")