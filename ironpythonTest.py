# coding: utf-8
import ScriptEnv
oAnsoftApp = CreateObject("Ansoft.ElectronicsDesktop")
oDesktop = oAnsoftApp.GetAppDesktop()
oDesktop.RestoreWindow()
sys = oDesktop.GetSysLibDirectory()
AddInfoMessage("SysLib Directory: " + sys)
user = oDesktop.GetUserLibDirectory()
AddInfoMessage("UserLib Directory: " + user)
per = oDesktop.GetPersonalLibDirectory()
AddInfoMessage("PersonalLib Directory: " + per)
pjt = oDesktop.GetProjectDirectory()
AddInfoMessage("Project Directory: " + pjt)
oProject = oDesktop.GetActiveProject()
oDesign = oProject.GetActiveDesign()
oEditor = oDesign.SetActiveEditor("SchematicEditor")
selectionArray = oEditor.GetSelections()
if len(selectionArray) == 0:
    AddInfoMessage("No selections!")
for i in selectionArray:
    AddInfoMessage("Selected element: " + i)
    compArray = oEditor.GetComponentInfo(i)
    for k in compArray:
        AddInfoMessage("GetComponentInfo: " + k)
    pinArray = oEditor.GetComponentPins(i)
    for j in pinArray:
        AddInfoMessage("GetComponentPins: " + j)
    portArray = oEditor.GetPortInfo(i)
    for l in portArray:
        AddInfoMessage("GetPortInfo: " + l)
    netArray = oEditor.GetWireConnections(i)
    for m in netArray:
        AddInfoMessage("GetWireConnections: " + m)
    netArray2 = oEditor.GetWireSegments(i)
    for n in netArray2:
        AddInfoMessage("GetWireSegments: " + n)
    netArray3 = oEditor.GetWireInfo(i)
    for o in netArray3:
        AddInfoMessage("GetWireInfo: " + o)
    sigs = oEditor.GetSignals(wn)
    for ll in sigs:
        AddInfoMessage("Element in array from GetSignals: " + ll)
oSimplorerApp = oAnsoftApp.GetApp("Twin Builder")
count = oSimplorerApp.GetProcessResources ("GDI")
oDesktop.CloseAllWindows()
oDesktop.AddMessage ("Project1", "TwinBuilder1", 1, "This isa test Warning")  #0：infomercial 1：warning 2：error 3：fatal
oDesktop.EnableAutoSave(True)
oDesktop.ExportOptionsFiles("D:/ansys/project/ye_unit2/")
Enabled = oDesktop.GetAutoSaveEnabled()
AddInfoMessage("AutoSaveEnabled: "+str(Enabled))
dnt = oDesktop.GetBuildDateTimeString()
AddInfoMessage("BuildDateTime: "+str(dnt))
for machine in oDesktop.GetDistributedAnalysisMachines():
    AddInfoMessage(str(machine))
machineNames =oDesktop.GetDistributedAnalysisMachinesForDesignType("Twin Builder")

#oDesktop.CloseProject("Project1")










