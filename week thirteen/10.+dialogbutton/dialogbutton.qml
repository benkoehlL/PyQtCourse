import QtQuick.Controls


ApplicationWindow {
    width: 640
    height: 480
    visible: true
    title: "DialogButton"

    DialogButtonBox {
        standardButtons: DialogButtonBox.Ok | DialogButtonBox.Cancel

        onAccepted: console.log("ok clicked")
        onRejected: console.log("Cancel clicked")



    }


}