import calendar
import locale; locale.setlocale(category=locale.LC_ALL,locale="Russian_Russia.1251")
cal=calendar.LocaleHTMLCalendar(firstweekday=0, locale='Russian_Russia.1251')

str=cal.formatyearpage(2020,12, css="calendar.css").decode('utf8')

with open('calendar.html', 'w', encoding='utf8') as f:
     print(str, file=f)