lista = [[["movw", "%A", "%D"], "010"],
        [["movw", "%A", "(%A)"], "100"],
        [["movw", "%A", "%D", "(%A)"], "110"],
        [["movw", "(%A)", "%D"], "010"],
        [["addw", "(%A)", "%D", "%D"], "010"],
        [["incw", "%A"], "001"],
        [["incw", "%D"], "010"],
        [["incw", "(%A)"], "100"],
        [["nop"], "000"],
        [["subw", "%D", "(%A)", "%A"], "001"],
        [["rsubw", "%D", "(%A)", "%A"], "001"],
        [["decw", "%A"], "001"],
        [["decw", "%D"], "010"],
        [["notw", "%A"], "001"],
        [["notw", "%D"], "010"],
        [["negw", "%A"], "001"],
        [["negw", "%D"], "010"],
        [["andw", "(%A)", "%D", "%D"], "010"],
        [["andw", "%D", "%A", "%A"], "001"],
        [["orw", "(%A)", "%D", "%D"], "010"],
        [["orw", "%D", "%A", "%A"], "001"],
        [["jmp"], "000"],
        [["je"], "000"],
        [["jne"], "000"],
        [["jg"], "000"],
        [["jge"], "000"],
        [["jl"], "000"],
        [["jle"], "000"]]

dicio = {}

for i in lista :
    dicio[i[0][0]] = i[1]


print(dicio)