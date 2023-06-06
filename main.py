from moviepy.editor import *


def move_letters(t, w):
    x = 100 - w * t * 0.5
    y = 'center'
    return (x, y)


def create_video(text):
    screensize = (100, 100)
    duration = 3

    txt_clip = (TextClip(text, color='white', font='Arial', fontsize=50)
        .set_duration(duration)
        .set_position(('left', 'center'))
        .set_start(0))

    w, h = txt_clip.size

    txt_clip = txt_clip.set_position(lambda t: move_letters(t, w))

    final_clip = CompositeVideoClip([txt_clip], size=screensize,
                                    bg_color=(0, 0, 0))

    final_clip.write_videofile('my_video.mp4', fps=25)


if __name__ == '__main__':
    text = input('Введите строку, которую хотите анимировать: ')
    create_video(text)

