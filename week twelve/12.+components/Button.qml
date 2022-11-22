import QtQuick


    Rectangle {
        id: root

        //export button property
        property alias text: label.text
        signal clicked

        width: 116; height: 26
        color: "lightsteelblue"
        border.color: "gray"

        Text {
            id: label
            anchors.centerIn: parent
            text: "Change Text"


        }

        MouseArea {
            anchors.fill: parent
            onClicked: {
                root.clicked()


            }


        }




    }