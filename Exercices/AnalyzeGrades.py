def analyze_grades(grades):
        file={}
        try:
            file["average"]= float(sum(grades)/len(grades))
            file["max"] = float(max(grades))
            file["min"]= float(min(grades))

            admitted=0
            for i in grades:
                if i >= 10:
                    admitted +=1
            file["admitted"]=admitted

            print(file)
        except (ZeroDivisionError, ValueError):
            print("It's empty here buddy!")

grades1=[]
analyze_grades(grades1)
analyze_grades([12.5, 8.0, 15.0, 9.5, 17.0])