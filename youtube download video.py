import webbrowser
url="https://www.youtube.com/watch?v=sIIdNAynO-M&list=RDsIIdNAynO-M&start_radio=1"
download=url[:12] + "ss" + url[12:]
webbrowser.open(download)

