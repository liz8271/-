#Воронина Елизавета Юрьевна группа 413, Аттрактор Лоренца, Python Visual Studio Code
import matplotlib.animation as animation
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import warnings
warnings.filterwarnings("ignore", category=matplotlib.MatplotlibDeprecationWarning)

def lorenz(xyz,s=10, r=28, b=2.667):
    x, y, z = xyz
    x_dot = s*(y - x)
    y_dot = r*x - y - x*z
    z_dot = x*y - b*z
    return np.array([x_dot, y_dot, z_dot])

dt = 0.01
num_steps = 1000

def lor(num_steps):         # создаем и заполняем массив точек
    xyz = np.empty((num_steps + 1, 3))  
    xyz[0] = np.array(input().split(), float)   #вводим начальные значения
    for num in range(num_steps):           #метод Эйлера
        xyz[num + 1] = xyz[num] + lorenz(xyz[num]) * dt
    return xyz

xyzs=lor(num_steps)
xyzs1=lor(num_steps)
xyzs2=lor(num_steps)




fig = plt.figure()
ax = fig.add_subplot(projection="3d")
ax.set(xlim3d=(-40, 40), xlabel='X')    #Устанавливаем названия осей и их ограничения
ax.set(ylim3d=(-40, 40), ylabel='Y')
ax.set(zlim3d=(0, 45), zlabel='Z')

def animate(i):     #функция анимации
    lines.set_data(xyzs[:i, 0],xyzs[:i, 1]) 
    print(xyzs[:i, 0])
    lines.set_3d_properties(xyzs[:i, 2])
    redDot.set_data(xyzs[i, 0],xyzs[i,1])
    redDot.set_3d_properties(xyzs[i, 2])
    
    lines1.set_data(xyzs1[:i, 0],xyzs1[:i, 1]) 
    lines1.set_3d_properties(xyzs1[:i, 2])
    redDot1.set_data(xyzs1[i, 0],xyzs1[i,1])
    redDot1.set_3d_properties(xyzs1[i, 2])
    
    lines2.set_data(xyzs2[:i, 0],xyzs2[:i, 1]) 
    lines2.set_3d_properties(xyzs2[:i, 2])
    redDot2.set_data(xyzs2[i, 0],xyzs2[i,1])
    redDot2.set_3d_properties(xyzs2[i, 2])
    return redDot, lines, redDot1, lines1, redDot2, lines2

redDot = ax.plot([], [],[],'o')[0]
lines = ax.plot([],[],[])[0]

redDot1 = ax.plot([], [],[],'o')[0]
lines1 = ax.plot([],[],[])[0]

redDot2 = ax.plot([], [],[],'o')[0]
lines2 = ax.plot([],[],[])[0]

ani = animation.FuncAnimation(fig, animate, frames=num_steps, interval=10, blit=True, repeat=True)
#writergif = animation.PillowWriter(fps=30)         # Сохраняем анимацию
#ani.save("animate.gif", writer=writergif)
plt.show()