from urllib.request import *

# This is a program that, very very crudely, scrapes the UB scholarship portal and
# finds the number of scholarships whose deadlines have not passed yet.
# Automatically running this when I open my computer provides a very convenient
# way to see if there are any scholarships I should apply to.

# The parameters in the link may be modified to change the filters for the
# search to a different major like Economics, Art, etc.



# Link to the UB scholarships page, with the Computer Science and Engineering filter applied
url = "https://buffalo.academicworks.com/opportunities?utf8=%E2%9C%93&term=&scopes%5B%5D=60&commit=Filter+Opportunities"

html = urlopen(url).read().decode("utf-8")
html = html[(html.find("<tbody>")+len("<tbody>")):html.find("</tbody>")]
scholarships = []
numOfScholarships = html.count("<tr>")

def isValid(scholarship):
    if (scholarship["status"] != "Ended"):
        return True
    return False


for i in range(numOfScholarships):
    section = html[(html.find("<tr>")+len("<tr>")):html.find("</tr>")]
    scholarship = {}

    awardDel="<td class=\"strong h4 table__column--max-width-250\">"
    awardAmount = section[section.find(awardDel)+len(awardDel):section.find("<", section.find("<")+1)].strip()

    nameDel = "a href"
    scholarshipName = section[section.find(">", section.find(nameDel))+1:section.find("</a>")]

    statusDel = "<td class=\"center\" width=100>"
    status = section[section.find(statusDel)+len(statusDel):section.find("</td>", section.find("</td>")+1)].strip()
    

    scholarship["name"] = scholarshipName
    scholarship["award"] = awardAmount
    scholarship["status"] = status
    scholarships.append(scholarship)

    html = html[(html.find("</tr>")+len("</tr>")):len(html)]


# Detailed Output (Prints out the name, award amount, and the deadline for the scholarship)
# for i in range(len(scholarships)):
#     scholarship = scholarships[i]
#     print("Name: " + scholarship["name"])
#     print("Award Amount: " + scholarship["award"])
#     print("Status: " + scholarship["status"])
#     print()


numOfValids = list(map(isValid, scholarships)).count(True)


# Pretty Output (Just tells you how many scholarships are still open)

if (numOfValids == 0):
    print("No valid scholarships :(")
elif (numOfValids == 1):
    print("There is one valid scholarship.")
else:
    print("There are " + str(numOfValids) + " valid scholarships! Go apply!")


# Raw output (Number of open scholarships)
# print(numOfValids)