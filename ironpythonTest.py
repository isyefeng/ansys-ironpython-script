# coding: utf-8
import ScriptEnv
oAnsoftApp = CreateObject("Ansoft.ElectronicsDesktop")
oDesktop = oAnsoftApp.GetAppDesktop()
oDesktop.RestoreWindow()               #最小化Twin Builder window
oProject = oDesktop.GetActiveProject() #获取ansys当前打开（活跃）的项目
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

'''
6 Desktop Commands
这一章主要是操作软件窗口
'''
oDesktop.CloseAllWindows()
oDesktop.AddMessage ("Project1", "TwinBuilder1", 0, "This isa test infomercial")  #0：infomercial 1：warning 2：error 3：fatal
oDesktop.EnableAutoSave(True)
oDesktop.ExportOptionsFiles("D:/ansys/project/ye_unit2/")
Enabled = oDesktop.GetAutoSaveEnabled()
AddInfoMessage("AutoSaveEnabled: "+str(Enabled))
dnt = oDesktop.GetBuildDateTimeString()
AddInfoMessage("BuildDateTime: "+str(dnt))
for machine in oDesktop.GetDistributedAnalysisMachines():
    AddInfoMessage(str(machine))
machineNames =oDesktop.GetDistributedAnalysisMachinesForDesignType("Twin Builder")
sys = oDesktop.GetSysLibDirectory()
AddInfoMessage("SysLib Directory: " + sys)
user = oDesktop.GetUserLibDirectory()
AddInfoMessage("UserLib Directory: " + user)
per = oDesktop.GetPersonalLibDirectory()
AddInfoMessage("PersonalLib Directory: " + per)
pjt = oDesktop.GetProjectDirectory()
AddInfoMessage("Project Directory: " + pjt)
AddInfoMessage("GetMessages: " + str(oDesktop.GetMessages("Project1","TwinBuilder1",0)))
AddInfoMessage("GetLibraryDirectory:"+str(oDesktop.GetLibraryDirectory()))  #输出库目录
AddInfoMessage("GetProjectList:"+str(oDesktop.GetProjectList()))  #输出所有打开工程名称的列表
for pjt in oDesktop.GetProjects():
    AddInfoMessage("GetProjects:"+str(pjt.GetName()))
AddInfoMessage("GetTempDirectory:"+str(oDesktop.GetTempDirectory))
AddInfoMessage("GetVersion:"+str(oDesktop.GetVersion()))
#oProject.ClearMessages() #清除项目输出信息
'''Desktop Commands
--Monitor job dialog'''
#oDesktop.LaunchJobMonitor("D:/ansys/project/ye_unit1/Project1.aedt")  #open a Monitor job window
#oProject = oDesktop.NewProject() #Create a new Project
#oDesktop.OpenProject("D:/ansys/project/ye/Project1.aedt") #这里使用‘/’,不能使用window格式的目录格式
#oDesktop.Print() #这个会让工程闪退，原因wei'zhi
#oDesktop.QuitApplication()
#oDesktop.RefreshJobMonitor()

#oProject = oDesktop.SetActiveProject ("Project2")  #相当于选中软件中打开的Project2工程
#oProject = oDesktop.SetActiveProjectByPath("D:/ansys/project/ye/Project1.aedt")  #同名的工程用这个接口

'''
7 Script Commands
这一章主要是操作工程（重要）
'''
#oProject.AnalyzeAll()   #开始分析
#oProject.Close() #关闭工程
oDefinitionManager = oProject.GetDefinitionManager()
for dsn in oProject.GetDesigns():
    AddInfoMessage(dsn.GetName())
AddInfoMessage (str(oProject.GetName()))        #get project name
AddInfoMessage(str(oProject.GetPath()))         #get project path

name_list = oProject.GetTopDesignList()         
for i in name_list:
    AddInfoMessage(str(i))
    
#oDesign2 =oDesign.InsertDesign("", "AmpChannel", "", "") #insert a new design
#oProject.Rename("D:/ansys/project/ye_unit1/Project1.aedt", True)  #重命名项目名称并保存
#oProject.Save()
#oProject.SaveAs("D:/ansys/project/ye_unit1/Project2.aedt", true)  #另存为
#oProject.SimulateAll()
'''
8 Definition Manager Script Commands
'''
oComponentManager = oDefinitionManager.GetManager("Component")

















#oDesktop.CloseProject("Project1")










