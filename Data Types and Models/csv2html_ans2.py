import sys
from xml.sax.saxutils import escape

def main():
    maxwidth, form = process_options()
    if maxwidth is not None:
        print_start()
        count = 0
        while count < 2:
            try:
                line = input()
                if count == 0:
                    color = "lightgreen"
                elif count % 2:
                    color = "white"
                else:
                    color = "lightyellow"
                print_line(line, color, maxwidth, form)
                count += 1
            except EOFError:
                break
        print_end()

def print_start():
    print("<table border='1'>")

def print_line(line, color, maxwidth, form):
    print("<tr bgcolor='{0}'>".format(color))
    numberFormat = "<td align='right'>{{0:{0}}}</td>".format(form)
    fields = extract_fields(line)
    for field in fields:
        if not field:
            print("<td></td>")
        else:
            number = field.replace(",", "")
            try:
                x = float(number)
                print(numberFormat.format(x))
            except ValueError:
                field = field.title()
                field = field.replace(" And ", " and ")
                if len(field) <= maxwidth:
                    field = escape(field)
                else:
                    field = "{0} ...".format(escape(field[:maxwidth]))
                print("<td>{0}</td>".format(field))
    print("</tr>")


def extract_fields(line):
    fields = []
    field = ""
    quote = None
    for c in line:
        if c in "\"'":
            if quote is None:
                quote = c
            elif quote == c:
                quote = None
            else:
                field += c
            continue
        if quote is None and c == ",":
            fields.append(field)
            field = ""
        else:
            field += c
    if field:
        fields.append(field)
    return fields

def print_end():
    print("</table>")

def process_options():
    maxwidth_arg = 'maxwidth='
    format_arg = 'format='
    maxwidth = 100
    form = ".0f"
    for arg in sys.argv[1:]:
        if arg in ("-h", "--help"):
            print('''
                usage:
                csv2html.py [maxwidth=int] [format=str] < infile.csv > outfile.html
                maxwidth is an optional integer; if specified, it sets the maximum
                number of characters that can be output for string fields,
                otherwise a default of 100 characters is used.
                (maxwidth - необязательное целое число. Если задано, определяет
                максимальное число символов для строковых полей. В противном случае
                используется значение по умолчанию 100.)
                format is the format to use for numbers; if not specified it
                defaults to ".0f".
                (format - формат вывода чисел. Если не задан, по умолчанию используется
                формат ".0f".)
                ''')
            return None, None
        elif arg.startswith(maxwidth_arg):
            try:
                maxwidth = int(arg.split('=')[1])
            except ValueError:
                pass
        elif arg.startswith(format_arg):
            form = str(arg.split('=')[1])
    return maxwidth, form

main()