import time

__author__ = 'JLyon'
import serial
from serial.tools import list_ports

class ExLink():
    def __init__(self, port):
        self.ser = serial.Serial(port, baudrate=9600, bytesize=8, timeout=3)

    def ListPorts(self):
        ports = list_ports.comports()
        for port in ports:
            print port

    def SetPort(self, port):
        self.ser.port = port
        self.ser.open()

    def crc(self, command):
        crc = 0x100
        for char in command:
            crc -= char
        return crc

    def PowerOff(self):
        self.ser.write([0x08, 0x22, 0x00, 0x00, 0x00, 0x01, 0xd5])
        #self.ser.write([0x08, 0x22, 0x00, 0x00, 0x00, 0x01, 0xd7])
        #self.ser.write([0x08, 0x22, 0x00, 0x00, 0x00, 0x01, 0xd6])

    def PowerOn(self):
        # WORKING - DO NOT DELETE
        self.ser.write([0x08, 0x22, 0x00, 0x00, 0x00, 0x02, 0xd6])

    def PowerToggle(self):
        self.ser.write([0x08, 0x22, 0x00, 0x00, 0x00, 0x00, 0xd6])

    def Volume(self, volume):
        if volume < 0 or volume > 100:
            print "Volume must be within the range of 0-100"
        cmd = [0x08, 0x22, 0x01, 0x00, 0x00, volume]
        cmd.append(self.crc(cmd))
        self.ser.write(cmd)

    def VolumeUp(self):
        self.ser.write([0x08, 0x22, 0x01, 0x00, 0x01, 0x00, 0xd4])

    def VolumeDown(self):
        self.ser.write([0x08, 0x22, 0x01, 0x00, 0x02, 0x00, 0xd3])

    def Mute(self):
        # WORKING - DO NOT DELETE
        self.ser.write([0x08, 0x22, 0x02, 0x00, 0x00, 0x00, 0xd4])

    def ChannelUp(self):
        self.ser.write([0x08, 0x22, 0x03, 0x00, 0x01, 0x00, 0xd2])

    def ChannelDown(self):
        self.ser.write([0x08, 0x22, 0x03, 0x00, 0x02, 0x00, 0xd1])

    def InputTV(self):
        self.ser.write([0x08, 0x22, 0x0a, 0x00, 0x00, 0x00, 0xcc])

    def InputAV1(self):
        self.ser.write([0x08, 0x22, 0x0a, 0x00, 0x01, 0x00, 0xcb])

    def InputAV2(self):
        self.ser.write([0x08, 0x22, 0x0a, 0x00, 0x01, 0x01, 0xca])

    def InputAV3(self):
        self.ser.write([0x08, 0x22, 0x0a, 0x00, 0x01, 0x02, 0xc9])

    def InputSVideo1(self):
        self.ser.write([0x08, 0x22, 0x0a, 0x00, 0x02, 0x00, 0xca])

    def InputSVideo2(self):
        self.ser.write([0x08, 0x22, 0x0a, 0x00, 0x02, 0x00, 0xc9])

    def InputSVideo3(self):
        self.ser.write([0x08, 0x22, 0x0a, 0x00, 0x02, 0x00, 0xc8])

    def InputComponent1(self):
        self.ser.write([0x08, 0x22, 0x0a, 0x00, 0x03, 0x00, 0xc9])

    def InputComponent2(self):
        self.ser.write([0x08, 0x22, 0x0a, 0x00, 0x03, 0x00, 0xc8])

    def InputComponent3(self):
        self.ser.write([0x08, 0x22, 0x0a, 0x00, 0x03, 0x00, 0xc7])

    def InputPC1(self):
        self.ser.write([0x08, 0x22, 0x0a, 0x00, 0x04, 0x00, 0xc8])

    def InputPC2(self):
        self.ser.write([0x08, 0x22, 0x0a, 0x00, 0x04, 0x00, 0xc7])

    def InputPC3(self):
        self.ser.write([0x08, 0x22, 0x0a, 0x00, 0x04, 0x00, 0xc6])

    def DVI1(self):
        self.ser.write([0x08, 0x22, 0x0a, 0x00, 0x06, 0x00, 0xc6])

    def DVI2(self):
        self.ser.write([0x08, 0x22, 0x0a, 0x00, 0x06, 0x00, 0xc5])

    def DVI3(self):
        self.ser.write([0x08, 0x22, 0x0a, 0x00, 0x06, 0x00, 0xc4])

    def HDMI1(self):
        # WORKING - DO NOT DELETE
        self.ser.write([0x08, 0x22, 0x0a, 0x00, 0x05, 0x00, 0xc7])

    def HDMI2(self):
        # WORKING - DO NOT DELETE
        self.ser.write([0x08, 0x22, 0x0a, 0x00, 0x05, 0x01, 0xc6])

    def HDMI3(self):
        # WORKING - DO NOT DELETE
        self.ser.write([0x08, 0x22, 0x0a, 0x00, 0x05, 0x02, 0xc5])

    def HDMI4(self):
        # WORKING - DO NOT DELETE
        self.ser.write([0x08, 0x22, 0x0a, 0x00, 0x05, 0x03, 0xc4])

    def Size169(self):
        self.ser.write([0x08, 0x22, 0x0b, 0x0a, 0x01, 0x00, 0xc0])

    def SizeZoom1(self):
        self.ser.write([0x08, 0x22, 0x0b, 0x0a, 0x01, 0x01, 0xbf])

    def SizeZoom2(self):
        self.ser.write([0x08, 0x22, 0x0b, 0x0a, 0x01, 0x02, 0xbe])

    def SizeWideFit(self):
        self.ser.write([0x08, 0x22, 0x0b, 0x0a, 0x01, 0x03, 0xbd])

    def Size43(self):
        self.ser.write([0x08, 0x22, 0x0b, 0x0a, 0x01, 0x04, 0xbc])

    def SizeScreenFit(self):
        self.ser.write([0x08, 0x22, 0x0b, 0x0a, 0x01, 0x05, 0xbb])

    def SizeSmartView1(self):
        self.ser.write([0x08, 0x22, 0x0b, 0x0a, 0x01, 0x06, 0xba])

    def SizeSmartView2(self):
        self.ser.write([0x08, 0x22, 0x0b, 0x0a, 0x01, 0x07, 0xb9])

    def ResetPicture(self):
        self.ser.write([0x08, 0x22, 0x0b, 0x0b, 0x00, 0x070, 0xc0])

    def Test(self):
        print "PowerOn"
        self.PowerOn()
        time.sleep(5)

        print "VolumeUp"
        self.VolumeUp()
        time.sleep(2)

        print "VolumeDown"
        self.VolumeDown()
        time.sleep(2)

        print "Mute"
        self.Mute()
        time.sleep(2)

        print "Volume(25)"
        self.Volume(25)
        time.sleep(2)

        print "ChannelUp"
        self.ChannelUp()
        time.sleep(3)

        print "ChannelDown"
        self.ChannelDown()
        time.sleep(3)

        print "HDMI1"
        self.HDMI1()
        time.sleep(3)

        print "HDMI2"
        self.HDMI2()
        time.sleep(3)

        print "HDMI3"
        self.HDMI3()
        time.sleep(3)

        print "HDMI4"
        self.HDMI4()
        time.sleep(3)

        print "Zoom1"
        self.SizeZoom1()
        time.sleep(2)

        print "16:9"
        self.Size169()
        time.sleep(2)

        print "Smart View I"
        self.SizeSmartView1()
        time.sleep(2)

        print "Smart View II"
        self.SizeSmartView2()
        time.sleep(2)

        print "Screen Fit"
        self.SizeScreenFit()
        time.sleep(2)

        print "ResetPicture"
        self.ResetPicture()
        time.sleep(2)

        print "PowerOff"
        self.PowerOff()
        time.sleep(5)

        print "PowerToggle"
        self.PowerToggle()
        time.sleep(5)

    # Another reference for commands: http://forum.samygo.tv/viewtopic.php?f=52&t=5381
    # Another reference for commands: http://forum.team-mediaportal.com/threads/samsung-led-tv-serial-control-help.91088/
    # Source list from Samsung: http://vchproject.org/images/Discrete_and_RS232_Compiled2003.xls
    """ Code List
        Power Toggle : "$08,$22,$00,$00,$00,$00,$d6" *NOT WORKING WITH TV OFF*
        Power On : "$08,$22,$00,$00,$00,$02,$d4" *NOT WORKING WITH TV OFF*
                    $08,$22,$00,$00,$00,$02,$d6     <<-- DONE
        Power Off : "$08,$22,$00,$00,$00,$01,$d5"   <<-- DONE

        Volume Up : "$08,$22,$01,$00,$01,$00,$d4"   <<-- DONE (Not Tested)
        Volume Down : "$08,$22,$01,$00,$02,$00,$d3" <<-- DONE (Not Tested)
        Mute Toggle : "$08,$22,$02,$00,$00,$00,$d4" <<-- DONE (Not Tested)
        Speaker On : "$08,$22,$0c,$06,$00,$00,$c4"
        Speaker Off : "$08,$22,$0c,$06,$00,$01,$c3"

        HDMI 1 : "$08,$22,$0a,$00,$05,$00,$c7"      <<--DONE
        HDMI 2 : "$08,$22,$02,$00,$00,$00,$d4"      <<--DONE (FIXED COMMAND)
        HDMI 3 : "$08,$22,$0a,$00,$05,$02,$c5"      <<--DONE
        HDMI 4 : "$08,$22,$0a,$00,$05,$03,$c4"      <<--DONE (FIXED CRC)
        VGA : "$08,$22,$0a,$00,$04,$00,$c8"
        Component 1 : "$08,$22,$0a,$00,$03,$00,$c9"
        Component 2 : "$08,$22,$0a,$00,$03,$01,$c8"
        A\V 1 : "$08,$22,$0a,$00,$01,$00,$cb"
        A\V 2 : "$08,$22,$0a,$00,$01,$01,$ca"
        S-Video : "$08,$22,$0a,$00,$02,$00,$ca"
        TV Tuner : "$08,$22,$0a,$00,$00,$00,$cc"

        16x9 Aspect : "$08,$22,$0b,$0a,$01,$00,$c0"
        Zoom 1 Aspect : "$08,$22,$0b,$0a,$01,$01,$bf"
        Zoom 2 Aspect : "$08,$22,$0b,$0a,$01,$02,$be"
        Wide Fit : "$08,$22,$0b,$0a,$01,$03,$bd"
        4x3 Aspect : "$08,$22,$0b,$0a,$01,$04,$bc"
        Just Scan : "$08,$22,$0b,$0a,$01,$05,$bb"
        Wide TV (PC) : "$08,$22,$0b,$0a,$01,$06,$ba"
        Wide PC (PC) : "$08,$22,$0b,$0a,$01,$07,$b9"
    """



    """
    def PowerOff(self):
        self.ser.write("n")

    def PowerOff2(self):
        cmd = [0x08, 0x22, 0x00, 0x00, 0x00, 0x01, 0xD5]
        self.ser.write(cmd)

    def PowerOff3(self):
        cmd = [0x08, 0x22, 0x00, 0x00, 0x00, 0x01, 0x2C]
        self.ser.write(cmd)

    def PowerOff4(self):
        self.ser.write([0xAD, 0xA1, 0x03, 0x00, 0x00, 0x01, 0xA5])

    def PowerOff5(self):
        self.ser.write([0xAD, 0xFF, 0x05, 0x41, 0xA1, 0x00, 0x00, 0x01, 0xE7])

    def PowerOn(self):
        self.ser.write("N")

    def PowerOn2(self):
        self.ser.write([0xAD, 0xA1, 0x03, 0x01, 0x00, 0x01, 0xA6])

    def PowerOn3(self):
        self.ser.write([0xAD, 0xFF, 0x05, 0x41, 0xA1, 0x01, 0x00, 0x01, 0xE8])
    """
