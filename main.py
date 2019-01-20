# from WasedaScheduleCreator.ScheduleScraper.CSV import CSV
# from WasedaScheduleCreator.ScheduleScraper.HTML import html
from HTML import html
from CSV import CSV
#Enter a HTML file as input

def main():
    schedule_raw = "Schedule_Raw_HTML/SHIN_Course Registration.htm"
    obj = html(schedule_raw)
    print(obj.getFileName())
    print(obj.getName())
    print(obj.toCSV())
    print(obj.getcsvFilename())


    csvobj = CSV(obj.getcsvFilename())
    print(csvobj.getCSVfilename())
    csvobj.toExcel()

main() #run conversion script