#!/usr/bin/env python3
import io
import os
import queue
import uuid


class Code:
    def __init__(self, outFile):
        self.outFile = outFile
        self.counter = 0
        self.vmFileName = None
        self.labelCounter = 0

    # DONE
    def close(self):
        self.outFile.close()

    # DONE
    def updateVmFileName(self, name):
        self.vmFileName = os.path.basename(name).split(".")[0]

    # DONE
    def commandsToFile(self, commands):
        for line in commands:
            self.outFile.write(f"{line}\n")

    # DONE
    def getUniqLabel(self):
        return self.vmFileName + str(self.labelCounter)

    # DONE
    def updateUniqLabel(self):
        self.labelCounter = self.labelCounter + 1

    # DONE
    def writeHead(self, command):
        self.counter = self.counter + 1
        return ";; " + command + " - " + str(self.counter)

    # DONE
    def writeInit(self, bootstrap, isDir):
        commands = []

        if bootstrap or isDir:
            commands.append(self.writeHead("init"))

        if bootstrap:
            commands.append("leaw $256,%A")
            commands.append("movw %A,%D")
            commands.append("leaw $SP,%A")
            commands.append("movw %D,(%A)")

        if isDir:
            commands.append("leaw $Main.main, %A")
            commands.append("jmp")
            commands.append("nop")

        if bootstrap or isDir:
            self.commandsToFile(commands)

    # TODO
    def writeLabel(self, label):
        commands = []
        commands.append(self.writeHead("label") + " " + label)

        # TODO ...
        self.commandsToFile(commands)

    # TODO
    def writeGoto(self, label):
        commands = []
        commands.append(self.writeHead("goto") + " " + label)

        # TODO ...
        self.commandsToFile(commands)

    # TODO
    def writeIf(self, label):
        commands.append(self.writeHead("if") + " " + label)
        commands = []

        # TODO ...
        self.commandsToFile(commands)

    # TODO
    def writeArithmetic(self, command):
        self.updateUniqLabel()
        if len(command) < 2:
            print("instrucão invalida {}".format(command))
        commands = []
        commands.append(self.writeHead(command))

        if command == "add":
            commands.append("leaw $SP, %A")
            commands.append("movw (%A), %D")
            commands.append("decw %D")
            commands.append("decw %D")
            commands.append("movw %D, %A")
            commands.append("movw (%A), %D")
            commands.append("leaw $SP, %A ")
            commands.append("movw (%A), %A")
            commands.append("subw %A, $1, %A")
            commands.append("addw (%A), %D, %D")
            commands.append("subw %A, $1, %A")
            commands.append("movw %D, (%A)")
            commands.append("leaw $SP, %A")
            commands.append("movw (%A), %A")
            commands.append("subw %A, $1, %A")
            commands.append("movw %A, %D")
            commands.append("leaw $SP, %A")
            commands.append("movw %D, (%A)")

             # TODO
        elif command == "sub":
            commands.append("leaw $SP, %A")
            commands.append("movw (%A), %D")
            commands.append("decw %D")
            commands.append("decw %D")
            commands.append("movw %D, %A")
            commands.append("movw (%A), %D")
            commands.append("leaw $SP, %A ")
            commands.append("movw (%A), %A")
            commands.append("subw %A, $1, %A")
            commands.append("subw %D, (%A), %D")
            commands.append("subw %A, $1, %A")
            commands.append("movw %D, (%A)")
            commands.append("leaw $SP, %A")
            commands.append("movw (%A), %A")
            commands.append("subw %A, $1, %A")
            commands.append("movw %A, %D")
            commands.append("leaw $SP, %A")
            commands.append("movw %D, (%A)")
            # TODO
        elif command == "or":
            pass # TODO
        elif command == "and":
            pass # TODO
        elif command == "not":
            
            commands.append("leaw $SP, %A")
            commands.append("movw (%A), %D")
            commands.append("decw %D")
            commands.append("movw %D, %A")
            commands.append("movw (%A), %D")
            commands.append("notw %D")
            commands.append("movw %D, (%A)")

        

                 # TODO
        elif command == "neg":

            commands.append("leaw $SP, %A")
            commands.append("movw (%A), %D")
            commands.append("decw %D")
            commands.append("movw %D, %A")
            commands.append("movw (%A), %D")
            commands.append("negw %D")
            commands.append("movw %D, (%A)")
           

             # TODO
        elif command == "eq":
            # dica, usar self.getUniqLabel() para obter um label único
            pass # TODO
        elif command == "gt":
            # dica, usar self.getUniqLabel() para obter um label único
            pass # TODO
        elif command == "lt":
            # dica, usar self.getUniqLabel() para obter um label único
            pass # TODO

        self.commandsToFile(commands)

    def writePop(self, command, segment, index):
        self.updateUniqLabel()
        commands = []
        commands.append(self.writeHead(command) + " " + segment + " " + str(index))

        if segment == "" or segment == "constant":
            return False
        elif segment == "local":
            
            commands.append("leaw $SP, %A")
            commands.append("movw (%A), %D")
            commands.append("decw %D")
            commands.append("movw %D, %A")
            commands.append("movw (%A), %D")

            commands.append("leaw $LCL, %A")
            commands.append("movw (%A), %A")

            commands.append(f"addw ${index}, %A, %A")
            commands.append("movw %D, (%A)")
            
            

            # dica: usar o argumento index (push local 1)
            pass # TODO
        elif segment == "argument":
            pass # TODO
        elif segment == "this":
            pass # TODO
        elif segment == "that":
            pass # TODO
        elif segment == "temp":
            # dica: usar o argumento index (push temp 0)
            pass # TODO
        elif segment == "static":
            pass # TODO
        elif segment == "pointer":
            pass # TODO

        self.commandsToFile(commands)

    def writePush(self, command, segment, index):
        commands = []
        commands.append(self.writeHead(command + " " + segment + " " + str(index)))

        if segment == "constant":

            commands.append(f"leaw ${index}, %A")
            commands.append("movw %A, %D")
            commands.append("leaw $SP, %A")
            commands.append("movw (%A), %A")

            commands.append("movw %D, (%A)")

            commands.append("leaw $SP, %A")
            commands.append("movw (%A), %D")
            commands.append("addw $1, (%A), %D")
            commands.append("leaw $SP, %A")
            commands.append("movw %D, (%A)")
            
            # dica: usar index para saber o valor da consante
            # push constant index
            pass # TODO
        elif segment == "local":

            commands.append(f"leaw ${index}, %A")
            commands.append("movw %A, %D")
            commands.append("leaw $LCL, %A")
            commands.append("addw %D, (%A), %D")
            commands.append("movw %D, %A")
            commands.append("movw (%A), %D")
            commands.append("leaw $SP, %A")
            commands.append("movw (%A), %A")
            commands.append("movw %D, (%A)")
            commands.append("movw %A, %D")
            commands.append("addw $1, %D, %D")
            commands.append("leaw $SP, %A")
            commands.append("movw %D, (%A)")



            pass # TODO
        elif segment == "argument":

            commands.append(f"leaw ${index}, %A")
            commands.append("movw %A, %D")
            commands.append("leaw $ARG, %A")
            commands.append("addw %D, (%A), %D")
            commands.append("movw %D, %A")
            commands.append("movw (%A), %D")
            commands.append("leaw $SP, %A")
            commands.append("movw (%A), %A")
            commands.append("movw %D, (%A)")
            commands.append("movw %A, %D")
            commands.append("addw $1, %D, %D")
            commands.append("leaw $SP, %A")
            commands.append("movw %D, (%A)")

            pass # TODO
        elif segment == "this":

            commands.append(f"leaw ${index}, %A")
            commands.append("movw %A, %D")
            commands.append("leaw $THIS, %A")
            commands.append("addw %D, (%A), %D")
            commands.append("movw %D, %A")
            commands.append("movw (%A), %D")
            commands.append("leaw $SP, %A")
            commands.append("movw (%A), %A")
            commands.append("movw %D, (%A)")
            commands.append("movw %A, %D")
            commands.append("addw $1, %D, %D")
            commands.append("leaw $SP, %A")
            commands.append("movw %D, (%A)")

            pass # TODO
        elif segment == "that":
            commands.append(f"leaw ${index}, %A")
            commands.append("movw %A, %D")
            commands.append("leaw $THAT, %A")
            commands.append("addw %D, (%A), %D")
            commands.append("movw %D, %A")
            commands.append("movw (%A), %D")
            commands.append("leaw $SP, %A")
            commands.append("movw (%A), %A")
            commands.append("movw %D, (%A)")
            commands.append("movw %A, %D")
            commands.append("addw $1, %D, %D")
            commands.append("leaw $SP, %A")
            commands.append("movw %D, (%A)")

            pass # TODO
        elif segment == "static":
            commands.append(f"leaw ${index}, %A")
            commands.append("movw %A, %D")
            commands.append("leaw $16, %A")
            commands.append("addw %D, %A, %D")
            commands.append("movw %D, %A")
            commands.append("movw (%A), %D")
            commands.append("leaw $SP, %A")
            commands.append("movw (%A), %A")
            commands.append("movw %D, (%A)")
            commands.append("movw %A, %D")
            commands.append("addw $1, %D, %D")
            commands.append("leaw $SP, %A")
            commands.append("movw %D, (%A)")
            pass # TODO
        elif segment == "temp":
            commands.append(f"leaw ${index}, %A")
            commands.append("movw %A, %D")
            commands.append("leaw $5, %A")
            commands.append("addw %D, %A, %D")
            commands.append("movw %D, %A")
            commands.append("movw (%A), %D")
            commands.append("leaw $SP, %A")
            commands.append("movw (%A), %A")
            commands.append("movw %D, (%A)")
            commands.append("movw %A, %D")
            commands.append("addw $1, %D, %D")
            commands.append("leaw $SP, %A")
            commands.append("movw %D, (%A)")
            pass # TODO
        elif segment == "pointer":
            commands.append(f"leaw ${index}, %A")
            commands.append("movw %A, %D")
            commands.append("leaw $3, %A")
            commands.append("addw %D, %A, %D")
            commands.append("movw %D, %A")
            commands.append("movw (%A), %D")
            commands.append("leaw $SP, %A")
            commands.append("movw (%A), %A")
            commands.append("movw %D, (%A)")
            commands.append("movw %A, %D")
            commands.append("addw $1, %D, %D")
            commands.append("leaw $SP, %A")
            commands.append("movw %D, (%A)")
            pass # TODO

        self.commandsToFile(commands)

    # TODO
    def writeCall(self, funcName, numArgs):
        commands = []
        commands.append(self.writeHead("call") + " " + funcName + " " + str(numArgs))

        # TODO
        # ...

        self.commandsToFile(commands)

    # TODO
    def writeReturn(self):
        commands = []
        commands.append(self.writeHead("return"))

        # TODO
        # ...

        self.commandsToFile(commands)

    # TODO
    def writeFunction(self, funcName, numLocals):
        commands = []
        commands.append(self.writeHead("func") + " " + funcName + " " + str(numLocals))

        # TODO
        # ...

        self.commandsToFile(commands)
