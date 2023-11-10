import cv2
import keyboard
import numpy as np
import pyautogui

class CapturaVideo:
    
    def configuracoes(self):
        self.fps = 30
        self.tamanho_tela = tuple(pyautogui.size())
        print(f'tamanho da tela {self.tamanho_tela}')
    
        self.codec = cv2.VideoWriter_fourcc(*'XVID')
    
    #definindo as caracteristicas do video
        self.video = cv2.VideoWriter('video.avi', self.codec, self.fps, self.tamanho_tela)
    
        return self.video
    
    def captura(self):
        while True:
            frame = pyautogui.screenshot()
            frame = np.array(frame)
            
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            
            self.video.write(frame)
            
            if keyboard.is_pressed('esc'):
                break
            
        self.video.release()
        cv2.destroyAllWindows()