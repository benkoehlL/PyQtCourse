import QtQuick

Window {
    width: 640
    height: 480
    visible:true
    title: "TextField Elements"


        /*
        TextInput {
        id: input1
        width: 96; height: 20
        focus: true
        text: "Text Input 1"
        KeyNavigation.tab: input2



    }

    TextInput {
        id: input2
        width: 96; height: 20
        text: "Text Input 2"
        KeyNavigation.tab: input1



    }


    TextEdit {
        id: input
        anchors.margins: 4
        anchors.fill: parent
        color:"red"





    }

    */


    Rectangle {
        width: 96; height: 96
        color: "lightsteelblue"
        border.color: "gray"


        TextEdit {
            id: input
            anchors.fill:parent
            focus:true



        }





    }



}