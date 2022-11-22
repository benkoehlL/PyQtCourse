import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {
    width: 640
    height: 480
    visible: true
    title: "Frame Example"

    Frame {
        ColumnLayout {
            anchors.fill: parent

            CheckBox {text: "Email"}
            CheckBox {text: "Calendar"}
            CheckBox {text: "Contact"}


        }



    }


 }