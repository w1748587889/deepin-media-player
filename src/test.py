#coding:utf-8

from video_information.gui import VideoInformGui, get_video_information
import gtk

if __name__ == "__main__":        
    def btn_clicked(widget):
        video_inform_gui = VideoInformGui("/home/long/视频/fsdjflksdfj附近的色拉夫家死掉了分第三集哭了夫家死掉了分第三集看了夫123.rmvb")

        video_inform_gui.show_window()
                
    win = gtk.Window(gtk.WINDOW_TOPLEVEL)
    btn = gtk.Button("ok")
    #
    # win.
    #
    win.set_size_request(300, 300)
    #
    # btn.
    #
    btn.connect("clicked", btn_clicked)
    #
    win.add(btn)
    win.show_all()
    gtk.main()
