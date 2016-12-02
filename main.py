from kivy.uix.button import Button 
from kivy.uix.label import Label 
from kivy.app import App 
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder 
from kivy.base import runTouchApp
from kivy.graphics import Color
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import (Rectangle,
											Ellipse,
											Line)
from kivy.uix.image import Image
from kivy.uix.dropdown import DropDown
from kivy.uix.screenmanager import ScreenManager, Screen 

Builder.load_string('''
#Home Screen Definition
<MenuScreen>:   	
	FloatLayout:
	#Setting Up the BackGround of main screen 
		canvas.before:
			Color: 
				rgba: 1, 0, 0, 1
			Rectangle:
				pos: self.pos
				size: self.size 

		canvas:
			Color:
				rgba: 	0.9568, 0.6431, 0.3764, 1
			Ellipse:
				pos: self.pos
				size: self.size
		#Exit Button with Image On it
		Button:
			text: 'Exit'
			size_hint: None, None
			# background_normal: ''
			# backgroud_color: [1, 0, 0, 0]
			on_press: exit(100)
			size: root.width*0.06, root.height*0.10
			pos_hint: {'center_x': 0.94, 'center_y': 0.94}
			Image:
				source: 'pics/exit.jpg'
				size_hint: None, None
				size: root.width*0.10, root.height*0.10
				y: self.parent.y + self.parent.height - 110
            	x: self.parent.x - 45

		Image:
			pos: root.pos
			pos_hint: {'center_x': 0.15, 'center_y': 0.45}
			size: root.width*0.5, root.height
			source: 'pics/laugh1.jpg'
			allow_stretch: True
		Label:
			id: 'main'
			text: 'F.R.I.E.N.D.S. JOKE KING'
			font_size: 30
			pos_hint: {'center_x': .25, 'center_y': .98}
			valign: 'top'
			halign: 'left'

		Label:
			id: 'choose'
			text: 'Click on "START" Button to start'
			font_size: 30
			pos_hint: {'center_x': .75, 'center_y': .98}
			text_size: root.width, root.height
			valign: 'middle'
			halign: 'center'
		
		Button:
			id: 'genre'
			# canvas:
			# 	Color:
			# 		rgba: 0, 1, 0, 1	
			# 	Rectangle:
			# 		pos: self.pos
			# 		size: self.size
			text: 'Start'
			font_size: 50
			size_hint: None, None
			size: root.width*0.5, root.height*0.10
			pos_hint: {'center_x': 0.74, 'center_y': .78}
			on_press: root.manager.current = 'settings'
			
#Second Page Screen Definition
<SettingsScreen>:
	FloatLayout:
	#Setting Up the Color/Design of the BackGround
		canvas.before:
			Color:
				rgba: 0, 0.329, 0, 1	
			Rectangle:
				pos: self.pos
				size: self.size
		canvas:
			Color:
				rgba: 0.1803,0.5451,344117, 1
			Ellipse:
				pos: self.pos
				size: self.size
		Button:
			text: 'Home'
			size_hint: None, None
			# background_normal: ''
			# backgroud_color: [1, 0, 0, 0]
			on_press: root.manager.current = 'menu'
			size: root.width*0.06, root.height*0.10
			pos_hint: {'center_x': 0.06, 'center_y': 0.94}
			Image:
				source: 'pics/home.png'
				size_hint: None, None
				size: root.width*0.10, root.height*0.10
				y: self.parent.y + self.parent.height - 110
            	x: self.parent.x - 45


		Button:
			text: 'Exit'
			size_hint: None, None
			# background_normal: ''
			# backgroud_color: [1, 0, 0, 0]
			on_press: exit(100)
			size: root.width*0.06, root.height*0.10
			pos_hint: {'center_x': 0.94, 'center_y': 0.94}
			Image:
				source: 'pics/exit.jpg'
				size_hint: None, None
				size: root.width*0.10, root.height*0.10
				y: self.parent.y + self.parent.height - 110
            	x: self.parent.x - 45

        Button:
        	text: 'HELLO'
        	size_hint: None, None
        	size: root.width*0.6, root.height*0.6
        	pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        	on_press: root.manager.current = 'image1'
        	Image:
        		source: 'pics/main.jpg'
        		# size_hint: None, None
        		# x: self.parent.x
        		# y: self.parent.y
        		# pos_hint: self.parent.pos_hint
				#size: self.parent.texture.size        		
				size_hint: None, None
	        	size: root.width, root.height
    	    	pos_hint: {'center_x': 0.7, 'center_y': 0.7}
    	Label: 
    		text: 'Click on Image to Proceed'
    		font_size: 40
    		pos_hint: {'center_x': 0.5, 'center_y':0.98}

#Defining Screens to show Joke Images and Gifs 

<One>:
	Button:
		on_press: root.manager.current = 'image2'
		canvas:
			Color:
				rgba: 0, 0.329, 0, 1	
			Rectangle:
				pos: self.pos
				size: self.size
		Image:
			source: 'pics/one.jpg'
			size_hint: None, None
			size: self.parent.size
			allow_stretch: True

<Two>:
	Button:
		on_press: root.manager.current='image3'
		canvas:
			Color:
				rgba: 0, 0.329, 0, 1	
			Rectangle:
				pos: self.pos
				size: self.size
		Image:
			source: 'pics/Two.jpg'
			size_hint: None, None
			size: self.parent.size
			allow_stretch: True

<Three>:
	Button:
		on_press: root.manager.current= 'image4'
		canvas:
			Color:
				rgba: 0, 0.329, 0, 1	
			Rectangle:
				pos: self.pos
				size: self.size
		Image:
			source: 'pics/Three.jpg'
			size_hint: None, None
			size: self.parent.size
			allow_stretch: True

<Four>:
	Button:
		on_press: root.manager.current= 'image5'
		canvas:
			Color:
				rgba: 0, 0.329, 0, 1	
			Rectangle:
				pos: self.pos
				size: self.size
		Image:
			source: 'pics/Four.jpg'
			size_hint: None, None
			size: self.parent.size
			allow_stretch: True
			size_hint: None, None
			size: self.parent.size
			allow_stretch: True

<Five>:
	Button:
		on_press: root.manager.current= 'image6'
		canvas:
			Color:
				rgba: 0, 0.329, 0, 1	
			Rectangle:
				pos: self.pos
				size: self.size
		Image:
			source: 'pics/Five.jpg'
			size_hint: None, None
			size: self.parent.size
			allow_stretch: True

<Six>:
	Button:
		on_press: root.manager.current= 'image7'
		canvas:
			Color:
				rgba: 0, 0.329, 0, 1	
			Rectangle:
				pos: self.pos
				size: self.size
		Image:
			source: 'pics/Six.jpg'
			size_hint: None, None
			size: self.parent.size
			allow_stretch: True

<Seven>:
	Button:
		on_press: root.manager.current= 'image8'
		canvas:
			Color:
				rgba: 0, 0.329, 0, 1	
			Rectangle:
				pos: self.pos
				size: self.size
		Image:
			source: 'pics/Seven.jpg'
			size_hint: None, None
			size: self.parent.size
			allow_stretch: True

<Eight>:
	Button:
		on_press: root.manager.current= 'image9'
		canvas:
			Color:
				rgba: 0, 0.329, 0, 1	
			Rectangle:
				pos: self.pos
				size: self.size
		Image:
			source: 'pics/Eight.jpg'
			size_hint: None, None
			size: self.parent.size
			allow_stretch: True

<Nine>:
	Button:
		on_press: root.manager.current= 'image10'
		canvas:
			Color:
				rgba: 0, 0.329, 0, 1	
			Rectangle:
				pos: self.pos
				size: self.size
		Image:
			source: 'pics/Nine.gif'
			size_hint: None, None
			size: self.parent.size
			allow_stretch: True
			anim_delay: 0.12

<Ten>:
	Button:
		on_press: root.manager.current= 'image11'
		canvas:
			Color:
				rgba: 0, 0.329, 0, 1	
			Rectangle:
				pos: self.pos
				size: self.size
		Image:
			source: 'pics/Ten.gif'
			size_hint: None, None
			size: self.parent.size
			allow_stretch: True
			anim_delay: 0.12

<Eleven>:
	Button:
		on_press: root.manager.current= 'image12'
		canvas:
			Color:
				rgba: 0, 0.329, 0, 1	
			Rectangle:
				pos: self.pos
				size: self.size
		Image:
			source: 'pics/Eleven.jpg'
			size_hint: None, None
			size: self.parent.size
			allow_stretch: True

<Twelve>:
	Button:
		on_press: root.manager.current= 'image13'
		canvas:
			Color:
				rgba: 0, 0.329, 0, 1	
			Rectangle:
				pos: self.pos
				size: self.size
		Image:
			source: 'pics/Twelve.jpg'
			size_hint: None, None
			size: self.parent.size
			allow_stretch: True

<Thirteen>:
	Button:
		on_press: root.manager.current= 'menu'
		canvas:
			Color:
				rgba: 0, 0.329, 0, 1	
			Rectangle:
				pos: self.pos
				size: self.size
		Image:
			source: 'pics/Thirteen.jpg'
			size_hint: None, None
			size: self.parent.size
			allow_stretch: True

'''
)

