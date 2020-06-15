import sys
import gi
import pickledb

gi.require_version('Gtk', '3.0')
from gi.repository import Gio
from gi.repository import Gtk



class MainWindow(Gtk.ApplicationWindow):

    def __init__(self, App):
        super(MainWindow, self).__init__(title="Counter", application=App)
        #self.set_default_size(280, 180)
        self.set_border_width(10)
        
        self.db = pickledb.load('pycounter.db', False)
        savedprev=self.db.get('previous')
        self.count=int(savedprev)
        print("Database loaded successfully")
        
        print("starting creating vbox")
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(vbox)
        
        
        
        self.countLabel = Gtk.Label(self.count)
        vbox.pack_start(self.countLabel, True, True, 0)

        incbutton = Gtk.Button.new_with_label("Increase")
        incbutton.connect("clicked", self.increase)
        vbox.pack_start(incbutton, True, True, 0)
        
        decbutton = Gtk.Button.new_with_label("Decrease")
        decbutton.connect("clicked", self.decrease)
        vbox.pack_start(decbutton, True, True, 0)
        
        resetbutton = Gtk.Button.new_with_label("Reset")
        resetbutton.connect("clicked", self.resett)
        vbox.pack_start(resetbutton, True, True, 0)
        
        exitbutton = Gtk.Button.new_with_label("Exit")
        exitbutton.connect("clicked", self.exitt)
        vbox.pack_start(exitbutton, True, True, 0)
        
        print("GUI creating done")
        
    def increase(self, incbutton):
        print('"Increased pressed')
        count=self.count
        count=count+1
        self.count=count
        self.countLabel.set_text (str(count));
        self.db.set('previous', count)
        self.db.dump()

        
    def decrease(self, decbutton):
        print('"decreased pressed')
        count=self.count
        count=count-1
        self.count=count
        self.countLabel.set_text (str(count));
        self.db.set('previous', count)
        self.db.dump()
        
    def resett(self, resetbutton):
        print('"Reset pressed')
        self.count=0
        self.countLabel.set_text ("0");
        self.db.set('previous', '0')
        self.db.dump()
        
        
            
    def exitt(self, exbutton):
    	app.quit()
    	print("Successfully shut down")
    	



class App(Gtk.Application):
    def __init__(self):
        Gtk.Application.__init__(self,
                                 application_id="com.githubbt40.orpyco",
                                 flags=Gio.ApplicationFlags.FLAGS_NONE)

    def do_activate(self):
        window = MainWindow(self)
        window.show_all()



if __name__ == '__main__':
    app = App()
    app.run(sys.argv)
