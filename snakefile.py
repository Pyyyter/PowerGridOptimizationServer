import os
class OSeMOSYS:
    def inputConverting(self, data, output, params, saveLog):
        if saveLog:
            log = "logs/convertLog.txt"
            os.system("otoole convert csv datafile "+ data +" "+ output + " " + params + " 2> " + log)
        else:
            os.system("otoole convert csv datafile " + data +" "+ output + " " + params)

    def preprocessData(self, script, input, output, model, processedModel, saveLog):
        if saveLog:
            log = "logs/dataProcessLog.txt"
            os.system("python " +script +" "+ input +" "+ output +" "+ model + " " + processedModel + " 2> " + log)
        else:
            os.system("python " +script +" "+ input +" "+ output +" "+ model + " " + processedModel)

    def glpsolOptimize(self, model, data, output, saveLog):
        if saveLog:
            log = "logs/modelResult.txt"
            os.system("glpsol -m " + model + " -d " + data + " --wlp " + output + " --check 2> " + log)
        else:
            os.system("glpsol -m " + model + " -d " + data + " --wlp " + output + " --check")

    def datafileToCsv(self, input, output, params, saveLog):
        if saveLog:
            log = "logs/postProcessingLog.txt"
            os.system("otoole convert csv excel " + input +" "+ output +" "+ params + " 2> " + log)
        else:
            os.system("otoole convert csv excel " + input +" "+ output +" "+ params)

    def postProcessing(self, input, output, params, saveLog):
        self.datafileToCsv(input, output, params, saveLog)
        

    def optimize(self, input, model, config, combedData, processedData, script, output, processedModel, processedOutput, saveLog):
        self.inputConverting(input, combedData, config, saveLog)
        print("Converteu Entrada")
        self.preprocessData(script, combedData, processedData, model, processedModel, saveLog)
        print("Processou Dados")
        self.glpsolOptimize(processedModel, processedData, output, saveLog)
        self.postProcessing(output, processedOutput, config, saveLog)
