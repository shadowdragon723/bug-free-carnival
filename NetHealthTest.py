# Import Libaries
import csv

# Pull in dataset from CSVs


# Nested for loop for each node to test connectivity to every other node - dump data into dataset


# Format and output dataset









# Class Definitions 

class officeSite:
    strSiteName = ""
    boolHasSilverPeak = False
    boolHasInternetRouting = False
    objSiteTargets = []
    def setSiteName(self,strSN):
        self.strSiteName = strSN
        return
    def setHasSilverPeak(self,boolHSP):
        self.boolHasSilverPeak = boolHSP
        return
    def setHasInternetRouting(self,boolHIR):
        self.boolHasInternetRouting = boolHIR
        return
    def addSiteTarget(self,objST):
        # check if the target exist already
        for objTarget in self.objSiteTargets:
            if objTarget == objST:
                return False
        self.objSiteTargets.append(objST)
        return True

class testTarget:
    strTargetName = ""
    strTargetType = ""
    strSite = ""
    intTargetPorts = []
    def setTargetName(self,strTN):
        self.strTargetName = strTN
        return 
    def setTargetType(self,strTT):
        self.strTargetType = strTT
        return
    def setSite(self,strS):
        self.strSite = strS
        return
    def addTargetPort (self,intTP):
        # check if the port exist already
        for intPort in self.intTargetPorts:
            if intPort == intTP:
                return False
        self.intTargetPorts.append(intTP)
        return True


class dataAccessAPI:
    # Add new Target
    
    # Import Data from source (CSV/DB)

    # Write Results

    # Create Dataset
    def createDataset (self):
        return