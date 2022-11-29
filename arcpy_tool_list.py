import arcpy

# Create a list of tools in the Analysis toolbox
tools = arcpy.ListTools("*_analysis")

# Loop through the list and print each tool's usage.
tool_list = []
for tool in tools:
    tool_list.append((arcpy.Usage(tool)))

for i in tool_list:
    print(i)
