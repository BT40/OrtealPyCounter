import sys
import gi
import pickledb


gi.require_version('Gtk', '3.0')
from gi.repository import Gio
from gi.repository import Gtk, Gdk



class MainWindow(Gtk.ApplicationWindow):

    def __init__(self, App):
        super(MainWindow, self).__init__(title="Counter", application=App, decorated=True, name="csswindow")
        #self.set_default_size(280, 180)
        self.set_border_width(10)
        
        try:
            self.set_icon_from_file("ortealicon512.png")
            print("Icon loaded successfully")
        except Exception as e:
            print("Failed loading Icon")
            print (e.message)
            
        
              
        
        
        self.db = pickledb.load('pycounter.db', False)
        savedprev=self.db.get('previous')
        self.count=int(savedprev)
        print("Database loaded successfully")
        
        #print("Starting creating vbox")
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(vbox)
        
        
        
        self.countLabel = Gtk.Label(label=self.count)
        self.countLabel.set_name('cntlab')
        vbox.pack_start(self.countLabel, True, True, 0)

        incbutton = Gtk.Button.new_with_label("Increase")
        incbutton.set_name('incbut')
        incbutton.connect("clicked", self.increase)
        vbox.pack_start(incbutton, True, True, 0)
        
        decbutton = Gtk.Button.new_with_label("Decrease")
        decbutton.connect("clicked", self.decrease)
        vbox.pack_start(decbutton, True, True, 0)
        
        resetbutton = Gtk.Button.new_with_label("Reset")
        resetbutton.set_name('resetbut')
        resetbutton.connect("clicked", self.resett)
        vbox.pack_start(resetbutton, True, True, 0)
        
        exitbutton = Gtk.Button.new_with_label("Exit")
        exitbutton.set_name('exitbut')
        exitbutton.connect("clicked", self.exitt)
        vbox.pack_start(exitbutton, True, True, 0)
        
        
        
        
        
        style_provider = Gtk.CssProvider()
        
        css = """
        

        #incbut {
            background-color: blue;
            color: #306754;
  	    font: 22px "Comic Sans";
        }
        
        #resetbut {
            background-color: red;
            color: #C24641;
  	    
        }
               
	#cntlab {
 	    font: 50px Sans;
 	    color: #25383C;
	}
        """
        style_provider.load_from_data(bytes(css.encode()))
	
        Gtk.StyleContext.add_provider_for_screen(
            Gdk.Screen.get_default(), style_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )
        
        print("GUI creating done")
        
    def increase(self, incbutton):
        print('Increase button pressed')
        count=self.count
        count=count+1
        self.count=count
        self.countLabel.set_text (str(count));
        self.db.set('previous', count)
        self.db.dump()

        
    def decrease(self, decbutton):
        print('Decrease button pressed')
        count=self.count
        count=count-1
        self.count=count
        self.countLabel.set_text (str(count));
        self.db.set('previous', count)
        self.db.dump()
        
    def resett(self, resetbutton):
        print('Reset button pressed')
        self.count=0
        self.countLabel.set_text ("0");
        self.db.set('previous', '0')
        self.db.dump()
        
        
            
    def exitt(self, exbutton):
    	app.quit()
    	print("Count saved to database, Successfully shut down")
    	
    
    
    
    
    

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
