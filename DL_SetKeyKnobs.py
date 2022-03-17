# --------------------------------------------------------------
#  DL_SetKeyKnobs.py
#  Version: v01.1
#  Author: Danilo de Lucio
# --------------------------------------------------------------

# --------------------------------------------------------------
#  USAGE:
#
#  Store different knob values and set all their 
# keyframes at the same time.
# --------------------------------------------------------------

import nuke

main_list = []
icon_path = './DL_SetKeyKnobs/key_icon.png'

def getKnobs():
    global node_name, knob_name, knob_value, main_list

    # Getting the Node name
    node_name = nuke.thisNode().name()

    # Getting the Knob name
    knob_name = nuke.thisKnob().name()

    # Getting the Knob value
    n = nuke.thisNode()
    knob_value = n[knob_name].getValue()
    
    # Appending values to list
    nodes_list = [node_name, knob_name, knob_value]
    if nodes_list not in main_list:
        main_list.append(nodes_list)

def clearKnobs():
    global main_list

    # Clearing the Knobs list
    main_list = []
    nuke.message('Your knobs list has been cleared!')

def setKeys():
    if main_list == []:
        nuke.message("You don't have registered knobs yet!")

    for i in main_list:
        nodeName = i[0]
        knobName = i[1]
        knobValue = i[2]

        # Creating and setting keyframes
        n = nuke.toNode(nodeName)
        k = n.knob(knobName)
        k.setAnimated()
        k.setValue(knobValue)

def showKnobs():
    if main_list == []:
        nuke.message("You don't have registered knobs yet!")

    else:
        print("")
        print("[ Node name | Knob name | Knob value ]")
        for i in main_list:
            print("- " + i[0] + " | " + i[1] + " | " + str(i[2]))
        print("")

        nuke.message('Your knob list was printed out on Script Editor!')

# DL_SetKeyKnobs button on Menu Animation
nuke.menu('Animation').addCommand('DL_SetKeyKnobs', 'getKnobs()', icon = icon_path)

# DL_SetKeyKnobs button on Toolbar
skn_menu = nuke.menu('Nodes').addMenu('DL_SetKeyKnobs', icon = icon_path)
skn_menu.addCommand('Set Keyframes for registered knobs', 'setKeys()', 'ctrl+alt+k')
skn_menu.addCommand('Show Knobs registered', 'showKnobs()')
skn_menu.addCommand('Clear Knobs registered', 'clearKnobs()')
