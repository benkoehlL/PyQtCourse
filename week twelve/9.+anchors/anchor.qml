import QtQuick

Window {
    width: 640
    height: 480
    visible:true
    title: "Anchors"

    Rectangle {
        width: 100; height: 100
        color: "red"
        id: redrect
        //x: 100; y:100
        //anchors.centerIn:parent
        //anchors.margins:10

        //left anchors
        //anchors.left:parent.left
        //anchors.leftMargin:8
        //anchors.horizontalCenter: parent.horizontalCenter



    }

    Rectangle {
        id:greenrect
        width: 100; height: 100
        color: "green"
        anchors.top: redrect.bottom
        anchors.horizontalCenter: redrect.horizontalCenter




    }




    }