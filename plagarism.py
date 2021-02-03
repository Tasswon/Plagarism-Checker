import mosspy
import os
import codecs

#have to register and get your own user id
userid = 0
count = 0

directory = input("Enter a directory: ")
language = input("Enter a language: ")

files = os.listdir(directory)
for i in range(len(files)):
    files[i] = directory + "/" + files[i]


for i in range(len(files)):
    for j in range(len(files)):
        try:
            if j < i + 1:
                continue
            if j > len(files):
                break
            m = mosspy.Moss(userid, language)

            # Submission Files
            m.addFile(files[i])
            m.addFile(files[j])

            url = m.send() # Submission Report URL
            print("Report Url: " + url + " --> " + str(count))

            # Save report file
            m.saveWebPage(url, "report_{}.html".format(count))

            html = codecs.open("report_{}.html".format(count), 'r')
            temp = html.read()
            html.close()
            if "No matches were found in your submission" in temp:
                os.remove("report_{}.html".format(count))

            count += 1

            del m
            del url
        except:
            print("\nException" + " --> " + str(count) + "\n")

print("Complete!")
# Download whole report locally including code diff links
#mosspy.download_report(url, "report/", connections=8)