from captura import CapturaVideo

if __name__=='__main__':
    
    captura_video = CapturaVideo()
    
    config = captura_video.configuracoes()
    
    captura_video.captura()