# Declare both main screens
class MenuScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

# Declare all the Screens with a Button and image on it to show the joke and move to next when clicked
class One(Screen):
	pass

class Two(Screen):
	pass
class Three(Screen):
	pass
class Four(Screen):
	pass
class Five(Screen):
	pass
class Six(Screen):
	pass
class Seven(Screen):
	pass

class Eight(Screen):
	pass
class Nine(Screen):
	pass
class Ten(Screen):
	pass
class Eleven(Screen):
	pass
class Twelve(Screen):
	pass
class Thirteen(Screen):
	pass

# Create the screen manager
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(SettingsScreen(name='settings'))
sm.add_widget(One(name='image1'))
sm.add_widget(Two(name='image2'))
sm.add_widget(Three(name='image3'))
sm.add_widget(Four(name='image4'))
sm.add_widget(Five(name='image5'))
sm.add_widget(Six(name='image6'))
sm.add_widget(Seven(name='image7'))
sm.add_widget(Eight(name='image8'))
sm.add_widget(Nine(name='image9'))
sm.add_widget(Ten(name='image10'))
sm.add_widget(Eleven(name='image11'))
sm.add_widget(Twelve(name='image12'))
sm.add_widget(Thirteen(name='image13'))
# class JokeKing(FloatLayout):
# 	class ShowScreen(Screen):
# 		pass
class FRIENDSJokeKingApp(App):
	def build(self):
		return sm
#runTouchApp(JokeKing())

if __name__ == '__main__':
	FRIENDSJokeKingApp().run()