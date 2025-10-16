dataFileName = "Data.html"
outputFileName = "out.csv"

netTotal = 0
grossTotal = 0

# Parse through the html and create a csv file for the data
with open(dataFileName, "r") as dataFile, open(outputFileName, "w") as outFile:
    content = dataFile.read()
    outFile.write("gross, net\n")

    # Net values come first, then gross values
    netPrecedent = "Net Payment</h4><div class=\"main\" role=\"note\"><span class=\"unit\">$</span><span class=\" value { "
    netAntecedent = ">= 0 ? positive : negative}"

    grossPrecedent = "<li><span class=\"label\">Gross</span><span class=\"data\">$ "
    grossAntecedent = "</span></li>"

    netStartInd = content.find(netPrecedent)

    while (netStartInd != -1):
        content = content[netStartInd+len(netPrecedent):len(content)]
        netEndInd = content.find(netAntecedent)
        netPay = content[0:netEndInd]

        grossStartInd = content.find(grossPrecedent)
        content = content[grossStartInd+len(grossPrecedent):len(content)]
        grossEndInd = content.find(grossAntecedent)
        grossPay = content[0:grossEndInd]

        netTotal += float(netPay)
        grossTotal += float(grossPay)

        outFile.write(grossPay + "," + netPay + "\n")

        # print("Net: " + netPay + ", Gross: " + grossPay)

        netStartInd = content.find(netPrecedent)
    
    outFile.write(str(round(grossTotal, 2)) + "," + str(round(netTotal, 2)))

    print("Total Net Pay: " + str(round(netTotal, 2)))
    print("Total Gross Pay: " + str(round(grossTotal, 2)))

    outFile.close()

dataFile.close()


