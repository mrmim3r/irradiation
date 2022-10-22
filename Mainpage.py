import streamlit as st
st.title('How IR radiation make the remote control work? ')

st.header('Introduction')
st.write('''
Light is electromagnetic waves characterized primarily by its wavelength ,  it is divided by into segments, when the visible light Is ranges from 0.4 to 0.7 micrometers. but there is some invisible light which it used in many different applications such as remote control. But how it really work? 
''')

st.image('img/1.png')


st.header('William Herschel experiment: ')
st.write('For answer this  question , I will talking about story happened in 1800 , when sir Fredrik William Herschel was in his lab, conducting an experiment; he measured the temperature of each color in the rainbow with thermometer , he found that the violet is coolest one and the red is hottest , where  temperature increase from the violet to the red . but when he placed the thermometer just outside red light, he noticed it was hotter then everything else even there was no visible light . after this experiment he conclude that there are invisible light beyond red light, he called theme  ” calorific rays “, today we call them infrared radiation')

col1, col2 = st.columns(2)
col1.image('img/2.png')
col2.image('img/3.png')

st.header('What is infrared radiation ?')
col3,col4 = st.columns(2)
col3.write('''
It is an electromagnetic wave with wavelength longer than visible light. it is invisible to human eye but we sense it as heat. Any body with temperature higher than 0 Kalvin or minus 273 degrees Celsius emits that wave. 
''')
col4.image('img/4.png')
st.write('''
The emission of infrared radiation from an object is possible when heated. The atoms and the molecules in the object start to vibrate, thereby radiating infrared in the form of heat. When the objects are not hot enough to produce visible light, they radiate infrared
''')
st.image('img/5.png')
st.write('''
IR radiation is one of three ways to heat is transferred from place to another , the other two is being convention and conduction . 
''')
st.image('img/6.png')

st.write('The relationship between radiation and temperature is described by Planck’s law which is used to calculate the intensity  of thermal radiation or radiance')
st.code('''
𝐿=2ℎ𝑐²/𝜆^5*1/(exp⁡(ℎ𝑐/𝜆𝑇)−1)
''')

st.write('this law applies to the black body that absorbs all wavelengths and emit a flux depending on their temperature for a given spectral band .')
st.image('img/7.png')
st.write('We notice when black body becomes hotter it emits shorter wavelengths and greater intensities')
st.header('IR radiation characteristics : ')
st.write('the corresponding wavelength range is 1 mm to 0.78 micrometers. By using this characteristics we can calculate another ones such as : ')

st.subheader("frequency ")
st.code("f =𝑐/𝜆")

st.write('c :  speed of light ')
st.write('𝜆:  wavelength ')
st.write('So It oscillate with 3.10^11 to 4.10^14 times in second')

st.subheader("period ")
st.code("𝜏 =1/f")
st.write('c :  speed of light') 
st.write('𝜆:  wavelength ')
st.write('''It complete the oscillate in 2.5x10^-15 up to 3.3x10^-12 second 

''')

st.subheader("Energy of photon ")
st.code("𝐸=ℎ.𝑓")
st.write('''
h : Planck's constant   
(6.26.10^-34 j.s)''')
st.write('E : energy of photon') 

st.subheader("Waves numbers: ")
st.code("𝑘=1 ⁄𝜆")
st.write('''
13300 1/cm , 10 1/cm''')


st.image('img/8.png')
st.image('img/note.png')

st.header('infrared sub-division :')
st.write(' according to NASA , IR region may be subdivided into three : ')
st.image('img/9.png')

st.subheader('Far-IR')
st.write('which are closer to the microwaves section on the electromagnetic spectrum, can be felt as instance heat; it has wavelength range from 1mm to 30 micrometers and it used in medical field where It is used mainly in the treatment of cancer therapy. ')

st.subheader('Mid-IR')
st.write('The wavelength ranges from 3 to 8 micrometers. This is used in the chemical industry and in astronomy where it is used in Optical components like mirrors, lenses and digital detectors are used to study the objects that are in space. These objects glow when they are exposed to radiated heat.')
st.image('img/10.png')

st.subheader('Near IR')
col5, col6 = st.columns([3,1])
col5.write('is closer to visible light on electromagnetic spectrum ; This is used in material science, fiber optic communication, and in the medical field. The wavelength ranges from 3 to 0.78 micrometer.  But the common use on remotes control ')


st.header('How remote control work ?')
st.write('If you open a remote control you will find a simple board compensate of three main parts ')
st.image('img/11.png')

st.subheader('power supply')
st.write('which gives the electric power necessaire for working ')
st.image('img/12.png')


st.header('Command part ')
st.write('which is part that transform the clicks of button  into electric signal , where all the functions like volume up and volume down ,  power are translate  into binary code from 7 bits plus start command and device address and the bits of stop . That all happen in circuit integrated ')


st.image('img/13.png')


st.subheader('Transmitter')
st.write('''which include IR led . IR led light up depends of signal, where  1 means on and  0 mean off . 
the receiver convert the light pulse into electric signal again and send it into microprocessor which make function happens .  
''')

st.image('img/15.png')

st.subheader('Why Do we need so many remote controls? ')
st.write('It is because that when you click button not only the command transfer to binary code but actually the IC add a device address to code . That make not there different between the devices but also on the same type too . That advantage make IR control more powerful than other type. ')

st.subheader('What is disadvantages of IR remote ?')
st.write(''' it doesn’t  work on long distance because it use near-IR that make the electronics can’t  detect the photon .
Also it require line to sight to work so it can work from the corner or when an object a front of it the because it travel on straight line and  can absorbed by most of objects like walls and even human body .
We can't really  consider all those like disadvantages or advantage because it depends to how we look at it . And in remote control  for some devices like TV or DVD player you will always  use it when you set down in front of them ''')
st.header('Conclusion')
st.write('There are a lot of devices use the EM  wave around us , from the small one like remote control to the big one like tv and antenna . Today , we discover one of theme from how it work to what that is use ')

