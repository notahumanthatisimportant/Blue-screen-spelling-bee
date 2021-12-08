import QtQuick 2.15
import QtQuick.Controls 2.15


ApplicationWindow {
    visible: true
    width: 1920
    height: 1080
    title: "HelloApp"
    flags: Qt.FramelessWindowHint | Qt.Window
    Rectangle {
        anchors.fill: parent
        Image {
            sourceSize.width: parent.width
            sourceSize.height: parent.height
            source: './3VNVbnA'
            fillMode: Image.PreserveAspectCrop
        }
        Rectangle {
            anchors.fill: parent
            color: "transparent"
            Text {
                text: ""
                font.pixelSize: 24
                color: "white"
            }
        }
    }
}