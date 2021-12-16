import QtQuick 2.15
import QtQuick.Controls 2.15

ApplicationWindow {
    visible: true
    width: 1920
    height: 1080
    title: "HelloApp"
    flags: Qt.FramelessWindowHint | Qt.Window | Qt.WindowStaysOnTopHint
    onClosing: close.accepted = false
    property string currTime: "0"
    property QtObject backend
    Rectangle {
        anchors.fill: parent
        Image {
            sourceSize.width: parent.width
            sourceSize.height: parent.height
            source: 'https://i.imgur.com/5iCBMve.jpg'
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
        Text {
            anchors {
                top: top.bottom
                topMargin: 12
                left: parent.left
                leftMargin: 12
            }
            text: currTime
            font.pixelSize: 48
            color: "white"
        }
      }
    Connections {
        target: backend
        function onUpdated(msg) {
            currTime = msg;
        }
    }
}}
