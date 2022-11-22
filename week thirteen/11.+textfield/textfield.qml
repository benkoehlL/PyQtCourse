import QtQuick.Controls
import QtQuick

ApplicationWindow {
    width: 640
    height: 480
    visible: true
    title: "TextField Example"

    TextField {
        anchors.centerIn: parent
        placeholderText: "Please enter name : "
        id: control


        background: Rectangle {
            implicitWidth: 200
            implicitHeight: 40
            color: control.enabled ? "transparent" : "#353637"
            border.color: control.enabled ? "#21be2b" : "transparent"



        }


    }


}